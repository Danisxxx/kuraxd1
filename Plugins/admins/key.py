from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from Plugins.Func import connect_to_db
import datetime
import random


def generate_key(length):
    key = f"KuramaChk-{random.randint(10000000, 99999999)}-PREMIUM"
    return key


@Client.on_message(filters.command("genkey", prefixes=['.', '/', '!', '?'], case_sensitive=False) & filters.text)
def generatekey(client, message):
    try:   
        conn = connect_to_db()
        cursor = conn.cursor()
        
        user_id = message.from_user.id
        cursor.execute('SELECT rango FROM users WHERE user_id = ?', (user_id,))
        result = cursor.fetchone()
        
        if all(role not in result[0] for role in ["Seller", "Owner"]):
            message.reply(f"<b>El chat no está autorizado para usar este comando. </b>")
            return
  
        days = int(message.command[1])
        
  
        key = generate_key(16)
  
        generate_by = message.from_user.id

        cursor.execute("INSERT INTO keys (key, status, user_claim, days, generate_by) VALUES (?, ?, ?, ?, ?)",
            (key, "LIVE", None, days, generate_by))
        conn.commit()
        
        username = message.from_user.username
        
        message.reply(f"""
[<a href="https://t.me/RefeDarwinScrapper">✯</a>] KEY GENERATE SUCCESS✳️
━━━━━━━━━━━━ 
[<a href="https://t.me/RefeDarwinScrapper">✯</a>] KEY: <code>{key}</code>
[<a href="https://t.me/RefeDarwinScrapper">✯</a>] TYPE: <code>Premium</code>
[<a href="https://t.me/RefeDarwinScrapper">✯</a>] DAYS: <code>{days}</code>
[<a href="https://t.me/RefeDarwinScrapper">✯</a>] GENERATE BY: @{username} 
━━━━━━━━━━━━  """, disable_web_page_preview=True)  
        
    except Exception as e:
        message.reply("Error al generar la clave.")
        print(e)
        
        
    admin_first_name = message.from_user.first_name
    admin_last_name = message.from_user.last_name
    admin_name = f"{admin_first_name} {admin_last_name}"
        
    message_text = f"🔑 El administrador {admin_name} - @{username} ha generado una clave con {days} días:\n\n<code>{key}</code> 🔑"
 
  
    client.send_message("6849316239", message_text)
        
        
@Client.on_message(filters.command("claim", prefixes=['.', '/', '!', '?'], case_sensitive=False) & filters.text)
def claimkey(client, message):
    conn = connect_to_db()
    user_id = message.from_user.id
    cursor = conn.cursor()

    cursor.execute('SELECT rango FROM users WHERE user_id = ?', (user_id,))
    result = cursor.fetchone()
    username = message.from_user.username

    if not result:
        return message.reply(f"<b>You're not registered. Please use /register to register.</b>")
  
    

    # Verifica si el usuario ya es Premium
    cursor.execute('SELECT rango FROM users WHERE user_id = ?', (user_id,))
    result = cursor.fetchone()
    
    datos = message.text.split(" ")
    
    if len(datos) < 2:
        message.reply(f"<b>Key incorrect.")
        return
    
    
    key = datos[1].strip()
    

    
    if result[0] in ["Baneado", "baneado"]:
             return message.reply(f"<b>You're not allowed to use the bot❌\nReason: Baned.")
            
 
    if result and "Premium" in result[0]:
            message.reply(f"You are already a Premium user. This key is not redeemable for you.")
            return


    if result and ("Owner" in result[0] or "Seller" in result[0]):
            message.reply(f"You're part of the staff, you can't redeem Keys.")
            return
        
    cursor.execute('SELECT status FROM keys WHERE key = ?', (key,))    
    key_status = cursor.fetchone()
    print(key_status)
    if not key_status:
        message.reply(f"The key doesn't exist.")
        return
    elif key_status[0] != 'LIVE':
        message.reply(f"<b>The key has already been redeemed.</b>")
        return
  
    cursor.execute('SELECT days FROM keys WHERE key = ?', (key,))
    days = cursor.fetchone()[0]
    
    current_time = datetime.datetime.now().timestamp()
    
    cursor.execute('UPDATE users SET rango = ?, creditos = ?, antispam = ?, dias = ?, fecha_registro = ? WHERE user_id = ?',
                    ('Premium', 0, 15, days, current_time, user_id))
    conn.commit()


    cursor.execute('UPDATE keys SET status = ?, user_claim = ?, days = ? WHERE key = ?',
        ('DEAD', user_id, days, key))
    conn.commit()
        
        
    username = message.from_user.username
    
    message.reply(f"""
[<a href="https://t.me/RefeDarwinScrapper">✯</a>] CLAIM SUCCESS✳️
━━━━━━━━━━━━ 
[<a href="https://t.me/RefeDarwinScrapper">✯</a>] KEY: <code>{key}</code>
[<a href="https://t.me/RefeDarwinScrapper">✯</a>] TYPE: <code>Premium</code>
[<a href="https://t.me/RefeDarwinScrapper">✯</a>] DAYS: <code>{days}</code>
[<a href="https://t.me/RefeDarwinScrapper">✯</a>] STATUS: @{username} <code>[Premium]</code>
━━━━━━━━━━━━ """, disable_web_page_preview=True)  
        
    admin_first_name = message.from_user.first_name
    admin_last_name = message.from_user.last_name
    admin_name = f"{admin_first_name} {admin_last_name}"
    username = message.from_user.username

    message_text = f"🔑 El usuario {admin_name} - @{username} ha canjeado una clave con éxito:\n\n<code>{key}</code> 🔑"
 
  
    client.send_message("6849316239", message_text)
 