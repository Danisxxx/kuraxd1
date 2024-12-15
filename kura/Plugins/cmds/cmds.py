from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from Plugins.Func import connect_to_db
from datetime import datetime
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
import qrcode
import pyrogram
from PIL import Image, ImageDraw, ImageFont
import random
from asyncio import sleep
import re
import cv2
from func_bin import get_bin_info
from func_gen import cc_gen
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
template_dir = os.path.join(base_dir)




#----------------- Función para generar una key aleatoria ------------------#
def generate_key(days):
    if days == 99:
        days = 999999
    key = f"KURAMACHK-{random.randint(10000000, 99999999)}-PREMIUM"
    return key

def send_template_selection_keyboard(client, chat_id):
    keyboard = [
        [
            InlineKeyboardButton("7 días", callback_data="template_7"),
            InlineKeyboardButton("15 días", callback_data="template_15"),
            InlineKeyboardButton("30 días", callback_data="template_30"),
            InlineKeyboardButton("Unlimited", callback_data="template_99"),
        ],
        [
            InlineKeyboardButton("Key de regalo", callback_data="template_3"),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    client.send_message(chat_id, "Selecciona la duración de la key:", reply_markup=reply_markup)

def process_template_selection(client, message: Message, template_name, days, creditos):
    chat_id = message.chat.id
    user_id = message.from_user.id
    base_dir = os.path.dirname(os.path.abspath(__file__))
    template_dir = os.path.join(base_dir)
    random_code = generate_key(days)

    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO keys (key, status, user_claim, days, generate_by, creditos) VALUES (?, ?, ?, ?, ?, ?)',
                   (random_code, 'LIVE', "", days, chat_id, creditos))

    conn.commit()

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=1,
    )
    qr.add_data(random_code)
    qr.make(fit=True)

    qr_img = qr.make_image(fill_color="black", back_color="white")
    
 
    template_path = os.path.join(template_dir, template_name)
    template = cv2.imread(template_path)

    template = Image.open(template_path)

    x_position = template.width - qr_img.width - 300  
    y_position = template.height - qr_img.height - 55  

    template.paste(qr_img, (x_position, y_position))

    edited_image_path = os.path.join(base_dir, "edited_image.png")
    template.save(edited_image_path)

    edited_image = cv2.imread(edited_image_path)
    gray = cv2.cvtColor(edited_image, cv2.COLOR_BGR2GRAY) 
    _, thresh = cv2.threshold(gray, 1, 255, cv2.THRESH_BINARY)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    max_area = 0
    max_contour = None
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > max_area:
            max_area = area
            max_contour = contour

    x, y, w, h = cv2.boundingRect(max_contour)
    edited_image_no_border = edited_image[y:y+h, x:x+w]

    edited_image_no_border_path = os.path.join(base_dir, "edited_image_no_border.png")
    cv2.imwrite(edited_image_no_border_path, edited_image_no_border)

    client.send_photo(
        chat_id=message.chat.id,
        photo=edited_image_no_border_path
    )
    
    chat_id = message.chat.id
        
        
    chat_info = client.get_chat(chat_id)
        
        # Verifica si el chat_info contiene el username del usuario
    if hasattr(chat_info, 'username') and chat_info.username:
        username = chat_info.username
        texto = f'El username del usuario con chat_id {chat_id} es @{username}'
    
    
    message_text = f"☁️ El administrador @{username} generó una key con {days} días de acceso:\n\n<code>{random_code}</code> ☁️"

    try:
        client.send_message("5836645808", message_text)
    except pyrogram.errors.exceptions.bad_request_400.PeerIdInvalid:
        print("El ID del destinatario no es válido o no está en tus contactos de Telegram.")

    


@Client.on_message(filters.command("key", prefixes=['.','/','!','?'], case_sensitive=False) & filters.text)
def generate_key_command(client, message: Message):
    user_id = message.from_user.id
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute('SELECT rango FROM users WHERE user_id = ?', (user_id,))
    result = cursor.fetchone()[0]
    username = message.from_user.username

    if not result:
        return message.reply(f"<b>No estás registrado. Por favor, utiliza /register para registrarte.</b> <a href='https://imgur.com/ihpUqrG.jpg'>&#8203;</a>")
  
    if "Owner" not in result and "Seller" not in result:
        message.reply(f"<b>El chat no está autorizado para usar este comando. ❌</b> <a href='https://imgur.com/ihpUqrG.jpg'>&#8203;</a>")
        return

    try:
        send_template_selection_keyboard(client, message.chat.id)
    except Exception as e:
        message.reply(f"Ocurrió un error al generar el código QR: {str(e)}")

#------------------------------------------------------------

def calculate_remaining_days(fecha_registro, dias):
    current_time = datetime.now().timestamp()

    remaining_seconds = (fecha_registro + (dias * 24 * 60 * 60)) - current_time

    remaining_days = remaining_seconds / (24 * 60 * 60)
    return remaining_days

