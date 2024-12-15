from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from Plugins.Func import connect_to_db
from datetime import datetime


footer_banner1 = 'https://imgur.com/ihpUqrG.jpg'

keyboard2 = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("KURAMACHK ⚡️", url="https://t.me/KURAMACHK_BOT")
                ]
            ]
        )

def calculate_remaining_days(fecha_registro, dias):
    # Obtener el tiempo actual en formato de timestamp
    current_time = datetime.now().timestamp()

    # Calcular el tiempo restante en segundos
    remaining_seconds = (fecha_registro + (dias * 24 * 60 * 60)) - current_time

    # Convierte los segundos restantes a días
    remaining_days = remaining_seconds / (24 * 60 * 60)
    return remaining_days


# Define el filtro para el comando /start
@Client.on_message(filters.command(["me", "plan", "id", "perfil"], prefixes=['.','/','!','?'], case_sensitive=False) & filters.text)
def perfil_command(client, message):
    # Extract user informat    # Connect to the SQLite database
    conn = connect_to_db()
    cursor = conn.cursor()

    user_id = message.from_user.id
         
    # Query the database for the user's status
    cursor.execute('SELECT rango, creditos, antispam, dias, fecha_registro FROM users WHERE user_id = ?', (user_id,))
    user_data = cursor.fetchone()
    
    if user_data:
            rank = user_data[0]
    else:
            rank = "Free"
    
    if not user_data:
     return message.reply(f"No estás registrado. Por favor, utiliza /register para registrarte. <a href='{footer_banner1}'>&#8203;</a>", reply_markup=keyboard2)

    # Obtener la fecha de vencimiento del plan del usuario (suponiendo que sea una cadena con formato YYYY-MM-DD)
    dias = str(user_data[3])
    fecha_registro = str(user_data[4])

    dias = int(dias)
    fecha_registro = float(fecha_registro)
    remaining_days = calculate_remaining_days(fecha_registro, dias)
    remaining_days_int = int(remaining_days)

    if remaining_days_int <= 0:
        remaining_days_int = 0


    chat_id = message.chat.id
    username = message.from_user.username
        # Envía un video con un subtítulo (caption)
    video_path = "https://imgur.com/jfRGk6l.mp4"  # Reemplaza con la ruta de tu video  # noqa: E501
        
    caption = f"""<a href='https://imgur.com/ihpUqrG.jpg'>&#8203;</a> 
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
━━━━━━━━━━━━━    """
        # Crear los botones con URL
    keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("𝑲𝒖𝒓𝒂𝒎𝒂𝑪𝒉𝒌⚡️", url="https://t.me/RefeDarwinScrapper"),
                ]
            ]
        )
    client.send_video(message.chat.id, video_path, caption=caption, reply_markup=keyboard)  # noqa: E501
