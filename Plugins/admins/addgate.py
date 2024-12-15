import re
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from Plugins.Func import connect_to_db

@Client.on_message(filters.command(["addgate"], prefixes=['.', '/', '!', '?'], case_sensitive=False))
def add_gateway_to_database(client, message):
    conn = connect_to_db()
    cursor = conn.cursor()
    user_id = message.from_user.id
    username = message.from_user.username
    cursor.execute('SELECT rango FROM users WHERE user_id = ?', (user_id,))
    user_rank = cursor.fetchone()
  
    
    if user_rank and (user_rank[0] == 'Owner' or user_rank[0] == 'Seller'):
        # Extrae los argumentos del comando
        args = message.text.split()[1:]
        if len(args) == 3:
            nombre = args[0]
            comando = args[1]
            pagina = args[2]

            # Inserta los datos en la base de datos
            cursor.execute('INSERT INTO gateways (nombre, comando, pagina) VALUES (?, ?, ?)', (nombre, comando, pagina))
            conn.commit()
 
            # Envía un mensaje de confirmación
            client.send_message(message.chat.id, f"Gateway '{nombre}' agregada correctamente.")
        else:
            client.send_message(message.chat.id, "Formato incorrecto. Uso: /addgate <nombre> <comando> <pagina>")
    else:
        message.reply("Access denied. ❌ <a href='https://imgur.com/ihpUqrG.jpg'>&#8203;</a>")
