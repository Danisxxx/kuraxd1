from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import random
from Plugins.Func import connect_to_db

footer_banner1 = 'https://imgur.com/llb5G2P.jpg'


@Client.on_message(filters.command(["panel"], prefixes=['.','/','!','?'], case_sensitive=False) & filters.text)
async def panel_command(client, message):
    user_id = message.from_user.id
    
    conn = connect_to_db()
    cursor = conn.cursor()
    user_id = message.from_user.id
    cursor.execute('SELECT rango, creditos, antispam, dias FROM users WHERE user_id = ?', (user_id,))
    user_data = cursor.fetchone()
          
    if user_data[0] not in ["Seller", "Owner"]:
                return await message.reply(f"<b>Access denied. ❌</b> <a href='{footer_banner1}'>&#8203;</a>")
            
    # Send a random video with a caption
    video_urls = [
        "https://imgur.com/jfRGk6l.mp4"
    ]

    # Obtener la lista de videos ya enviados
    sent_videos = getattr(client, "sent_videos", [])

    # Verificar si se han enviado todos los videos disponibles
    if len(sent_videos) == len(video_urls):
        # Se han enviado todos los videos, restablecer la lista de sent_videos
        sent_videos = []

    # Seleccionar un video aleatorio que no se haya enviado anteriormente
    video_path = None
    while not video_path:
        random_video = random.choice(video_urls)
        if random_video not in sent_videos:
            video_path = random_video

    # Agregar el video a la lista de sent_videos
    sent_videos.append(video_path)

    # Actualizar la lista de sent_videos en el cliente
    setattr(client, "sent_videos", sent_videos)

    caption = """<a href='https://imgur.com/ihpUqrG.jpg'>&#8203;</a>
<b>[<a href="https://t.me/RefeDarwinScrapper">✯</a>]  BIENVENIDO ADMIN, GRACIAS POR SER PARTE DE NUESTRO EQUIPO ESTOS SON NUESTROS COMANDOS:
━━━━━━━━━━━━━━━━
[<a href="https://t.me/RefeDarwinScrapper">✯</a>]  /comd - Activar o desactivar Gateways - Solo Owners
━━━━━━━━━━━━━━━━
[<a href="https://t.me/RefeDarwinScrapper">✯</a>]  /global - Conteo de usuarios en la Base De datos
━━━━━━━━━━━━━━━━
[<a href="https://t.me/RefeDarwinScrapper">✯</a>]  /addcr - USE: /addcr 1234555 10, Agregar Creditos
━━━━━━━━━━━━━━━━
[<a href="https://t.me/RefeDarwinScrapper">✯</a>]  /removecr - Reiniciar Creditos de un usuario
━━━━━━━━━━━━━━━━
[<a href="https://t.me/RefeDarwinScrapper">✯</a>]  /admin - Agregar Seller /Solo Owners
━━━━━━━━━━━━━━━━
[<a href="https://t.me/RefeDarwinScrapper">✯</a>]  /banuser - Banear Usuario
━━━━━━━━━━━━━━━━
[<a href="https://t.me/RefeDarwinScrapper">✯</a>]  /key - Generar Key Premium, use: .key
━━━━━━━━━━━━━━━━
[<a href="https://t.me/RefeDarwinScrapper">✯</a>]  /delkey xxxxxx elimina la key y el usuario que canjeo.
━━━━━━━━━━━━━━━━
[<a href="https://t.me/RefeDarwinScrapper">✯</a>]  /genkey - USE:  .genkey 10, Generate Keys.
━━━━━━━━━━━━━━━━
[<a href="https://t.me/RefeDarwinScrapper">✯</a>]  /deldb - Quitar membresía, usuarios Premium/Grupos/Staffs
━━━━━━━━━━━━━━━━
[<a href="https://t.me/RefeDarwinScrapper">✯</a>]  /addstaff - Agregar Nuevo addstaff Premium - USE: /addstaff 123454664 10
━━━━━━━━━━━━━━━━
[<a href="https://t.me/RefeDarwinScrapper">✯</a>]  /addgp - Agregar Nuevo grupo Premium - USE: /addgp 123454664 10
━━━━━━━━━━━━━━━━
[<a href="https://t.me/RefeDarwinScrapper">✯</a>]  /mensaje - enviar un mensaje a todos los usuarios. / solo Owners
━━━━━━━━━━━━━━━━
[<a href="https://t.me/RefeDarwinScrapper">✯</a>]  /premium - Agregar Nuevo Usuario Premium Manual - USE: /premium 123454664 10
━━━━━━━━━━━━━━━━
</b>"""

    # Create the buttons
    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("GRUPO OFICIAL", url="https://t.me/CHATKURAMA"),
            ]
        ]
    )

    # Send the video with the caption and buttons
    await message.reply(caption, reply_markup=keyboard)
