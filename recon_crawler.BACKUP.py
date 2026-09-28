#!/usr/bin/env python3
"""
Harness-drivable recon crawler (Playwright + real Chrome profile).

USE ONLY on targets you are explicitly authorized to test. Driving a real
Chrome profile means you are acting as a logged-in you -- keep it pointed at
in-scope assets only.

Designed to be called by an orchestrator ("harness"):
  - Pass config in, get a structured dict back.
  - Every finding is ALSO streamed to a JSONL "notebook" as it happens, so an
    AI harness can tail the file and reason in real time.

Setup:
    pip install playwright
    playwright install chromium          # only needed if you DON'T use real Chrome
    # For a real Chrome profile you need Chrome itself installed (channel="chrome").

Constraint:
    CLOSE Chrome completely before running with a real profile, or the profile
    lock will fail.

CLI:
    python recon_crawler.py https://example.com \
        --profile "/path/to/Chrome/User Data" --profile-name "Default"

Programmatic (from your harness):
    from recon_crawler import CrawlConfig, run_crawl
    result = await run_crawl(CrawlConfig(seed="https://example.com",
                                         user_data_dir="/path/to/User Data",
                                         profile_directory="Default"))
"""

import asyncio
import json
import re
import sys
import time
import argparse
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import urlparse, urldefrag, urljoin
from collections import deque
from typing import Optional

from playwright.async_api import async_playwright


# ---- Config the harness controls -------------------------------------------
@dataclass
class CrawlConfig:
    seed: str
    user_data_dir: Optional[str] = None      # path to Chrome "User Data" dir
    profile_directory: str = "Default"       # which profile inside it
    headless: bool = False                   # real profiles usually want headed
    attach_port: Optional[int] = None        # CDP port of a Chrome YOU launched
    max_depth: int = 2
    max_pages: int = 50
    request_delay: float = 0.3               # each worker waits this between pages
    concurrency: int = 5                     # number of parallel worker tabs
    nav_timeout_ms: int = 20000
    capture_bodies: bool = True              # store response bodies (in-scope, text)
    max_body_bytes: int = 200_000           # skip bodies bigger than this
    allow_subdomains: bool = False           # *.host if True
    scope_file: Optional[str] = None         # path to scope.txt (include/exclude rules)
    interact: bool = False                   # click SPA elements to reveal routes
    mine_js: bool = True                     # fetch JS files and extract endpoints
    max_clicks_per_page: int = 25            # cap clicks per page when interacting
    # --- Authentication ---
    pause_for_login: bool = False            # open browser, let YOU log in, then crawl
    smart_login: bool = False                # auto-fill creds, pause only if 2FA/CAPTCHA
    creds_file: Optional[str] = None         # path to cred.txt (email/password)
    login_url: Optional[str] = None          # page to land on for login (defaults to seed)
    auto_login: bool = False                 # fill a login form automatically (manual selectors)
    user_selector: Optional[str] = None      # CSS selector for the username/email field
    pass_selector: Optional[str] = None      # CSS selector for the password field
    submit_selector: Optional[str] = None    # CSS selector for the submit button
    output_root: str = "output"              # notes are organized per-domain under here
    # notebook_path / report_path are derived per-domain at runtime (see run_crawl)
    notebook_path: str = ""                  # filled in automatically if left blank
    report_path: str = ""                    # filled in automatically if left blank


# ---- The notebook: one structured record per finding -----------------------
class Notebook:
    """Append-only JSONL log. The harness tails this to 'see' everything."""
    def __init__(self, path):
        self.path = Path(path)
        self.path.write_text("")  # truncate
        self._fh = self.path.open("a", encoding="utf-8")

    def note(self, kind, **data):
        # human-readable local time, e.g. "2026-09-27 13:34:35"
        rec = {"time": time.strftime("%Y-%m-%d %H:%M:%S"), "kind": kind, **data}
        self._fh.write(json.dumps(rec, ensure_ascii=False) + "\n")
        self._fh.flush()  # flush so a tailing harness sees it immediately

    def close(self):
        self._fh.close()


class ScopeRules:
    """
    Load in-scope / out-of-scope rules from a scope file and decide if a URL
    is allowed. Exclusion ALWAYS wins over inclusion (security-tool convention).

    scope.txt format (one rule per line, '#' comments allowed):

        # lines with no prefix, or a '+' prefix, are IN-SCOPE
        *.smtp2go.com
        +app-us.smtp2go.com

        # lines with a '-' prefix are OUT-OF-SCOPE (excluded)
        -status.smtp2go.com
        -*.blog.smtp2go.com
        -/logout
        -/api/billing

    Matching:
      * host patterns: 'example.com' matches ONLY that exact host.
        Use '*.example.com' to match any subdomain (plus the base).
      * path patterns: start with '/' and match if the URL path starts with it.
    """
    def __init__(self, include=None, exclude=None):
        self.include = include or []   # list of (kind, pattern)
        self.exclude = exclude or []

    @classmethod
    def from_file(cls, path):
        inc, exc = [], []
        p = Path(path)
        if not p.exists():
            print(f"[!] scope file not found: {p} (crawling with default scope)")
            return cls()
        for raw in p.read_text().splitlines():
            line = raw.strip()
            if not line or line.startswith("#"):
                continue
            bucket = inc
            if line[0] in "+-":
                if line[0] == "-":
                    bucket = exc
                line = line[1:].strip()
            if not line:
                continue
            kind = "path" if line.startswith("/") else "host"
            bucket.append((kind, line.lower()))
        print(f"[+] scope: {len(inc)} include rule(s), {len(exc)} exclude rule(s)")
        return cls(inc, exc)

    @staticmethod
    def _host_match(pattern, host):
        if pattern.startswith("*."):
            # wildcard: the base host AND any subdomain of it
            base = pattern[2:]
            return host == base or host.endswith("." + base)
        # bare hostname = EXACT match only (no subdomains). Use *.x for subdomains.
        return host == pattern

    def _matches(self, rules, host, path):
        for kind, pat in rules:
            if kind == "host" and self._host_match(pat, host):
                return True
            if kind == "path" and path.startswith(pat):
                return True
        return False

    def has_includes(self):
        return bool(self.include)

    def allows(self, url):
        u = urlparse(url)
        host, path = (u.netloc or "").lower(), (u.path or "/").lower()
        if not host:
            return False
        # exclusion wins, always
        if self._matches(self.exclude, host, path):
            return False
        # if include rules exist, the URL must match at least one
        if self.include:
            return self._matches(self.include, host, path)
        # no include rules -> not decided here (caller falls back to host logic)
        return None


