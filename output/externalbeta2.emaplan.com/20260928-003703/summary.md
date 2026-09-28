# Recon summary — externalbeta2.emaplan.com

- **Target seed:** https://externalbeta2.emaplan.com/ema
- **Crawled at:** 2026-09-28 00:39:11
- **Hosts in scope:** externalbeta2.emaplan.com

## At a glance

| What | Count |
|------|------:|
| Pages crawled | 5 |
| Links found | 4 |
| API / XHR endpoints | 15 |
| Forms | 3 |
| URL parameters | 30 |
| JavaScript files | 11 |
| Hidden endpoints (from JS) | 98 |
| Possible secrets in JS | 1 |
| Pages with storage data | 4 |

## Response status codes

- **200** — 141 response(s)
- **201** — 14 response(s)
- **204** — 1 response(s)
- **301** — 3 response(s)
- **302** — 9 response(s)
- **307** — 1 response(s)
- **404** — 1 response(s)

## Pages crawled

- http://emoneyadvisor.com
- https://auth.externalbeta2.emaplan.com/help/login
- https://auth.externalbeta2.emaplan.com/login/default
- https://auth.externalbeta2.emaplan.com/oauth2/default/v1/authorize?client_id=0oaedsgzjxZlGjbOX4h7&redirect_uri=https%3A%2F%2Fexternalbeta2.emaplan.com%2Fema%2Fauthorization-code%2Fcallback&response_type=code&scope=openid%20profile&code_challenge=jzd1j9GlsxoWIkywxsBsz6V7LvQpYe28xUt8lo1Ds_c&code_challenge_method=S256&state=OpenIdConnect.AuthenticationProperties%3DJNmIUO4xYCnDmUgxacykrQjAI8LLNuDyy3yu2X7N-TxZJ4w2Bx482FRrqHEnNtrWC-b0y0CJs2YJwLRs80IB2hjdA3SrfUR6lat1wOQNy4UD5-P8aEp0BYjgJXRQXqtlPR1hYi2mEnAGTOh3XAxXvhas-WOM0si4SHcyWhFUWRAbLUq9s7VozK9dDV1GHrUFVunW6uz1h6_-GTqXkG3d-sHezI4qkBezdUW5a196or88TZqMEWwMYom0HtreGu6xagDa9hcB3X_ybLoKifoRL6uxv78WOgw_zbPvTJDDj4x4rYTQmuf-WHBEfHnmxnibO_4Aq44fakjTIawdlgbL6ggS2CyhsoBPRvKsFVIg0hKMgmE0rh335hy9daFaC2z1Tj7DSGrBIuZ-Jggep37mqx7CkaM2a4-2PtCgIRtXVGhbfGyHvpj0NQS5Nyz6ckax1z0DUM8ROwP3O3u_8oWJVKhG2WTxrbW3JYFgLeH1TMCyFDvzswP-Y82RM-7jPPe46aF3aLF6KWs-OX69Iq701v0tK3s1jy6PbdZwvANoML17uBcBcz0Mg_e9H2HUkuXDzpQl9BLuc5gw9YufQa8TVz6PBFXqgSftxkVPbmOIHC_41Ut1u3h-o_RwmW0hq9QM0i0Ex0MtVVV08qBT-NqGJ3H2T8pQmnQiiIMpsR0JBIn0RN6-sZjrboYoT1tjCmU5_3r4ot95emRcWhpu4UY4hs-Eb42tiUwMdHJhxBsYEZGbO6z5Vx3XXdO1E57C7gJC&response_mode=form_post&nonce=639261328547808898.ZTJhZjg2MGUtZmRlNi00NzdlLWFkNjktNGFhN2VjZThjZjIx&login_hint=H1Advisor01091&partner=ema&office=ema&logo=partner%2Fdefault%2FFiles%2FImages%2FIcons%2FPortalLogin.png&enable_spi_sso=False&post_logout_redirect_uri=https%3A%2F%2Fexternalbeta2.emaplan.com%2Fema&x-client-SKU=ID_NET472&x-client-ver=8.22.0.0
- https://externalbeta2.emaplan.com/ema

