from pyrogram import Client, filters
from Plugins.Func import connect_to_db
import random
import requests
import time

@Client.on_message(filters.command("extra", ["/", "."]))
async def generate_extra(client, message):
    tiempoinicio = time.perf_counter()

    user_id = message.from_user.id
    
   
    inputm = message.text.split(None, 1)
    if len(inputm) != 2 or not inputm[1]:
        # Si el argumento está vacío o no se proporciona, mostrar el formato esperado
        message_text = "<b>⚠️ Uso incorrecto. Usa /extra seguido de los primeros 6 dígitos del BIN.</b>"
        await message.reply_text(
            text=message_text,
        )
        return

    BIN = inputm[1][:6]
    req = requests.get(f"https://bins.antipublic.cc/bins/{BIN}").json()

    try:
        brand = req['brand']
        country = req['country']
        country_name = req['country_name']
        country_flag = req['country_flag']
        country_currencies = req['country_currencies']
        bank = req['bank']
        level = req['level']
        typea = req['type']
    except KeyError:
        message_text = "Lo siento, el BIN no está en mi base de datos."
        await message.reply_text(
            text=message_text
        )
        return

    
    extrapole_results = []
    for _ in range(28):
        random_digits = "".join(random.choice("0123456789") for _ in range(6))
        random_month = random.randint(1, 12)
        random_year = random.randint(2024, 2030)
        extra = f"{BIN}{random_digits}xxxx|{random_month:02d}|{random_year}"
        extrapole_results.append(f"<code>{BIN}{random_digits}xxxx|{random_month:02d}|{random_year}</code>")

    similar_bins = [f"<code>{BIN}{random.choice('0123456789')}{random.choice('0123456789')}{random.choice('0123456789')}{random.choice('0123456789')}</code>" for _ in range(2)]

    tiempofinal = time.perf_counter()

    formatted_results = ""
    for result in extrapole_results:
        formatted_results += f"[<a href='https://t.me/RefeDarwinScrapper'>✯</a>] {result}\n"
    
    message_text = f"""
{formatted_results}━━━━━━━━━━━━
[<a href="https://t.me/RefeDarwinScrapper">✯</a>] TIME: {tiempofinal - tiempoinicio:.2f} segundos
[<a href="https://t.me/RefeDarwinScrapper">✯</a>] CHK BY: @{message.from_user.username} </b>
[<a href="https://t.me/RefeDarwinScrapper">✯</a>] BOT BY: @Crypto_locker5
"""

    await message.reply_text(
        text=message_text,  disable_web_page_preview=True
    )