class ReconCrawler:
    def __init__(self, cfg: CrawlConfig):
        self.cfg = cfg
        self.host = urlparse(cfg.seed).netloc
        # hosts we consider in-scope; login may add the post-redirect host
        self.allowed_hosts = {self.host}
        # registrable-ish base (last two labels), e.g. app.smtp2go.com -> smtp2go.com
        self.base_domain = ".".join(self.host.split(".")[-2:])
        # scope rules from a file (include / exclude). May be empty.
        self.scope = ScopeRules.from_file(cfg.scope_file) if cfg.scope_file \
            else ScopeRules()
        self.nb = Notebook(cfg.notebook_path)
        self.queue = deque([(cfg.seed, 0)])
        self.seen_pages = set()
        # Aggregate findings (returned to harness at the end)
        self.links = set()
        self.js_files = set()
        self.forms = []
        self.requests = []        # {method, url, resource_type}
        self.responses = []       # {url, status, headers, body?}
        self.params = set()
        self.console = []
        self.storage = {}
        # JS mining results
        self.js_endpoints = set()   # endpoints/paths extracted from JS bodies
        self.js_secrets = []        # possible secrets/keys spotted in JS

    # -- scope --------------------------------------------------------------
    def in_scope(self, url):
        host = urlparse(url).netloc
        if not host:
            return False

        # 1) explicit scope file is AUTHORITATIVE when it has include rules.
        verdict = self.scope.allows(url)
        if verdict is False:
            return False            # excluded -> always out
        if verdict is True:
            return True             # matches an include -> in
        # verdict is None means: the scope file did not decide.
        #   - if include rules EXIST, "not decided" means "not in the list" -> OUT.
        #     (do NOT fall through to host guesses that could re-allow it)
        if self.scope.has_includes():
            return False

        # 2) no scope-file includes -> fall back to host logic
        if host in self.allowed_hosts:
            return True
        if self.cfg.allow_subdomains:
            if host == self.base_domain or host.endswith("." + self.base_domain):
                return True
        return False

    def normalize(self, url):
        url, _ = urldefrag(url)
        return url.rstrip("/") or url

    def record_params(self, url):
        q = urlparse(url).query
        for pair in q.split("&"):
            if "=" in pair and pair.split("=")[0]:
                p = pair.split("=")[0]
                if p not in self.params:
                    self.params.add(p)
                    self.nb.note("param", name=p, seen_on=url)

    # -- network hooks ------------------------------------------------------
    def _wire_network(self, context):
        def on_request(req):
            if not self.in_scope(req.url):
                return
            rec = {"method": req.method, "url": self.normalize(req.url),
                   "resource_type": req.resource_type}
            self.requests.append(rec)
            self.record_params(req.url)
            self.nb.note("request", **rec)

        async def on_response(resp):
            if not self.in_scope(resp.url):
                return
            rec = {"url": self.normalize(resp.url), "status": resp.status,
                   "headers": dict(resp.headers)}
            if self.cfg.capture_bodies:
                ctype = resp.headers.get("content-type", "")
                if any(t in ctype for t in ("text", "json", "javascript",
                                            "xml", "html")):
                    try:
                        body = await resp.body()
                        if len(body) <= self.cfg.max_body_bytes:
                            rec["body"] = body.decode("utf-8", "replace")
                    except Exception:
                        pass
            self.responses.append(rec)
            self.nb.note("response", url=rec["url"], status=rec["status"],
                         has_body="body" in rec)

        context.on("request", on_request)
        context.on("response", lambda r: asyncio.create_task(on_response(r)))

    # -- DOM extraction -----------------------------------------------------
    async def extract(self, page, url):
        new_links = set()
        # Grab hrefs broadly: <a>, <area>, and anything with a data-href/route.
        hrefs = await page.eval_on_selector_all(
            "a[href], area[href], [data-href], [data-url], [data-route]",
            """els => els.map(e =>
                 e.href || e.getAttribute('data-href') ||
                 e.getAttribute('data-url') || e.getAttribute('data-route')
               ).filter(Boolean)""")
        for href in hrefs:
            try:
                absu = href if href.startswith("http") else urljoin(url, href)
            except Exception:
                absu = href
            n = self.normalize(absu)
            if n not in self.links:
                self.links.add(n)
                self.record_params(n)
                self.nb.note("link", url=n, found_on=url)
            if self.in_scope(n):
                new_links.add(n)

        for src in await page.eval_on_selector_all(
                "script[src]", "els => els.map(e => e.src)"):
            if src not in self.js_files:
                self.js_files.add(src)
                self.nb.note("js_file", url=src, found_on=url)

        forms = await page.eval_on_selector_all(
            "form",
            """els => els.map(f => ({
                action: f.action, method: f.method,
                inputs: Array.from(f.querySelectorAll('input,select,textarea'))
                          .map(i => ({name: i.name, type: i.type})).filter(x=>x.name)
            }))""")
        for f in forms:
            f["found_on"] = url
            self.forms.append(f)
            self.nb.note("form", **f)

        # grab storage -- often leaks tokens/config
        try:
            store = await page.evaluate(
                """() => ({
                    local: {...localStorage},
                    session: {...sessionStorage}
                })""")
            if store["local"] or store["session"]:
                self.storage[url] = store
                self.nb.note("storage", url=url,
                             local_keys=list(store["local"].keys()),
                             session_keys=list(store["session"].keys()))
        except Exception:
            pass

        return new_links

    # -- SPA interaction: click things to reveal JS-rendered routes ---------
    async def _interact(self, page, base_url):
        """Click in-scope nav elements to surface routes that have no <a href>.
        Records any new same-app URL the click navigates to, then returns."""
        found = set()
        # only interact while we're on an in-scope page
        if not self.in_scope(page.url):
            return found
        selectors = ("[role='link'], [role='menuitem'], [role='tab'], "
                     "nav a, nav button, .nav a, .menu a, li[onclick], "
                     "button[onclick], [data-navigate], [data-target]")
        try:
            handles = await page.query_selector_all(selectors)
        except Exception:
            return found
        start_url = page.url
        for h in handles[: self.cfg.max_clicks_per_page]:
            try:
                if not await h.is_visible():
                    continue
                await h.click(timeout=3000, no_wait_after=True)
                await asyncio.sleep(0.6)
                cur = self.normalize(page.url)
                if cur == self.normalize(start_url):
                    continue
                if self.in_scope(cur):
                    if cur not in self.links:
                        self.links.add(cur)
                        self.nb.note("link", url=cur, found_on=base_url,
                                     via="click")
                    found.add(cur)
                else:
                    # a click took us OUT of scope -> record nothing, don't explore
                    self.nb.note("scope_skip", url=cur, reason="click left scope")
                # always return to the in-scope page we started on
                try:
                    await page.goto(start_url, timeout=self.cfg.nav_timeout_ms,
                                    wait_until="networkidle")
                except Exception:
                    break
            except Exception:
                continue
        return found
    # Selectors tried in order to auto-detect fields on ANY login page.
    USER_SELECTORS = [
        "input[type='email']",
        "input[name*='email' i]", "input[id*='email' i]",
        "input[autocomplete='username']",
        "input[name*='user' i]", "input[id*='user' i]",
        "input[name*='login' i]", "input[id*='login' i]",
        "input[type='text']",
    ]
    PASS_SELECTORS = ["input[type='password']",
                      "input[name*='pass' i]", "input[id*='pass' i]"]
    SUBMIT_SELECTORS = [
        "button[type='submit']", "input[type='submit']",
        "button[name*='login' i]", "button[id*='login' i]",
        "button:has-text('Log in')", "button:has-text('Sign in')",
        "button:has-text('Login')", "button:has-text('Continue')",
        "button:has-text('Next')", "button:has-text('Submit')",
        "input[value*='Next' i]", "input[value*='Continue' i]",
    ]
    # Markers that suggest an EXTRA step (2FA / OTP / CAPTCHA) is required.
    EXTRA_AUTH_SELECTORS = [
        "input[name*='otp' i]", "input[id*='otp' i]",
        "input[name*='code' i]", "input[id*='code' i]",
        "input[name*='token' i]", "input[autocomplete='one-time-code']",
        "input[inputmode='numeric']",
        "iframe[src*='recaptcha']", "iframe[src*='hcaptcha']",
        "div.g-recaptcha", "div[class*='captcha' i]",
    ]

    async def _first_visible(self, page, selectors):
        for sel in selectors:
            try:
                el = page.locator(sel).first
                if await el.count() and await el.is_visible():
                    return el, sel
            except Exception:
                continue
        return None, None

    async def _wait_first_visible(self, page, selectors, timeout=12.0):
        """Poll for any of the selectors to become visible (JS-rendered forms)."""
        import time as _t
        deadline = _t.time() + timeout
        while _t.time() < deadline:
            el, sel = await self._first_visible(page, selectors)
            if el:
                return el, sel
            await asyncio.sleep(0.4)
        return None, None

    async def _find_submit_in_form(self, field_el):
        """Find the submit control in the SAME form as field_el, skipping
        reset/forgot buttons. Falls back to a page-wide search."""
        # scope to the ancestor <form> of the password field
        try:
            form = field_el.locator("xpath=ancestor::form[1]")
            if await form.count():
                for sel in ["input[type='submit']", "button[type='submit']",
                            "button:has-text('Log in')",
                            "button:has-text('Sign in')",
                            "input[type='button']"]:
                    cand = form.locator(sel).first
                    try:
                        if await cand.count() and await cand.is_visible():
                            # skip obvious reset/forgot controls
                            blob = " ".join(filter(None, [
                                await cand.get_attribute("id") or "",
                                await cand.get_attribute("name") or "",
                                await cand.get_attribute("value") or "",
                                (await cand.text_content()) or "",
                            ])).lower()
                            if any(w in blob for w in
                                   ("reset", "forgot", "forget", "cancel")):
                                continue
                            return cand
                    except Exception:
                        continue
        except Exception:
            pass
        # fallback: page-wide, but still skip reset/forgot
        for sel in self.SUBMIT_SELECTORS:
            el = field_el.page.locator(sel).first
            try:
                if await el.count() and await el.is_visible():
                    blob = " ".join(filter(None, [
                        await el.get_attribute("id") or "",
                        await el.get_attribute("value") or "",
                        (await el.text_content()) or "",
                    ])).lower()
                    if any(w in blob for w in ("reset", "forgot", "forget")):
                        continue
                    return el
            except Exception:
                continue
        return None

    async def _needs_extra_auth(self, page):
        # still on a login-ish URL?
        url = page.url.lower()
        url_login_ish = any(k in url for k in
                            ("login", "signin", "sign-in", "auth", "mfa",
                             "2fa", "otp", "verify", "challenge"))
        # any OTP/CAPTCHA element visible?
        el, marker = await self._first_visible(page, self.EXTRA_AUTH_SELECTORS)
        # password field still visible = login probably didn't go through
        pw, _ = await self._first_visible(page, self.PASS_SELECTORS)
        return bool(el) or bool(pw) or url_login_ish, marker

    async def _pause_for_human(self, why):
        print("\n" + "=" * 60)
        print(f"  ACTION NEEDED: {why}")
        print("  Finish it in the browser window (2FA code, CAPTCHA, etc).")
        print("  Then come back here and press ENTER to continue crawling.")
        print("=" * 60)
        await asyncio.get_event_loop().run_in_executor(None, input)

    async def _reseed_after_login(self, page):
        """After login, seed the queue from the page we landed on. If login left
        us on a browser error page (chrome-error://...) or a blank/non-app page,
        recover by navigating straight to the target app -- we're authenticated
        now, so the cookies carry over."""
        # let a heavy SPA finish loading before we read the URL / DOM
        try:
            await page.wait_for_load_state("networkidle",
                                           timeout=self.cfg.nav_timeout_ms)
        except Exception:
            pass
        await asyncio.sleep(1.5)  # small grace for late client-side rendering

        # After a MANUAL login you may have ended up in a different tab, or the
        # app opened a new one. Look across all open tabs and switch to the one
        # that's actually on an in-scope http(s) page.
        try:
            for cand in reversed(context_pages := page.context.pages):
                cu = self.normalize(cand.url or "")
                if cu.startswith(("http://", "https://")) \
                        and not cu.startswith("chrome-error") \
                        and self.in_scope(cu):
                    if cand is not page:
                        print(f"[+] Using the tab you logged into: {cu}")
                        self.nb.note("login_tab_switch", url=cu)
                    page = cand
                    break
        except Exception:
            pass

        landed = self.normalize(page.url or "")
        # Recover from a failed/interrupted post-login navigation.
        bad = (not landed.startswith(("http://", "https://"))
               or landed.startswith("chrome-error")
               or landed in ("about:blank",))
        if bad:
            print(f"[!] login landed on a broken page ({landed or 'blank'}); "
                  f"navigating to the target app instead...")
            self.nb.note("login_landing_recover", bad_url=landed)
            for attempt in (1, 2):
                try:
                    await page.goto(self.cfg.seed,
                                    timeout=self.cfg.nav_timeout_ms,
                                    wait_until="networkidle")
                    await asyncio.sleep(1.0)
                    landed = self.normalize(page.url or "")
                    if landed.startswith(("http://", "https://")) \
                            and not landed.startswith("chrome-error"):
                        break
                except Exception as e:
                    self.nb.note("reseed_recover_error", attempt=attempt,
                                 error=str(e))
                    await asyncio.sleep(1.5)
            if not landed.startswith(("http://", "https://")) \
                    or landed.startswith("chrome-error"):
                print("[!] still couldn't load the target app after login. "
                      "The seed URL may be wrong, or the app errored.")
                self.nb.note("reseed_failed", url=landed)
                return

        try:
            host = urlparse(landed).netloc
        except Exception:
            return
        if self.scope.allows(landed) is False:
            print(f"[!] post-login landing {landed} is OUT of scope; not crawling it.")
            self.nb.note("scope_skip", url=landed, reason="excluded post-login")
            return
        if self.scope.has_includes() and self.scope.allows(landed) is not True:
            print(f"[!] post-login host {host} not in scope file; skipping it.")
            self.nb.note("scope_skip", host=host, reason="not in include rules")
            return
        if host and host not in self.allowed_hosts:
            self.allowed_hosts.add(host)
            self.nb.note("scope_add", host=host, reason="post-login redirect")
            print(f"[+] Added post-login host to scope: {host}")
        # Seed the landing page itself (unless it's already queued)...
        already = any(self.normalize(u) == landed for u, _ in self.queue)
        if landed and landed not in self.seen_pages and not already:
            self.queue.appendleft((landed, 0))
            self.nb.note("reseed", url=landed)
        # ...AND extract the links already on it right now, so the queue isn't
        # empty even if the worker later re-navigates and hits SPA timing.
        try:
            found = await self.extract(page, landed)
            n = 0
            for link in found:
                if self.in_scope(link) and link not in self.seen_pages:
                    self.queue.append((link, 1))
                    n += 1
            print(f"[+] Seeded {n} in-scope link(s) from {host}.")
            self.nb.note("reseed_links", count=n)
        except Exception as e:
            self.nb.note("reseed_extract_error", error=str(e))

    async def _handle_login(self, page):
        login_target = self.cfg.login_url or self.cfg.seed

        # ---- Mode 1: fully manual (open + wait) ----
        if self.cfg.pause_for_login:
            # honor a login_url from cred.txt even in manual mode, if present
            target = login_target
            creds = read_creds(self.cfg.creds_file) if self.cfg.creds_file else {}
            if creds.get("login_url"):
                target = creds["login_url"]
            try:
                await page.goto(target, timeout=self.cfg.nav_timeout_ms)
            except Exception as e:
                self.nb.note("login_nav_error", url=target, error=str(e))
            # show the identifier/password so you can copy them while logging in
            if creds.get("email"):
                print(f"\n    username/email: {creds['email']}")
            if creds.get("password"):
                print(f"    password:       {creds['password']}")
            await self._pause_for_human(
                "Log in FULLY in the browser (username, password, 2FA - all of it)")
            self.nb.note("login", mode="manual", ok=True)
            await self._reseed_after_login(page)
            return

        # ---- Mode 2: smart (creds file + conditional pause) ----
        if self.cfg.smart_login:
            creds = read_creds(self.cfg.creds_file)
            if not creds.get("email") or not creds.get("password"):
                print("[!] cred.txt missing email/password.")
                self.nb.note("login", mode="smart", ok=False, reason="no creds")
                return
            target = creds.get("login_url") or login_target
            try:
                await page.goto(target, timeout=self.cfg.nav_timeout_ms,
                                wait_until="domcontentloaded")
            except Exception as e:
                self.nb.note("login_nav_error", url=target, error=str(e))

            # fill username (WAIT for it - login forms are often JS-rendered)
            user_el, usel = await self._wait_first_visible(
                page, self.USER_SELECTORS, timeout=15.0)
            if not user_el:
                print("[!] couldn't find a username/email field after waiting. "
                      "Falling back to manual login.")
                await self._pause_for_human("Log in manually (autofill failed)")
                self.nb.note("login", mode="smart", ok=True, fallback="manual")
                await self._reseed_after_login(page)
                return
            await user_el.fill(creds["email"])

            # Password may be on the same page, OR revealed only after a
            # "Next"/"Continue" step that VERIFIES the username first (common in
            # enterprise apps). Try same-page first; if absent, submit the
            # username and WAIT (poll) for the password field to appear.
            pass_el, psel = await self._first_visible(page, self.PASS_SELECTORS)
            if not pass_el:
                nxt = await self._find_submit_in_form(user_el)
                if not nxt:
                    nxt, _ = await self._first_visible(page, self.SUBMIT_SELECTORS)
                if nxt:
                    self.nb.note("login", mode="smart", step="submit_username")
                    print("[+] Submitted username; waiting for the password step...")
                    try:
                        await nxt.click(no_wait_after=True, timeout=8000)
                    except Exception:
                        try:
                            await user_el.press("Enter")
                        except Exception:
                            pass
                    # wait for the app to verify the username and render the
                    # password field (poll up to ~20s instead of a fixed 1.5s)
                    try:
                        await page.wait_for_load_state("networkidle", timeout=8000)
                    except Exception:
                        pass
                    pass_el, psel = await self._wait_first_visible(
                        page, self.PASS_SELECTORS, timeout=20.0)
                    if not pass_el:
                        # maybe it's an extra step we can't auto-fill (2FA, etc.)
                        print("[!] password field didn't appear after the "
                              "username step. Handing over to you.")
                        await self._pause_for_human(
                            "Enter the password (and any 2FA) in the browser")
                        self.nb.note("login", mode="smart", ok=True,
                                     fallback="manual after username")
                        await self._reseed_after_login(page)
                        return
            if pass_el:
                await pass_el.fill(creds["password"])
                self.nb.note("login", mode="smart", step="filled",
                             user_sel=usel, pass_sel=psel)
                # Find the submit control INSIDE the same form as the password
                # field, so we don't hit a stray "Reset Password" / "Forgot"
                # button elsewhere on the page.
                submit = await self._find_submit_in_form(pass_el)
                try:
                    if submit:
                        # no_wait_after: login navigates away, so don't wait for
                        # the (now detached) button to settle after clicking.
                        await submit.click(no_wait_after=True, timeout=8000)
                    else:
                        await pass_el.press("Enter")
                except Exception as e:
                    # click may "fail" simply because navigation started -
                    # that's fine; fall back to Enter just in case.
                    self.nb.note("login", mode="smart", submit_note=str(e))
                    try:
                        await pass_el.press("Enter")
                    except Exception:
                        pass

            # give the site a moment to process
            try:
                await page.wait_for_load_state("networkidle",
                                               timeout=self.cfg.nav_timeout_ms)
            except Exception:
                pass

            # decide: did creds alone work, or is there another step?
            needs, marker = await self._needs_extra_auth(page)
            if needs:
                self.nb.note("login", mode="smart", extra_auth=True,
                             marker=marker, url=page.url)
                await self._pause_for_human(
                    f"Extra verification detected ({marker or 'login not complete'})")
                self.nb.note("login", mode="smart", ok=True, after="manual step")
            else:
                print("[+] Login succeeded with credentials alone. Crawling...")
                self.nb.note("login", mode="smart", ok=True, after="creds only")
            await self._reseed_after_login(page)
            return

        # ---- Mode 3: legacy explicit-selector auto-login (env vars) ----
        if self.cfg.auto_login:
            import os
            user = os.environ.get("RECON_USER")
            pw = os.environ.get("RECON_PASS")
            if not (user and pw and self.cfg.user_selector
                    and self.cfg.pass_selector):
                self.nb.note("login", mode="auto", ok=False,
                             reason="missing creds or selectors")
                return
            try:
                await page.goto(login_target, timeout=self.cfg.nav_timeout_ms)
                await page.fill(self.cfg.user_selector, user)
                await page.fill(self.cfg.pass_selector, pw)
                if self.cfg.submit_selector:
                    await page.click(self.cfg.submit_selector)
                else:
                    await page.press(self.cfg.pass_selector, "Enter")
                await page.wait_for_load_state("networkidle",
                                               timeout=self.cfg.nav_timeout_ms)
                self.nb.note("login", mode="auto", ok=True)
            except Exception as e:
                self.nb.note("login", mode="auto", ok=False, error=str(e))

    # -- main loop (parallel worker pool) -----------------------------------
    async def crawl(self):
        async with async_playwright() as p:
            attached = False
            if self.cfg.attach_port:
                # Attach to a Chrome the USER launched in debug mode. The site
                # only ever sees a genuine, human-driven browser -> beats
                # bot-detection and version-mismatch launch problems.
                port = self.cfg.attach_port
                browser = None
                _last = None
                for host in ("localhost", "127.0.0.1"):
                    endpoint = f"http://{host}:{port}"
                    print(f"[+] Attaching to your Chrome at {endpoint} ...")
                    try:
                        browser = await p.chromium.connect_over_cdp(endpoint)
                        break
                    except Exception as e:
                        _last = e
                        print(f"    ({host} failed, trying next)")
                if browser is None:
                    raise _last
                context = browser.contexts[0] if browser.contexts \
                    else await browser.new_context()
                attached = True
            else:
                # Flags that make the automated browser behave like a normal one.
                stealth_args = [
                    "--disable-blink-features=AutomationControlled",
                    "--no-default-browser-check",
                    "--no-first-run",
                    "--start-maximized",
                ]
                launch_kwargs = dict(headless=self.cfg.headless)
                if self.cfg.user_data_dir:
                    launch_kwargs.update(
                        user_data_dir=self.cfg.user_data_dir,
                        channel="chrome",
                        args=stealth_args + [
                            f"--profile-directory={self.cfg.profile_directory}"],
                        ignore_default_args=["--enable-automation"],
                        viewport=None,
                    )
                    context = await p.chromium.launch_persistent_context(**launch_kwargs)
                else:
                    browser = await p.chromium.launch(
                        headless=self.cfg.headless, channel="chrome",
                        args=stealth_args,
                        ignore_default_args=["--enable-automation"])
                    context = await browser.new_context(viewport=None)

            # hide navigator.webdriver so sites can't trivially detect automation
            try:
                await context.add_init_script(
                    "Object.defineProperty(navigator,'webdriver',{get:()=>undefined});")
            except Exception:
                pass

            self._wire_network(context)
            context.on("console", lambda m: (
                self.console.append({"type": m.type, "text": m.text}),
                self.nb.note("console", type=m.type, text=m.text)))

            # one page for login; auth (cookies) is shared across the context
            login_page = context.pages[0] if context.pages \
                else await context.new_page()
            self.nb.note("start", seed=self.cfg.seed, host=self.host,
                         workers=self.cfg.concurrency, attached=attached)
            if attached:
                # In attach mode you've ALREADY logged in by hand in that Chrome.
                # Skip auto-login; just seed from wherever you are / the target.
                print("[+] Using your existing logged-in session. Seeding crawl...")
                await self._reseed_after_login(login_page)
            else:
                await self._handle_login(login_page)

            # move whatever is queued (seed + post-login landing) into an
            # asyncio queue the workers share
            self._aqueue = asyncio.Queue()
            for item in self.queue:
                self._aqueue.put_nowait(item)
            self.queue.clear()

            # spawn N worker tabs
            n = max(1, self.cfg.concurrency)
            pages = [login_page]
            for _ in range(n - 1):
                pages.append(await context.new_page())

            workers = [asyncio.create_task(self._worker(pg, i))
                       for i, pg in enumerate(pages)]

            # wait until the queue is fully drained, then stop the workers
            await self._aqueue.join()
            for w in workers:
                w.cancel()
            await asyncio.gather(*workers, return_exceptions=True)

            # crawling done -> now mine the JS files for hidden endpoints,
            # using the authenticated browser so we can fetch in-scope scripts.
            if self.cfg.mine_js and self.js_files:
                await self._mine_js_files(context)

            self.nb.note("done", pages=len(self.seen_pages),
                         js_endpoints=len(self.js_endpoints))
            if not attached:
                await context.close()
            else:
                print("[+] Done. Your Chrome stays open (attach mode).")

    async def _worker(self, page, wid):
        """One parallel crawler tab pulling URLs from the shared queue."""
        while True:
            url, depth = await self._aqueue.get()
            try:
                url = self.normalize(url)
                # stop conditions
                if url in self.seen_pages:
                    continue
                # HARD scope gate: never visit an out-of-scope URL, no matter
                # how it got into the queue (seed, reseed, discovered link).
                if not self.in_scope(url):
                    self.nb.note("scope_skip", url=url, worker=wid)
                    continue
                if self.cfg.max_depth >= 0 and depth > self.cfg.max_depth:
                    continue
                if len(self.seen_pages) >= self.cfg.max_pages:
                    continue
                # claim it (sync set op = atomic between awaits, no double-crawl)
                self.seen_pages.add(url)

                try:
                    await page.goto(url, timeout=self.cfg.nav_timeout_ms,
                                    wait_until="networkidle")
                except Exception as e:
                    self.nb.note("nav_error", url=url, error=str(e), worker=wid)
                    continue

                self.nb.note("page", url=url, depth=depth, worker=wid,
                             title=await page.title())
                new_links = await self.extract(page, url)
                if self.cfg.interact:
                    new_links |= await self._interact(page, url)

                for link in new_links:
                    if self.in_scope(link) and link not in self.seen_pages:
                        self._aqueue.put_nowait((link, depth + 1))

                if self.cfg.request_delay:
                    await asyncio.sleep(self.cfg.request_delay)
            except asyncio.CancelledError:
                # let cancellation propagate after marking the task done
                self._aqueue.task_done()
                raise
            finally:
                # every get() must be matched by task_done() or join() hangs
                if not asyncio.current_task().cancelled():
                    self._aqueue.task_done()

    # -- JS mining: pull hidden endpoints out of script files ---------------
    # Endpoint-ish strings: absolute URLs, and paths like /api/v3/foo
    _RE_ENDPOINT = re.compile(
        r"""["'`]"""                                  # opening quote
        r"""(                                          
            https?://[^\s"'`]+                         # full URL
          | /(?:[A-Za-z0-9_\-./]+)?                    # or an absolute path
            (?:api|v\d|graphql|rest|internal|admin|user|account|auth|
               token|upload|download|export|webhook|callback)
            [A-Za-z0-9_\-./]*                          # ...containing a keyword
          | /[A-Za-z0-9_\-]+/[A-Za-z0-9_\-./]{2,}      # or any 2+ segment path
        )"""
        r"""["'`]""",                                  # closing quote
        re.VERBOSE)
    # Very rough "possible secret" spotters (keys/tokens hardcoded in JS)
    _RE_SECRETS = [
        ("AWS key",        re.compile(r"AKIA[0-9A-Z]{16}")),
        ("Google API key", re.compile(r"AIza[0-9A-Za-z_\-]{35}")),
        ("Slack token",    re.compile(r"xox[baprs]-[0-9A-Za-z\-]{10,}")),
        ("Bearer/JWT",     re.compile(r"eyJ[A-Za-z0-9_\-]{10,}\.[A-Za-z0-9_\-]{10,}\.[A-Za-z0-9_\-]{6,}")),
        ("Generic api_key",re.compile(r"""(?i)(?:api[_-]?key|secret|token)["']?\s*[:=]\s*["'][A-Za-z0-9_\-]{16,}["']""")),
    ]

    async def _fetch_text(self, context, url):
        """Fetch a URL's text using the browser's authenticated session."""
        try:
            resp = await context.request.get(url, timeout=self.cfg.nav_timeout_ms)
            if resp.ok:
                return await resp.text()
        except Exception as e:
            self.nb.note("js_fetch_error", url=url, error=str(e))
        return None

    async def _mine_js_files(self, context):
        js = sorted(self.js_files)
        print(f"[+] Mining {len(js)} JavaScript file(s) for hidden endpoints...")
        self.nb.note("js_mine_start", count=len(js))
        for src in js:
            body = await self._fetch_text(context, src)
            if not body:
                continue
            found = set()
            for m in self._RE_ENDPOINT.finditer(body):
                ep = m.group(1)
                # normalize relative endpoints against the JS file's origin
                if ep.startswith("/"):
                    origin = "{0.scheme}://{0.netloc}".format(urlparse(src))
                    ep_abs = origin + ep
                else:
                    ep_abs = ep
                found.add(ep)
                # if the resolved endpoint is in scope, treat it as a real lead
                if self.in_scope(ep_abs):
                    if ep_abs not in self.links:
                        self.links.add(ep_abs)
                self.js_endpoints.add(ep)
            # secret spotting
            for label, rx in self._RE_SECRETS:
                for sm in rx.finditer(body):
                    snippet = sm.group(0)
                    self.js_secrets.append({"type": label, "file": src,
                                            "match": snippet[:80]})
                    self.nb.note("js_secret", type=label, file=src,
                                 match=snippet[:80])
            if found:
                self.nb.note("js_mined", file=src, endpoints=len(found))
        print(f"[+] JS mining done: {len(self.js_endpoints)} endpoint string(s), "
              f"{len(self.js_secrets)} possible secret(s).")
        self.nb.note("js_mine_done", endpoints=len(self.js_endpoints),
                     secrets=len(self.js_secrets))

    def result(self):
        return {
            "seed": self.cfg.seed,
            "host": self.host,
            "pages_crawled": sorted(self.seen_pages),
            "links": sorted(self.links),
            "js_files": sorted(self.js_files),
            "js_endpoints": sorted(self.js_endpoints),
            "js_secrets": self.js_secrets,
            "forms": self.forms,
            "params": sorted(self.params),
            "requests": self.requests,
            "responses": [{k: v for k, v in r.items() if k != "body"}
                          for r in self.responses],  # bodies stay in notebook
            "console": self.console,
            "storage": self.storage,
        }

    def ai_report(self):
        """
        A compact, deduplicated, self-describing view built for an LLM to
        extract from. Key differences vs the raw report:
          - deduplicated endpoints (method + path, host-relative)
          - a short 'schema' block so the AI knows what each field means
          - counts + capped lists so it fits in a context window
          - everything grouped by the attack-surface category it belongs to
        """
        from urllib.parse import urlparse as _up

        def rel(u):
            p = _up(u)
            return (p.path or "/") + (("?" + p.query) if p.query else "")

        # Deduplicate network calls into unique "METHOD /path" endpoints,
        # grouped by host, with the set of params seen on each.
        endpoints = {}
        for req in self.requests:
            u = _up(req["url"])
            key = f'{req["method"]} {u.path}'
            host = u.netloc
            e = endpoints.setdefault((host, key), {"host": host,
                    "method": req["method"], "path": u.path,
                    "params": set(), "resource_type": req.get("resource_type")})
            for pair in (u.query or "").split("&"):
                if "=" in pair and pair.split("=")[0]:
                    e["params"].add(pair.split("=")[0])
        endpoint_list = []
        for e in endpoints.values():
            e = dict(e)
            e["params"] = sorted(e["params"])
            endpoint_list.append(e)
        endpoint_list.sort(key=lambda x: (x["host"], x["path"], x["method"]))

        # Interesting responses: non-200s are usually the useful signal
        notable = [{"status": r["status"], "url": rel(r["url"]),
                    "content_type": r.get("headers", {}).get("content-type", "")}
                   for r in self.responses if r["status"] >= 400]

        forms = [{"method": (f.get("method") or "get").upper(),
                  "action": f.get("action", ""),
                  "found_on": f.get("found_on", ""),
                  "fields": [i["name"] for i in f.get("inputs", []) if i.get("name")]}
                 for f in self.forms]

        return {
            "schema": {
                "_description": "Recon crawl of a web app, structured for AI "
                                "extraction. All lists are deduplicated.",
                "target": "the seed URL and hosts that were in scope",
                "endpoints": "unique API/page endpoints as METHOD + path, with "
                             "query params seen; the primary attack surface",
                "forms": "HTML forms with their field names (input points)",
                "params": "all URL parameter names seen anywhere",
                "js_endpoints": "paths found INSIDE javascript, not linked on "
                                "pages (often hidden/admin/internal)",
                "js_secrets": "heuristic secret matches in JS - verify, many "
                              "are false positives",
                "notable_responses": "HTTP responses with status >= 400",
                "storage": "localStorage/sessionStorage keys per page - may "
                           "hold tokens/config",
            },
            "target": {
                "seed": self.cfg.seed,
                "hosts_in_scope": sorted(self.allowed_hosts),
                "crawled_at": time.strftime("%Y-%m-%d %H:%M:%S"),
            },
            "counts": {
                "pages": len(self.seen_pages),
                "endpoints": len(endpoint_list),
                "forms": len(forms),
                "params": len(self.params),
                "js_files": len(self.js_files),
                "js_endpoints": len(self.js_endpoints),
                "js_secrets": len(self.js_secrets),
                "notable_responses": len(notable),
            },
            "pages": sorted(self.seen_pages),
            "endpoints": endpoint_list,
            "forms": forms,
            "params": sorted(self.params),
            "js_endpoints": sorted(self.js_endpoints),
            "js_secrets": self.js_secrets,
            "notable_responses": notable,
            "storage": {u: {"local": list(s.get("local", {}).keys()),
                            "session": list(s.get("session", {}).keys())}
                        for u, s in self.storage.items()},
        }

    def write_summary(self, path):
        """Write a clean, human-readable Markdown report of the crawl."""
        r = self.result()
        # unique API-ish endpoints (XHR/fetch/api paths), method + url
        api = sorted({f"{req['method']} {req['url']}"
                      for req in self.requests
                      if req.get("resource_type") in ("xhr", "fetch")
                      or "/api" in req["url"]})
        # group response statuses
        status_counts = {}
        for resp in self.responses:
            status_counts[resp["status"]] = status_counts.get(resp["status"], 0) + 1

        L = []
        w = L.append
        w(f"# Recon summary — {r['host']}")
        w("")
        w(f"- **Target seed:** {r['seed']}")
        w(f"- **Crawled at:** {time.strftime('%Y-%m-%d %H:%M:%S')}")
        w(f"- **Hosts in scope:** {', '.join(sorted(self.allowed_hosts))}")
        w("")
        w("## At a glance")
        w("")
        w(f"| What | Count |")
        w(f"|------|------:|")
        w(f"| Pages crawled | {len(r['pages_crawled'])} |")
        w(f"| Links found | {len(r['links'])} |")
        w(f"| API / XHR endpoints | {len(api)} |")
        w(f"| Forms | {len(r['forms'])} |")
        w(f"| URL parameters | {len(r['params'])} |")
        w(f"| JavaScript files | {len(r['js_files'])} |")
        w(f"| Hidden endpoints (from JS) | {len(r['js_endpoints'])} |")
        w(f"| Possible secrets in JS | {len(r['js_secrets'])} |")
        w(f"| Pages with storage data | {len(r['storage'])} |")
        w("")

        if status_counts:
            w("## Response status codes")
            w("")
            for code in sorted(status_counts):
                w(f"- **{code}** — {status_counts[code]} response(s)")
            w("")

        w("## Pages crawled")
        w("")
        for u in r["pages_crawled"]:
            w(f"- {u}")
        w("")

        if api:
            w("## API / XHR endpoints (likely the interesting ones)")
            w("")
            for e in api:
                w(f"- `{e}`")
            w("")

        if r["forms"]:
            w("## Forms (possible input / injection points)")
            w("")
            for f in r["forms"]:
                fields = ", ".join(i["name"] for i in f.get("inputs", []) if i.get("name"))
                w(f"- **{f.get('method','get').upper()}** `{f.get('action','')}`")
                w(f"  - on: {f.get('found_on','')}")
                if fields:
                    w(f"  - fields: {fields}")
            w("")

        if r["params"]:
            w("## URL parameters seen")
            w("")
            w(", ".join(f"`{p}`" for p in r["params"]))
            w("")

        if r["js_files"]:
            w("## JavaScript files (worth mining for hidden endpoints)")
            w("")
            for j in r["js_files"]:
                w(f"- {j}")
            w("")

        if r["js_endpoints"]:
            w("## Hidden endpoints extracted from JavaScript")
            w("")
            w("These paths/URLs were found *inside* the JS bundles — they are "
              "not linked anywhere on the pages, so they're prime recon leads:")
            w("")
            for e in r["js_endpoints"]:
                w(f"- `{e}`")
            w("")

        if r["js_secrets"]:
            w("## ⚠️ Possible secrets spotted in JavaScript")
            w("")
            w("Heuristic matches — verify by hand, many are false positives, "
              "and treat anything real as sensitive:")
            w("")
            for s in r["js_secrets"]:
                w(f"- **{s['type']}** in {s['file']}")
                w(f"  - `{s['match']}`")
            w("")

        if r["storage"]:
            w("## Browser storage found (may leak tokens / config)")
            w("")
            for url, store in r["storage"].items():
                lk = ", ".join(store.get("local", {}).keys())
                sk = ", ".join(store.get("session", {}).keys())
                w(f"- {url}")
                if lk: w(f"  - localStorage keys: {lk}")
                if sk: w(f"  - sessionStorage keys: {sk}")
            w("")

        w("---")
        w("*Full machine-readable detail is in `report.json`; "
          "the live event log is in `notebook.jsonl`.*")

        Path(path).write_text("\n".join(L), encoding="utf-8")


