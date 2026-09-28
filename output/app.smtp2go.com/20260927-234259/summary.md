# Recon summary — app.smtp2go.com

- **Target seed:** https://app.smtp2go.com
- **Crawled at:** 2026-09-27 23:44:04
- **Hosts in scope:** app-us.smtp2go.com, app.smtp2go.com

## At a glance

| What | Count |
|------|------:|
| Pages crawled | 2 |
| Links found | 5 |
| API / XHR endpoints | 7 |
| Forms | 2 |
| URL parameters | 6 |
| JavaScript files | 10 |
| Hidden endpoints (from JS) | 1 |
| Possible secrets in JS | 0 |
| Pages with storage data | 0 |

## Response status codes

- **200** — 51 response(s)
- **302** — 4 response(s)
- **308** — 1 response(s)

## Pages crawled

- https://app-us.smtp2go.com/dashboard/main
- https://app.smtp2go.com

## API / XHR endpoints (likely the interesting ones)

- `GET https://app-us.smtp2go.com/api/dashboard/main/?unix_secs_start=1787875200&unix_secs_end=1790553599`
- `GET https://app-us.smtp2go.com/api/dashboard/notices/?unix_secs_start=1787875200&unix_secs_end=1790553599`
- `GET https://app-us.smtp2go.com/api/dashboard/usage/?unix_secs_start=1787875200&unix_secs_end=1790553599`
- `GET https://app-us.smtp2go.com/end-points`
- `POST https://app-us.smtp2go.com/api/login`
- `POST https://app-us.smtp2go.com/zdesk_chat_auth?CSRF_key=FFddWbDPJrweqR%2FaEh4lSCldNDK%2Fc%2BTx%2Fzdh2r2VxZ4`
- `POST https://app.smtp2go.com/api/login`

## Forms (possible input / injection points)

- **POST** `https://app.smtp2go.com/api/login/`
  - on: https://app.smtp2go.com
  - fields: red_deep_link, red_deep_query, username, password, remember_me
- **POST** `https://app.smtp2go.com/forgot-password/`
  - on: https://app.smtp2go.com
  - fields: email

## URL parameters seen

`CSRF_key`, `login_id`, `unix_secs_end`, `unix_secs_start`, `v`, `version`

## JavaScript files (worth mining for hidden endpoints)

- https://app.smtp2go.com/static/assets/admin/pages/scripts/login-soft.js?version=1790216816
- https://app.smtp2go.com/static/assets/global/plugins/jquery-1.11.0.min.js?version=1790216816
- https://app.smtp2go.com/static/assets/global/plugins/jquery-migrate-1.2.1.min.js?version=1790216816
- https://app.smtp2go.com/static/assets/global/plugins/jquery-slimscroll/jquery.slimscroll.min.js?version=1790216816
- https://app.smtp2go.com/static/assets/global/plugins/jquery-ui/jquery-ui-1.10.3.custom.min.js?version=1790216816
- https://app.smtp2go.com/static/assets/global/plugins/jquery-validation/js/jquery.validate.min.js?version=1790216816
- https://app.smtp2go.com/static/assets/global/plugins/jquery.blockui.min.js?version=1790216816
- https://app.smtp2go.com/static/assets/global/plugins/moment-timezone-all-years.min.js?version=1790216816
- https://app.smtp2go.com/static/assets/global/plugins/moment.min.js?version=1790216816
- https://app.smtp2go.com/static/js/functions.js?version=1790216816

## Hidden endpoints extracted from JavaScript

These paths/URLs were found *inside* the JS bundles — they are not linked anywhere on the pages, so they're prime recon leads:

- `/dashboard/team/`

---
*Full machine-readable detail is in `report.json`; the live event log is in `notebook.jsonl`.*