from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from Plugins.Func import connect_to_db
from pyrogram.types import Message



# Define el filtro para el comando /totals
@Client.on_message(filters.command("global", prefixes=['.','/','!','?'], case_sensitive=False) & filters.text)
def get_totals(client: Client, message: Message):
    conn = connect_to_db()
    cursor = conn.cursor()
    user_id = message.from_user.id
    cursor.execute('SELECT rango, creditos, antispam, dias FROM users WHERE user_id = ?', (user_id,))
    user_data = cursor.fetchone()
          
    if user_data[0] not in ["Seller", "Owner"]:
                return message.reply(f"<b>El chat no está autorizado para usar este comando. ❌</b>")
            

    # Si el usuario es un administrador, obtiene los totales y los envía
    user_query = "SELECT COUNT(*) FROM users"


    # Contar usuarios con diferentes rangos (normalizados a minúsculas)
    owner_count_query = "SELECT COUNT(*) FROM users WHERE LOWER(rango) = 'owner'"
    seller_count_query = "SELECT COUNT(*) FROM users WHERE LOWER(rango) = 'seller'"
    premium_count_query = "SELECT COUNT(*) FROM users WHERE LOWER(rango) = 'premium'"
    grupo_count_query = "SELECT COUNT(*) FROM users WHERE LOWER(rango) = 'grupo'"
    free_user_count_query = "SELECT COUNT(*) FROM users WHERE LOWER(rango) = 'free'"
    staff_count_query = "SELECT COUNT(*) FROM users WHERE LOWER(rango) = 'staff'"

    cursor.execute(user_query)
    user_count = cursor.fetchone()[0]

    cursor.execute(owner_count_query)
    owner_count = cursor.fetchone()[0]

    cursor.execute(seller_count_query)
    seller_count = cursor.fetchone()[0]

    cursor.execute(premium_count_query)
    premium_count = cursor.fetchone()[0]

    cursor.execute(grupo_count_query)
    grupo_count = cursor.fetchone()[0]

    cursor.execute(staff_count_query)
    staff_count = cursor.fetchone()[0]

    cursor.execute(free_user_count_query)
    free_user_count = cursor.fetchone()[0]


    message.reply_text(f"""<a href='https://imgur.com/ihpUqrG.jpg'>&#8203;</a> 
[<a href="https://t.me/RefeDarwinScrapper">✯</a>] ONWERS: {owner_count}
[<a href="https://t.me/RefeDarwinScrapper">✯</a>] SELLERS {seller_count}
[<a href="https://t.me/RefeDarwinScrapper">✯</a>] PREMIUM USERS: {premium_count}
[<a href="https://t.me/RefeDarwinScrapper">✯</a>] FREE USERS: {free_user_count}
[<a href="https://t.me/RefeDarwinScrapper">✯</a>] STAFFS: {staff_count}
[<a href="https://t.me/RefeDarwinScrapper">✯</a>] GRUPOS: {grupo_count}
[<a href="https://t.me/RefeDarwinScrapper">✯</a>] TOTAL USERS AND GROUPS: {user_count}
""")  