# ---- Profile aliases -------------------------------------------------------
# Define your Chrome profiles ONCE here (or in profiles.json next to this file),
# then refer to them by short name: "A", "work", "bugbounty", etc.
#
# Find the path in Chrome by visiting chrome://version and copying
# "Profile Path" -- the parent is the user_data_dir, the last folder is the name.
DEFAULT_PROFILES = {
    # "A": {
    #     "user_data_dir": "/Users/you/Library/Application Support/Google/Chrome",
    #     "profile_directory": "Default",
    # },
    # "bugbounty": {
    #     "user_data_dir": "/Users/you/Library/Application Support/Google/Chrome",
    #     "profile_directory": "Profile 1",
    # },
}


def load_profiles():
    """Merge DEFAULT_PROFILES with an optional profiles.json beside the script."""
    profiles = dict(DEFAULT_PROFILES)
    pjson = Path(__file__).parent / "profiles.json"
    if pjson.exists():
        try:
            profiles.update(json.loads(pjson.read_text()))
        except Exception as e:
            print(f"[!] could not read profiles.json: {e}")
    return profiles


def resolve_profile(profile):
    """Accept an alias ('A'), a full path, or None. Return (user_data_dir, name)."""
    if not profile:
        return None, "Default"
    profiles = load_profiles()
    if profile in profiles:
        p = profiles[profile]
        return p["user_data_dir"], p.get("profile_directory", "Default")
    # not an alias -> treat it as a raw path
    return profile, "Default"


