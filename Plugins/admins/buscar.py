from asyncio import sleep
from pyrogram import Client, filters
import datetime

from Plugins.Func import connect_to_db

def buscar_info_usuario(user_id):
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute('SELECT rango, creditos, antispam, dias FROM users WHERE user_id = ?', (user_id,))
    user_info = cursor.fetchone()
    conn.close()
    return user_info


@Client.on_message(filters.command(["buscar"], ["/", "."]))
def buscar(client, message):
        conn = connect_to_db()
        cursor = conn.cursor()
        user_id2 = message.from_user.id
        cursor.execute('SELECT rango, creditos, antispam, dias FROM users WHERE user_id = ?', (user_id2,))
        user_data = cursor.fetchone()
    
        if all(role not in user_data[0] for role in ["Seller", "Owner"]):
            return message.reply(f"<b>Access Denied.❌</b> <a href='https://imgur.com/ihpUqrG.jpg'>&#8203;</a>")
        
        
        # Conectar a la base de datos SQLite
        user_id = message.text.split(" ")[1]
        user = client.get_users(user_id)
        if user:
            username = user.username
        user_info = buscar_info_usuario(user_id)
        if user_info:
            rango, creditos, antispam, dias = user_info
            footer_banner1 = 'https://imgur.com/llb5G2P.jpg'
            
            respuesta = f"""<a href='{footer_banner1}'>&#8203;</a>[<a href="https://t.me/RefeDarwinScrapper">✯</a>] 𝑲𝒖𝒓𝒂𝒎𝒂 𝑪𝒉𝒌
[<a href="https://t.me/RefeDarwinScrapper">✯</a>] User ID ↯ {user_id} 
[<a href="https://t.me/RefeDarwinScrapper">✯</a>] Info User ↯ @{username} 
━━━━━━━━━━━━━━━━
[<a href="https://t.me/RefeDarwinScrapper">✯</a>] Rango ↯ <code>{rango}</code>
[<a href="https://t.me/RefeDarwinScrapper">✯</a>] Días de acceso ↯ <code>{dias}</code>
[<a href="https://t.me/RefeDarwinScrapper">✯</a>] Créditos ↯ <code>{creditos}</code>
━━━━━━━━━━━━━━━━"""
            message.reply(respuesta)
        else:
            message.reply("Usuario no encontrado en la base de datos.")