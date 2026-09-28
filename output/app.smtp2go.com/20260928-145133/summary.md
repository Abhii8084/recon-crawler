# Recon summary — app.smtp2go.com

- **Target seed:** https://app.smtp2go.com
- **Crawled at:** 2026-09-28 14:54:07
- **Hosts in scope:** app-us.smtp2go.com, app.smtp2go.com

## At a glance

| What | Count |
|------|------:|
| Pages crawled | 34 |
| Links found | 50 |
| API / XHR endpoints | 62 |
| Forms | 2 |
| URL parameters | 24 |
| JavaScript files | 33 |
| Hidden endpoints (from JS) | 99 |
| Possible secrets in JS | 0 |
| Pages with storage data | 3 |

## Response status codes

- **200** — 465 response(s)
- **302** — 40 response(s)
- **307** — 38 response(s)
- **308** — 30 response(s)

## Pages crawled

- https://app-us.smtp2go.com/account
- https://app-us.smtp2go.com/account/2fa
- https://app-us.smtp2go.com/account/changeplan
- https://app-us.smtp2go.com/account/changeplan/?auto_checkout=1
- https://app-us.smtp2go.com/account/team
- https://app-us.smtp2go.com/account/updatebilling
- https://app-us.smtp2go.com/compliance
- https://app-us.smtp2go.com/dashboard/main
- https://app-us.smtp2go.com/dashboard/main/?None=
- https://app-us.smtp2go.com/email-testing
- https://app-us.smtp2go.com/reports/activity
- https://app-us.smtp2go.com/reports/archive
- https://app-us.smtp2go.com/reports/charts
- https://app-us.smtp2go.com/reports/data-exports
- https://app-us.smtp2go.com/reports/sms
- https://app-us.smtp2go.com/reports/summary
- https://app-us.smtp2go.com/reports/summary/?filter=sender_email&date_filter=30days
- https://app-us.smtp2go.com/reports/suppressions
- https://app-us.smtp2go.com/sending
- https://app-us.smtp2go.com/sending/apikeys
- https://app-us.smtp2go.com/sending/ipauth
- https://app-us.smtp2go.com/sending/sms_settings
- https://app-us.smtp2go.com/sending/smtp_users
- https://app-us.smtp2go.com/sending/verified_senders
- https://app-us.smtp2go.com/settings/authentication
- https://app-us.smtp2go.com/settings/dedicatedips
- https://app-us.smtp2go.com/settings/display
- https://app-us.smtp2go.com/settings/integrations
- https://app-us.smtp2go.com/settings/sendingoptions
- https://app-us.smtp2go.com/settings/subaccounts
- https://app-us.smtp2go.com/settings/templates
- https://app-us.smtp2go.com/settings/webhooks
- https://app-us.smtp2go.com/support-zdsso
- https://app.smtp2go.com

## API / XHR endpoints (likely the interesting ones)

- `GET http://app-us.smtp2go.com/sending/apikeys`
- `GET https://app-us.smtp2go.com/api/dashboard/edit_account/dpa`
- `GET https://app-us.smtp2go.com/api/dashboard/main/?unix_secs_start=1787961600&unix_secs_end=1790639999`
- `GET https://app-us.smtp2go.com/api/dashboard/notices/?unix_secs_start=1787961600&unix_secs_end=1790639999`
- `GET https://app-us.smtp2go.com/api/dashboard/usage/?unix_secs_start=1787961600&unix_secs_end=1790639999`
- `GET https://app-us.smtp2go.com/api/reports/suppression/?action=&CSRF_key=okIXdFo%2B865byoE7Tv6JymlxccL0RE5nd%2BLNw4rjwAI&client_timezone=Asia%2FCalcutta&unix_secs_start=0&unix_secs_end=1790620199&recipient_search=&shown_records=0&shown_columns=%7B%22description%22%3Afalse%2C%22email_subject%22%3Afalse%7D&shown_events%5B%5D=bounce&shown_events%5B%5D=spam&shown_events%5B%5D=unsubscribe&shown_events%5B%5D=manual&shown_events%5B%5D=compliance&continue_token=&file_type=csv`
- `GET https://app-us.smtp2go.com/api/reports/suppression/?action=load-usernames&CSRF_key=okIXdFo%2B865byoE7Tv6JymlxccL0RE5nd%2BLNw4rjwAI`
- `GET https://app-us.smtp2go.com/api/settings/data_format`
- `GET https://app-us.smtp2go.com/api/settings/dedicatedips/?action=&CSRF_key=bEY4DfpX1RIkkCx5LzzkgFtm1A6fV%2BX1cLF3LM2n3fU`
- `GET https://app-us.smtp2go.com/api/settings/ipallowlist/?action=init&CSRF_key=okIXdFo%2B865byoE7Tv6JymlxccL0RE5nd%2BLNw4rjwAI`
- `GET https://app-us.smtp2go.com/api/settings/ipauth_users/?action=load-active-ips&CSRF_key=bEY4DfpX1RIkkCx5LzzkgFtm1A6fV%2BX1cLF3LM2n3fU`
- `GET https://app-us.smtp2go.com/api/settings/ipauth_users/?action=load-active-ips&CSRF_key=okIXdFo%2B865byoE7Tv6JymlxccL0RE5nd%2BLNw4rjwAI`
- `GET https://app-us.smtp2go.com/api/settings/ipauth_users/?action=load-pending-ips&CSRF_key=okIXdFo%2B865byoE7Tv6JymlxccL0RE5nd%2BLNw4rjwAI`
- `GET https://app-us.smtp2go.com/api/settings/sendingoptions/?login_id=`
- `GET https://app-us.smtp2go.com/api/settings/smtp_users/?action=load-active-users&CSRF_key=bEY4DfpX1RIkkCx5LzzkgFtm1A6fV%2BX1cLF3LM2n3fU`
- `GET https://app-us.smtp2go.com/api/settings/subaccounts/?action=&CSRF_key=bEY4DfpX1RIkkCx5LzzkgFtm1A6fV%2BX1cLF3LM2n3fU&search_term=&state_to_display=active&shown_records=0&shown_columns=%7B%22name%22%3Atrue%2C%22logIn%22%3Atrue%2C%22status%22%3Atrue%2C%22team%22%3Atrue%2C%22id%22%3Afalse%2C%22usage%22%3Atrue%2C%22plan%22%3Afalse%2C%22dedip%22%3Afalse%2C%22ippool%22%3Afalse%2C%22archive%22%3Afalse%2C%22sms%22%3Afalse%2C%222fa%22%3Afalse%2C%22region%22%3Afalse%7D&continue_token=`
- `GET https://app-us.smtp2go.com/api/settings/subaccounts/?action=&CSRF_key=bEY4DfpX1RIkkCx5LzzkgFtm1A6fV%2BX1cLF3LM2n3fU&state_to_display=active&shown_records=0&page_size=-1&continue_token=`
- `GET https://app-us.smtp2go.com/api/settings/team/?CSRF_key=okIXdFo%2B865byoE7Tv6JymlxccL0RE5nd%2BLNw4rjwAI`
- `GET https://app-us.smtp2go.com/api/settings/webhooks/?action=&CSRF_key=zcHA9am2piM5E4spDKduQjqfvuHVo7Pp3pxCaTQuNIA`
- `GET https://app-us.smtp2go.com/compliance/?action=get_last_updated&url=https%3A%2F%2Fsmtp2go.b-cdn.net%2Ffile%2Fcompliance%2FAcceptable%2520Usage%2520Policy.pdf`
- `GET https://app-us.smtp2go.com/compliance/?action=get_last_updated&url=https%3A%2F%2Fsmtp2go.b-cdn.net%2Ffile%2Fcompliance%2FCOI%2520-%2520Sand%2520Dune%2520Mail%2520Limited.pdf`
- `GET https://app-us.smtp2go.com/compliance/?action=get_last_updated&url=https%3A%2F%2Fsmtp2go.b-cdn.net%2Ffile%2Fcompliance%2FCyber%2520Security%2520Policy.pdf`
- `GET https://app-us.smtp2go.com/compliance/?action=get_last_updated&url=https%3A%2F%2Fsmtp2go.b-cdn.net%2Ffile%2Fcompliance%2FData%2520Breach%2520Response%2520Policy.pdf`
- `GET https://app-us.smtp2go.com/compliance/?action=get_last_updated&url=https%3A%2F%2Fsmtp2go.b-cdn.net%2Ffile%2Fcompliance%2FData%2520Protection%2520Policy.pdf`
- `GET https://app-us.smtp2go.com/compliance/?action=get_last_updated&url=https%3A%2F%2Fsmtp2go.b-cdn.net%2Ffile%2Fcompliance%2FDisaster%2520Recovery%2520Plan%2520Policy.pdf`
- `GET https://app-us.smtp2go.com/compliance/?action=get_last_updated&url=https%3A%2F%2Fsmtp2go.b-cdn.net%2Ffile%2Fcompliance%2FDisaster%2520and%2520Pandemic%2520Response%2520Planning%2520Policy.pdf`
- `GET https://app-us.smtp2go.com/compliance/?action=get_last_updated&url=https%3A%2F%2Fsmtp2go.b-cdn.net%2Ffile%2Fcompliance%2FISO%252027001%252025-26.pdf`
- `GET https://app-us.smtp2go.com/compliance/?action=get_last_updated&url=https%3A%2F%2Fsmtp2go.b-cdn.net%2Ffile%2Fcompliance%2FISO%25209001%2520CA%252025-26.pdf`
- `GET https://app-us.smtp2go.com/compliance/?action=get_last_updated&url=https%3A%2F%2Fsmtp2go.b-cdn.net%2Ffile%2Fcompliance%2FIncident%2520Response%2520Plan%2520and%2520Business%2520Continuity.pdf`
- `GET https://app-us.smtp2go.com/compliance/?action=get_last_updated&url=https%3A%2F%2Fsmtp2go.b-cdn.net%2Ffile%2Fcompliance%2FInformation%2520Security%2520Policy.pdf`
- `GET https://app-us.smtp2go.com/compliance/?action=get_last_updated&url=https%3A%2F%2Fsmtp2go.b-cdn.net%2Ffile%2Fcompliance%2FLab%2520Security%2520Policy.pdf`
- `GET https://app-us.smtp2go.com/compliance/?action=get_last_updated&url=https%3A%2F%2Fsmtp2go.b-cdn.net%2Ffile%2Fcompliance%2FPatch%2520Management.pdf`
- `GET https://app-us.smtp2go.com/compliance/?action=get_last_updated&url=https%3A%2F%2Fsmtp2go.b-cdn.net%2Ffile%2Fcompliance%2FRemote%2520Access%2520Policy.pdf`
- `GET https://app-us.smtp2go.com/compliance/?action=get_last_updated&url=https%3A%2F%2Fsmtp2go.b-cdn.net%2Ffile%2Fcompliance%2FSecure%2520Engineering%2520Policy.pdf`
- `GET https://app-us.smtp2go.com/compliance/?action=get_last_updated&url=https%3A%2F%2Fsmtp2go.b-cdn.net%2Ffile%2Fcompliance%2FSubject%2520Access%2520Request%2520Policy.pdf`
- `GET https://app-us.smtp2go.com/compliance/?action=get_last_updated&url=https%3A%2F%2Fsmtp2go.b-cdn.net%2Ffile%2Fcompliance%2FSystem%2520Monitoring%2520and%2520Auditing.pdf`
- `GET https://app-us.smtp2go.com/compliance/?action=get_last_updated&url=https%3A%2F%2Fsmtp2go.b-cdn.net%2Ffile%2Fcompliance%2FThird%2520Party%2520Risk%2520Management%2520Policy.pdf`
- `GET https://app-us.smtp2go.com/compliance/?action=get_last_updated&url=https%3A%2F%2Fsmtp2go.b-cdn.net%2Ffile%2Fcompliance%2FWeb%2520Application%2520Security%2520Policy.pdf`
- `GET https://app-us.smtp2go.com/compliance/?action=get_last_updated&url=https%3A%2F%2Fsmtp2go.b-cdn.net%2Ffile%2Fcompliance%2Fsmtp2go-hr-w9.pdf`
- `GET https://app-us.smtp2go.com/end-points`
- `GET https://app-us.smtp2go.com/sending/apikeys`
- `GET https://app-us.smtp2go.com/static/js/riot/charts/demographic-chart.tag?version=1790560966`
- `GET https://app-us.smtp2go.com/static/js/riot/charts/filter-chart-subaccountdrop.tag?version=1790560966`
- `GET https://app-us.smtp2go.com/static/js/riot/charts/main.tag?version=1790560966`
- `GET https://app-us.smtp2go.com/static/js/riot/charts/persubaccount-chart.tag?version=1790560966`
- `GET https://app-us.smtp2go.com/static/js/riot/charts/peruser-chart.tag?version=1790560966`
- `GET https://app-us.smtp2go.com/static/js/riot/charts/usage-chart.tag?version=1790560966`
- `GET https://app-us.smtp2go.com/static/js/riot/filter-eventdrop.tag?version=1790560966`
- `GET https://app-us.smtp2go.com/static/js/riot/filter-subaccountdrop.tag?version=1790560966`
- `GET https://app-us.smtp2go.com/static/js/riot/filter-userdrop.tag?version=1790560966`
- `GET https://app-us.smtp2go.com/static/js/riot/ip-allow-list/edit.tag?version=1790560966`
- `GET https://app-us.smtp2go.com/static/js/riot/ip-allow-list/table.tag?version=1790560966`
- `GET https://app-us.smtp2go.com/static/js/riot/webhooks.tag?version=1790560966`
- `GET https://app-us.smtp2go.com/static/vue/settings/api-auth/main.css?version=1790560966`
- `GET https://app-us.smtp2go.com/static/vue/settings/api-auth/main.js?version=1790560966`
- `GET https://app-us.smtp2go.com/static/vue/settings/api-auth/vendor.js?version=1790560966`
- `POST https://app-us.smtp2go.com/api/login`
- `POST https://app-us.smtp2go.com/api/settings/api_users/?action=load-all-active-users&CSRF_key=bEY4DfpX1RIkkCx5LzzkgFtm1A6fV%2BX1cLF3LM2n3fU`
- `POST https://app-us.smtp2go.com/zdesk_chat_auth?CSRF_key=bEY4DfpX1RIkkCx5LzzkgFtm1A6fV%2BX1cLF3LM2n3fU`
- `POST https://app-us.smtp2go.com/zdesk_chat_auth?CSRF_key=okIXdFo%2B865byoE7Tv6JymlxccL0RE5nd%2BLNw4rjwAI`
- `POST https://app-us.smtp2go.com/zdesk_chat_auth?CSRF_key=zcHA9am2piM5E4spDKduQjqfvuHVo7Pp3pxCaTQuNIA`
- `POST https://app.smtp2go.com/api/login`