## API / XHR endpoints (likely the interesting ones)

- `DELETE https://auth.externalbeta2.emaplan.com//api/v1/sessions/me`
- `GET https://auth.externalbeta2.emaplan.com/api/internal/brand/theme/style-sheet?touch-point=SIGN_IN_PAGE&v=bfdbe22ada7761bc8c6c1210b47e1a85becbf81c599bc0b94cb7f3a13d26012e1afff23b39acf61777606e994baf32ad`
- `GET https://emoneyadvisor.com/wp-content/uploads/2023/02/Icon_Efficiency.json`
- `GET https://emoneyadvisor.com/wp-content/uploads/2023/02/Icon_Goal.json`
- `GET https://emoneyadvisor.com/wp-content/uploads/2023/02/Icon_People.json`
- `GET https://emoneyadvisor.com/wp-content/uploads/2023/02/Icon_Upward.json`
- `POST https://auth.externalbeta2.emaplan.com/LAkp0ipvQa3Z-ozrLA/X5QY4SmX1VpQX0/MClz/dm/c8dVtMMmk`
- `POST https://auth.externalbeta2.emaplan.com/api/v1/internal/device/nonce`
- `POST https://auth.externalbeta2.emaplan.com/idp/idx/challenge/answer`
- `POST https://auth.externalbeta2.emaplan.com/idp/idx/identify`
- `POST https://auth.externalbeta2.emaplan.com/idp/idx/introspect`
- `POST https://emoneyadvisor.com/akam/13/pixel_115070e`
- `POST https://externalbeta2.emaplan.com/L5CyF_/alv87/O4KgF/KA/3DaYrXfG9tXhtGai/QV4AAQ/dC4/vDBANDlA`
- `POST https://externalbeta2.emaplan.com/akam/13/pixel_77a47caf`
- `POST https://externalbeta2.emaplan.com/ema/api/v1/log/browser/event`

## Forms (possible input / injection points)

- **POST** `https://auth.externalbeta2.emaplan.com/oauth2/default/v1/authorize`
  - on: https://externalbeta2.emaplan.com/ema
  - fields: identifier
- **POST** `https://auth.externalbeta2.emaplan.com/oauth2/default/v1/authorize`
  - on: https://auth.externalbeta2.emaplan.com/oauth2/default/v1/authorize?client_id=0oaedsgzjxZlGjbOX4h7&redirect_uri=https%3A%2F%2Fexternalbeta2.emaplan.com%2Fema%2Fauthorization-code%2Fcallback&response_type=code&scope=openid%20profile&code_challenge=jzd1j9GlsxoWIkywxsBsz6V7LvQpYe28xUt8lo1Ds_c&code_challenge_method=S256&state=OpenIdConnect.AuthenticationProperties%3DJNmIUO4xYCnDmUgxacykrQjAI8LLNuDyy3yu2X7N-TxZJ4w2Bx482FRrqHEnNtrWC-b0y0CJs2YJwLRs80IB2hjdA3SrfUR6lat1wOQNy4UD5-P8aEp0BYjgJXRQXqtlPR1hYi2mEnAGTOh3XAxXvhas-WOM0si4SHcyWhFUWRAbLUq9s7VozK9dDV1GHrUFVunW6uz1h6_-GTqXkG3d-sHezI4qkBezdUW5a196or88TZqMEWwMYom0HtreGu6xagDa9hcB3X_ybLoKifoRL6uxv78WOgw_zbPvTJDDj4x4rYTQmuf-WHBEfHnmxnibO_4Aq44fakjTIawdlgbL6ggS2CyhsoBPRvKsFVIg0hKMgmE0rh335hy9daFaC2z1Tj7DSGrBIuZ-Jggep37mqx7CkaM2a4-2PtCgIRtXVGhbfGyHvpj0NQS5Nyz6ckax1z0DUM8ROwP3O3u_8oWJVKhG2WTxrbW3JYFgLeH1TMCyFDvzswP-Y82RM-7jPPe46aF3aLF6KWs-OX69Iq701v0tK3s1jy6PbdZwvANoML17uBcBcz0Mg_e9H2HUkuXDzpQl9BLuc5gw9YufQa8TVz6PBFXqgSftxkVPbmOIHC_41Ut1u3h-o_RwmW0hq9QM0i0Ex0MtVVV08qBT-NqGJ3H2T8pQmnQiiIMpsR0JBIn0RN6-sZjrboYoT1tjCmU5_3r4ot95emRcWhpu4UY4hs-Eb42tiUwMdHJhxBsYEZGbO6z5Vx3XXdO1E57C7gJC&response_mode=form_post&nonce=639261328547808898.ZTJhZjg2MGUtZmRlNi00NzdlLWFkNjktNGFhN2VjZThjZjIx&login_hint=H1Advisor01091&partner=ema&office=ema&logo=partner%2Fdefault%2FFiles%2FImages%2FIcons%2FPortalLogin.png&enable_spi_sso=False&post_logout_redirect_uri=https%3A%2F%2Fexternalbeta2.emaplan.com%2Fema&x-client-SKU=ID_NET472&x-client-ver=8.22.0.0
  - fields: identifier
