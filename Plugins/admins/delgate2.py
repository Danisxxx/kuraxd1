import re
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from Plugins.Func import connect_to_db
import os

@Client.on_message(filters.command(["delgate2"], prefixes=['.', '/', '!', '?'], case_sensitive=False))
def delete_gateway_from_database(client, message):
    conn = connect_to_db()
    cursor = conn.cursor()
    user_id = message.from_user.id
    username = message.from_user.username
    cursor.execute('SELECT rango FROM users WHERE user_id = ?', (user_id,))
    user_rank = cursor.fetchone()
    
    if user_rank and (user_rank[0] == 'Owner' or user_rank[0] == 'Seller'):
        # Extrae los argumentos del comando
        args = message.text.split()[1:]
        if len(args) == 1:
            comando = args[0]
            
            # Eliminar la gateway de la base de datos
            cursor.execute('DELETE FROM gateways2 WHERE comando = ?', (comando,))
            conn.commit()
            
            # Eliminar la línea correspondiente del archivo command_status.txt
            with open("command_status.txt", "r") as file:
                lines = file.readlines()
            with open("command_status.txt", "w") as file:
                for line in lines:
                    if not line.startswith(comando):
                        file.write(line)
            
            # Envía un mensaje de confirmación
            client.send_message(message.chat.id, f"Gateway '{comando}' eliminada correctamente.")
        else:
            client.send_message(message.chat.id, "Formato incorrecto. Uso: /delgate <comando>")
    else:
        message.reply("Access denied. ❌ <a href='https://imgur.com/ihpUqrG.jpg'>&#8203;</a>")