def read_creds(path):
    """
    Read credentials from a simple text file. Supported formats:

        # use EITHER email or username for the login identifier:
        email=you@example.com
        username=yourname
        password=secret
        login_url=https://externalbeta2.emaplan.com/ema   (optional)

    OR just two bare lines (identifier on line 1, password on line 2).

    After reading, creds["email"] always holds whatever identifier was given
    (email OR username), so the rest of the code can stay simple.
    """
    creds = {}
    p = Path(path or "cred.txt")
    if not p.exists():
        print(f"[!] creds file not found: {p}")
        return creds
    lines = [l.strip() for l in p.read_text().splitlines()
             if l.strip() and not l.strip().startswith("#")]
    if any("=" in l for l in lines):
        for l in lines:
            if "=" in l:
                k, v = l.split("=", 1)
                creds[k.strip().lower()] = v.strip()
    else:  # bare two-line format
        if len(lines) >= 2:
            creds["email"], creds["password"] = lines[0], lines[1]
    # normalize: several keys can supply the login identifier
    if not creds.get("email"):
        for alias in ("username", "user", "login", "identifier", "id"):
            if creds.get(alias):
                creds["email"] = creds[alias]
                break
    return creds


async def crawl(target, profile=None, *, depth=-1, max_pages=1000,
                subdomains=True, login=False, creds_file=None,
                isolated_dir=None, interact=True, concurrency=5,
                scope_file=None, mine_js=True, attach_port=None):
    """
    Dead-simple entry point for your harness.

        await crawl("app.smtp2go.com", creds_file="cred.txt",
                    isolated_dir="~/recon-chrome")

    depth=-1 means UNLIMITED depth (follow links as deep as they go).
    interact=True clicks SPA nav elements to surface routes with no <a href>.
    """
    if not target.startswith(("http://", "https://")):
        target = "https://" + target
    if isolated_dir:
        user_data_dir = str(Path(isolated_dir).expanduser())
        profile_directory = "Default"
    else:
        user_data_dir, profile_directory = resolve_profile(profile)
    cfg = CrawlConfig(
        seed=target, user_data_dir=user_data_dir,
        profile_directory=profile_directory,
        max_depth=depth, max_pages=max_pages, allow_subdomains=subdomains,
        interact=interact, concurrency=concurrency, scope_file=scope_file,
        mine_js=mine_js, attach_port=attach_port,
        pause_for_login=login,
        # if --login (manual) is set, don't also run smart autofill; but still
        # keep creds_file so manual mode can read login_url + show credentials.
        smart_login=bool(creds_file) and not login,
        creds_file=creds_file,
        headless=False if (login or creds_file) else CrawlConfig.headless)
    return await run_crawl(cfg)