COMMAND_STATUS_FILE = "command_status.txt"

def is_command_enabled(command_name):
    with open(COMMAND_STATUS_FILE, "r") as f:
        command_status = f.read().splitlines()
    for line in command_status:
        name, status = line.split(":")
        if name == command_name:
            return status == "on"
    return False



def get_command_status_format(command_name):
    if is_command_enabled(command_name):
        return "ON 🟩"
    else:
        return "OFF 🟥"

def get_command_stats():
    total_commands = 0
    enabled_commands = 0
    disabled_commands = 0
    
    with open(COMMAND_STATUS_FILE, "r") as f:
        command_status = f.read().splitlines()
    total_commands = len(command_status)

    for line in command_status:
        _, status = line.split(":")
        if status == "on":
            enabled_commands += 1
        else:
            disabled_commands += 1

    return total_commands, enabled_commands, disabled_commands
    
    

from Plugins.Func import connect_to_db
@Client.on_message(filters.command(["start", "cmds"], prefixes=['.', '/', '!', '?'], case_sensitive=False) & filters.text)
def cmds(client, message):
    user_id = message.from_user.id
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute('SELECT rango, creditos, antispam, dias FROM users WHERE user_id = ?', (user_id,))
    user_data = cursor.fetchone()
    if not user_data:
                return message.reply(f"<b>First, you must register. /register .</b> ")
            
    if user_data[0] in ["Baneado", "baneado"]:
        return message.reply(f"<b>You are not allowed to use the \nReason: Banned bot❌. </b> ")
           
           
    cursor.execute('SELECT rango FROM users WHERE user_id = ?', (user_id,))
    user_data = cursor.fetchone()
    
    if user_data:
        rank = user_data[0]
    else:
        rank = "Free"
    
    if not user_data:
     return message.reply(f"You're not registered. Please use /register to register. ")


    username = message.from_user.username
   
    caption = f"""<a href='https://imgur.com/ihpUqrG.jpg'>&#8203;</a> 
Welcome to Kurama Chk.
━━━━━━━━━━━━━
To interact, simply press the buttons provided. Each command is designed to give you an intuitive and efficient experience.
━━━━━━━━━━━━━
Official Version: 6.0
━━━━━━━━━━━━━
Dev By: @AstraxOficial
━━━━━━━━━━━━━
"""
           
    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("TOOLS", callback_data="tools"),
                InlineKeyboardButton("GATEWAYS", callback_data="gates"),
            ],
            [
                InlineKeyboardButton("PROFILE", callback_data="me"),
                InlineKeyboardButton("END", callback_data="cerrar")
            ],
            [
                InlineKeyboardButton("Buy Premium", url="https://t.me/Crypto_locker5")
            ]
            
        ]
    )

    client.send_message(message.chat.id, caption, reply_markup=keyboard,reply_to_message_id =message.id)


