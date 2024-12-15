import requests 
from pyrogram import Client, filters
from pyrogram.types import Message
import iso3166


from Plugins.Func import connect_to_db
@Client.on_message(filters.command(["rand", "fake", "rnd"], prefixes=['.', '/', '!', '?'], case_sensitive=False) & filters.text)
async def cmds(client, message):
      user_id = message.from_user.id
      user_id = message.from_user.id
      conn = connect_to_db()
      cursor = conn.cursor()
      cursor.execute('SELECT rango, creditos, antispam, dias FROM users WHERE user_id = ?', (user_id,))
      user_data = cursor.fetchone()
      if not user_data:
                        return await message.reply(f"<b>You are not registered. Please use /register to sign up.</b> <a href='https://imgur.com/ihpUqrG.jpg'>&#8203;</a>")
      

      if user_data[0] in ["Baneado", "baneado"]:
            return await message.reply(f"<b>You are not allowed to use the bot.❌\nReason: Baneado. </b>")
            
      username = message.from_user.username

      try:
            country = message.text.split()[1]
      except IndexError:
            await message.reply("<b>Error, ejemplo: /rand  <code>MX - CA - ES - US - FR - UK</code></b>")
            return
         
         # Verificar si el código de país es válido
      if country.upper() not in iso3166.countries_by_alpha2:
            await message.reply(f"<b>El código de país '{country}' no es válido. Introduce un código de país válido, ejemplo: /rand us</b>")
            return

      api = requests.get(f"https://randomuser.me/api/?nat={country}&inc=name,location,phone&exc=location.city").json()

      nombre = api["results"][0]["name"]["first"]
      last = api["results"][0]["name"]["last"]
      loca = api["results"][0]["location"]["street"]["name"]
      nm = api["results"][0]["location"]["street"]["number"]
      city = api["results"][0]["location"]["city"]
      state = api["results"][0]["location"]["state"]
      country = api["results"][0]["location"]["country"]
      postcode = api["results"][0]["location"]["postcode"]
      phone = api["results"][0]["phone"]
      ID = message.from_user.id
      first = message.from_user.first_name
         
      username = message.from_user.username
      
      await message.reply(f"""             
[<a href="https://t.me/RefeDarwinScrapper">✯</a>] FAKE RANDOM ADDRESS
━━━━━━━━━━━━
[<a href="https://t.me/RefeDarwinScrapper">✯</a>] NAME: <code>{nombre} {last}</code>
[<a href="https://t.me/RefeDarwinScrapper">✯</a>] STREET: <code>{loca} {nm}</code>                               
━━━━━━━━━━━━
[<a href="https://t.me/RefeDarwinScrapper">✯</a>] CITY: <code>{city}</code>
[<a href="https://t.me/RefeDarwinScrapper">✯</a>] STATE: <code>{state}</code>
[<a href="https://t.me/RefeDarwinScrapper">✯</a>] COUNTRY: <code>{country}</code>
[<a href="https://t.me/RefeDarwinScrapper">✯</a>] ZIP CODE: <code>{postcode}</code>
[<a href="https://t.me/RefeDarwinScrapper">✯</a>] PHONE NUMBER <code>{phone}</code>
━━━━━━━━━━━━
[<a href="https://t.me/RefeDarwinScrapper">✯</a>] CHK BY: @{message.from_user.username} [{user_data[0]}] </b>
[<a href="https://t.me/RefeDarwinScrapper">✯</a>] OWNER BOT: @Crypto_locker5                      
""", disable_web_page_preview=True)     