- **POST** `https://auth.externalbeta2.emaplan.com/login/default`
  - on: https://auth.externalbeta2.emaplan.com/login/default
  - fields: identifier

## URL parameters seen

`client_id`, `code_challenge`, `code_challenge_method`, `elq1pcGUID`, `enable_spi_sso`, `firstPartyCookieDomain`, `login_hint`, `logo`, `ms`, `nonce`, `office`, `optin`, `partner`, `post_logout_redirect_uri`, `pps`, `redirect_uri`, `ref`, `ref2`, `response_mode`, `response_type`, `scope`, `siteid`, `state`, `stateToken`, `touch-point`, `tzo`, `v`, `ver`, `x-client-SKU`, `x-client-ver`

## JavaScript files (worth mining for hidden endpoints)

- https://auth.externalbeta2.emaplan.com/LAkp0ipvQa3Z-ozrLA/X5QY4SmX1VpQX0/MClz/dm/c8dVtMMmk
- https://emacontent.com/okta-widget/1.0.67/main.js
- https://ok10static2.oktacdn.com/assets/apps/admin.step-up-authentication/1.5.0/main-step-up-authentication.external.pack.js
- https://ok10static2.oktacdn.com/assets/js/common/ajax-step-up.6e7265025154739bf909ffec4d291893.js
- https://ok10static2.oktacdn.com/assets/js/mvc/dll-common/courage.common.pack.js
- https://ok10static2.oktacdn.com/assets/js/mvc/loginpage/initLoginPage.pack.d4f8b33efa60705220b2a7cf56e43e20.js
- https://ok10static2.oktacdn.com/assets/js/okta-datetime-i18n.min.0e9b1559c41042eb0efeb421b5017b71.js
- https://ok10static2.oktacdn.com/assets/js/properties/saasure-js-bundle.cba6072b76f4d387aaecd8921bfd1107.js
- https://ok10static2.oktacdn.com/assets/js/saasure.jqueryui.min.ac7c9d8343e0f05331da9e9db7341edf.js
- https://ok10static2.oktacdn.com/assets/js/sdk/okta-signin-widget/7.48.2/js/okta-sign-in.min.js
- https://s2.go-mpulse.net/boomerang/DASML-QSKNT-6X5KT-8N8KT-H5CMM

## Hidden endpoints extracted from JavaScript

These paths/URLs were found *inside* the JS bundles — they are not linked anywhere on the pages, so they're prime recon leads:

