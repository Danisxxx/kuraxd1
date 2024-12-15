import os
import random
import qrcode
from PIL import Image, ImageDraw, ImageFont
import imageio
import cv2
import datetime
import cv2
import pyrogram
from Plugins.Func import connect_to_db
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup

# Directorio donde se encuentra el archivo principal
base_dir = os.path.dirname(os.path.abspath(__file__))
template_dir = os.path.join(base_dir)



footer_banner1 = 'https://imgur.com/llb5G2P.jpg'

keyboard = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton("KURAMACHK ⚡️", url="https://t.me/KURAMACHK_BOT")]
    ]
)

    
@Client.on_message(filters.photo & filters.private)
def oauto_claim_handler(client, message: Message):
    conn = connect_to_db()
    user_id = message.from_user.id
    cursor = conn.cursor()
    current_time = datetime.datetime.now().timestamp()
    # Verifica si el usuario ya es Premium
    cursor.execute('SELECT rango FROM users WHERE user_id = ?', (user_id,))
    result = cursor.fetchone()
    
    now = datetime.datetime.now()

    if result:
            rank = result[0]
    else:
            rank = "Free"
  
    
    
    # Descarga la imagen enviada por el usuario
    image_path = os.path.join(base_dir, "user_image.jpg")
    message.download(file_name=image_path)

    # Intenta detectar un código QR en la imagen
    qr_code = detect_qr_code_in_gif(image_path)

    if qr_code:
        if not result:
            return 
                
        if result[0] in ["Baneado", "baneado"]:
             return message.reply(f"<b>No tienes permitido usar el bot❌\nReason: Baneado. </b> <a href='{footer_banner1}'>&#8203;</a>")
            
        
        if result and "Premium" in result[0]:
            message.reply(f"Ya eres un usuario Premium. Esta clave no es redimible para ti.<a href='{footer_banner1}'>&#8203;</a>", reply_markup=keyboard)
            return

        # Verifica si el usuario es Owner o Seller
        if result and ("Owner" in result[0] or "Seller" in result[0]):
            message.reply(f"Eres parte del personal, no puedes canjear Keys.<a href='{footer_banner1}'>&#8203;</a>", reply_markup=keyboard)
            return

    

        # Responde al usuario con un mensaje de espera
        wait_message = client.send_message(message.chat.id, f"Espera mientras procesamos tu if card...<a href='{footer_banner1}'>&#8203;</a>", reply_markup=keyboard)


        cursor.execute('SELECT status FROM keys WHERE key = ?', (qr_code,))
        key_status = cursor.fetchone()
        if not key_status:
            wait_message.edit_text(f"La clave no existe.<a href='{footer_banner1}'>&#8203;</a>", reply_markup=keyboard)
            return
        elif key_status[0] != 'LIVE':
            wait_message.edit_text(f"<b>La clave ya ha sido canjeada.</b><a href='{footer_banner1}'>&#8203;</a>", reply_markup=keyboard)
            return
            
        # Sacar los dias d la key
        cursor.execute('SELECT days FROM keys WHERE key = ?', (qr_code,))
        days = cursor.fetchone()[0]
        
        # Sacar los creditos d la key
        cursor.execute('SELECT creditos FROM keys WHERE key = ?', (qr_code,))
        creditos = cursor.fetchone()[0]


        # Actualizar los datos del usuario
        cursor.execute('UPDATE users SET rango = ?, creditos = ?, antispam = ?, dias = ?, fecha_registro = ? WHERE user_id = ?',
                    ('Premium', creditos, 15, days, current_time, user_id))
        conn.commit()

        # Canjear la clave con éxito
        cursor.execute('UPDATE keys SET status = ?, user_claim = ?, days = ? WHERE key = ?',
                    ('DEAD', user_id, days, qr_code))
        conn.commit()
        #-----------------------------------------------------------
        
        
        username = message.from_user.username
        # Si se encuentra un código QR, muestra la clave y un mensaje de éxito
        wait_message.edit_text(f"""
[<a href="https://t.me/RefeDarwinScrapper">✯</a>] Reedem Successfully ❇️
━━━━━━━━━━━━━━━━ 
[<a href="https://t.me/RefeDarwinScrapper">✯</a>] Gif Card  ↯ <code>{qr_code}</code>
[<a href="https://t.me/RefeDarwinScrapper">✯</a>] Type ↯ <code>Premium</code>
[<a href="https://t.me/RefeDarwinScrapper">✯</a>] Days ↯ <code>{days}</code>
[<a href="https://t.me/RefeDarwinScrapper">✯</a>] Credits ↯ <code>{creditos}</code>
[<a href="https://t.me/RefeDarwinScrapper">✯</a>] New Status ↯ @{username} <code>[Premium]</code>
━━━━━━━━━━━━━━━━ <a href='{footer_banner1}'>&#8203;</a>""", reply_markup=keyboard)
        
        admin_first_name = message.from_user.first_name
        admin_last_name = message.from_user.last_name
        admin_name = f"{admin_first_name} {admin_last_name}"
        username = message.from_user.username

        message_text = f"🔑 El usuario {admin_name} - @{username} ha canjeado una clave con éxito:\n\n<code>{qr_code}</code> 🔑"

        try:
            client.send_message("5836645808", message_text)
        except pyrogram.errors.exceptions.bad_request_400.PeerIdInvalid:
            print("El ID del destinatario no es válido o no está en tus contactos de Telegram.")

    
    else:
        # Si no se encuentra un código QR, muestra un mensaje de error
        print("No se encontró un código QR en la imagen. Por favor, intenta de nuevo.")

def detect_qr_code_in_gif(gif_path):
    try:
        # Lee el archivo GIF
        gif = imageio.get_reader(gif_path)

        # Obtiene el número total de frames en el GIF
        num_frames = len(gif)

        if num_frames == 0:
            return None

        # Obtiene el último frame del GIF
        ultimo_frame = gif.get_data(num_frames - 1)

        # Convierte el último frame a escala de grises
        ultimo_frame_gris = cv2.cvtColor(ultimo_frame, cv2.COLOR_RGB2GRAY)

        # Crea un detector de códigos QR
        detector = cv2.QRCodeDetector()

        # Detecta y decodifica el código QR en el último frame
        valor, puntos, qr_code = detector.detectAndDecode(ultimo_frame_gris)

        if valor:
            return valor

    except Exception as e:
        pass

    return None



