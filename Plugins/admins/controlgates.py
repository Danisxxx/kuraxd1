from pyrogram import filters, Client
from Plugins.Func import connect_to_db

footer_banner1 = 'https://imgur.com/ihpUqrG.jpg'

COMMAND_STATUS_FILE = "command_status.txt"

def is_command_enabled(command_name):
    with open(COMMAND_STATUS_FILE, "r") as f:
        command_status = f.read().splitlines()
    for line in command_status:
        name, status = line.split(":")
        if name == command_name:
            return status == "on"
    return False

def update_command_status(command_name, status):
    with open(COMMAND_STATUS_FILE, "r") as f:
        command_status = f.read().splitlines()
    updated_status = []
    found = False
    for line in command_status:
        name, _ = line.split(":")
        if name == command_name:
            updated_status.append(f"{name}:{status}")
            found = True
        else:
            updated_status.append(line)
    if not found:
        updated_status.append(f"{command_name}:{status}")
    with open(COMMAND_STATUS_FILE, "w") as f:
        f.write("\n".join(updated_status))

@Client.on_message(filters.command('addcommand', prefixes=['.', '/', '!', '?'], case_sensitive=False) & filters.text)
def agregar_comando(_, message):
    # Verificar si el usuario que envió el comando es el propietario del bot
    if message.from_user.id != 6200131196:
        return message.reply(f"<i>Solo el propietario del bot puede utilizar este comando.</i> <a href='{footer_banner1}'>&#8203;</a>")
    try:
        # Obtener el nombre del comando a agregar
        nombre_comando = message.text.split()[1]
    except KeyError:
        return message.reply(f"<i>Indica el comando que deseas agregar.</i> <a href='{footer_banner1}'>&#8203;</a>")

    # Agregar el comando con estado "on" al archivo
    update_command_status(nombre_comando, "on")

    message.reply(f"<i>Comando '{nombre_comando}' agregado.</i>")


@Client.on_message(filters.command('comd', prefixes=['.', '/', '!', '?'], case_sensitive=False) & filters.text)
def alternar_comando(_, message):
    
    conn = connect_to_db()
    cursor = conn.cursor()
    user_id = message.from_user.id
    username = message.from_user.username  
    
    cursor.execute('SELECT rango, creditos, antispam, dias FROM users WHERE user_id = ?', (user_id,))
    user_data = cursor.fetchone()
    # Verificar si el usuario que envió el comando es el propietario del bot
    if all(role not in user_data[0] for role in ["Owner"]):
         
        return message.reply("Access denied. ❌ <a href='https://imgur.com/ihpUqrG.jpg'>&#8203;</a> ")

    try:
        # Obtener el nombre del comando para apagarlo o encenderlo
        nombre_comando = message.text.split()[1]
    except KeyError:
        return message.reply(f"<i>Indica el comando que deseas desactivar o activar.</i> <a href='{footer_banner1}'>&#8203;</a>")

    # Verificar el estado actual del comando
    if is_command_enabled(nombre_comando):
        # Si está encendido, apagarlo
        update_command_status(nombre_comando, "off")
        message.reply(f"<i>Comando '{nombre_comando}' desactivado.</i> <a href='{footer_banner1}'>&#8203;</a>")
    else:
        # Si está apagado, encenderlo
        update_command_status(nombre_comando, "on")
        message.reply(f"<i>Comando '{nombre_comando}' activado.</i> <a href='{footer_banner1}'>&#8203;</a>") 