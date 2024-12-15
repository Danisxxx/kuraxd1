from pyrogram import Client, filters

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from Plugins.Func import connect_to_db
import datetime
import pyrogram



@Client.on_message(filters.command("addgp", prefixes=['.', '/', '!', '?'], case_sensitive=False) & filters.text)
def add_group_to_database(client, message):
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
            group_days = int(days)
        except ValueError:
            message.reply("Formato de comando incorrecto. Uso: /addgp <group_id> <days>")
            return
        
        
        cursor.execute('SELECT user_id FROM users WHERE user_id = ?', (target_chat_id,))
        existing_group = cursor.fetchone()
        
        if existing_group:
            cursor.execute('DELETE FROM users WHERE user_id = ?', (target_chat_id,))
            conn.commit()

    
        expiration_date = datetime.datetime.now()

 
        cursor.execute('INSERT INTO users (user_id, rango, dias, fecha_registro) VALUES (?, ?, ?, ?)',
                    (target_chat_id, 'Grupo', group_days, expiration_date.timestamp()))
        conn.commit()
        

        message.reply(f"Grupo {target_chat_id} agregado a la base de datos por {group_days} días.")
        
        
        owner_chat_id = 6849316239
    
        client.send_message(owner_chat_id, f"<b>Nuevo grupo agregado con {group_days} días: {target_chat_id} por {username} ⭐</b>")
        
        
    else:
        message.reply("Access denied. ❌ <a href='https://imgur.com/ihpUqrG.jpg'>&#8203;</a> ")
    
    
    

@Client.on_message(filters.command("addstaff", prefixes=['.', '/', '!', '?'], case_sensitive=False) & filters.text)
def add_staff_to_database(client, message):
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
            group_days = int(days)
        except ValueError:
            message.reply("Formato de comando incorrecto. Uso: /addstaff <group_id> <days>")
            return

        cursor.execute('SELECT user_id FROM users WHERE user_id = ?', (target_chat_id,))
        existing_group = cursor.fetchone()
        
        
        if existing_group:
            cursor.execute('DELETE FROM users WHERE user_id = ?', (target_chat_id,))
            conn.commit()
            
    
        expiration_date = datetime.datetime.now()

 
        cursor.execute('INSERT INTO users (user_id, rango, dias, fecha_registro) VALUES (?, ?, ?, ?)',
                    (target_chat_id, 'Staff', group_days, expiration_date.timestamp()))
        conn.commit()
        
        message.reply(f"Staff {target_chat_id} agregado a la base de datos por {group_days} días.")
        
        
        owner_chat_id = 6849316239
    
        client.send_message(owner_chat_id, f"<b>Nuevo Staff agregado con {group_days} días: {target_chat_id} por {username} ⭐</b>")
        
        
    else:
        message.reply("Access denied. ❌ <a href='https://imgur.com/ihpUqrG.jpg'>&#8203;</a> ")
    
    