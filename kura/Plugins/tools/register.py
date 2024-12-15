from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from Plugins.Func import connect_to_db
import datetime


    #---------------REGISTER USER NONE---------------#    
@Client.on_message(filters.command("register", prefixes=['.','/','!','?'], case_sensitive=False) & filters.text)
def register_command(client, message):
    conn = connect_to_db()
    cursor = conn.cursor()
    username = message.from_user.username
    user_id = message.from_user.id
    cursor.execute('SELECT user_id FROM users WHERE user_id = ?', (user_id,))
    existing_user = cursor.fetchone()


    if existing_user:
        message.reply(f"<b>You're already registered.</b> <a href='https://imgur.com/ihpUqrG.jpg'>&#8203;</a>")
    else:
        registration_time = datetime.datetime.now().timestamp()
        cursor.execute('INSERT INTO users (user_id, rango, creditos, antispam, dias, fecha_registro) VALUES (?, ?, ?, ?, ?, ?)', (user_id, 'Free', 0, 60, 0, registration_time))
        conn.commit()
        message.reply(f"<b>Full registration.</b> <a href='https://imgur.com/ihpUqrG.jpg'>&#8203;</a>")

        seller_chat_id = 6849316239 # Replace with the ID of the chat where you want to send the message
        client.send_message(seller_chat_id, f"<b>Nuevo Usuario Registrado {user_id} {username}</b>")