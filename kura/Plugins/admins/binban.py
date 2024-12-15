from Plugins.Func import connect_to_db
import requests
import datetime
from pyrogram import Client, filters
from pyrogram.types import Message
import os
from os.path import isfile







@Client.on_message(filters.command(["binban"], prefixes=['.','/','!','?'], case_sensitive=False) & filters.text)
def bin_banned_command(_, message: Message):
    conn = connect_to_db()
    cursor = conn.cursor()
    user_id = message.from_user.id
    username = message.from_user.username  
    footer_banner = 'https://imgur.com/llb5G2P.jpg'
    
    cursor.execute('SELECT rango, creditos, antispam, dias FROM users WHERE user_id = ?', (user_id,))
    user_data = cursor.fetchone()
    
           
    if all(role not in user_data[0] for role in ["Seller", "Owner"]):
            return message.reply("Access denied. ❌ <a href='https://imgur.com/ihpUqrG.jpg'>&#8203;</a> ")
    
    
    
    # Obtener el texto del mensaje, excluyendo el comando /binban
    texto = message.text.split(maxsplit=1)[1]
    texto = texto[:6]
    
    # Abrir el archivo binban.txt en modo de escritura (append)
    with open('binban.txt', 'a') as file:
        file.write(texto + '\n')
    
    # Responder al usuario que se agregó exitosamente el BIN
    message.reply(f"Se agregó correctamente el BIN {texto} a la lista de baneados. <a href='https://imgur.com/ihpUqrG.jpg'>&#8203;</a>")
   