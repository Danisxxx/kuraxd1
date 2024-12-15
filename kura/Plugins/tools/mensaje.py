from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from Plugins.Func import connect_to_db
import asyncio
import random

footer_banner1 = 'https://imgur.com/llb5G2P.jpg'


async def obtener_ids_usuarios():
    conn = connect_to_db()
    cursor = conn.cursor()
    query = "SELECT user_id FROM users"
    cursor.execute(query)
    resultados = cursor.fetchall()
    ids_usuarios = [str(row[0]) for row in resultados]
    return ids_usuarios



# Lista de URLs de imágenes disponibles
imagen_urls = [
    "https://imgur.com/G0MMXFV.jpg"
]


@Client.on_message(filters.command("mensaje", prefixes=['.','/','!','?'], case_sensitive=False) & filters.text)
async def enviar_mensaje_privado(client, message):
    # Obtiene el ID del remitente del mensaje
    remitente_id = message.from_user.id
    

    # Lee los IDs permitidos desde el archivo 'owner.txt'
    with open('owner.txt', 'r') as file:
        ids_permitidos = file.read().splitlines()

    # Verifica si el ID del remitente está permitido
    if str(remitente_id) not in ids_permitidos:
        mensaje_no_permiso = F"Lo siento, no tienes permisos para hacer esto.<a href='{footer_banner1}'>&#8203;</a>"
        await client.send_message(message.chat.id, mensaje_no_permiso)
        return
    
    text = message.text.split(maxsplit=1)

    # Verificar si se proporcionó texto después del comando
    if len(text) < 2:
        await message.reply(f"Debes proporcionar texto después del comando /mensaje. <a href='{footer_banner1}'>&#8203;</a>")
        return
    # Obtiene el mensaje personalizado después del comando
    mensaje_personalizado = message.text.split(maxsplit=1)[1]

    # Envía un mensaje de confirmación al remitente
    mensaje_confirmacion = f"El mensaje se está enviando a todos los usuarios. <a href='{footer_banner1}'>&#8203;</a>"
    await client.send_message(message.chat.id, mensaje_confirmacion)

    # Obtiene los IDs de los usuarios desde la base de datos
    ids_usuarios = await obtener_ids_usuarios()

    # Envía el mensaje personalizado y la imagen a todos los usuarios en paralelo
    tasks = []
    for user_id in ids_usuarios:
        try:
            # Selecciona una imagen aleatoria de la lista de imagen_urls
            imagen_url = random.choice(imagen_urls)
            keyboard = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("REFERENCIAS", url="https://t.me/REFEDARWINSCRAPPER"),
                        InlineKeyboardButton("SCRAPP FREE", url="https://t.me/SCRAPPERFREE"),
                    ],
                    [
                        InlineKeyboardButton("GRUPO OFICIAL", url="https://t.me/CHATKURAMA")
                    ]
                ]
            )
            # Envía la imagen junto con el mensaje personalizado como leyenda
            task = client.send_photo(user_id, imagen_url, caption=f"<b>{mensaje_personalizado}</b>", reply_markup=keyboard)
            tasks.append(task)
        except Exception as e:
            error_msg = f"Error al enviar mensaje a {user_id}: {str(e)} <a href='{footer_banner1}'>&#8203;</a>"
            await client.send_message(message.chat.id, error_msg)

    # Espera a que se completen todas las tareas de envío de mensajes
    await asyncio.gather(*tasks)

    # Muestra un mensaje cuando se ha enviado el mensaje a todos los usuarios
    mensaje_enviado = f"El mensaje se ha enviado a todos los usuarios. <a href='{footer_banner1}'>&#8203;</a>"
    await client.send_message(message.chat.id, mensaje_enviado)