- `//fonts.googleapis.com/css`
- `/admin/api/step-up/error`
- `/admin/app/bulk-assign-clear`
- `/admin/app/bulk-assign-post`
- `/admin/apps/app-instance-autocomplete`
- `/admin/groups/autocomplete`
- `/admin/sso/step-up`
- `/admin/users/search`
- `/api/internal/su/orgs/`
- `/api/v1/altcha`
- `/api/v1/authn`
- `/api/v1/authn/introspect`
- `/api/v1/authn/recovery/password`
- `/api/v1/authn/recovery/token`
- `/api/v1/authn/recovery/unlock`
- `/api/v1/registration/`
- `/api/v1/registration/form`
- `/api/v1/sessions/me`
- `/api/v1/sessions/me/lifecycle/refresh`
- `/api/v1/users`
- `/auth/services/devicefingerprint`
- `/help/login`
- `/idp/idx/introspect`
- `/idp/myaccount/emails`
- `/idp/myaccount/emails/`
- `/idp/myaccount/password`
- `/idp/myaccount/phones`
- `/idp/myaccount/phones/`
- `/idp/myaccount/profile`
- `/idp/myaccount/profile/schema`
- `/img/logos/default.png`
- `/img/security/default.png`
- `/img/security/unknown-device.png`
- `/img/security/unknown.png`
- `/job/status`
- `/joblist/status`
- `/js/sections/timeout-worker-v1.js`
- `/labels/json/`
- `/login/getimage`
- `/login/sessionCookieRedirect`
- `/my/prefs/messages/`
- `/oauth2`
- `/oauth2/`
- `/oauth2/default`
- `/security/xsrf-token`
- `/session/extend`
- `/sso/idps/`
- `/su/org/`
- `/superOrgAdminPromotions/existingSuperOrgAdmins`
- `/user-summary/`
- `/usermail/sendmail/dialog`
- `/v1/authorize`
- `/v1/interact`
- `/v1/logout`
- `/v1/revoke`
- `/v1/token`
- `/v1/userinfo`
- `http://a`
- `http://a#б`
- `http://a/c%20d?a=1&c=3`
- `http://getfirefox.com`
- `http://www.apple.com/safari/`
- `http://www.google.com/chrome`
- `http://www.microsoft.com/windows/internet-explorer/default.aspx`
- `http://www.w3.org/2000/svg`
- `http://x`
- `http://тест`
- `https://a@b`
- `https://apps.apple.com/us/app/okta-verify/id490179405`
- `https://c.go-mpulse.net/api/config.json`
- `https://emacontent.com/libs/econs/0.3/fonts/econs-0.3.otf`
- `https://emacontent.com/libs/econs/0.3/fonts/econs-0.3.woff`
- `https://emacontent.com/libs/econs/0.3/fonts/econs-0.3.woff2`
- `https://fonts.googleapis.com/css2?family=Inter:ital,opsz,wght@0,14..32,100..900;1,14..32,100..900&display=swap`
- `https://fonts.googleapis.com/css2?family=Inter:ital,opsz,wght@0,14..32,100..900;1,14..32,100..900&display=swap\`
- `https://github.com/zloirock/core-js`
- `https://github.com/zloirock/core-js/blob/v3.26.1/LICENSE`
- `https://global.oktacdn.com/okta-signin-widget/`
- `https://hcaptcha.com/1/api.js`
- `https://hcaptcha.com/privacy`
- `https://hcaptcha.com/terms`
- `https://incode.id/privacy`
- `https://incode.id/terms`
- `https://itunes.apple.com/us/app/google-authenticator/id388497605`
- `https://itunes.apple.com/us/app/okta-mobile/id580709251?mt=8`
- `https://itunes.apple.com/us/app/okta-verify/id490179405`
- `https://play.google.com/store/apps/details?id=com.google.android.apps.authenticator2`
- `https://play.google.com/store/apps/details?id=com.okta.android.auth`
- `https://withpersona.com/legal/privacy-policy`
- `https://withpersona.com/legal/terms-of-use`
- `https://www.clearme.com/member-terms`
- `https://www.clearme.com/privacy-policy`
- `https://www.duosecurity.com/docs/duoweb#3.-show-the-iframe`
- `https://www.google.com/recaptcha/api.js`
- `https://www.okta.com/okta-consumer-products-terms/`
- `https://www.okta.com/privacy-policy/`
- `https://{yourOktaDomain}.com/oauth2/{authServerId}`
- `https://{yourOktaDomain}.com})`

