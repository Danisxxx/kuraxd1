import requests

def main():
    session = requests.Session()
    
    headers = {
        'authority': 'tractive.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9',
        'sec-ch-ua': '"Not A(Brand";v="99", "Microsoft Edge";v="121", "Chromium";v="121"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0',
    }

    response = session.get('https://tractive.com/', headers=headers)
    headers = {
        'authority': 'tractive.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        #'authorization': 'Bearer jnq5hljgej51oyenig8r23hhp36rgjk0',
        # 'cookie': '_vwo_uuid_v2=DB2960AE464A31F5A8CDE1750BAB2CA06|5b1d8ecd5c68201bc96e335a92c41fea; tractive_store=eu_en; _ga=GA1.1.1087820171.1707504362; cikneeto_uuid=id:453c571a-7d63-4e76-97b9-ac027c4e5507; _vwo_uuid=DB2960AE464A31F5A8CDE1750BAB2CA06; _vwo_ds=3%241707504360%3A74.36598288%3A%3A; PHPSESSID=ukgiub4fkb3bpbun4kdk6lami4; banner_id=4846; _vis_opt_s=1%7C; _vis_opt_test_cookie=1; _vis_opt_exp_105_combi=2; _gcl_au=1.1.519120900.1707504365; cookie_consent=analytics,marketing,required; _tt_enable_cookie=1; _ttp=q0wmJ-Nmj4lzLFW0hD2LBO89SLg; _vis_opt_exp_92_combi=4; _vis_opt_exp_105_goal_2=1; _uetsid=7cce8bf0c77b11eea1813d0a1fb954c3; _uetvid=7ccec2e0c77b11ee969941efc53b8848; _tq_id.TV-7290455481-1.b6c8=8834a573922858d0.1707504369.0.1707504394..; FPGSID=1.1707504362.1707504434.G-0SS4FLYQP7.H7MRgm-JvCzFMEFZb2NO5w; _vwo_sn=0%3A5%3A%3A%3A1; _ga_0SS4FLYQP7=GS1.1.1707504362.1.1.1707504437.0.0.0; cikneeto=date:1707504437771',
        'referer': 'https://tractive.com/en/pc/accessories?sku=TRAMINDB',
        'sec-ch-ua': '"Not A(Brand";v="99", "Microsoft Edge";v="121", "Chromium";v="121"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0',
    }

    response = session.get('https://tractive.com/eu_en/rest/eu_en/V1/cart/ensureId', headers=headers).cookies
    print(response)
    
    headers = {
        'authority': 'tractive.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'max-age=0',
        # 'cookie': '_vwo_uuid_v2=DB2960AE464A31F5A8CDE1750BAB2CA06|5b1d8ecd5c68201bc96e335a92c41fea; _ga=GA1.1.1087820171.1707504362; cikneeto_uuid=id:453c571a-7d63-4e76-97b9-ac027c4e5507; _vwo_uuid=DB2960AE464A31F5A8CDE1750BAB2CA06; _vwo_ds=3%241707504360%3A74.36598288%3A%3A; PHPSESSID=ukgiub4fkb3bpbun4kdk6lami4; banner_id=4846; _vis_opt_s=1%7C; _vis_opt_test_cookie=1; _vis_opt_exp_105_combi=2; _gcl_au=1.1.519120900.1707504365; cookie_consent=analytics,marketing,required; _tt_enable_cookie=1; _ttp=q0wmJ-Nmj4lzLFW0hD2LBO89SLg; _vis_opt_exp_92_combi=4; _vis_opt_exp_105_goal_2=1; _tq_id.TV-7290455481-1.b6c8=8834a573922858d0.1707504369.0.1707504394..; _vis_opt_exp_92_goal_3=1; _vis_opt_exp_105_goal_3=1; _fbp=fb.1.1707504465960.1812979903; cikneeto=date:1707504467872; FPGSID=1.1707504362.1707504499.G-0SS4FLYQP7.H7MRgm-JvCzFMEFZb2NO5w; tractive_store=us_en; _vwo_sn=0%3A9%3A%3A%3A1; _uetsid=7cce8bf0c77b11eea1813d0a1fb954c3; _uetvid=7ccec2e0c77b11ee969941efc53b8848; _ga_0SS4FLYQP7=GS1.1.1707504362.1.1.1707504534.0.0.0; _geuid=01b0af82-8aa4-4067-9621-2fab7116645b; _gess=true; _li_dcdm_c=.tractive.com; _lc2_fpi=265cae000887--01hp7k731qqywew97bb1gvka9h; _lc2_fpi_meta={%22w%22:1707504536631}; aws-waf-token=0ba63e1a-bb4d-4082-92e2-b6626aec51e6:CQoApg+CwYsRAAAA:nCx81QSU1BVkudHD5ca85Z10/lFXWxTLdDZ3LShfojFSrYOL0jyrk3T6Nbd+3TpHVeMdxCdULRbs5Frb6fHrKE3flP20Us6ictZdjVBuZRYMUQsDXS2J4jmqD/NeFavtQVCE4Zvdm/iIXqvmH/5b8Vwby9v380Pnnu6jJrgw14d4B0cR88/FoCIsTbwIK0xcJIGMBpN0OKuL/s+Ldaqrdx48lJ6D3SDz/h+9CygGME5FTUdzLQ==',
        'if-modified-since': 'Wed, 07 Feb 2024 05:44:00 GMT',
        'if-none-match': 'W/"36e5afceacd20cdfafe842378b0bf8e2"',
        'sec-ch-ua': '"Not A(Brand";v="99", "Microsoft Edge";v="121", "Chromium";v="121"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0',
    }

    params = {
        'openCart': '1',
        'store': 'us_en',
    }

    response = session.get('https://tractive.com/checkout/', params=params, headers=headers)
    
    headers = {
        'authority': 'tractive.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        #'authorization': 'Bearer jnq5hljgej51oyenig8r23hhp36rgjk0',
        # 'cookie': '_vwo_uuid_v2=DB2960AE464A31F5A8CDE1750BAB2CA06|5b1d8ecd5c68201bc96e335a92c41fea; _ga=GA1.1.1087820171.1707504362; cikneeto_uuid=id:453c571a-7d63-4e76-97b9-ac027c4e5507; _vwo_uuid=DB2960AE464A31F5A8CDE1750BAB2CA06; _vwo_ds=3%241707504360%3A74.36598288%3A%3A; PHPSESSID=ukgiub4fkb3bpbun4kdk6lami4; banner_id=4846; _vis_opt_s=1%7C; _vis_opt_test_cookie=1; _vis_opt_exp_105_combi=2; _gcl_au=1.1.519120900.1707504365; cookie_consent=analytics,marketing,required; _tt_enable_cookie=1; _ttp=q0wmJ-Nmj4lzLFW0hD2LBO89SLg; _vis_opt_exp_92_combi=4; _vis_opt_exp_105_goal_2=1; _tq_id.TV-7290455481-1.b6c8=8834a573922858d0.1707504369.0.1707504394..; _vis_opt_exp_92_goal_3=1; _vis_opt_exp_105_goal_3=1; _fbp=fb.1.1707504465960.1812979903; cikneeto=date:1707504467872; FPGSID=1.1707504362.1707504499.G-0SS4FLYQP7.H7MRgm-JvCzFMEFZb2NO5w; tractive_store=us_en; _vwo_sn=0%3A9%3A%3A%3A1; _uetsid=7cce8bf0c77b11eea1813d0a1fb954c3; _uetvid=7ccec2e0c77b11ee969941efc53b8848; _ga_0SS4FLYQP7=GS1.1.1707504362.1.1.1707504534.0.0.0; _geuid=01b0af82-8aa4-4067-9621-2fab7116645b; _gess=true; _li_dcdm_c=.tractive.com; _lc2_fpi=265cae000887--01hp7k731qqywew97bb1gvka9h; _lc2_fpi_meta={%22w%22:1707504536631}; aws-waf-token=0ba63e1a-bb4d-4082-92e2-b6626aec51e6:CQoAeIWDhFQJAAAA:Yly2TqIzzBRsRzaNXkB3lR8tNcawtZ9y0juqVpwKp2v9/AnazEmDRo7qGZcPoYHq2APUTSctYs4BZN3DeJiusGJM5SiExE5RTwNQO8fEXl/uGoS2jpc8l6+UBVdxhlLB5g1kNPBH5psY3wP2bXWsy0TzUIcI3WmeSuTktI/T1ENhjBfZnKypCcjIuAE/kijFE5/umaCF4OvNY7BIS5cVJUXROinH4ZmIYAjV/HhUxLMld8kYGA==',
        'newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjI4MDg1MiIsImFwIjoiMTEyMDIxODI5MSIsImlkIjoiNmJlNzU3ODhmMTllYWMyMiIsInRyIjoiOGJmMTQyM2M5MGIxNjk2NDQ2ZTU3YTA0YThmZDMzMDAiLCJ0aSI6MTcwNzUwNDU0MDE5MX19',
        'referer': 'https://tractive.com/checkout/?openCart=1&store=us_en',
        'sec-ch-ua': '"Not A(Brand";v="99", "Microsoft Edge";v="121", "Chromium";v="121"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'traceparent': '00-8bf1423c90b1696446e57a04a8fd3300-6be75788f19eac22-01',
        'tracestate': '280852@nr=0-1-280852-1120218291-6be75788f19eac22----1707504540191',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0',
    }

    response = session.get('https://tractive.com/us_en/rest/us_en/V1/cart/getId', headers=headers).text
    print(response)
    return
    
    headers = {
        'authority': 'tractive.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        #'authorization': 'Bearer jnq5hljgej51oyenig8r23hhp36rgjk0',
        'content-type': 'application/json',
        # 'cookie': '_vwo_uuid_v2=DB2960AE464A31F5A8CDE1750BAB2CA06|5b1d8ecd5c68201bc96e335a92c41fea; _ga=GA1.1.1087820171.1707504362; cikneeto_uuid=id:453c571a-7d63-4e76-97b9-ac027c4e5507; _vwo_uuid=DB2960AE464A31F5A8CDE1750BAB2CA06; _vwo_ds=3%241707504360%3A74.36598288%3A%3A; PHPSESSID=ukgiub4fkb3bpbun4kdk6lami4; banner_id=4846; _vis_opt_s=1%7C; _vis_opt_test_cookie=1; _vis_opt_exp_105_combi=2; _gcl_au=1.1.519120900.1707504365; cookie_consent=analytics,marketing,required; _tt_enable_cookie=1; _ttp=q0wmJ-Nmj4lzLFW0hD2LBO89SLg; _vis_opt_exp_92_combi=4; _vis_opt_exp_105_goal_2=1; _tq_id.TV-7290455481-1.b6c8=8834a573922858d0.1707504369.0.1707504394..; _vis_opt_exp_92_goal_3=1; _vis_opt_exp_105_goal_3=1; _fbp=fb.1.1707504465960.1812979903; cikneeto=date:1707504467872; tractive_store=us_en; _geuid=01b0af82-8aa4-4067-9621-2fab7116645b; _gess=true; _li_dcdm_c=.tractive.com; _lc2_fpi=265cae000887--01hp7k731qqywew97bb1gvka9h; _lc2_fpi_meta={%22w%22:1707504536631}; _uetsid=7cce8bf0c77b11eea1813d0a1fb954c3; _uetvid=7ccec2e0c77b11ee969941efc53b8848; _vwo_sn=0%3A11%3A%3A%3A1; guid=3f071c1e9ce03a2b54c92cdd9f08be0f; _ga_0SS4FLYQP7=GS1.1.1707504362.1.1.1707504556.0.0.0; FPGSID=1.1707504362.1707504560.G-0SS4FLYQP7.H7MRgm-JvCzFMEFZb2NO5w; aws-waf-token=0ba63e1a-bb4d-4082-92e2-b6626aec51e6:CQoAj4KCuwYTAAAA:Ql+PhjhBoKXAOfFD+Sm/tHuc6CCKoMglTprZxSki5jzsjUQ4+4YbyvDAECSThTHHWSJxTpr30NmgG5ZbTsy8LhTNXd+bd/dGRvOILn+3sLAPGb/ACynCvX9j/1VgO+6RkeJh53ttTrXKR6RnDCvtx8J3tCgD4QA5ICCYQElr3wFf9JCC94k7Y8+bJEdMdhrFtm0HeaP67UpmDMOU6zlfIA+iFOURu9Zkj0I4xp2+6OKqLHKoCA==',
        'newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjI4MDg1MiIsImFwIjoiMTEyMDIxODI5MSIsImlkIjoiZWU3ZmNhMTc0NGU1YjY1OCIsInRyIjoiYTdiNDJmNDRkZmE4MWIyMzc4NDY1NTVjMzUwMjQ5MDAiLCJ0aSI6MTcwNzUwNDU3MjgzNX19',
        'origin': 'https://tractive.com',
        'referer': 'https://tractive.com/checkout/?openCart=1&store=us_en',
        'sec-ch-ua': '"Not A(Brand";v="99", "Microsoft Edge";v="121", "Chromium";v="121"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'traceparent': '00-a7b42f44dfa81b237846555c35024900-ee7fca1744e5b658-01',
        'tracestate': '280852@nr=0-1-280852-1120218291-ee7fca1744e5b658----1707504572835',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0',
    }

    json_data = {
        'billingAddress': {
            'city': 'New York',
            'countryId': 'US',
            'customAttributes': {
                'terms_accepted': True,
                'privacy_accepted': True,
                'uptodate_accepted': False,
            },
            'extension_attributes': {
                'terms_accepted': True,
                'privacy_accepted': True,
                'uptodate_accepted': False,
            },
            'firstname': 'Andres',
            'lastname': 'Bermudez',
            'postcode': '10080',
            'region': 'New York',
            'regionId': '43',
            'regionCode': 'NY',
            'street': [
                'street 16th, av. billonarie',
                '',
            ],
            'telephone': '2486354657',
        },
        'email': 'naneteharlequin@jcnorris.com',
        'paymentMethod': {
            'method': 'adyen_cc',
            'additional_data': {
                'cc_type': 'visa',
                'stateData': '{"riskData":{"clientData":"eyJ2ZXJzaW9uIjoiMS4wLjAiLCJkZXZpY2VGaW5nZXJwcmludCI6IkRwcXdVNHpFZE4wMDUwMDAwMDAwMDAwMDAwOXkzdE9SbGUyUTAwMjU1Mzc4MDBjVkI5NGlLekJHcUlkNzBJdkV1TkJpeDdSWDNhejgwMDJDQ3Q5cWlRR0NjMDAwMDBxWmtURTAwMDAwSHhaMmZZNHUwN0VDNEZsU0FCbVE6NDAiLCJwZXJzaXN0ZW50Q29va2llIjpbXSwiY29tcG9uZW50cyI6eyJ1c2VyQWdlbnQiOiIzMTZmZTVjYTA0NjMxZDkyOThlZDc4NzE0ZTU1NjY4NSIsIndlYmRyaXZlciI6MCwibGFuZ3VhZ2UiOiJlbi1VUyIsImNvbG9yRGVwdGgiOjI0LCJkZXZpY2VNZW1vcnkiOjQsInBpeGVsUmF0aW8iOjEsImhhcmR3YXJlQ29uY3VycmVuY3kiOjIsInNjcmVlbldpZHRoIjo3NjgsInNjcmVlbkhlaWdodCI6MTM2NiwiYXZhaWxhYmxlU2NyZWVuV2lkdGgiOjcyOCwiYXZhaWxhYmxlU2NyZWVuSGVpZ2h0IjoxMzY2LCJ0aW1lem9uZU9mZnNldCI6MCwidGltZXpvbmUiOiJVVEMiLCJzZXNzaW9uU3RvcmFnZSI6MSwibG9jYWxTdG9yYWdlIjoxLCJpbmRleGVkRGIiOjEsImFkZEJlaGF2aW9yIjowLCJvcGVuRGF0YWJhc2UiOjAsInBsYXRmb3JtIjoiV2luMzIiLCJwbHVnaW5zIjoiMjljZjcxZTNkODFkNzRkNDNhNWIwZWI3OTQwNWJhODciLCJjYW52YXMiOiI0NGMwNDA5MGU2MzI3ZWQ1MTBlOWNmZjUxODkyNDlmNSIsIndlYmdsIjoiM2Y5MjQ3MTQyZjZiOTZjMmQyYzYzMTYwNDI5YzBjYzkiLCJ3ZWJnbFZlbmRvckFuZFJlbmRlcmVyIjoiR29vZ2xlIEluYy4gKEdvb2dsZSl+QU5HTEUgKEdvb2dsZSwgVnVsa2FuIDEuMy4wIChTd2lmdFNoYWRlciBEZXZpY2UgKFN1Ynplcm8pICgweDAwMDBDMERFKSksIFN3aWZ0U2hhZGVyIGRyaXZlcikiLCJhZEJsb2NrIjowLCJoYXNMaWVkTGFuZ3VhZ2VzIjowLCJoYXNMaWVkUmVzb2x1dGlvbiI6MCwiaGFzTGllZE9zIjowLCJoYXNMaWVkQnJvd3NlciI6MCwiZm9udHMiOiJiYzA4ZTExZjczNzIxYmQ1MzM3MmJkMzc0ODNkNDU4OSIsImF1ZGlvIjoiOTAyZjBmZTk4NzE5Yjc3OWVhMzdmMjc1MjhkZmIwYWEiLCJlbnVtZXJhdGVEZXZpY2VzIjoiMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAifX0="},"checkoutAttemptId":"520cf155-81db-4398-b3f2-fda360ffc878170750627623976753BEC46E67F5E8F233679DB0E9336AED40392CE1E5DC79FCB085CB44728D8","paymentMethod":{"type":"scheme","holderName":"Andres Bermudez","encryptedCardNumber":"eyJhbGciOiJSU0EtT0FFUCIsImVuYyI6IkEyNTZDQkMtSFM1MTIiLCJ2ZXJzaW9uIjoiMSJ9.SVTOSddDp3aHIcUa1mqvv5cV_WCVhmDRSMzh88aYqkPQm8i9dCgOyAXhpEYkurve-cHlkWqaehsh_5bdMb2doSJQ59NTfqgxfxAeFoyvWpx0ubwgyGhq5jhIad7RoKe9cL6R4aG1VKqUcl8zt76Znu53L036NqhPy8r0V97dihAlQ-wFjzNnR6JIhvlDtetAofEwltO3AyML5ym8qJhg01TydGlVrcF1LP8A1_RSd-NG2WuYHbKmFFI-ZEin7GWBvtcwdXhD4ToHYf7i8FrV-kSEpFSyRcoHODpWN4moIpp0UvtZsOd4waUCt_9xn_lFQVZ7NZtSDTbJX0s-fykaRg.MUvdAoMgxY9ZNQZtLyTt2Q.eelcR3TY8bvOxKrYibrBGYSH1MUCAy7TYPe19xwpr1stv-S03koTovwBv_GRDyCsLGkEK8S7Rs5B8lxBv4le2FEqKswdK4rvfSmz61M7ziPwEG05mJx6PiKMt4_QCgniW2hYoDxpXe2VlB_NOeKxtTcfsuPoo15lthuG7-epAubub24jcXBue3hRIFTGf1Z2jjLZazwP_M9bYrYX-Q0wuzRK2TuyVfDP3zheIWiM8RTkWSwpKEAr6m0WSdIoYX0raui54iND2ekmbGUw_fNnwCLdjSLMizgI7a7H1yP4TB0JvltiZi7P6dpNt6zkJkktdX1UTP3ruZk7q5a4_vwMSNpvXNH6XLO23gHEVBwFeJkCEYA216LMIJYmCvt1BKJcVhZMXTpMGPzq7qu7Le-pmJWFFP3jF_9C9MU1JieTrcLMU1mGhu7pFJN7WYuG6itpC4ohoiMH5xtxijNm8TqjWxIQcAnbFLnmAtgbW9bObEU2bCJ08C_fsmhnMEPAzbylZYAStvaMNpIpa_sxjV7WPryCNMIdVa7YTYNIGzZgaWCIRGKo7pBPSUwLxYdoTrDgbKsy92gJNK08Xjb-5egez6hfjqZ84pNwfQjZy5hsyew.MoDLavW7ZdJjUa-d2HLK5UP80Er_5CryXx_YG1iWspU","encryptedExpiryMonth":"eyJhbGciOiJSU0EtT0FFUCIsImVuYyI6IkEyNTZDQkMtSFM1MTIiLCJ2ZXJzaW9uIjoiMSJ9.wn931ixOkLDpwyUU6qZkRhCKyXWhzBwVdjxMG3-5rrvDyJ2uLelNhebe_N_gpXLD0njbF_F5kY9rb_c-Eiq1lJv2-p0xMcoZj-4t6N3KUK7DB-p5i7WmGYRJ23Wy5osydIQ7BkleZJKEJLuPAb3Y9vZqTAS4vpRweNk92oeHu2kvcKXVdQWOSWv_ldyUWUz8YJr7souqEivaw9HP4_spcuE5_R6WQwLWWD2Y2i3zhb96hYGYKoxv04i9hWEhKFRuj-fYXSjmmXWQ4BNhQ5gbSYYwXu3h6BJ02D9F_e9jOADX9GR6qwXJsWHtjH46CQifXXy0lgcPQjjM_PX0g0gBSA.OU_-JlloDcOh4g9eWurpTg.k9wGCBPL3tsL3hmWNjeb0uK4XT69KrynqaX2V__jxx-ysrDSlb5erFTRt6U5gqX79X5V2tAbaznO1Q-3VXWS1A.XpRBhzWAuNzJUD2UvMuN0rre3gyxZlyK-7dcHi3vmfo","encryptedExpiryYear":"eyJhbGciOiJSU0EtT0FFUCIsImVuYyI6IkEyNTZDQkMtSFM1MTIiLCJ2ZXJzaW9uIjoiMSJ9.ue7DoRbTFxEXMSIeAIXrdw6-nnacsqMajJEUphK0GkBgL6x9eNOMNROgCPYQGbqrzA1cb_CNJTFe3esnvlDIowkVWIvLSBmsQrYCvhz-179xArKPa7lZErsqapw04Jeg5ht9Iwh3xrlHnkxHvChGaNIPTKliUJVd2t6E5TMGAxXLluN0cAuqnLYwFJXQ6OIqN_vImAsw65b5e-n4tM1yAtsquPgUxhXc4pWIlAm1VOK-YnoptxEQxp4XvWtCg_t17yatTXXT1E0Z5Apdwm6_0r4J_vH88kmdqG2KJqxxuKyrovekpJuIREsraR5XIU8Hipum6uDD5aqGzhTUqRQYuQ.Bm91ja35lN9jqKy10rfXNg.D6JczJPC4B0LqZO8JYbFdoVv01NfF2GS7-4_wpqm7rsvXTHcvDHPK6UXUsHXjqkSWeuz53EwLcj0ILZLci8mJg.2Qs-vJkU4xAbuhbyq-0fsw9bYcQWhXO5P6co-XMj33c","encryptedSecurityCode":"eyJhbGciOiJSU0EtT0FFUCIsImVuYyI6IkEyNTZDQkMtSFM1MTIiLCJ2ZXJzaW9uIjoiMSJ9.kRXSm0294c7BUOx65O00mz-l2z_52tKfWeC80BcdD6c7ZZc5YhdJNHftfJcUWyLhSTL7AbQgPonNXGcOfa4W6fzqBdGfNdx9EQjtGrRIW-ZNb9J998Bv7iuGY7q3ki1-f80gydjpghMO5kA7h8flVrX5YdN7_KlmM5-BVgpSg4xNuIBBQdd1dxMPxd68bFzWnTzc7llMAKJkHy3OvRxsAvsDgj7-1viFQhz_ripKBOPW00a85YNcB4IIRt3BYzzNJgUkTcGcX3avQPKgV89cGX81GdJnMmJAMHOsEQGFRzvp3ZFU7QYE8oyW9snLNU4y1-9df3ML9Gt-GscD0Oizlw.Mu-j1dBa6cNGzMEeLXBgVg.qH2g_o6gOnoi-Vhshff9lcxGbfcTMKpo4cBbd9L_z-yI9xIW7Tq0PiYMyzZg62f5HMp1oHfu7RGNkqw5dUjVCDAXjnKhfB2w_GdiQ9XY9Sr5MJpmtk3jsE52G6Oy6-S-t_4w91cHBzrhlmvve1s20VG86JG-Tbb9asLewio5_KRGsHKePgpO83-P1ASIDMJyHRdrV6LtjXjKZh4KdS-4dyUMO1NvjOsYL6q-yEQ8fl9p6Mksqs_kQrPWlqoFe6GfSB1hkr2ish53n0cM7tSP3beSHbJHNVZKvx2bRjXoqYrJf0KEIalZO1f3cWbz0A97gYdT7Z0RfrzKV-46xGC2qoZoyPGrZOhsUaD6f6VLa9D9IfZMXZU-DLBi_QKAWaG2GNfiz8x9CgELVh8FDexdd4SHuQ8LfHXrkFZqt5B1gqJLUwwShUt6b13nWgL3GLvW9omwfzAcNW_P3rWuZ0iDdwq5r0AnLXGnNt-CbFeBeUaRJOy798-fnVO6Dl61A04ZfWfrCHWWxN2zVlDoG9rsouN56f8VVs-Oj-LYvqZFB_8PujVVB9fQ1-IGEG6UJaJquzB0sSr9hShT_axFJKmRsw.upT3UEy9WQge8PGDeWQ_mk05et258D2YmESyE0E4ew4","brand":"visa"},"browserInfo":{"acceptHeader":"*/*","colorDepth":24,"language":"en-US","javaEnabled":false,"screenHeight":768,"screenWidth":1366,"userAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0","timeZoneOffset":0},"origin":"https://tractive.com","clientStateDataIndicator":true}',
            },
        },
        'cartId': 'icPDgjACAAq6dBwxHJvF3TUHzpa3Geys',
    }

    response = session.post(
        'https://tractive.com/us_en/rest/us_en/V1/guest-carts/icPDgjACAAq6dBwxHJvF3TUHzpa3Geys/payment-information',
        headers=headers,
        json=json_data,
    ).text
    
    print(response)

run = main()