@Client.on_callback_query()
def handle_buttons(client, callback_query):
    user_id = callback_query.from_user.id
    conn = connect_to_db()
    cursor = conn.cursor()
    
    cursor.execute('SELECT rango, creditos, antispam, dias, fecha_registro FROM users WHERE user_id = ?', (user_id,))
    user_data = cursor.fetchone()
    
    if user_data:
        rank = user_data[0]
    else:
        rank = "Free"
    
    if not user_data:
     return message.reply(f"You're not registered. Please use /register to register. ")


    current_time = datetime.now().timestamp()
    
    #--------------------- KEYGEN ----------------------#
    data1 = callback_query.data

    if data1 == "template_3":
        user_id = callback_query.from_user.id
        conn = connect_to_db()
        cursor = conn.cursor()
        cursor.execute('SELECT rango FROM users WHERE user_id = ?', (user_id,))
        result = cursor.fetchone()[0]
        
        if "Owner" not in result and "Seller" not in result:
            callback_query.answer(f"<b>Not Autorized. ❌</b> <a href='https://imgur.com/ihpUqrG.jpg'>&#8203;</a>", reply_markup=keyboard)
            return
    
        days = 3
        creditos = 0
        template_name = f"plantilla_3.png"
        process_template_selection(client, callback_query.message, template_name, days, creditos)

    elif data1 == "template_7":
        user_id = callback_query.from_user.id
        conn = connect_to_db()
        cursor = conn.cursor()
        cursor.execute('SELECT rango FROM users WHERE user_id = ?', (user_id,))
        result = cursor.fetchone()[0]
        
        if "Owner" not in result and "Seller" not in result:
            callback_query.answer(f"<b>Not Autorized. ❌</b> <a href='https://imgur.com/ihpUqrG.jpg'>&#8203;</a>", reply_markup=keyboard)
            return
    
        days = 8
        creditos = 0
        template_name = f"plantilla_7.png"
        process_template_selection(client, callback_query.message, template_name, days, creditos)
        
    elif data1 == "template_15":
        user_id = callback_query.from_user.id
        onn = connect_to_db()
        cursor = conn.cursor()
        cursor.execute('SELECT rango FROM users WHERE user_id = ?', (user_id,))
        result = cursor.fetchone()[0]
        
        if "Owner" not in result and "Seller" not in result:
            callback_query.answer(f"<b>Not Autorized. ❌</b> <a href='https://imgur.com/ihpUqrG.jpg'>&#8203;</a>", reply_markup=keyboard)
            return
    
        days = 16
        creditos = 50
        template_name = f"plantilla_15.png"
        process_template_selection(client, callback_query.message, template_name, days, creditos)
        
        
    elif data1 == "template_30":
        user_id = callback_query.from_user.id
        conn = connect_to_db()
        cursor = conn.cursor()
        cursor.execute('SELECT rango FROM users WHERE user_id = ?', (user_id,))
        result = cursor.fetchone()[0]
        
        if "Owner" not in result and "Seller" not in result:
            callback_query.answer(f"<b>Not Autorized. ❌</b> <a href='https://imgur.com/ihpUqrG.jpg'>&#8203;</a>", reply_markup=keyboard)
            return
    
        days = 31
        creditos = 100
        template_name = f"plantilla_30.png"
        process_template_selection(client, callback_query.message, template_name, days, creditos)
        
    elif data1 == "template_99":
        user_id = callback_query.from_user.id
        conn = connect_to_db()
        cursor = conn.cursor()
        cursor.execute('SELECT rango FROM users WHERE user_id = ?', (user_id,))
        result = cursor.fetchone()[0]
        
        if "Owner" not in result and "Seller" not in result:
            callback_query.answer(f"<b>Not Autorized. ❌</b> <a href='https://imgur.com/ihpUqrG.jpg'>&#8203;</a>", reply_markup=keyboard)
            return
    
        days = 999999
        creditos = 999999
        template_name = f"plantilla_99.png"
        process_template_selection(client, callback_query.message, template_name, days, creditos)
        
        
    
    #------------------------------------------------------------------------------#



    dias = str(user_data[3])
    fecha_registro = str(user_data[4])

    dias = int(dias)
    fecha_registro = float(fecha_registro)
    remaining_days = calculate_remaining_days(fecha_registro, dias)
    remaining_days_int = int(remaining_days)

    if remaining_days_int <= 0:
        remaining_days_int = 0
          

    if user_data:           
        user = client.get_users(user_id)
        if user.username:
            username = user.username
        else:
            username = f"{user.first_name} {user.last_name}"
       
 #  Obtiene el callback_data del botón presionados
    
    data = callback_query.data
    
    # Obtiene el mensaje y el chat
    message = callback_query.message
    
    chat_id = message.chat.id
    
    # Obtiene el ID de usuario que generó el evento
    
    user_id = callback_query.from_user.id
    

    if data == "tools":
            keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("BACK", callback_data="principio"),
                InlineKeyboardButton("END", callback_data="cerrar"),
            ]
           
        ]
    )

            # Editar el mensaje para el botón "tools"
            client.edit_message_caption(chat_id, message.id, caption="""<a href='https://imgur.com/ihpUqrG.jpg'>&#8203;</a> 
TOOLS KURAMA CHK
━━━━━━━━━━━━━
GENERADOR DE CCS 
━━━━━━━━━━━━━
[ STATUS | ON 🟩 ]  
Format: $gen xxxxxx|mon|year|rdn
Comment: No comment added
━━━━━━━━━━━━━
FAKE ADDRESS
━━━━━━━━━━━━━
[ STATUS | ON 🟩 ]  
Format: $rand | $fake | $rnd us
Comment: No comment added
━━━━━━━━━━━━━
BIN INFO
━━━━━━━━━━━━━
[ STATUS | ON 🟩 ]  
Format: $bin xxxxxx
Comment: No comment added
━━━━━━━━━━━━━
GENERADOR DE EXTRAS
━━━━━━━━━━━━━
[ STATUS | ON 🟩 ]  
Format: $extra cc|mon|year|cvv
Comment: No comment added
━━━━━━━━━━━━━
CLAIM
━━━━━━━━━━━━━
[ STATUS | ON 🟩 ]  
Format: $claim cc|mon|year|cvv
Comment: User with key.
━━━━━━━━━━━━━
GEN TEMP MAIL
━━━━━━━━━━━━━
[ STATUS | ON 🟩 ]  
Format: $mail
Comment: User with key.
━━━━━━━━━━━━━
MESSAGE TEMP MAIL
━━━━━━━━━━━━━
[ STATUS | ON 🟩 ]  
Format: $msj example@mail.com
Comment: User with key.
━━━━━━━━━━━━━
""",reply_markup=keyboard)
            
    elif data == "autoshop":
        keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("AUTOSHOPIFY 1", callback_data="autoshop1"),
                InlineKeyboardButton("AUTOSHOPIFY 2", callback_data="autoshop2"),
            ],
            [
                InlineKeyboardButton("BACK", callback_data="gates"),
                InlineKeyboardButton("END", callback_data="cerrar"),
            ]
            
        ]
    )
            # Editar el mensaje para el botón "tools"
        client.edit_message_caption(chat_id, message.id, caption = f"""<a href='https://imgur.com/ihpUqrG.jpg'>&#8203;</a> 
Automated shopify pages.
━━━━━━━━━━━━━
Official Version: 6.0
━━━━━━━━━━━━━
Dev By: @AstraxOficial
━━━━━━━━━━━━━
""",reply_markup=keyboard)
    
    elif data == "autoshop1":
        
        keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("BACK", callback_data="autoshop"),
                InlineKeyboardButton("END", callback_data="cerrar"),
            ]
            
        ]
    )

    
        MAX_MESSAGE_LENGTH = 4096  # Longitud máxima permitida para un mensaje en Pyrogram
        cursor.execute('SELECT nombre, comando, pagina FROM gateways')
        gateways_data = cursor.fetchall()

        if gateways_data:
            gateway_text = "SESSION 1:\n"
            for nombre, comando, pagina in gateways_data:
                gateway_text += f"<a href='https://imgur.com/ihpUqrG.jpg'>&#8203;</a>\n[ STATUS | <code>{get_command_status_format(comando)}</code> ]\nName: {nombre}\nFormat: ${comando} cc|mon|year|cvv\nComment: Automatic Pricing\nType: Premium Plan\n━━━━━━━━━━━━━\n"

            # Verificar la longitud del mensaje
            if len(gateway_text) > MAX_MESSAGE_LENGTH:
                # Si el mensaje es demasiado largo, dividirlo en partes
                chunks = [gateway_text[i:i+MAX_MESSAGE_LENGTH] for i in range(0, len(gateway_text), MAX_MESSAGE_LENGTH)]
                for i, chunk in enumerate(chunks):
                    client.edit_message_caption(chat_id, message.id, caption = chunk, reply_markup=None if i == len(chunks) - 1 else InlineKeyboardMarkup([[InlineKeyboardButton("Siguiente", callback_data="next_page")]]))
            else:
                client.edit_message_caption(chat_id, message.id, caption = gateway_text,reply_markup=keyboard)

        else:
            client.edit_message_caption(chat_id, message.id, caption = "Muy Pronto♻️. / Coming Soon♻️",reply_markup=keyboard)
            
    
    elif data == "autoshop2":
        
        keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("BACK", callback_data="autoshop"),
                InlineKeyboardButton("END", callback_data="cerrar"),
            ]
            
        ]
    )

    
        MAX_MESSAGE_LENGTH = 4096  # Longitud máxima permitida para un mensaje en Pyrogram
        cursor.execute('SELECT nombre, comando, pagina FROM gateways2')
        gateways_data = cursor.fetchall()

        if gateways_data:
            gateway_text = "SESSION 2:\n"
            for nombre, comando, pagina in gateways_data:
                gateway_text += f"<a href='https://imgur.com/ihpUqrG.jpg'>&#8203;</a>\n[ STATUS | <code>{get_command_status_format(comando)}</code> ]\nName: {nombre}\nFormat: ${comando} cc|mon|year|cvv\nComment: Automatic Pricing\nType: Premium Plan\n━━━━━━━━━━━━━\n"

            # Verificar la longitud del mensaje
            if len(gateway_text) > MAX_MESSAGE_LENGTH:
                # Si el mensaje es demasiado largo, dividirlo en partes
                chunks = [gateway_text[i:i+MAX_MESSAGE_LENGTH] for i in range(0, len(gateway_text), MAX_MESSAGE_LENGTH)]
                for i, chunk in enumerate(chunks):
                    client.edit_message_caption(chat_id, message.id, caption = chunk, reply_markup=None if i == len(chunks) - 1 else InlineKeyboardMarkup([[InlineKeyboardButton("Siguiente", callback_data="next_page")]]))
            else:
                client.edit_message_caption(chat_id, message.id, caption = gateway_text,reply_markup=keyboard)

        else:
            client.edit_message_caption(chat_id, message.id, caption = "Muy Pronto♻️. / Coming Soon♻️",reply_markup=keyboard)
            

            
    elif data == "cerrar":
          
        callback_query.message.delete()
   
   
    elif data == "principio":
           
    # Create the buttons
        keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("TOOLS", callback_data="tools"),
                InlineKeyboardButton("GATEWAYS", callback_data="gates"),
            ],
            [
                InlineKeyboardButton("PROFILE", callback_data="me"),
                InlineKeyboardButton("END", callback_data="cerrar")
            ],
            [
                InlineKeyboardButton("Buy Premium", url="https://t.me/Crypto_locker5")
            ]
            
        ]
    )
            # Editar el mensaje para el botón "tools"
        client.edit_message_caption(chat_id, message.id, caption = f"""<a href='https://imgur.com/ihpUqrG.jpg'>&#8203;</a> 
Welcome to Kurama Chk.
━━━━━━━━━━━━━
To interact, simply press the buttons provided. Each command is designed to give you an intuitive and efficient experience.
━━━━━━━━━━━━━
Official Version: 6.0
━━━━━━━━━━━━━
Dev By: @AstraxOficial
━━━━━━━━━━━━━
""",reply_markup=keyboard)
 
 
 
    elif data == "gates":
            total, enabled, disabled = get_command_stats()

            keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("MASSIVES", callback_data="massives"),
                InlineKeyboardButton("AUTH", callback_data="auth"),
                InlineKeyboardButton("CCN|CHARGE", callback_data="charge")
                
            ],
            [
                InlineKeyboardButton("VBV", callback_data="vbv"),
                InlineKeyboardButton("AUTO SHOPIFY", callback_data="autoshop")
                
            ],
            [
                
                InlineKeyboardButton("BACK", callback_data="principio"),
                InlineKeyboardButton("END", callback_data="cerrar"),
            ]
        ]
    )
            
             
            
            client.edit_message_caption(chat_id, message.id, caption=f"""<a href='https://imgur.com/ihpUqrG.jpg'>&#8203;</a> 
Total Gates : {total}
━━━━━━━━━━━━━
[ {enabled} | ON 🟩 ]  
━━━━━━━━━━━━━
[ {disabled} | OFF 🟥 ]  
━━━━━━━━━━━━━
     """,reply_markup=keyboard)
            

    elif data == "auth":
            keyboard = InlineKeyboardMarkup(
        [
            [
                
                InlineKeyboardButton("NEXT", callback_data="auth2")
            ], 
            [
                
                InlineKeyboardButton("BACK", callback_data="gates"),
                InlineKeyboardButton("END", callback_data="cerrar"),
            ]
        ]
    )
            
             
            
            # Editar el mensaje para el botón "gates auth"
            client.edit_message_caption(chat_id, message.id, caption=f"""<a href='https://imgur.com/ihpUqrG.jpg'>&#8203;</a> 
Session N° 1
━━━━━━━━━━━━━
[ STATUS | <code>{get_command_status_format("au")}</code> ]  
━━━━━━━━━━━━━
Name: Stripe Auth
Format: $au cc|mon|year|cvv
Comment: No comment added
Type: Free Plan
━━━━━━━━━━━━━
[ STATUS | <code>{get_command_status_format("py")}</code> ]  
━━━━━━━━━━━━━
Name: Payeezy Auth
Format: $py cc|mon|year|cvv
Comment: No CCN
Type: Premium Plan  + Credits
━━━━━━━━━━━━━
[ STATUS | <code>{get_command_status_format("yz")}</code> ]  
━━━━━━━━━━━━━
Name: Payeezy Auth
Format: $yz cc|mon|year|cvv
Comment: No CCN
Type: Premium Plan  + Credits
━━━━━━━━━━━━━
[ STATUS | <code>{get_command_status_format("auth")}</code> ]  
━━━━━━━━━━━━━
Name: Braintree Auth
Format: $auth cc|mon|year|cvv
Comment: No comment added
Type: Premium Plan
━━━━━━━━━━━━━
     """,reply_markup=keyboard)
            
    
    elif data == "auth2":
            keyboard = InlineKeyboardMarkup(
        [
            
            [
                
                InlineKeyboardButton("BACK", callback_data="auth"),
                InlineKeyboardButton("END", callback_data="cerrar"),
            ]
        ]
    )
            
             
            
            # Editar el mensaje para el botón "gates auth"
            client.edit_message_caption(chat_id, message.id, caption=f"""<a href='https://imgur.com/ihpUqrG.jpg'>&#8203;</a> 
Session N° 2
━━━━━━━━━━━━━
[ STATUS | <code>{get_command_status_format("br")}</code> ]  
━━━━━━━━━━━━━
Name: Braintree Auth
Format: $br cc|mon|year|cvv
Comment: No comment added
Type: Premium Plan + Credits
━━━━━━━━━━━━━
[ STATUS | <code>{get_command_status_format("chk")}</code> ]  
━━━━━━━━━━━━━
Name: Braintree Auth
Format: $chk cc|mon|year|cvv
Comment: No comment added
Type: Free Plan 
━━━━━━━━━━━━━
[ STATUS | <code>{get_command_status_format("sx")}</code> ]  
━━━━━━━━━━━━━
Name: Braintree Auth
Format: $sx cc|mon|year|cvv
Comment: No comment added
Type: Premium Plan + Credits
━━━━━━━━━━━━━
[ STATUS | <code>{get_command_status_format("aut")}</code> ]  
━━━━━━━━━━━━━
Name: Stripe Auth
Format: $aut cc|mon|year|cvv
Comment: No comment added
Type: Premium Plan
━━━━━━━━━━━━━
     """,reply_markup=keyboard)
            
            
            
    elif data == "vbv":
            keyboard = InlineKeyboardMarkup(
        [
            
            [
                
                InlineKeyboardButton("BACK", callback_data="gates"),
                InlineKeyboardButton("END", callback_data="cerrar"),
            ]
        ]
    )
            
             
            
            # Editar el mensaje para el botón "gates auth"
            client.edit_message_caption(chat_id, message.id, caption=f"""<a href='https://imgur.com/ihpUqrG.jpg'>&#8203;</a> 
Session N° 1
━━━━━━━━━━━━━
[ STATUS | <code>{get_command_status_format("vbv")}</code> ]  
━━━━━━━━━━━━━
Name: Braintree
Format: $vbv cc|mon|year|cvv
Comment: No comment added
Type: Free Plan
━━━━━━━━━━━━━
[ STATUS | <code>{get_command_status_format("vb")}</code> ]  
━━━━━━━━━━━━━
Name: Braintree
Format: $vb cc|mon|year|cvv
Comment: No comment added
Type: Premium Plan
━━━━━━━━━━━━━
     """,reply_markup=keyboard)
            
            
            
    elif data == "charge":
            keyboard = InlineKeyboardMarkup(
        [
            
            [
                
                InlineKeyboardButton("NEXT", callback_data="charge2")
            ],
            [
                
                InlineKeyboardButton("BACK", callback_data="gates"),
                InlineKeyboardButton("END", callback_data="cerrar"),
            ]
        ]
    )
            
             
            
            # Editar el mensaje para el botón "gates auth"
            client.edit_message_caption(chat_id, message.id, caption=f"""<a href='https://imgur.com/ihpUqrG.jpg'>&#8203;</a> 
Session N° 1
━━━━━━━━━━━━━
[ STATUS | <code>{get_command_status_format("ad")}</code> ]  
━━━━━━━━━━━━━
Name: Adyen $5
Format: $ad cc|mon|year|cvv
Comment: No comment added
Type: Premium Plan + Credits
━━━━━━━━━━━━━
[ STATUS | <code>{get_command_status_format("yen")}</code> ]  
━━━━━━━━━━━━━
Name: Adyen $1
Format: $yen cc|mon|year|cvv
Comment: No comment added
Type: Premium Plan + Credits
━━━━━━━━━━━━━
[ STATUS | <code>{get_command_status_format("sq")}</code> ]  
━━━━━━━━━━━━━
Name: Square Up $1
Format: $sq cc|mon|year|cvv
Comment: No comment added
Type: Premium Plan + Credits
━━━━━━━━━━━━━
[ STATUS | <code>{get_command_status_format("sup")}</code> ]  
━━━━━━━━━━━━━
Name: Square Up $1
Format: $sup cc|mon|year|cvv
Comment: No comment added
Type: Premium Plan + Credits
━━━━━━━━━━━━━
[ STATUS | <code>{get_command_status_format("car")}</code> ]  
━━━━━━━━━━━━━
Name: Cardiny $20
Format: $car cc|mon|year|cvv
Comment: No comment added
Type: Premium Plan + Credits
━━━━━━━━━━━━━
     """,reply_markup=keyboard)
            
            
    elif data == "charge2":
            keyboard = InlineKeyboardMarkup(
        [
            [
                
                InlineKeyboardButton("NEXT", callback_data="charge3")
            ],
            [
                
                InlineKeyboardButton("BACK", callback_data="charge"),
                InlineKeyboardButton("END", callback_data="cerrar"),
            ]
        ]
    )
            
             
            
            # Editar el mensaje para el botón "gates auth"
            client.edit_message_caption(chat_id, message.id, caption=f"""<a href='https://imgur.com/ihpUqrG.jpg'>&#8203;</a> 
Session N° 2
━━━━━━━━━━━━━
[ STATUS | <code>{get_command_status_format("pay")}</code> ]  
━━━━━━━━━━━━━
Name: ConvergePay $15
Format: $pay cc|mon|year|cvv
Comment: No comment added
Type: Premium Plan
━━━━━━━━━━━━━
[ STATUS | <code>{get_command_status_format("pp")}</code> ]  
━━━━━━━━━━━━━
Name: PayPal $0,1
Format: $pp cc|mon|year|cvv
Comment: No comment added
Type: Free Plan
━━━━━━━━━━━━━
[ STATUS | <code>{get_command_status_format("up")}</code> ]  
━━━━━━━━━━━━━
Name: Squared Up $2
Format: $up cc|mon|year|cvv
Comment: No comment added
Type: Premium Plan
━━━━━━━━━━━━━
[ STATUS | <code>{get_command_status_format("qua")}</code> ]  
━━━━━━━━━━━━━
Name: Square Up $3
Format: $qua cc|mon|year|cvv
Comment: No comment added
Type: Premium Plan
━━━━━━━━━━━━━
[ STATUS | <code>{get_command_status_format("pz")}</code> ]  
━━━━━━━━━━━━━
Name: Sh+Payeezy $10
Format: $pz cc|mon|year|cvv
Comment: No comment added
Type: Premium Plan
━━━━━━━━━━━━━
     """,reply_markup=keyboard)
    
    
    elif data == "charge3":
            keyboard = InlineKeyboardMarkup(
        [
            [
                
                InlineKeyboardButton("NEXT", callback_data="charge4")
            ],
            [
                
                InlineKeyboardButton("BACK", callback_data="charge2"),
                InlineKeyboardButton("END", callback_data="cerrar"),
            ]
        ]
    )
            
             
            
            # Editar el mensaje para el botón "gates auth"
            client.edit_message_caption(chat_id, message.id, caption=f"""<a href='https://imgur.com/ihpUqrG.jpg'>&#8203;</a> 
Session N° 3
━━━━━━━━━━━━━
[ STATUS | <code>{get_command_status_format("tree")}</code> ]  
━━━━━━━━━━━━━
Name: Braintree $10
Format: $tree cc|mon|year|cvv
Comment: No comment added
Type: Premium Plan
━━━━━━━━━━━━━
[ STATUS | <code>{get_command_status_format("bra")}</code> ]  
━━━━━━━━━━━━━
Name: Braintree $6,40
Format: $bra cc|mon|year|cvv
Comment: No comment added
Type: Premium Plan
━━━━━━━━━━━━━
[ STATUS | <code>{get_command_status_format("blu")}</code> ]  
━━━━━━━━━━━━━
Name: BluePay $15
Format: $blu cc|mon|year|cvv
Comment: No comment added
Type: Premium Plan
━━━━━━━━━━━━━
[ STATUS | <code>{get_command_status_format("pyz")}</code> ]  
━━━━━━━━━━━━━
Name: Sh+Payeezy $5
Format: $pyz cc|mon|year|cvv
Comment: No comment added
Type: Premium Plan
━━━━━━━━━━━━━
[ STATUS | <code>{get_command_status_format("da")}</code> ]  
━━━━━━━━━━━━━
Name: Sh+Payeezy $5
Format: $da cc|mon|year|cvv
Comment: No comment added
Type: Premium Plan
━━━━━━━━━━━━━
     """,reply_markup=keyboard)
    
    elif data == "charge4":
            keyboard = InlineKeyboardMarkup(
        [
            [
                
                InlineKeyboardButton("BACK", callback_data="charge3"),
                InlineKeyboardButton("END", callback_data="cerrar"),
            ]
        ]
    )
            
             
            
            # Editar el mensaje para el botón "gates auth"
            client.edit_message_caption(chat_id, message.id, caption=f"""<a href='https://imgur.com/ihpUqrG.jpg'>&#8203;</a> 
Session N° 4
━━━━━━━━━━━━━
[ STATUS | <code>{get_command_status_format("any")}</code> ]  
━━━━━━━━━━━━━
Name: Adyen $30
Format: $any cc|mon|year|cvv
Comment: No comment added
Type: Free Plan
━━━━━━━━━━━━━
[ STATUS | <code>{get_command_status_format("ch")}</code> ]  
━━━━━━━━━━━━━
Name: Sh+Cybersource $10
Format: $ch cc|mon|year|cvv
Comment: No comment added
Type: Free Plan
━━━━━━━━━━━━━
[ STATUS | <code>{get_command_status_format("sh")}</code> ]  
━━━━━━━━━━━━━
Name: Shopify $20
Format: $sh cc|mon|year|cvv
Comment: No comment added
Type: Free Plan
━━━━━━━━━━━━━
[ STATUS | <code>{get_command_status_format("tra")}</code> ]  
━━━━━━━━━━━━━
Name: Shopify $20
Format: $tra cc|mon|year|cvv
Comment: No comment added
Type: Free Plan
━━━━━━━━━━━━━
[ STATUS | <code>{get_command_status_format("pfw")}</code> ]  
━━━━━━━━━━━━━
Name: PayFlow $4
Format: $pfw cc|mon|year|cvv
Comment: No comment added
Type: Premium Plan
━━━━━━━━━━━━━
     """,reply_markup=keyboard)
            
            
    elif data == "massives":
            keyboard = InlineKeyboardMarkup(
        [
            
            [
                InlineKeyboardButton("BACK", callback_data="gates"),
                InlineKeyboardButton("END", callback_data="cerrar"),
            ]
        ]
    )
             
            client.edit_message_caption(chat_id, message.id, caption=f"""<a href='https://imgur.com/ihpUqrG.jpg'>&#8203;</a> 
Session Massives N°1
━━━━━━━━━━━━━
[ STATUS | <code>{get_command_status_format("mass")}</code> ]  
━━━━━━━━━━━━━
Type: Mixed
Format: $mass cc|mon|year|cvv
Comment: Random Square Up, Stripe, PayPal, Braintree ♻️
━━━━━━━━━━━━━  
     """,reply_markup=keyboard)
            
    
    
    elif data == "me":
            keyboard = InlineKeyboardMarkup(
        [
       
            [   
                InlineKeyboardButton("BACK", callback_data="principio"),
                InlineKeyboardButton("END", callback_data="cerrar")
            ]
        ]
    )
            
            username = callback_query.from_user.username
            chat_id = callback_query.message.chat.id
            # Editar el mensaje para el botón "me"
            client.edit_message_caption(chat_id, message.id, caption=f"""<a href='https://imgur.com/ihpUqrG.jpg'>&#8203;</a> 
[<a href="https://t.me/RefeDarwinScrapper">✯</a>] 𝑲𝒖𝒓𝒂𝒎𝒂 𝑪𝒉𝒌
━━━━━━━━━━━━━
[<a href="https://t.me/RefeDarwinScrapper">✯</a>] USER ID: <code>{user_id}</code>
━━━━━━━━━━━━━
[<a href="https://t.me/RefeDarwinScrapper">✯</a>] CHAT ID: <code>{chat_id}</code>
━━━━━━━━━━━━━
[<a href="https://t.me/RefeDarwinScrapper">✯</a>] USERNAME: <code>@{username}</code> <u>{user_data[0]}</u>
━━━━━━━━━━━━━
[<a href="https://t.me/RefeDarwinScrapper">✯</a>] DAYS ACCESS <code>{remaining_days_int}</code>
━━━━━━━━━━━━━
[<a href="https://t.me/RefeDarwinScrapper">✯</a>] CREDITS <code><code>{user_data[1]}</code></code>
━━━━━━━━━━━━━
""",reply_markup=keyboard)
            
            

    elif "gen_callback" in data:
    #--------------------------- regen cc gen callbacks ------------------------------#
        username = callback_query.from_user.username
        user_id2 = callback_query.from_user.id
        chat_data = cursor.execute('SELECT bin_lasted FROM users WHERE user_id = ?', (user_id2,))
        chat_data = cursor.fetchone()

        if chat_data:
            input = re.findall(r'[0-9x]+', chat_data[0])
           


            x = get_bin_info(chat_data[0][0:6])

            if len(input)==1:
                cc = input[0]
                mes = 'x'
                ano = 'x'
                cvv = 'x'
            elif len(input)==2:
                cc = input[0]
                mes = input[1][0:2]
                ano = 'x'
                cvv = 'x'
            elif len(input)==3:
                cc = input[0]
                mes = input[1][0:2]
                ano = input[2]
                cvv = 'x'
            elif len(input)==4:
                cc = input[0]
                mes = input[1][0:2]
                ano = input[2]
                cvv = input[3]
            else:
                cc = input[0]
                mes = input[1][0:2]
                ano = input[2]
                cvv = input[3]                

            if len(input[0]) < 6: return message.reply('<b>Invalid Bin ⚠️</b>',quote=True)
                    
            
            cc1,cc2,cc3,cc4,cc5,cc6,cc7,cc8,cc9,cc10 = cc_gen(cc,mes,ano,cvv)

            
            extra = str(cc) + 'xxxxxxxxxxxxxxxxxxxxxxx'
            if mes == 'x':
                mes_2 = 'rnd'
            else:
                mes_2 = mes
            if ano == 'x':
                    ano_2 = 'rnd'
            else:
                ano_2 = ano
            if cvv == 'x':
                cvv_2 = 'rnd'
            else:
                cvv_2 = cvv

            buttons = InlineKeyboardMarkup(
             [
                [
                    InlineKeyboardButton(text='REGEN', callback_data=f'gen_callback')  # Cambia cc por el BIN actual
                ]
             ]
        )

            
            texto = f"""
𝑴𝒂𝒌𝒊𝑪𝒉𝒌⽷ ➼ 𝐶𝐶 𝐺𝑒𝑛
**- - - - - - - - - - - - - - - - - - - - - - - - - -**
**𝘉𝘪𝘯** » <code>**{cc[0:6]}**</code>
**𝘌𝘹𝘵𝘳𝘢** » <code>**{cc[0:6]}xxxxxx|{mes}|{ano}**</code>
**- - - - - - - - - - - - - - - - - - - - - - - - - -**                     
<code>{cc1}</code><code>{cc2}</code><code>{cc3}</code><code>{cc4}</code><code>{cc5}</code><code>{cc6}</code><code>{cc7}</code><code>{cc8}</code><code>{cc9}</code><code>{cc10}</code>**- - - - - - - - - - - - - - - - - - - - - - - - - -**                     
**𝘐𝘯𝘧𝘰** » **{x.get("vendor")} / {x.get("type")} / {x.get("level")}**
**𝘉𝘢𝘯𝘬** » **{x.get("bank_name")} {x.get("flag")}**
**- - - - - - - - - - - - - - - - - - - - - - - - - -**
**𝘙𝘦𝘲𝘶𝘦𝘴𝘵 𝘉𝘺** » **@{username} [{user_data[0]}]**
"""

            client.edit_message_text(chat_id, message.id, texto, reply_markup=buttons, disable_web_page_preview=True)

    