## ⚠️ Possible secrets spotted in JavaScript

Heuristic matches — verify by hand, many are false positives, and treat anything real as sensitive:

- **Generic api_key** in https://ok10static2.oktacdn.com/assets/js/sdk/okta-signin-widget/7.48.2/js/okta-sign-in.min.js
  - `token":"enrollSymantecVip"`

## Browser storage found (may leak tokens / config)

- https://externalbeta2.emaplan.com/ema
  - localStorage keys: ak_a, ak_ax
  - sessionStorage keys: okta-transaction-storage
- https://auth.externalbeta2.emaplan.com/oauth2/default/v1/authorize?client_id=0oaedsgzjxZlGjbOX4h7&redirect_uri=https%3A%2F%2Fexternalbeta2.emaplan.com%2Fema%2Fauthorization-code%2Fcallback&response_type=code&scope=openid%20profile&code_challenge=jzd1j9GlsxoWIkywxsBsz6V7LvQpYe28xUt8lo1Ds_c&code_challenge_method=S256&state=OpenIdConnect.AuthenticationProperties%3DJNmIUO4xYCnDmUgxacykrQjAI8LLNuDyy3yu2X7N-TxZJ4w2Bx482FRrqHEnNtrWC-b0y0CJs2YJwLRs80IB2hjdA3SrfUR6lat1wOQNy4UD5-P8aEp0BYjgJXRQXqtlPR1hYi2mEnAGTOh3XAxXvhas-WOM0si4SHcyWhFUWRAbLUq9s7VozK9dDV1GHrUFVunW6uz1h6_-GTqXkG3d-sHezI4qkBezdUW5a196or88TZqMEWwMYom0HtreGu6xagDa9hcB3X_ybLoKifoRL6uxv78WOgw_zbPvTJDDj4x4rYTQmuf-WHBEfHnmxnibO_4Aq44fakjTIawdlgbL6ggS2CyhsoBPRvKsFVIg0hKMgmE0rh335hy9daFaC2z1Tj7DSGrBIuZ-Jggep37mqx7CkaM2a4-2PtCgIRtXVGhbfGyHvpj0NQS5Nyz6ckax1z0DUM8ROwP3O3u_8oWJVKhG2WTxrbW3JYFgLeH1TMCyFDvzswP-Y82RM-7jPPe46aF3aLF6KWs-OX69Iq701v0tK3s1jy6PbdZwvANoML17uBcBcz0Mg_e9H2HUkuXDzpQl9BLuc5gw9YufQa8TVz6PBFXqgSftxkVPbmOIHC_41Ut1u3h-o_RwmW0hq9QM0i0Ex0MtVVV08qBT-NqGJ3H2T8pQmnQiiIMpsR0JBIn0RN6-sZjrboYoT1tjCmU5_3r4ot95emRcWhpu4UY4hs-Eb42tiUwMdHJhxBsYEZGbO6z5Vx3XXdO1E57C7gJC&response_mode=form_post&nonce=639261328547808898.ZTJhZjg2MGUtZmRlNi00NzdlLWFkNjktNGFhN2VjZThjZjIx&login_hint=H1Advisor01091&partner=ema&office=ema&logo=partner%2Fdefault%2FFiles%2FImages%2FIcons%2FPortalLogin.png&enable_spi_sso=False&post_logout_redirect_uri=https%3A%2F%2Fexternalbeta2.emaplan.com%2Fema&x-client-SKU=ID_NET472&x-client-ver=8.22.0.0
  - localStorage keys: ak_a, ak_ax
  - sessionStorage keys: okta-transaction-storage
- https://auth.externalbeta2.emaplan.com/help/login
  - localStorage keys: ak_a, ak_ax
- https://auth.externalbeta2.emaplan.com/login/default
  - localStorage keys: ak_a, ak_ax
  - sessionStorage keys: okta-transaction-storage

---
*Full machine-readable detail is in `report.json`; the live event log is in `notebook.jsonl`.*