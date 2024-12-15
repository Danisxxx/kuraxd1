#----- LIBRERIAS------#
import os
import logging
from pyrogram import Client
from dotenv import load_dotenv
import asyncio
from Plugins.Func import connect_to_db
from datetime import datetime

async def calculate_remaining_days(fecha_registro, dias):
    current_time = datetime.now().timestamp()

    remaining_seconds = (fecha_registro + (dias * 24 * 60 * 60)) - current_time

    remaining_days = remaining_seconds / (24 * 60 * 60)
    return remaining_days


#---CLIENTE----#
config = load_dotenv(".env")
KuramaChk = Client(
    "KuramaChk",
    api_id = os.getenv('API_ID'),
    api_hash = os.getenv('API_HASH'),
    bot_token = os.getenv('BOT_TOKEN'),  # Asegúrate de que BOT_TOKEN en tu .env es actualizado
    plugins = dict(root = 'Plugins')
)

@KuramaChk.on_callback_query()
def callback_privates(client, callback_query):
        reply_message = callback_query.message.reply_to_message
        if reply_message is not None and reply_message.from_user is not None:
            if reply_message.from_user.id != callback_query.from_user.id:
                callback_query.answer("Abre tu propio Menú ⚠️")
                return 
       
        callback_query.continue_propagation()
        
async def main():
    await KuramaChk.start()
    

    
    await send_periodic_message(KuramaChk)
    
    
async def send_periodic_message(client):
    while True:
        conn = connect_to_db()
        cursor = conn.cursor()
        cursor.execute("SELECT user_id, rango, fecha_registro, dias FROM users")
        users_data = cursor.fetchall()
        
        for user_id, rango, fecha_registro, dias in users_data:
            if dias is None:
                pass
            elif fecha_registro is None:
                pass
            else:
                dias = int(dias)
                fecha_registro = float(fecha_registro)
                remaining_days = await calculate_remaining_days(fecha_registro, dias)
                remaining_days_int = int(remaining_days)

            try:
                if remaining_days <= 0:
                    pass
                            
                elif remaining_days <= 4:
                    await client.send_message(user_id, f"<b>⚠️ Attention, your subscription to Kurama Chk is about to expire, you have {remaining_days_int} days left. To renew your membership, contact @Crypto_locker5 | @AstraxOficial. ⚠️</b>")
            except:
                print('usuario no valido')
        
        
    
        await asyncio.sleep(36000)
        
        
logging.basicConfig(level=logging.INFO)
KuramaChk.run(main())



    