async def run_crawl(cfg: CrawlConfig):
    """Entry point for a harness. Returns the structured result dict."""
    # Organize notes per-domain: output/<host>/<timestamp>/{notebook,report}
    if not cfg.notebook_path or not cfg.report_path:
        host = urlparse(cfg.seed).netloc.replace(":", "_")
        stamp = time.strftime("%Y%m%d-%H%M%S")
        run_dir = Path(cfg.output_root) / host / stamp
        run_dir.mkdir(parents=True, exist_ok=True)
        cfg.notebook_path = cfg.notebook_path or str(run_dir / "notebook.jsonl")
        cfg.report_path = cfg.report_path or str(run_dir / "report.json")
        print(f"[+] Notes for {host} -> {run_dir}")

    crawler = ReconCrawler(cfg)
    try:
        await crawler.crawl()
    finally:
        crawler.nb.close()
    result = crawler.result()
    Path(cfg.report_path).write_text(json.dumps(result, indent=2,
                                                 ensure_ascii=False))
    # human-readable summary next to the JSON report
    summary_path = str(Path(cfg.report_path).with_name("summary.md"))
    try:
        crawler.write_summary(summary_path)
        print(f"[+] Readable summary: {summary_path}")
    except Exception as e:
        print(f"[!] could not write summary: {e}")
    # compact, structured report built for feeding to an AI
    ai_path = str(Path(cfg.report_path).with_name("ai_report.json"))
    try:
        Path(ai_path).write_text(
            json.dumps(crawler.ai_report(), indent=2, ensure_ascii=False))
        size_kb = Path(ai_path).stat().st_size / 1024
        print(f"[+] AI-friendly report: {ai_path}  ({size_kb:.0f} KB)")
    except Exception as e:
        print(f"[!] could not write AI report: {e}")
    return result


