from pyrogram import Client, filters
from Plugins.Func import connect_to_db
# Connect to the SQLite database


# Errores
def error_message(message, text):
    return message.reply(text)

@Client.on_message(filters.command("addcr", prefixes=['.','/','!','?'], case_sensitive=False) & filters.text)
def creditosusuarios(client, message):
    conn = connect_to_db()
    cursor = conn.cursor()
    
    
    datos = message.text.split(" ", 2)
        # Verificar que el usuario tenga permisos para usar el comando
    admin = cursor.execute('SELECT rango FROM users WHERE user_id = ?', (message.from_user.id,)).fetchone()
    if not admin or admin[0] not in ["Owner","Seller"]:
        return
    if len(datos) < 3:
        error_message(message, f"<b>Debes especificar el ID del usuario los creditos para el usuaurio.</b>")
        return
    user_id_set = datos[1].strip()
    creditos = datos[2].strip()
    if not user_id_set.isdigit():
        error_message(message, f"<b>El ID del usuario debe ser un número</b>")
        return
    if not creditos:
        error_message(message, "<b>Debes especificar los creditos para el usuario</b>")
        return
    
    admin = cursor.execute("SELECT rango FROM users WHERE user_id = ?", (message.from_user.id,)).fetchone()
    if not admin:
        message.reply(f"<b>No tienes permisos para usar este comando</b>")
        return
    elif admin[0] == "Seller":
        user_id_set = message.command[1]
        # Si es un seller solo puede quitar rango Banned y Premium, o agregarse a sí mismo
        if user_id_set == str(message.from_user.id):
            user = cursor.execute("SELECT rango FROM users WHERE user_id = ?", (int(user_id_set),)).fetchone()
            if user[0] != "Seller":
                message.reply(f"<b>Solo puedes ponerte créditos a ti mismo o a usuarios Free Users y Premium</b>")
                return
        else:
            user = cursor.execute("SELECT rango FROM users WHERE user_id = ?", (int(user_id_set),)).fetchone()
            if user[0] not in ["Free User", "Premium"]:
                message.reply(f"<b>No Puedes ponerle creditos a otro Seller O al creador.</b>")
                return
    elif admin[0] != "Owner":
        message.reply(f"<b>No tienes permisos para usar este comando</b>")
        return
    
    # Buscar al usuario y actualizar su rango
    user = cursor.execute("SELECT * FROM users WHERE user_id = ?", (int(user_id_set),)).fetchone()
    if not user:
        error_message(message, "<b>El usuario no existe.</b>")
        return
    cursor.execute("UPDATE users SET creditos = ? WHERE user_id = ?", (creditos, int(user_id_set)))
    conn.commit()
    if cursor.rowcount > 0:
        message.reply(f"<b>Los Creditos de <code>{user_id_set}</code> ha sido actualizado ha</b>  <code>{creditos}</code>")
    else:
        error_message(message, f"<b>No se pudo actualizar el antispam de usuario {user_id_set}</b>")
    
    if admin[0] == "Seller":
        seller_chat_id = 6712112939 # Replace with the ID of the chat where you want to send the message
        seller_name = message.from_user.first_name        
        client.send_message(seller_chat_id, f"<b>El Seller <code>{seller_name}</code> Agrego Creditos A {user_id_set}</b>")

@Client.on_message(filters.command("removecr", prefixes=['.','/','!','?'], case_sensitive=False) & filters.text)
def quitar_creditos(client, message):
    conn = connect_to_db()
    cursor = conn.cursor()

    datos = message.text.split(" ", 2)

    # Verificar que el usuario tenga permisos para usar el comando
    admin = cursor.execute('SELECT rango FROM users WHERE user_id = ?', (message.from_user.id,)).fetchone()
    if not admin or admin[0] not in ["Owner", "Seller"]:
        message.reply("Access denied. ❌ <a href='https://imgur.com/ihpUqrG.jpg'>&#8203;</a> ")
        return

    if len(datos) < 2:
        error_message(message, f"<b>Debes especificar el ID del usuario al que deseas quitar los créditos.</b>")
        return

    user_id_set = datos[1].strip()

    if not user_id_set.isdigit():
        error_message(message, f"<b>El ID del usuario debe ser un número.</b>")
        return

    # Verificar si el usuario es un vendedor y solo puede quitar créditos a ciertos rangos
    if admin[0] == "Seller":
        user_id_set = message.command[1]
        # Si es un seller, solo puede quitar créditos a usuarios Free Users y Premium o a sí mismo
        if user_id_set != str(message.from_user.id):
            user = cursor.execute("SELECT rango FROM users WHERE user_id = ?", (int(user_id_set),)).fetchone()
            if user[0] not in ["Free User", "Premium"]:
                message.reply(f"<b>No puedes quitar créditos a otro Seller o al creador.</b>")
                return

    # Buscar al usuario y actualizar sus créditos
    user = cursor.execute("SELECT * FROM users WHERE user_id = ?", (int(user_id_set),)).fetchone()
    if not user:
        error_message(message, "<b>El usuario no existe.</b>")
        return

    cursor.execute("UPDATE users SET creditos = 0 WHERE user_id = ?", (int(user_id_set),))
    conn.commit()

    if cursor.rowcount > 0:
        message.reply(f"<b>Los créditos de <code>{user_id_set}</code> han sido reseteados a 0.</b>")
    else:
        error_message(message, f"<b>No se pudo resetear los créditos del usuario {user_id_set}.</b>")

    if admin[0] == "Seller":
        seller_chat_id = 6849316239  # Reemplaza con el ID del chat donde deseas enviar el mensaje
        seller_name = message.from_user.first_name
        client.send_message(seller_chat_id, f"<b>El Seller <code>{seller_name}</code> Quitó los créditos de {user_id_set}.</b>")

    