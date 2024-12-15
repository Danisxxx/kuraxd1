from Plugins.Func import connect_to_db
from pyrogram import Client, filters


    
    
@Client.on_message(filters.command("ban", prefixes=['.','/','!','?'], case_sensitive=False) & filters.text)
def ban_user(client, message):
    # Connect to the SQLite database
    conn = connect_to_db()
    cursor = conn.cursor()
    que = message.from_user.id
            # Verificar que el usuario tenga permisos para usar el comando
    admin = cursor.execute('SELECT rango FROM users WHERE user_id = ?', (que,)).fetchone()
    if not admin or admin[0] not in ["Owner"]:
        return message.reply("Access denied. ❌ <a href='https://imgur.com/ihpUqrG.jpg'>&#8203;</a> ")
    
    datos = message.text.split(" ", 1)
    
    if len(datos) < 2 and message.reply_to_message:
        # Si no se proporciona un ID, pero se responde a un mensaje, obtener el ID del usuario al que se responde
        user_id = message.reply_to_message.from_user.id
    elif len(datos) < 2:
        message.reply(f"<b>Debes especificar el ID del usuario a banear o responder a su mensaje</b>")
        return
    else:
        user_id = datos[1].strip()
        if not user_id.isdigit():
            message.reply(f"<b>El ID del usuario debe ser un número</b>")
            return
    
    # Verificar si el usuario tiene los permisos necesarios
    admin = cursor.execute("SELECT rango FROM users WHERE user_id = ?", (message.from_user.id,)).fetchone()
    
    # Verificar si el usuario intenta banearse a si mismo
    if int(user_id) == message.from_user.id:
        message.reply(f"<b>No puedes banearte a ti mismo</b>")
        return
    
    # Buscar al usuario y actualizar sus datos
    user = cursor.execute("SELECT * FROM users WHERE user_id = ?", (int(user_id),)).fetchone()
    if not user:
        message.reply(f"<b>El usuario no existe</b>")
        return
    
    if admin[0] == "Seller":
        user_rank = cursor.execute("SELECT rango FROM users WHERE user_id = ?", (int(user_id),)).fetchone()[0]
        if user_rank not in ["Free User", "Premium"]:
            message.reply(f"<b>Solo puedes banear usuarios con el rango Free User o Premium </b>")
            return

    elif admin[0] not in "Owner":
     message.reply(f"<b>No tienes permisos para banear usuarios</b>")
     return

    
    # Banear al usuario y actualizar sus créditos
    cursor.execute("UPDATE users SET rango = 'Baneado', antispam = '150', creditos = '0', dias = '0' WHERE user_id = ?", (int(user_id),))
    conn.commit()
    message.reply(f"<b>El usuario con ID <code>{user_id}</code> ha sido baneado</b>")
    if admin[0] == "Seller":
         seller_chat_id = 6200131196 # Replace with the ID of the chat where you want to send the message
         seller_name = message.from_user.first_name        
         client.send_message(seller_chat_id, f"<b>El seller {seller_name} </b>\n ha baneado al usuario <code>{user_id}</code>")




@Client.on_message(filters.command("unban", prefixes=['.','/','!','?'], case_sensitive=False) & filters.text)
def unban_user(client, message):
    # Connect to the SQLite database
    conn = connect_to_db()
    cursor = conn.cursor()
    que = message.from_user.id
            # Verificar que el usuario tenga permisos para usar el comando
    admin = cursor.execute('SELECT rango FROM users WHERE user_id = ?', (que,)).fetchone()
    if not admin or admin[0] not in ["Owner"]:
        return message.reply("Access denied. ❌ <a href='https://imgur.com/ihpUqrG.jpg'>&#8203;</a> ")
    
    
    datos = message.text.split(" ", 1)
    
    if len(datos) < 2 and message.reply_to_message:
        # Si no se proporciona un ID, pero se responde a un mensaje, obtener el ID del usuario al que se responde
        user_id = message.reply_to_message.from_user.id
    elif len(datos) < 2:
        message.reply(f"<b>Debes especificar el ID del usuario a desbanear o responder a su mensaje</b>")
        return
    else:
        user_id = datos[1].strip()
        if not user_id.isdigit():
            message.reply(f"<b>El ID del usuario debe ser un número</b>")
            return
    
    # Verificar si el usuario tiene los permisos necesarios
    admin = cursor.execute("SELECT rango FROM users WHERE user_id = ?", (message.from_user.id,)).fetchone()
    
    # Verificar si el usuario intenta banearse a si mismo
    if int(user_id) == message.from_user.id:
        message.reply(f"<b>No puedes desbanearte a ti mismo</b>")
        return
    
    # Buscar al usuario y actualizar sus datos
    user = cursor.execute("SELECT * FROM users WHERE user_id = ?", (int(user_id),)).fetchone()
    if not user:
        message.reply(f"<b>El usuario no existe</b>")
        return
    
    if admin[0] == "Seller":
        user_rank = cursor.execute("SELECT rango FROM users WHERE user_id = ?", (int(user_id),)).fetchone()[0]
        if user_rank not in ["Free User", "Premium"]:
            message.reply(f"<b>Solo puedes desbanear usuarios con el rango Free User o Premium </b>")
            return

    elif admin[0] not in "Owner":
     message.reply(f"<b>No tienes permisos para desbanear usuarios</b>")
     return

    
    # Banear al usuario y actualizar sus créditos
    cursor.execute("UPDATE users SET rango = 'Free', antispam = '150', creditos = '0', dias = '0' WHERE user_id = ?", (int(user_id),))
    conn.commit()
    message.reply(f"<b>El usuario con ID <code>{user_id}</code> ha sido desbaneado</b>")
    if admin[0] == "Seller":
         seller_chat_id = 6200131196 # Replace with the ID of the chat where you want to send the message
         seller_name = message.from_user.first_name        
         client.send_message(seller_chat_id, f"<b>El seller {seller_name} </b>\n ha desbaneado al usuario <code>{user_id}</code>")





