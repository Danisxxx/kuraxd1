import time
from pyrogram import Client, filters
from pyrogram.types import Message
from func_bin import get_bin_info
from Plugins.Func import connect_to_db

#------COMANDO BIN--------#
@Client.on_message(filters.command("bin", prefixes=['.','/','!'], case_sensitive=False) & filters.text)
def bin_handler(client, message):
    user_id = message.from_user.id
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute('SELECT rango, creditos, antispam, dias FROM users WHERE user_id = ?', (user_id,))
    user_data = cursor.fetchone()
    if not user_data:
                  return message.reply(f"<b>You are not registered. Please use /register to sign up.</b> <a href='https://imgur.com/ihpUqrG.jpg'>&#8203;</a>")
    

    if user_data[0] in ["Baneado", "baneado"]:
        return message.reply(f"<b>You are not allowed to use the bot.❌\nReason: Baneado. </b>")
    BIN = message.text[len("/bin"):11].strip()
    
    if len(BIN) < 6:
        message.reply("BIN INCORRECTO FORMATO DE BIN 6 DIGITOS /bin 455664")
        return
        
    if not BIN:
        message.reply("HERRAMIENTA BIN INFO, USE /bin 4556747")
        return
    
    func = get_bin_info(BIN[:6])
    
    message.reply(f"""<b>
[<a href="https://t.me/RefeDarwinScrapper">✯</a>] BIN INFO           
━━━━━━━━━━━━━━
[<a href="https://t.me/RefeDarwinScrapper">✯</a>] BIN: {BIN[:6]} 
[<a href="https://t.me/RefeDarwinScrapper">✯</a>] COUNTRY: {func.get("country")} {func.get("flag")}   
[<a href="https://t.me/RefeDarwinScrapper">✯</a>] TYPE:  {func.get("type")}          
[<a href="https://t.me/RefeDarwinScrapper">✯</a>] LEVEL: {func.get("level")}  
[<a href="https://t.me/RefeDarwinScrapper">✯</a>] VENDOR: {func.get("vendor")}  
[<a href="https://t.me/RefeDarwinScrapper">✯</a>] BANK: {func.get("bank")}  </b> 
━━━━━━━━━━━━━━
[<a href="https://t.me/RefeDarwinScrapper">✯</a>] CHK BY: @{message.from_user.username} [{user_data[0]}] </b>
[<a href="https://t.me/RefeDarwinScrapper">✯</a>] BOT BY: @luisabinader1""",  disable_web_page_preview=True)