def _cli():
    ap = argparse.ArgumentParser(
        description="Recon crawler. Short form: recon_crawler.py <target> [profile]")
    ap.add_argument("target", help="domain or URL, e.g. app.smtp2go.com")
    ap.add_argument("profile", nargs="?", default=None,
                    help="profile alias (from profiles.json) or path. Optional.")
    ap.add_argument("--depth", type=int, default=-1,
                    help="link depth to follow; -1 = unlimited (default)")
    ap.add_argument("--max-pages", type=int, default=1000)
    ap.add_argument("--attach", dest="attach_port", type=int, metavar="PORT",
                    help="attach to a Chrome you launched with "
                         "--remote-debugging-port=PORT (you log in by hand there)")
    ap.add_argument("--scope", dest="scope_file", nargs="?", const="scope.txt",
                    help="scope file (default scope.txt) with include/exclude "
                         "rules; excluded URLs are always skipped")
    ap.add_argument("--workers", type=int, default=5,
                    help="parallel worker tabs (default 5). Higher = faster "
                         "but heavier on the target and your machine.")
    ap.add_argument("--no-subdomains", action="store_true")
    ap.add_argument("--no-interact", action="store_true",
                    help="don't click SPA elements (link-following only)")
    ap.add_argument("--no-mine-js", action="store_true",
                    help="skip fetching JS files to extract hidden endpoints")
    ap.add_argument("--headless", action="store_true")
    ap.add_argument("--login", action="store_true",
                    help="open browser, wait for you to log in fully, then crawl")
    ap.add_argument("--creds", dest="creds_file", nargs="?", const="cred.txt",
                    help="smart login from a creds file (default cred.txt): "
                         "auto-fills email/password, pauses only for 2FA/CAPTCHA")
    ap.add_argument("--isolated-dir",
                    help="persistent browser dir (e.g. ~/recon-chrome); "
                         "log in once, session persists, won't touch your Chrome")
    a = ap.parse_args()

    result = asyncio.run(crawl(
        a.target, profile=a.profile, depth=a.depth,
        max_pages=a.max_pages, subdomains=not a.no_subdomains,
        login=a.login, creds_file=a.creds_file, isolated_dir=a.isolated_dir,
        interact=not a.no_interact, concurrency=a.workers,
        scope_file=a.scope_file, mine_js=not a.no_mine_js,
        attach_port=a.attach_port))
    print(f"\nDone. {len(result['pages_crawled'])} pages crawled.")


if __name__ == "__main__":
    _cli()