## Forms (possible input / injection points)

- **POST** `https://app.smtp2go.com/api/login/`
  - on: https://app.smtp2go.com
  - fields: red_deep_link, red_deep_query, username, password, remember_me
- **POST** `https://app.smtp2go.com/forgot-password/`
  - on: https://app.smtp2go.com
  - fields: email

## URL parameters seen

`CSRF_key`, `None`, `action`, `auto_checkout`, `client_timezone`, `continue_token`, `date_filter`, `file_type`, `filter`, `login_id`, `m`, `p`, `page_size`, `recipient_search`, `search_term`, `shown_columns`, `shown_events%5B%5D`, `shown_records`, `state_to_display`, `unix_secs_end`, `unix_secs_start`, `url`, `v`, `version`

## JavaScript files (worth mining for hidden endpoints)

- https://app.smtp2go.com/static/assets/admin/pages/scripts/login-soft.js?version=1790560966
- https://app.smtp2go.com/static/assets/global/plugins/jquery-1.11.0.min.js?version=1790560966
- https://app.smtp2go.com/static/assets/global/plugins/jquery-migrate-1.2.1.min.js?version=1790560966
- https://app.smtp2go.com/static/assets/global/plugins/jquery-slimscroll/jquery.slimscroll.min.js?version=1790560966
- https://app.smtp2go.com/static/assets/global/plugins/jquery-ui/jquery-ui-1.10.3.custom.min.js?version=1790560966
- https://app.smtp2go.com/static/assets/global/plugins/jquery-validation/js/jquery.validate.min.js?version=1790560966
- https://app.smtp2go.com/static/assets/global/plugins/jquery.blockui.min.js?version=1790560966
- https://app.smtp2go.com/static/assets/global/plugins/moment-timezone-all-years.min.js?version=1790560966
- https://app.smtp2go.com/static/assets/global/plugins/moment.min.js?version=1790560966
- https://app.smtp2go.com/static/js/functions.js?version=1790560966
- https://bat.bing.com/bat.js
- https://bat.bing.com/p/action/5218485.js
- https://bat.bing.com/p/insights/s/0.8.70
- https://bat.bing.com/p/insights/t/5218485
- https://cdn.announcekit.app/widget-v2.js
- https://cdn.smtp2go.com/app/v1.0.3299/js/common.d2359d9f.js
- https://cdn.smtp2go.com/app/v1.0.3299/js/page-dashboard-a.b715be1e.js
- https://cdn.smtp2go.com/app/v1.0.3299/js/page-dashboard-b.ecf65f5a.js
- https://cdn.smtp2go.com/app/v1.0.3299/js/vendor.322bf4a8.js
- https://cdn.smtp2go.com/app/v1.0.3299/static/assets/global/plugins/pace/pace.min.js
- https://googleads.g.doubleclick.net/pagead/viewthroughconversion/700498227/?random=1790587324798&cv=11&fst=1790587324798&bg=ffffff&guid=ON&async=1&en=gtag.config&gtm=45be69n1v9203804702z8893108960za20gzb893108960zd893108960xecxf1&gcd=13l3l3l3l1l1&dma=0&tag_exp=115938465~115938468~118897920~118897930~120213116~120385422~120469145~120469153&u_w=3440&u_h=1440&url=https%3A%2F%2Fapp-us.smtp2go.com%2Fdashboard%2Fmain%2F%3FNone%3D&rcb=1&frm=0&tiba=SMTP2GO%20%7C%20Dashboard&hn=www.googleadservices.com&npa=0&pscdl=noapi&auid=2111033616.1790587091&uaa=arm&uab=64&uafvl=Google%2520Chrome%3B153.0.8010.53%7CNot_A%2520Brand%3B8.0.0.0%7CChromium%3B153.0.8010.53&uamb=0&uam=&uap=macOS&uapv=26.6.2&uaw=0&data=event%3Dgtag.config&ept=9&rfmt=3&fmt=4
- https://googleads.g.doubleclick.net/pagead/viewthroughconversion/700498227/?random=1790587324820&cv=11&fst=1790587324820&bg=ffffff&guid=ON&async=1&en=form_start&gtm=45be69n1v9203804702za20gzb893108960zd893108960xecxf1&gcd=13l3l3l3l1l1&dma=0&tag_exp=115938465~115938468~118897920~118897930~120213116~120385422~120469145~120469153&u_w=3440&u_h=1440&url=https%3A%2F%2Fapp-us.smtp2go.com%2Fdashboard%2Fmain%2F%3FNone%3D&rcb=1&frm=0&tiba=SMTP2GO%20%7C%20Dashboard&ae=a&hn=www.googleadservices.com&npa=0&pscdl=noapi&auid=2111033616.1790587091&uaa=arm&uab=64&uafvl=Google%2520Chrome%3B153.0.8010.53%7CNot_A%2520Brand%3B8.0.0.0%7CChromium%3B153.0.8010.53&uamb=0&uam=&uap=macOS&uapv=26.6.2&uaw=0&data=event%3Dform_start&gap.fsrc=1&ept=9&rfmt=3&fmt=4
- https://googleads.g.doubleclick.net/pagead/viewthroughconversion/700498227/?random=1790587324824&cv=11&fst=1790587324824&bg=ffffff&guid=ON&async=1&en=form_submit&gtm=45be69n1v9203804702za20gzb893108960zd893108960xecxf1&gcd=13l3l3l3l1l1&dma=0&tag_exp=115938465~115938468~118897920~118897930~120213116~120385422~120469145~120469153&u_w=3440&u_h=1440&url=https%3A%2F%2Fapp-us.smtp2go.com%2Fdashboard%2Fmain%2F%3FNone%3D&rcb=1&frm=0&tiba=SMTP2GO%20%7C%20Dashboard&ae=a&hn=www.googleadservices.com&npa=0&pscdl=noapi&auid=2111033616.1790587091&uaa=arm&uab=64&uafvl=Google%2520Chrome%3B153.0.8010.53%7CNot_A%2520Brand%3B8.0.0.0%7CChromium%3B153.0.8010.53&uamb=0&uam=&uap=macOS&uapv=26.6.2&uaw=0&data=event%3Dform_submit&gap.fsrc=2&ept=9&rfmt=3&fmt=4
- https://googleads.g.doubleclick.net/pagead/viewthroughconversion/700498227/?random=1790587337706&cv=11&fst=1790587337706&bg=ffffff&guid=ON&async=1&en=gtag.config&gtm=45be69n1v9203804702z8893108960za20gzb893108960zd893108960xecxf1&gcd=13l3l3l3l1l1&dma=0&tag_exp=115938466~115938469~118897920~118897930~120213116~120385422~120469145~120469153&u_w=1512&u_h=982&url=https%3A%2F%2Fapp-us.smtp2go.com%2Fdashboard%2Fmain%2F%3FNone%3D&rcb=10&frm=0&tiba=SMTP2GO%20%7C%20Dashboard&hn=www.googleadservices.com&npa=0&pscdl=noapi&auid=2111033616.1790587091&uaa=arm&uab=64&uafvl=Google%2520Chrome%3B153.0.8010.53%7CNot_A%2520Brand%3B8.0.0.0%7CChromium%3B153.0.8010.53&uamb=0&uam=&uap=macOS&uapv=26.6.2&uaw=0&data=event%3Dgtag.config&ept=9&rfmt=3&fmt=4
- https://googleads.g.doubleclick.net/pagead/viewthroughconversion/700498227/?random=1790587402849&cv=11&fst=1790587402849&bg=ffffff&guid=ON&async=1&en=gtag.config&gtm=45be69n1v9203804702z8893108960za20gzb893108960zd893108960xecxf1&gcd=13l3l3l3l1l1&dma=0&tag_exp=115616986~115938465~115938469~118897920~118897930~120213116~120385423~120469145~120469153~121280969&u_w=1512&u_h=982&url=https%3A%2F%2Fapp-us.smtp2go.com%2Femail-testing%2F&rcb=12&frm=0&tiba=SMTP2GO%20%7C%20Email%20Testing&hn=www.googleadservices.com&npa=0&pscdl=noapi&auid=2111033616.1790587091&uaa=arm&uab=64&uafvl=Google%2520Chrome%3B153.0.8010.53%7CNot_A%2520Brand%3B8.0.0.0%7CChromium%3B153.0.8010.53&uamb=0&uam=&uap=macOS&uapv=26.6.2&uaw=0&data=event%3Dgtag.config&ept=9&rfmt=3&fmt=4
- https://googleads.g.doubleclick.net/pagead/viewthroughconversion/700498227/?random=1790587403746&cv=11&fst=1790587403746&bg=ffffff&guid=ON&async=1&en=form_start&gtm=45be69n1v9203804702za20gzb893108960zd893108960xecxf1&gcd=13l3l3l3l1l1&dma=0&tag_exp=115616986~115938465~115938469~118897920~118897930~120213116~120385423~120469145~120469153~121280969&u_w=1512&u_h=982&url=https%3A%2F%2Fapp-us.smtp2go.com%2Femail-testing%2F&rcb=12&frm=0&tiba=SMTP2GO%20%7C%20Email%20Testing&ae=a&hn=www.googleadservices.com&npa=0&pscdl=noapi&auid=2111033616.1790587091&uaa=arm&uab=64&uafvl=Google%2520Chrome%3B153.0.8010.53%7CNot_A%2520Brand%3B8.0.0.0%7CChromium%3B153.0.8010.53&uamb=0&uam=&uap=macOS&uapv=26.6.2&uaw=0&data=event%3Dform_start&gap.fsrc=1&ept=9&rfmt=3&fmt=4
- https://googleads.g.doubleclick.net/pagead/viewthroughconversion/700498227/?random=1790587403750&cv=11&fst=1790587403750&bg=ffffff&guid=ON&async=1&en=form_submit&gtm=45be69n1v9203804702za20gzb893108960zd893108960xecxf1&gcd=13l3l3l3l1l1&dma=0&tag_exp=115616986~115938465~115938469~118897920~118897930~120213116~120385423~120469145~120469153~121280969&u_w=1512&u_h=982&url=https%3A%2F%2Fapp-us.smtp2go.com%2Femail-testing%2F&rcb=12&frm=0&tiba=SMTP2GO%20%7C%20Email%20Testing&ae=a&hn=www.googleadservices.com&npa=0&pscdl=noapi&auid=2111033616.1790587091&uaa=arm&uab=64&uafvl=Google%2520Chrome%3B153.0.8010.53%7CNot_A%2520Brand%3B8.0.0.0%7CChromium%3B153.0.8010.53&uamb=0&uam=&uap=macOS&uapv=26.6.2&uaw=0&data=event%3Dform_submit&gap.fsrc=2&ept=9&rfmt=3&fmt=4
- https://googleads.g.doubleclick.net/pagead/viewthroughconversion/700498227/?random=1790587416392&cv=11&fst=1790587416392&bg=ffffff&guid=ON&async=1&en=gtag.config&gtm=45be69n1v9203804702z8893108960za20gzb893108960zd893108960xecxf1&gcd=13l3l3l3l1l1&dma=0&tag_exp=115938465~115938469~118897920~118897930~120213116~120385423~120469145~120469153&u_w=1512&u_h=982&url=https%3A%2F%2Fapp-us.smtp2go.com%2Fdashboard%2Fmain%2F&rcb=3&frm=0&tiba=SMTP2GO%20%7C%20Dashboard&hn=www.googleadservices.com&npa=0&pscdl=noapi&auid=2111033616.1790587091&uaa=arm&uab=64&uafvl=Google%2520Chrome%3B153.0.8010.53%7CNot_A%2520Brand%3B8.0.0.0%7CChromium%3B153.0.8010.53&uamb=0&uam=&uap=macOS&uapv=26.6.2&uaw=0&data=event%3Dgtag.config&ept=9&rfmt=3&fmt=4
- https://smtp2gostatus.com/embed/script.js
- https://static.zdassets.com/ekr/snippet.js?key=0cf7a737-17e8-46e7-aa2a-3286490173c0
- https://www.googletagmanager.com/gtag/js?id=AW-700498227&cx=c&gtm=4e69n1
- https://www.googletagmanager.com/gtm.js?id=GTM-K485WR2
- https://www.redditstatic.com/ads/pixel.js

