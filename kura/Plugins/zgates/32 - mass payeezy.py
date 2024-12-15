import requests
from Plugins.SegundoPlano.antispam import *
import check_template
import names
import re
import time
import random
from func_bin import get_bin_info
from Plugins.Func import connect_to_db
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
#-------------------------------#
import payeezymax


proxiess = "proxys.txt"

keyboard = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton("Premium for only $3", url="https://t.me/RefeDarwinScrapper/9175")]
    ]
)


COMMAND_STATUS_FILE = "command_status.txt"

def is_command_enabled(command_name):
    with open(COMMAND_STATUS_FILE, "r") as f:
        command_status = f.read().splitlines()
    for line in command_status:
        name, status = line.split(":")
        if name == command_name:
            return status == "on"
    return False


name_gate = "Massive"
subtype = "Payeezy"
command = "pymass"

@Client.on_message(filters.command([f"{command}"], prefixes=['.', '/', '!', '?'], case_sensitive=False) & filters.text)
def braintree3(client, message, command=command):
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
        
    # Obtener créditos actuales del usuario
    select_query = "SELECT creditos FROM users WHERE user_id = ?"
    cursor.execute(select_query, (user_id,))
    current_credits = cursor.fetchone()[0]
        
  
    ccs = message.text[len(f"/{command} "):].split("\n")      
                  
      
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
        
    x = get_bin_info(ccs[0][:6])
    
    #---------- PLANTILLA DE CARGA #1 ------------#
    loading_message = message.reply(f"""<b>
[<a href="https://t.me/RefeDarwinScrapper">✯</a>] 𝑲𝒖𝒓𝒂𝒎𝒂 𝑪𝒉𝒌
[<a href="https://t.me/RefeDarwinScrapper">✯</a>] Gateway ↯ <code>{name_gate} {subtype}</code>   
━━━━━━━━━━━━━━━━
[<a href="https://t.me/RefeDarwinScrapper">✯</a>] CC ↯ <code>{ccs[0]}</code>
[<a href="https://t.me/RefeDarwinScrapper">✯</a>] Status ↯ <b>Loading...</b> 
━━━━━━━━━━━━━━━━
[<a href="https://t.me/RefeDarwinScrapper">✯</a>] Bin ↯ <code>{x.get("type")}</code> | <code>{x.get("level")}</code> | <code>{x.get("vendor")}</code>
[<a href="https://t.me/RefeDarwinScrapper">✯</a>] Country ↯ <code>{x.get("country")} {x.get("flag")}</code>
[<a href="https://t.me/RefeDarwinScrapper">✯</a>] Bank ↯ <code>{x.get("bank_name")}</code>
━━━━━━━━━━━━━━━━  </b>""", reply_markup=keyboard, disable_web_page_preview=True)
    
    resultados = []
    for ccs1 in ccs:
        expl = re.findall(r'\d+', ccs1)
        cc = expl[0]
        mes = expl[1]
        ano = expl[2]
        cvv = expl[3]      
        tarjeta = f"{cc}|{mes}|{ano}|{cvv}"        
        bin_number = cc[:6]  
 
        inicio = time.time()
        
        gates = ['payeezy']
        gate = random.choice(gates)

        if "payeezy" in gate:
            gateway2 = "Payeezy Auth"
            msg, respuesta = payeezymax.payeezy(tarjeta)
            
      
        proxyy = "LIVE 🟩"
        gateway = f'<code>{name_gate} {subtype}</code>'
        end = time.time()
        tiempo = str(inicio - end)[1:5]
        
        respuestas = f"""[<a href="https://t.me/RefeDarwinScrapper">✯</a>] <code>{tarjeta}</code>
[<a href="https://t.me/RefeDarwinScrapper">✯</a>] Status ↯ {msg}
[<a href="https://t.me/RefeDarwinScrapper">✯</a>] Response ↯ {respuesta}
[<a href="https://t.me/RefeDarwinScrapper">✯</a>] Gateway ↯ {gateway2}
[<a href="https://t.me/RefeDarwinScrapper">✯</a>] Time ↯ <code>{tiempo} (segundos)</code>
━ • ━━━━━━━━━━━━ • ━"""  
    
        if "APPROVED" in msg:
            chat_id = -1002000802973
        
            client.send_message(chat_id, f"""<b>
[<a href="https://t.me/RefeDarwinScrapper">✯</a>] 𝑲𝒖𝒓𝒂𝒎𝒂 𝑪𝒉𝒌
[<a href="https://t.me/RefeDarwinScrapper">✯</a>] Gateway ↯ <code>{gateway}</code>   
━━━━━━━━━━━━━━━━
[<a href="https://t.me/RefeDarwinScrapper">✯</a>] CC ↯ <code>{tarjeta}</code>
[<a href="https://t.me/RefeDarwinScrapper">✯</a>] Status ↯ <b>{msg}</b> 
[<a href="https://t.me/RefeDarwinScrapper">✯</a>] Result ↯ {respuesta}
━━━━━━━━━━━━━━━━
[<a href="https://t.me/RefeDarwinScrapper">✯</a>] Bin ↯ <code>{x.get("type")}</code> | <code>{x.get("level")}</code> | <code>{x.get("vendor")}</code>
[<a href="https://t.me/RefeDarwinScrapper">✯</a>] Country ↯ <code>{x.get("country")} {x.get("flag")}</code>
[<a href="https://t.me/RefeDarwinScrapper">✯</a>] Bank ↯ <code>{x.get("bank_name")}</code>
━━━━━━━━━━━━━━━━
[<a href="https://t.me/RefeDarwinScrapper">✯</a>] Proxy  ↯ <code>{proxyy}</code>
[<a href="https://t.me/RefeDarwinScrapper">✯</a>] Time taken ↯ <code>{tiempo} (segundos)</code>
[<a href="https://t.me/RefeDarwinScrapper">✯</a>] Checked by ↯ @{username} [{user_data[0]}]
[<a href="https://t.me/RefeDarwinScrapper">✯</a>] Bot by ↯ @Crypto_locker5 </b>""")
            
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
                
   
        resultados.append(f"{respuestas}")
        mensaje_final = "\n".join(resultados)
        
            

        final = loading_message.edit_text(f"""<a href='https://imgur.com/ihpUqrG.jpg'>&#8203;</a>━ •  𝗖𝗔𝗥𝗗 𝗜𝗡𝗙𝗢  • ━ 
{mensaje_final}
[<a href="https://t.me/RefeDarwinScrapper">✯</a>] Country ↯ <code>{x.get("country")} {x.get("flag")}</code>
[<a href="https://t.me/RefeDarwinScrapper">✯</a>] Type ↯ <code>{x.get("type")}</code>
[<a href="https://t.me/RefeDarwinScrapper">✯</a>] Level ↯ <code>{x.get("level")}</code>
[<a href="https://t.me/RefeDarwinScrapper">✯</a>] Vendor ↯ <code>{x.get("vendor")}</code>
[<a href="https://t.me/RefeDarwinScrapper">✯</a>] Bank ↯ <code>{x.get("bank_name")}</code>   
━ • ━━━━━━━━━━━━ • ━  
[<a href="https://t.me/RefeDarwinScrapper">✯</a>] Credits: {current_credits}  
[<a href="https://t.me/RefeDarwinScrapper">✯</a>] Requests By: @{username} [{user_data[0]}]
[<a href="https://t.me/RefeDarwinScrapper">✯</a>] Owner Bot: @Crypto_locker5""", reply_markup=keyboard)     
        
        if "APPROVED" in msg:
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