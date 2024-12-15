from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from Plugins.Func import connect_to_db
import datetime
import pyrogram


# Comando para agregar usuarios Premium
@Client.on_message(filters.command("premium", prefixes=['.', '/', '!', '?'], case_sensitive=False) & filters.text)
def add_premium_to_database(client, message):
    conn = connect_to_db()
    cursor = conn.cursor()
    user_id = message.from_user.id
    username = message.from_user.username
    cursor.execute('SELECT rango FROM users WHERE user_id = ?', (user_id,))
    user_rank = cursor.fetchone()
    
    
    
    if user_rank and (user_rank[0] == 'Owner' or user_rank[0] == 'Seller'):
        try:
            _, group_id, days = message.text.split(" ")
            target_chat_id = int(group_id)
            user_days = int(days)
        except ValueError:
            message.reply("Formato de comando incorrecto. Uso: /premium <group_id> <days>")
            return
        
        
        cursor.execute('SELECT user_id FROM users WHERE user_id = ?', (target_chat_id,))
        existing_group = cursor.fetchone()
        
        
        expiration_date = datetime.datetime.now()

        if existing_group:
            cursor.execute('UPDATE users SET rango = ?, dias = ?, fecha_registro = ? WHERE user_id = ?',
               ('Premium', user_days, expiration_date.timestamp(), target_chat_id))
            
            message.reply(f"Usuario {target_chat_id} agregado a la base de datos por {user_days} días.")
        
        
            owner_chat_id = 6712112939
        
            client.send_message(owner_chat_id, f"<b>Nuevo Usuario agregado con {user_days} días: {target_chat_id} por {username} ⭐</b>")
        

            conn.commit()
            return
 
        cursor.execute('INSERT INTO users (user_id, rango, dias, fecha_registro) VALUES (?, ?, ?, ?)',
                    (target_chat_id, 'Premium', user_days, expiration_date.timestamp()))
        conn.commit()

        message.reply(f"Usuario {target_chat_id} agregado a la base de datos por {user_days} días.")
        
        
        owner_chat_id = 6712112939
    
        client.send_message(owner_chat_id, f"<b>Nuevo Usuario agregado con {user_days} días: {target_chat_id} por {username} ⭐</b>")
        
        
    else:
        message.reply("Access denied. ❌ <a href='https://imgur.com/ihpUqrG.jpg'>&#8203;</a> ")