## Hidden endpoints extracted from JavaScript

These paths/URLs were found *inside* the JS bundles — they are not linked anywhere on the pages, so they're prime recon leads:

- `/_/service_worker`
- `/_/service_worker/`
- `/ag/g/c`
- `/api/dashboard/dismiss-downgrade-banner/`
- `/api/dashboard/main/`
- `/as/d/ccm/conversion`
- `/as/p/c`
- `/ccm/collect`
- `/ccm/conversion`
- `/ccm/form-data`
- `/ccm/s/collect`
- `/d/ccm/form-data`
- `/dashboard/main/`
- `/dashboard/notices/`
- `/dashboard/team/`
- `/dashboard/usage/`
- `/ddm/activity`
- `/g/collect`
- `/g/d/ccm/conversion`
- `/ga/g/c`
- `/gs/ccm/conversion`
- `/gtag/destination`
- `/gtag/js`
- `/measurement/conversion`
- `/measurement/enhanced`
- `/p/action/`
- `/pagead/1p-conversion`
- `/pagead/conversion`
- `/pagead/form-data`
- `/pagead/set_partitioned_cookie`
- `/pagead/uconversion`
- `/pagead/viewthroughconversion`
- `/public/estManifest`
- `/rmkt/collect`
- `/settings/subaccounts/`
- `/static/assets/`
- `/travel/flights/click/conversion`
- `http://www.w3.org/2000/svg`
- `https://${n}/embeddable/zendesk_host`
- `https://45hj7q5l4w10.statuspage.io/embed/frame`
- `https://Electron`
- `https://aba337625608d678c785a8649566e231@o4507427284123728.ingest.de.sentry.io/4507427362963540`
- `https://ad.doubleclick.net/activity;`
- `https://ade.googlesyndication.com`
- `https://ads.reddit.com`
- `https://adservice.google.com/pagead/regclk`
- `https://alb.reddit.com/rp`
- `https://alb.reddit.com/rp.gif`
- `https://announcekit.app`
- `https://announcekit.app/?utm_source=${t}&utm_medium=referral&utm_campaign=powered-by`
- `https://bat.bing.com/p/insights/c/k`
- `https://bat.bing.com/p/insights/s/0.8.70`
- `https://bat.bing.com/p/insights/t/`
- `https://cct.google/taggy/agent.js`
- `https://clarity.microsoft.com/js/`
- `https://connect.facebook.net/en_US/fbevents.js`
- `https://developers.smtp2go.com/`
- `https://ekr.zdassets.com/compose/${t}`
- `https://fonts.googleapis.com/css?family=${e}:400,500,600,700&subset=latin-ext,cyrillic,cyrillic-ext&display=swap`
- `https://m.youtube.com`
- `https://pagead2.googlesyndication.com`
- `https://pagead2.googlesyndication.com/pagead/gen_204?id=tcfe`
- `https://pixel-config.reddit.com/pixels`
- `https://static.zdassets.com/ekr/`
- `https://support.smtp2go.com/hc/en-gb/articles/115003599568`
- `https://support.smtp2go.com/hc/en-gb/articles/223087607`
- `https://support.smtp2go.com/hc/en-gb/articles/223087727-Bounce-Spam-Percentages-and-Ratings`
- `https://support.smtp2go.com/hc/en-gb/articles/360003124714-Open-Tracking`
- `https://support.smtp2go.com/hc/en-gb/articles/900002237106`
- `https://ui.ads.microsoft.com`
- `https://v2.zopim.com/w?${this.zopimKey}`
- `https://www.facebook.com/tr/`
- `https://www.google.co.in/pagead/1p-user-list/700498227/?random\x3d1790587324798\x26cv\x3d11\x26fst\x3d1790586000000\x26bg\x3dffffff\x26guid\x3dON\x26async\x3d1\x26en\x3dgtag.config\x26gtm\x3d45be69n1v9203804702z8893108960za20gzb893108960zd893108960xecxf1\x26gcd\x3d13l3l3l3l1l1\x26dma\x3d0\x26tag_exp\x3d115938465~115938468~118897920~118897930~120213116~120385422~120469145~120469153\x26u_w\x3d3440\x26u_h\x3d1440\x26url\x3dhttps%3A%2F%2Fapp-us.smtp2go.com%2Fdashboard%2Fmain%2F%3FNone%3D\x26rcb\x3d1\x26frm\x3d0\x26tiba\x3dSMTP2GO%20%7C%20Dashboard\x26hn\x3dwww.googleadservices.com\x26npa\x3d0\x26pscdl\x3dnoapi\x26auid\x3d2111033616.1790587091\x26uaa\x3darm\x26uab\x3d64\x26uafvl\x3dGoogle%2520Chrome%3B153.0.8010.53%7CNot_A%2520Brand%3B8.0.0.0%7CChromium%3B153.0.8010.53\x26uamb\x3d0\x26uam\x3d\x26uap\x3dmacOS\x26uapv\x3d26.6.2\x26uaw\x3d0\x26data\x3devent%3Dgtag.config\x26ept\x3d9\x26rfmt\x3d3\x26fmt\x3d3\x26is_vtc\x3d1\x26cid\x3dCAQS-gEAQM4h3Kdrnjf3-nx51tSkrT0Nk2xuecAAR6TvNvc8mgxs0cNKrCSc-vLax3eVpi8HxTd-azNaROKtRliSzTXS-oHFn_IR8VxGSzbV6iLbupN6cVU8x4TM1nqjYDNuAG_MpaIINJJzG5AoZMqnwZhJLbNsRSAhiazScrK9UwwOqiliyEX0au6HiRd8NZ07V0P9nRqaHWXJ2KpWwGeZleqVGKEEbEdP5eTTKivV5NF8GscMePXCdVIHfCVBeZbnqDTR-pY7F3WBF_aPo8A81T64mc3U9hMyMUXaZjlwEgc_Q5RHq8iRv72AkpEHg0bbDDjILuHvdlLQktBA\x26random\x3d745525637\x26rmt_tld\x3d1\x26ipr\x3dy`
- `https://www.google.co.in/pagead/1p-user-list/700498227/?random\x3d1790587324820\x26cv\x3d11\x26fst\x3d1790586000000\x26bg\x3dffffff\x26guid\x3dON\x26async\x3d1\x26en\x3dform_start\x26gtm\x3d45be69n1v9203804702za20gzb893108960zd893108960xecxf1\x26gcd\x3d13l3l3l3l1l1\x26dma\x3d0\x26tag_exp\x3d115938465~115938468~118897920~118897930~120213116~120385422~120469145~120469153\x26u_w\x3d3440\x26u_h\x3d1440\x26url\x3dhttps%3A%2F%2Fapp-us.smtp2go.com%2Fdashboard%2Fmain%2F%3FNone%3D\x26rcb\x3d1\x26frm\x3d0\x26tiba\x3dSMTP2GO%20%7C%20Dashboard\x26ae\x3da\x26hn\x3dwww.googleadservices.com\x26npa\x3d0\x26pscdl\x3dnoapi\x26auid\x3d2111033616.1790587091\x26uaa\x3darm\x26uab\x3d64\x26uafvl\x3dGoogle%2520Chrome%3B153.0.8010.53%7CNot_A%2520Brand%3B8.0.0.0%7CChromium%3B153.0.8010.53\x26uamb\x3d0\x26uam\x3d\x26uap\x3dmacOS\x26uapv\x3d26.6.2\x26uaw\x3d0\x26data\x3devent%3Dform_start\x26gap.fsrc\x3d1\x26ept\x3d9\x26rfmt\x3d3\x26fmt\x3d3\x26is_vtc\x3d1\x26cid\x3dCAQS-gEAQM4h3IlHBQt_YGp3klEVCeHdb8PkgtE1h0b0NT3DH0BeNcSx7Ns_ng65w_kOzpCyJ1tPcPRdFHXUxENTFR4j41Kkml_uYbMWFnbYEXVslSuo-ZmXu5-a-9022InOp7eBTxcNuQaggTrT7Ih0Tjgi081YLM7fwbMyegenv07ZymFv1lsfwHYmSkgGPMOZNN4XHTPDAuUbD5VznCJ4F_-2JkFzsLx9ugm7YRCYJgomkZU0N5-Nvx8xu3qN4DmuTj0Hz0eKGOGmKXiafYiZagBKHkniK59H_Q78K_oUKdWhWor5NFdjE7qN6eKfKWlg7oEh1f2J5mAnU6gv\x26random\x3d3279076572\x26rmt_tld\x3d1\x26ipr\x3dy`
- `https://www.google.co.in/pagead/1p-user-list/700498227/?random\x3d1790587324824\x26cv\x3d11\x26fst\x3d1790586000000\x26bg\x3dffffff\x26guid\x3dON\x26async\x3d1\x26en\x3dform_submit\x26gtm\x3d45be69n1v9203804702za20gzb893108960zd893108960xecxf1\x26gcd\x3d13l3l3l3l1l1\x26dma\x3d0\x26tag_exp\x3d115938465~115938468~118897920~118897930~120213116~120385422~120469145~120469153\x26u_w\x3d3440\x26u_h\x3d1440\x26url\x3dhttps%3A%2F%2Fapp-us.smtp2go.com%2Fdashboard%2Fmain%2F%3FNone%3D\x26rcb\x3d1\x26frm\x3d0\x26tiba\x3dSMTP2GO%20%7C%20Dashboard\x26ae\x3da\x26hn\x3dwww.googleadservices.com\x26npa\x3d0\x26pscdl\x3dnoapi\x26auid\x3d2111033616.1790587091\x26uaa\x3darm\x26uab\x3d64\x26uafvl\x3dGoogle%2520Chrome%3B153.0.8010.53%7CNot_A%2520Brand%3B8.0.0.0%7CChromium%3B153.0.8010.53\x26uamb\x3d0\x26uam\x3d\x26uap\x3dmacOS\x26uapv\x3d26.6.2\x26uaw\x3d0\x26data\x3devent%3Dform_submit\x26gap.fsrc\x3d2\x26ept\x3d9\x26rfmt\x3d3\x26fmt\x3d3\x26is_vtc\x3d1\x26cid\x3dCAQS-gEAQM4h3Hme0B733RnZw83O2As1oZbANN68Hkl5dua9sF-Nivcr8b1eQOX1IEzkD5zvSr-FNQs9CT2Tg9Ya2DM2OKiigu5HIAass5xkbtbjLdTmXF9gxna-QlPT0IkpHI_yCd1xKnpVXaPW2w3QAymTkMlDJQxaBvR_4UM2K5RTqbTGqeY8pGk0hcJM8JhDlL2YvPCcMkcfRKz8HY_0s2CKcn4bfSbg1SRpaV_dRA57VaTEM-C616WkX870zLdMirxDdL__IeXUgmrERGIJlpZHdF86_dw43yXDctSW6qPfT-Rxi_pbLzLRwC6amyttrn08e_9m9ctUqo3Z\x26random\x3d33006494\x26rmt_tld\x3d1\x26ipr\x3dy`
- `https://www.google.co.in/pagead/1p-user-list/700498227/?random\x3d1790587337706\x26cv\x3d11\x26fst\x3d1790586000000\x26bg\x3dffffff\x26guid\x3dON\x26async\x3d1\x26en\x3dgtag.config\x26gtm\x3d45be69n1v9203804702z8893108960za20gzb893108960zd893108960xecxf1\x26gcd\x3d13l3l3l3l1l1\x26dma\x3d0\x26tag_exp\x3d115938466~115938469~118897920~118897930~120213116~120385422~120469145~120469153\x26u_w\x3d1512\x26u_h\x3d982\x26url\x3dhttps%3A%2F%2Fapp-us.smtp2go.com%2Fdashboard%2Fmain%2F%3FNone%3D\x26rcb\x3d10\x26frm\x3d0\x26tiba\x3dSMTP2GO%20%7C%20Dashboard\x26hn\x3dwww.googleadservices.com\x26npa\x3d0\x26pscdl\x3dnoapi\x26auid\x3d2111033616.1790587091\x26uaa\x3darm\x26uab\x3d64\x26uafvl\x3dGoogle%2520Chrome%3B153.0.8010.53%7CNot_A%2520Brand%3B8.0.0.0%7CChromium%3B153.0.8010.53\x26uamb\x3d0\x26uam\x3d\x26uap\x3dmacOS\x26uapv\x3d26.6.2\x26uaw\x3d0\x26data\x3devent%3Dgtag.config\x26ept\x3d9\x26rfmt\x3d3\x26fmt\x3d3\x26is_vtc\x3d1\x26cid\x3dCAQS-gEAQM4h3OiGxeBg-m6PzOmqdcmj3vPQrZNyBFSpp_U32TGq9Ybfiy5gPih_6idUDkcoO9zkWxjnHRwgU25Kpp9Xl7LiG193wB8cHI_qK9fAPLtDNEhQ5KjYQktNpYWlxVxNysftquFlF77XbFklpPj1z8--SXZSrKNviO2LuAMgEevhG1N4SMh53jRuEWYI0ftfh0oTj7Iw74q_aHjOHI5_bGrbE4TYNZ6uxuElo6FwFMwTNoKO4zR69FdKQ7kpDt1NvXDQl8NKgkYUg3urgfmgQxlJ0JBe6oiW4eJhbyg4NiOiNfC_v79hD87cgxbzAQBBnMYHhVcC7UdS\x26random\x3d2567710181\x26rmt_tld\x3d1\x26ipr\x3dy`
- `https://www.google.co.in/pagead/1p-user-list/700498227/?random\x3d1790587402849\x26cv\x3d11\x26fst\x3d1790586000000\x26bg\x3dffffff\x26guid\x3dON\x26async\x3d1\x26en\x3dgtag.config\x26gtm\x3d45be69n1v9203804702z8893108960za20gzb893108960zd893108960xecxf1\x26gcd\x3d13l3l3l3l1l1\x26dma\x3d0\x26tag_exp\x3d115616986~115938465~115938469~118897920~118897930~120213116~120385423~120469145~120469153~121280969\x26u_w\x3d1512\x26u_h\x3d982\x26url\x3dhttps%3A%2F%2Fapp-us.smtp2go.com%2Femail-testing%2F\x26rcb\x3d12\x26frm\x3d0\x26tiba\x3dSMTP2GO%20%7C%20Email%20Testing\x26hn\x3dwww.googleadservices.com\x26npa\x3d0\x26pscdl\x3dnoapi\x26auid\x3d2111033616.1790587091\x26uaa\x3darm\x26uab\x3d64\x26uafvl\x3dGoogle%2520Chrome%3B153.0.8010.53%7CNot_A%2520Brand%3B8.0.0.0%7CChromium%3B153.0.8010.53\x26uamb\x3d0\x26uam\x3d\x26uap\x3dmacOS\x26uapv\x3d26.6.2\x26uaw\x3d0\x26data\x3devent%3Dgtag.config\x26ept\x3d9\x26rfmt\x3d3\x26fmt\x3d3\x26is_vtc\x3d1\x26cid\x3dCAQS-gEAQM4h3FsiELsEa3DsrBALVRuCSK6vL9gOiKNFLVzMCmeADthFjQV17GquLtPYMyOZnq5Ix0yLESa4tTyYPvqNYFs_YToHgBsY6qjLJc8QHCaG_IL2yuKGX4o_BcSAVVBRdlTdvBV5qVybX3BieSnk9WhnwWDEOqVhcLTLmy1-qIe44kA3HL-qUqidV6cEQiCrJckhRzYLQvxYBnkpgsT2Y3o7kmh_wX0bqg79onRFMkDklQQQ35_HyPyd0LoZMHQ3U3hGuN0K0XDyiAX8k_laIGmk3iisp05bS02RazDvxtSBeTECyNhngwiLoBocVmjXSOaJEb78MzW4\x26random\x3d3637030327\x26rmt_tld\x3d1\x26ipr\x3dy`
- `https://www.google.co.in/pagead/1p-user-list/700498227/?random\x3d1790587403746\x26cv\x3d11\x26fst\x3d1790586000000\x26bg\x3dffffff\x26guid\x3dON\x26async\x3d1\x26en\x3dform_start\x26gtm\x3d45be69n1v9203804702za20gzb893108960zd893108960xecxf1\x26gcd\x3d13l3l3l3l1l1\x26dma\x3d0\x26tag_exp\x3d115616986~115938465~115938469~118897920~118897930~120213116~120385423~120469145~120469153~121280969\x26u_w\x3d1512\x26u_h\x3d982\x26url\x3dhttps%3A%2F%2Fapp-us.smtp2go.com%2Femail-testing%2F\x26rcb\x3d12\x26frm\x3d0\x26tiba\x3dSMTP2GO%20%7C%20Email%20Testing\x26ae\x3da\x26hn\x3dwww.googleadservices.com\x26npa\x3d0\x26pscdl\x3dnoapi\x26auid\x3d2111033616.1790587091\x26uaa\x3darm\x26uab\x3d64\x26uafvl\x3dGoogle%2520Chrome%3B153.0.8010.53%7CNot_A%2520Brand%3B8.0.0.0%7CChromium%3B153.0.8010.53\x26uamb\x3d0\x26uam\x3d\x26uap\x3dmacOS\x26uapv\x3d26.6.2\x26uaw\x3d0\x26data\x3devent%3Dform_start\x26gap.fsrc\x3d1\x26ept\x3d9\x26rfmt\x3d3\x26fmt\x3d3\x26is_vtc\x3d1\x26cid\x3dCAQS-gEAQM4h3FqTurJ02cAY871GY6UPvKUTEpQBp0bBdduTKy49cvPn9BRWl049twfmiZSrM2eRsWAf_98WTSEpTnxzSBQwyE5ousKmjhAJMQfq710bh6D3XwDAgT5R1WpLucu1R2QE8LxjZwse1fNGHzb_wXsScXWMypRq7QdH7vgEocgJ1DyqayQjqvugr1h8cHoUecIEpU922ee86FZKyavqeW8bJd8CkYC5e5HDLcD4UAGhvy8ZxjEjBXKYTaq0wl6-1g7OX_2DhFvCBBzizx37z7etQIO6kGYuYvXKrW0VcO0jb7rxKqwTpTk_MbcLYazxO96rU8h3Bw-q\x26random\x3d747637782\x26rmt_tld\x3d1\x26ipr\x3dy`
- `https://www.google.co.in/pagead/1p-user-list/700498227/?random\x3d1790587403750\x26cv\x3d11\x26fst\x3d1790586000000\x26bg\x3dffffff\x26guid\x3dON\x26async\x3d1\x26en\x3dform_submit\x26gtm\x3d45be69n1v9203804702za20gzb893108960zd893108960xecxf1\x26gcd\x3d13l3l3l3l1l1\x26dma\x3d0\x26tag_exp\x3d115616986~115938465~115938469~118897920~118897930~120213116~120385423~120469145~120469153~121280969\x26u_w\x3d1512\x26u_h\x3d982\x26url\x3dhttps%3A%2F%2Fapp-us.smtp2go.com%2Femail-testing%2F\x26rcb\x3d12\x26frm\x3d0\x26tiba\x3dSMTP2GO%20%7C%20Email%20Testing\x26ae\x3da\x26hn\x3dwww.googleadservices.com\x26npa\x3d0\x26pscdl\x3dnoapi\x26auid\x3d2111033616.1790587091\x26uaa\x3darm\x26uab\x3d64\x26uafvl\x3dGoogle%2520Chrome%3B153.0.8010.53%7CNot_A%2520Brand%3B8.0.0.0%7CChromium%3B153.0.8010.53\x26uamb\x3d0\x26uam\x3d\x26uap\x3dmacOS\x26uapv\x3d26.6.2\x26uaw\x3d0\x26data\x3devent%3Dform_submit\x26gap.fsrc\x3d2\x26ept\x3d9\x26rfmt\x3d3\x26fmt\x3d3\x26is_vtc\x3d1\x26cid\x3dCAQS-gEAQM4h3HB6oMdOYN0sTLekCXXoBzQAL_qNeKVZfK_vfhQc2lzfRQaWEJILWdaWCj4pCng5HN6VX_BjT7ZHKsjOtyt_cHsPytPqX5cIF8rPWqiVoHje5sSgDYRPk1sPoTkEqVHn2-kBKvGtHFK3ZZVMH38MZE3ahnXf3O8cbHurph6QtKkT9Mkh2h_SOcPOmKXWvhkysbPBtEbLpJtJypdF2LfDaN9oyAj1Yfpjv2Yl4ktRAb6D7Wpxcm4FjicT4IDj9dlxhwdbTZCNriSdoOBpNbF3SSI19aDM0jpPJyXTb95VdwaBq7IHrwUQ5jdGkLmIXncVLd4QxgGp\x26random\x3d1532877886\x26rmt_tld\x3d1\x26ipr\x3dy`
- `https://www.google.co.in/pagead/1p-user-list/700498227/?random\x3d1790587416392\x26cv\x3d11\x26fst\x3d1790586000000\x26bg\x3dffffff\x26guid\x3dON\x26async\x3d1\x26en\x3dgtag.config\x26gtm\x3d45be69n1v9203804702z8893108960za20gzb893108960zd893108960xecxf1\x26gcd\x3d13l3l3l3l1l1\x26dma\x3d0\x26tag_exp\x3d115938465~115938469~118897920~118897930~120213116~120385423~120469145~120469153\x26u_w\x3d1512\x26u_h\x3d982\x26url\x3dhttps%3A%2F%2Fapp-us.smtp2go.com%2Fdashboard%2Fmain%2F\x26rcb\x3d3\x26frm\x3d0\x26tiba\x3dSMTP2GO%20%7C%20Dashboard\x26hn\x3dwww.googleadservices.com\x26npa\x3d0\x26pscdl\x3dnoapi\x26auid\x3d2111033616.1790587091\x26uaa\x3darm\x26uab\x3d64\x26uafvl\x3dGoogle%2520Chrome%3B153.0.8010.53%7CNot_A%2520Brand%3B8.0.0.0%7CChromium%3B153.0.8010.53\x26uamb\x3d0\x26uam\x3d\x26uap\x3dmacOS\x26uapv\x3d26.6.2\x26uaw\x3d0\x26data\x3devent%3Dgtag.config\x26ept\x3d9\x26rfmt\x3d3\x26fmt\x3d3\x26is_vtc\x3d1\x26cid\x3dCAQS-gEAQM4h3GuQirYFvAdVBOhjj_9_H415dBLjkVmax2u_iMbNlSukxAOlf-slMHGYhInzlwDL_KUFfjIAn5G0ldvCg5f6M2IBkHH-4Myn9tQmS-xCmV7V8VfTFzKEap76V2xWA1pqRmMdonP7nLHLn_3yp98Q_3WLfayYKszAMhqeV_3GAiK_WObDlWDsAYxf63HxEiNvUnbVpT0iczpWGHqdM92Gb6roiiiD7v5c5zcWXSIkSQD2r1wb-NIn5uiPpyOv-DNWlHoK5fdoqJGl6a7MroloCSYxh5tDmi9BSTKYlxrLnJi36Pe9bpJqRtqLIZ7sgBIXjvr3FTJL\x26random\x3d1600838748\x26rmt_tld\x3d1\x26ipr\x3dy`
- `https://www.google.com`
- `https://www.google.com/`
- `https://www.google.com/ccm/geo`
- `https://www.google.com/pagead/1p-user-list/700498227/?random\x3d1790587324798\x26cv\x3d11\x26fst\x3d1790586000000\x26bg\x3dffffff\x26guid\x3dON\x26async\x3d1\x26en\x3dgtag.config\x26gtm\x3d45be69n1v9203804702z8893108960za20gzb893108960zd893108960xecxf1\x26gcd\x3d13l3l3l3l1l1\x26dma\x3d0\x26tag_exp\x3d115938465~115938468~118897920~118897930~120213116~120385422~120469145~120469153\x26u_w\x3d3440\x26u_h\x3d1440\x26url\x3dhttps%3A%2F%2Fapp-us.smtp2go.com%2Fdashboard%2Fmain%2F%3FNone%3D\x26rcb\x3d1\x26frm\x3d0\x26tiba\x3dSMTP2GO%20%7C%20Dashboard\x26hn\x3dwww.googleadservices.com\x26npa\x3d0\x26pscdl\x3dnoapi\x26auid\x3d2111033616.1790587091\x26uaa\x3darm\x26uab\x3d64\x26uafvl\x3dGoogle%2520Chrome%3B153.0.8010.53%7CNot_A%2520Brand%3B8.0.0.0%7CChromium%3B153.0.8010.53\x26uamb\x3d0\x26uam\x3d\x26uap\x3dmacOS\x26uapv\x3d26.6.2\x26uaw\x3d0\x26data\x3devent%3Dgtag.config\x26ept\x3d9\x26rfmt\x3d3\x26fmt\x3d3\x26is_vtc\x3d1\x26cid\x3dCAQS-gEAQM4h3Kdrnjf3-nx51tSkrT0Nk2xuecAAR6TvNvc8mgxs0cNKrCSc-vLax3eVpi8HxTd-azNaROKtRliSzTXS-oHFn_IR8VxGSzbV6iLbupN6cVU8x4TM1nqjYDNuAG_MpaIINJJzG5AoZMqnwZhJLbNsRSAhiazScrK9UwwOqiliyEX0au6HiRd8NZ07V0P9nRqaHWXJ2KpWwGeZleqVGKEEbEdP5eTTKivV5NF8GscMePXCdVIHfCVBeZbnqDTR-pY7F3WBF_aPo8A81T64mc3U9hMyMUXaZjlwEgc_Q5RHq8iRv72AkpEHg0bbDDjILuHvdlLQktBA\x26random\x3d745525637\x26rmt_tld\x3d0\x26ipr\x3dy`
- `https://www.google.com/pagead/1p-user-list/700498227/?random\x3d1790587324820\x26cv\x3d11\x26fst\x3d1790586000000\x26bg\x3dffffff\x26guid\x3dON\x26async\x3d1\x26en\x3dform_start\x26gtm\x3d45be69n1v9203804702za20gzb893108960zd893108960xecxf1\x26gcd\x3d13l3l3l3l1l1\x26dma\x3d0\x26tag_exp\x3d115938465~115938468~118897920~118897930~120213116~120385422~120469145~120469153\x26u_w\x3d3440\x26u_h\x3d1440\x26url\x3dhttps%3A%2F%2Fapp-us.smtp2go.com%2Fdashboard%2Fmain%2F%3FNone%3D\x26rcb\x3d1\x26frm\x3d0\x26tiba\x3dSMTP2GO%20%7C%20Dashboard\x26ae\x3da\x26hn\x3dwww.googleadservices.com\x26npa\x3d0\x26pscdl\x3dnoapi\x26auid\x3d2111033616.1790587091\x26uaa\x3darm\x26uab\x3d64\x26uafvl\x3dGoogle%2520Chrome%3B153.0.8010.53%7CNot_A%2520Brand%3B8.0.0.0%7CChromium%3B153.0.8010.53\x26uamb\x3d0\x26uam\x3d\x26uap\x3dmacOS\x26uapv\x3d26.6.2\x26uaw\x3d0\x26data\x3devent%3Dform_start\x26gap.fsrc\x3d1\x26ept\x3d9\x26rfmt\x3d3\x26fmt\x3d3\x26is_vtc\x3d1\x26cid\x3dCAQS-gEAQM4h3IlHBQt_YGp3klEVCeHdb8PkgtE1h0b0NT3DH0BeNcSx7Ns_ng65w_kOzpCyJ1tPcPRdFHXUxENTFR4j41Kkml_uYbMWFnbYEXVslSuo-ZmXu5-a-9022InOp7eBTxcNuQaggTrT7Ih0Tjgi081YLM7fwbMyegenv07ZymFv1lsfwHYmSkgGPMOZNN4XHTPDAuUbD5VznCJ4F_-2JkFzsLx9ugm7YRCYJgomkZU0N5-Nvx8xu3qN4DmuTj0Hz0eKGOGmKXiafYiZagBKHkniK59H_Q78K_oUKdWhWor5NFdjE7qN6eKfKWlg7oEh1f2J5mAnU6gv\x26random\x3d3279076572\x26rmt_tld\x3d0\x26ipr\x3dy`
- `https://www.google.com/pagead/1p-user-list/700498227/?random\x3d1790587324824\x26cv\x3d11\x26fst\x3d1790586000000\x26bg\x3dffffff\x26guid\x3dON\x26async\x3d1\x26en\x3dform_submit\x26gtm\x3d45be69n1v9203804702za20gzb893108960zd893108960xecxf1\x26gcd\x3d13l3l3l3l1l1\x26dma\x3d0\x26tag_exp\x3d115938465~115938468~118897920~118897930~120213116~120385422~120469145~120469153\x26u_w\x3d3440\x26u_h\x3d1440\x26url\x3dhttps%3A%2F%2Fapp-us.smtp2go.com%2Fdashboard%2Fmain%2F%3FNone%3D\x26rcb\x3d1\x26frm\x3d0\x26tiba\x3dSMTP2GO%20%7C%20Dashboard\x26ae\x3da\x26hn\x3dwww.googleadservices.com\x26npa\x3d0\x26pscdl\x3dnoapi\x26auid\x3d2111033616.1790587091\x26uaa\x3darm\x26uab\x3d64\x26uafvl\x3dGoogle%2520Chrome%3B153.0.8010.53%7CNot_A%2520Brand%3B8.0.0.0%7CChromium%3B153.0.8010.53\x26uamb\x3d0\x26uam\x3d\x26uap\x3dmacOS\x26uapv\x3d26.6.2\x26uaw\x3d0\x26data\x3devent%3Dform_submit\x26gap.fsrc\x3d2\x26ept\x3d9\x26rfmt\x3d3\x26fmt\x3d3\x26is_vtc\x3d1\x26cid\x3dCAQS-gEAQM4h3Hme0B733RnZw83O2As1oZbANN68Hkl5dua9sF-Nivcr8b1eQOX1IEzkD5zvSr-FNQs9CT2Tg9Ya2DM2OKiigu5HIAass5xkbtbjLdTmXF9gxna-QlPT0IkpHI_yCd1xKnpVXaPW2w3QAymTkMlDJQxaBvR_4UM2K5RTqbTGqeY8pGk0hcJM8JhDlL2YvPCcMkcfRKz8HY_0s2CKcn4bfSbg1SRpaV_dRA57VaTEM-C616WkX870zLdMirxDdL__IeXUgmrERGIJlpZHdF86_dw43yXDctSW6qPfT-Rxi_pbLzLRwC6amyttrn08e_9m9ctUqo3Z\x26random\x3d33006494\x26rmt_tld\x3d0\x26ipr\x3dy`
- `https://www.google.com/pagead/1p-user-list/700498227/?random\x3d1790587337706\x26cv\x3d11\x26fst\x3d1790586000000\x26bg\x3dffffff\x26guid\x3dON\x26async\x3d1\x26en\x3dgtag.config\x26gtm\x3d45be69n1v9203804702z8893108960za20gzb893108960zd893108960xecxf1\x26gcd\x3d13l3l3l3l1l1\x26dma\x3d0\x26tag_exp\x3d115938466~115938469~118897920~118897930~120213116~120385422~120469145~120469153\x26u_w\x3d1512\x26u_h\x3d982\x26url\x3dhttps%3A%2F%2Fapp-us.smtp2go.com%2Fdashboard%2Fmain%2F%3FNone%3D\x26rcb\x3d10\x26frm\x3d0\x26tiba\x3dSMTP2GO%20%7C%20Dashboard\x26hn\x3dwww.googleadservices.com\x26npa\x3d0\x26pscdl\x3dnoapi\x26auid\x3d2111033616.1790587091\x26uaa\x3darm\x26uab\x3d64\x26uafvl\x3dGoogle%2520Chrome%3B153.0.8010.53%7CNot_A%2520Brand%3B8.0.0.0%7CChromium%3B153.0.8010.53\x26uamb\x3d0\x26uam\x3d\x26uap\x3dmacOS\x26uapv\x3d26.6.2\x26uaw\x3d0\x26data\x3devent%3Dgtag.config\x26ept\x3d9\x26rfmt\x3d3\x26fmt\x3d3\x26is_vtc\x3d1\x26cid\x3dCAQS-gEAQM4h3OiGxeBg-m6PzOmqdcmj3vPQrZNyBFSpp_U32TGq9Ybfiy5gPih_6idUDkcoO9zkWxjnHRwgU25Kpp9Xl7LiG193wB8cHI_qK9fAPLtDNEhQ5KjYQktNpYWlxVxNysftquFlF77XbFklpPj1z8--SXZSrKNviO2LuAMgEevhG1N4SMh53jRuEWYI0ftfh0oTj7Iw74q_aHjOHI5_bGrbE4TYNZ6uxuElo6FwFMwTNoKO4zR69FdKQ7kpDt1NvXDQl8NKgkYUg3urgfmgQxlJ0JBe6oiW4eJhbyg4NiOiNfC_v79hD87cgxbzAQBBnMYHhVcC7UdS\x26random\x3d2567710181\x26rmt_tld\x3d0\x26ipr\x3dy`
- `https://www.google.com/pagead/1p-user-list/700498227/?random\x3d1790587402849\x26cv\x3d11\x26fst\x3d1790586000000\x26bg\x3dffffff\x26guid\x3dON\x26async\x3d1\x26en\x3dgtag.config\x26gtm\x3d45be69n1v9203804702z8893108960za20gzb893108960zd893108960xecxf1\x26gcd\x3d13l3l3l3l1l1\x26dma\x3d0\x26tag_exp\x3d115616986~115938465~115938469~118897920~118897930~120213116~120385423~120469145~120469153~121280969\x26u_w\x3d1512\x26u_h\x3d982\x26url\x3dhttps%3A%2F%2Fapp-us.smtp2go.com%2Femail-testing%2F\x26rcb\x3d12\x26frm\x3d0\x26tiba\x3dSMTP2GO%20%7C%20Email%20Testing\x26hn\x3dwww.googleadservices.com\x26npa\x3d0\x26pscdl\x3dnoapi\x26auid\x3d2111033616.1790587091\x26uaa\x3darm\x26uab\x3d64\x26uafvl\x3dGoogle%2520Chrome%3B153.0.8010.53%7CNot_A%2520Brand%3B8.0.0.0%7CChromium%3B153.0.8010.53\x26uamb\x3d0\x26uam\x3d\x26uap\x3dmacOS\x26uapv\x3d26.6.2\x26uaw\x3d0\x26data\x3devent%3Dgtag.config\x26ept\x3d9\x26rfmt\x3d3\x26fmt\x3d3\x26is_vtc\x3d1\x26cid\x3dCAQS-gEAQM4h3FsiELsEa3DsrBALVRuCSK6vL9gOiKNFLVzMCmeADthFjQV17GquLtPYMyOZnq5Ix0yLESa4tTyYPvqNYFs_YToHgBsY6qjLJc8QHCaG_IL2yuKGX4o_BcSAVVBRdlTdvBV5qVybX3BieSnk9WhnwWDEOqVhcLTLmy1-qIe44kA3HL-qUqidV6cEQiCrJckhRzYLQvxYBnkpgsT2Y3o7kmh_wX0bqg79onRFMkDklQQQ35_HyPyd0LoZMHQ3U3hGuN0K0XDyiAX8k_laIGmk3iisp05bS02RazDvxtSBeTECyNhngwiLoBocVmjXSOaJEb78MzW4\x26random\x3d3637030327\x26rmt_tld\x3d0\x26ipr\x3dy`
- `https://www.google.com/pagead/1p-user-list/700498227/?random\x3d1790587403746\x26cv\x3d11\x26fst\x3d1790586000000\x26bg\x3dffffff\x26guid\x3dON\x26async\x3d1\x26en\x3dform_start\x26gtm\x3d45be69n1v9203804702za20gzb893108960zd893108960xecxf1\x26gcd\x3d13l3l3l3l1l1\x26dma\x3d0\x26tag_exp\x3d115616986~115938465~115938469~118897920~118897930~120213116~120385423~120469145~120469153~121280969\x26u_w\x3d1512\x26u_h\x3d982\x26url\x3dhttps%3A%2F%2Fapp-us.smtp2go.com%2Femail-testing%2F\x26rcb\x3d12\x26frm\x3d0\x26tiba\x3dSMTP2GO%20%7C%20Email%20Testing\x26ae\x3da\x26hn\x3dwww.googleadservices.com\x26npa\x3d0\x26pscdl\x3dnoapi\x26auid\x3d2111033616.1790587091\x26uaa\x3darm\x26uab\x3d64\x26uafvl\x3dGoogle%2520Chrome%3B153.0.8010.53%7CNot_A%2520Brand%3B8.0.0.0%7CChromium%3B153.0.8010.53\x26uamb\x3d0\x26uam\x3d\x26uap\x3dmacOS\x26uapv\x3d26.6.2\x26uaw\x3d0\x26data\x3devent%3Dform_start\x26gap.fsrc\x3d1\x26ept\x3d9\x26rfmt\x3d3\x26fmt\x3d3\x26is_vtc\x3d1\x26cid\x3dCAQS-gEAQM4h3FqTurJ02cAY871GY6UPvKUTEpQBp0bBdduTKy49cvPn9BRWl049twfmiZSrM2eRsWAf_98WTSEpTnxzSBQwyE5ousKmjhAJMQfq710bh6D3XwDAgT5R1WpLucu1R2QE8LxjZwse1fNGHzb_wXsScXWMypRq7QdH7vgEocgJ1DyqayQjqvugr1h8cHoUecIEpU922ee86FZKyavqeW8bJd8CkYC5e5HDLcD4UAGhvy8ZxjEjBXKYTaq0wl6-1g7OX_2DhFvCBBzizx37z7etQIO6kGYuYvXKrW0VcO0jb7rxKqwTpTk_MbcLYazxO96rU8h3Bw-q\x26random\x3d747637782\x26rmt_tld\x3d0\x26ipr\x3dy`
- `https://www.google.com/pagead/1p-user-list/700498227/?random\x3d1790587403750\x26cv\x3d11\x26fst\x3d1790586000000\x26bg\x3dffffff\x26guid\x3dON\x26async\x3d1\x26en\x3dform_submit\x26gtm\x3d45be69n1v9203804702za20gzb893108960zd893108960xecxf1\x26gcd\x3d13l3l3l3l1l1\x26dma\x3d0\x26tag_exp\x3d115616986~115938465~115938469~118897920~118897930~120213116~120385423~120469145~120469153~121280969\x26u_w\x3d1512\x26u_h\x3d982\x26url\x3dhttps%3A%2F%2Fapp-us.smtp2go.com%2Femail-testing%2F\x26rcb\x3d12\x26frm\x3d0\x26tiba\x3dSMTP2GO%20%7C%20Email%20Testing\x26ae\x3da\x26hn\x3dwww.googleadservices.com\x26npa\x3d0\x26pscdl\x3dnoapi\x26auid\x3d2111033616.1790587091\x26uaa\x3darm\x26uab\x3d64\x26uafvl\x3dGoogle%2520Chrome%3B153.0.8010.53%7CNot_A%2520Brand%3B8.0.0.0%7CChromium%3B153.0.8010.53\x26uamb\x3d0\x26uam\x3d\x26uap\x3dmacOS\x26uapv\x3d26.6.2\x26uaw\x3d0\x26data\x3devent%3Dform_submit\x26gap.fsrc\x3d2\x26ept\x3d9\x26rfmt\x3d3\x26fmt\x3d3\x26is_vtc\x3d1\x26cid\x3dCAQS-gEAQM4h3HB6oMdOYN0sTLekCXXoBzQAL_qNeKVZfK_vfhQc2lzfRQaWEJILWdaWCj4pCng5HN6VX_BjT7ZHKsjOtyt_cHsPytPqX5cIF8rPWqiVoHje5sSgDYRPk1sPoTkEqVHn2-kBKvGtHFK3ZZVMH38MZE3ahnXf3O8cbHurph6QtKkT9Mkh2h_SOcPOmKXWvhkysbPBtEbLpJtJypdF2LfDaN9oyAj1Yfpjv2Yl4ktRAb6D7Wpxcm4FjicT4IDj9dlxhwdbTZCNriSdoOBpNbF3SSI19aDM0jpPJyXTb95VdwaBq7IHrwUQ5jdGkLmIXncVLd4QxgGp\x26random\x3d1532877886\x26rmt_tld\x3d0\x26ipr\x3dy`
- `https://www.google.com/pagead/1p-user-list/700498227/?random\x3d1790587416392\x26cv\x3d11\x26fst\x3d1790586000000\x26bg\x3dffffff\x26guid\x3dON\x26async\x3d1\x26en\x3dgtag.config\x26gtm\x3d45be69n1v9203804702z8893108960za20gzb893108960zd893108960xecxf1\x26gcd\x3d13l3l3l3l1l1\x26dma\x3d0\x26tag_exp\x3d115938465~115938469~118897920~118897930~120213116~120385423~120469145~120469153\x26u_w\x3d1512\x26u_h\x3d982\x26url\x3dhttps%3A%2F%2Fapp-us.smtp2go.com%2Fdashboard%2Fmain%2F\x26rcb\x3d3\x26frm\x3d0\x26tiba\x3dSMTP2GO%20%7C%20Dashboard\x26hn\x3dwww.googleadservices.com\x26npa\x3d0\x26pscdl\x3dnoapi\x26auid\x3d2111033616.1790587091\x26uaa\x3darm\x26uab\x3d64\x26uafvl\x3dGoogle%2520Chrome%3B153.0.8010.53%7CNot_A%2520Brand%3B8.0.0.0%7CChromium%3B153.0.8010.53\x26uamb\x3d0\x26uam\x3d\x26uap\x3dmacOS\x26uapv\x3d26.6.2\x26uaw\x3d0\x26data\x3devent%3Dgtag.config\x26ept\x3d9\x26rfmt\x3d3\x26fmt\x3d3\x26is_vtc\x3d1\x26cid\x3dCAQS-gEAQM4h3GuQirYFvAdVBOhjj_9_H415dBLjkVmax2u_iMbNlSukxAOlf-slMHGYhInzlwDL_KUFfjIAn5G0ldvCg5f6M2IBkHH-4Myn9tQmS-xCmV7V8VfTFzKEap76V2xWA1pqRmMdonP7nLHLn_3yp98Q_3WLfayYKszAMhqeV_3GAiK_WObDlWDsAYxf63HxEiNvUnbVpT0iczpWGHqdM92Gb6roiiiD7v5c5zcWXSIkSQD2r1wb-NIn5uiPpyOv-DNWlHoK5fdoqJGl6a7MroloCSYxh5tDmi9BSTKYlxrLnJi36Pe9bpJqRtqLIZ7sgBIXjvr3FTJL\x26random\x3d1600838748\x26rmt_tld\x3d0\x26ipr\x3dy`
- `https://www.googleadservices.com`
- `https://www.googletagmanager.com`
- `https://www.googletagmanager.com/`
- `https://www.googletagmanager.com/static/service_worker/`
- `https://www.redditstatic.com/ads/pixel.js`
- `https://www.redditstatic.com/campaign-management/`
- `https://www.smtp2go.com/setupguide/salesforce/`
- `https://www.youtube.com`

## Browser storage found (may leak tokens / config)

- https://app-us.smtp2go.com/dashboard/main/?None=
  - localStorage keys: ZD-store, ZD-suid, _uetvid_exp, ZD-settings, _uetsid_exp, ZD-buid, {announcekit}:57544, _uetvid, graphcolors.1, _gcl_ls, _uetsid, __zlcstore
  - sessionStorage keys: _rdt_cfg, _cltk
- https://app-us.smtp2go.com/email-testing
  - localStorage keys: ZD-store, ZD-suid, _uetvid_exp, ZD-settings, _uetsid_exp, ZD-buid, {announcekit}:57544, _uetvid, graphcolors.1, _gcl_ls, _uetsid, __zlcstore
  - sessionStorage keys: _rdt_cfg, _cltk
- https://app-us.smtp2go.com/settings/dedicatedips
  - localStorage keys: ZD-store, ZD-suid, _uetvid_exp, ZD-settings, _uetsid_exp, ZD-buid, {announcekit}:57544, _uetvid, graphcolors.1, _gcl_ls, _uetsid, __zlcstore
  - sessionStorage keys: _rdt_cfg, _cltk

---
*Full machine-readable detail is in `report.json`; the live event log is in `notebook.jsonl`.*