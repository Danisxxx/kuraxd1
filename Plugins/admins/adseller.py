from pyrogram import Client, filters

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from Plugins.Func import connect_to_db
import datetime
import pyrogram



    #---------------ADD SELLER USER---------------#    
@Client.on_message(filters.command("admin", prefixes=['.','/','!','?'], case_sensitive=False) & filters.text)
def add_premium_to_database(client, message):
    conn = connect_to_db()
    cursor = conn.cursor()
    user_id = message.from_user.id
    username = message.from_user.username
    cursor.execute('SELECT rango FROM users WHERE user_id = ?', (user_id,))
    user_rank = cursor.fetchone()
    
    if user_rank and (user_rank[0] == 'Owner'):
        try:
            _, group_id = message.text.split(" ")
            target_chat_id = int(group_id)
        except ValueError:
            message.reply("Formato de comando incorrecto. Uso: /admin [user_id]")
            return
        
        
        cursor.execute('SELECT user_id FROM users WHERE user_id = ?', (target_chat_id,))
        existing_group = cursor.fetchone()
        
        if existing_group:
            cursor.execute('DELETE FROM users WHERE user_id = ?', (target_chat_id,))
            conn.commit()

    
        expiration_date = datetime.datetime.now()

 
        cursor.execute('INSERT INTO users (user_id, rango, dias, fecha_registro) VALUES (?, ?, ?, ?)',
                    (target_chat_id, 'Seller', 999999, expiration_date.timestamp()))
        conn.commit()

        message.reply(f"Usuario promovido a seller.")
        
        
    
        
    else:
        message.reply("Access denied. ❌ <a href='https://imgur.com/ihpUqrG.jpg'>&#8203;</a> ")

          




#---------------REMOVE PREMIUM USER---------------#    
@Client.on_message(filters.command("deldb", prefixes=['.', '/', '!', '?'], case_sensitive=False) & filters.text)
def removepremium_command(client, message):
    conn = connect_to_db()
    cursor = conn.cursor()
    user_id = message.from_user.id
    cursor.execute('SELECT rango FROM users WHERE user_id = ?', (user_id,))
    result = cursor.fetchone()[0]
    
    if "Owner" not in result and "Seller" not in result:
        message.reply("Access denied. ❌ <a href='https://imgur.com/ihpUqrG.jpg'>&#8203;</a> ")
        return
    
    else:
        args = message.text.split(' ')[1]
        try:
            user_id = int(args)
        except ValueError:
            message.reply(f"<b>El valor proporcionado no es un ID de usuario válido.</b>")
            return

        # Check if the user exists in the database
        cursor.execute('SELECT user_id, rango FROM users WHERE user_id = ?', (user_id,))
        user_data = cursor.fetchone()

        if user_data:
            user_id, user_role = user_data
            if "Owner" in user_role or "Seller" in user_role:
                message.reply(f"<b>El usuario es parte del personal no puedes eliminarlo.</b>")
                return
            
                # Remove the premium user from the database
            cursor.execute('DELETE FROM users WHERE user_id = ?', (user_id,))
            conn.commit()
            admin_first_name = message.from_user.first_name
            admin_last_name = message.from_user.last_name
            admin_name = f"{admin_first_name} {admin_last_name}"
            username = message.from_user.username
            message.reply(f"<b>Usuario {user_id} eliminado de la base de datos.</b>")
            message_text = f"❌ El administrador {admin_name} - @{username} eliminó al usuario Premium con ID {user_id} de la base de datos ❌"
            seller_chat_id = -1001816346504  # Reemplaza con el ID del chat donde deseas enviar el mensaje
            seller_name = message.from_user.first_name
            client.send_message(seller_chat_id, f"<b>El Seller <code>{seller_name}</code> elimino del los premium al usuario/Grupo con ID {user_id}.</b>")

            client.send_message("6200131196", message_text)
     
        else:
            message.reply(f"<b>El usuario/Grupo con ID {user_id} no existe en la base de datos.</b>")
