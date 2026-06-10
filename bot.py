from telegram import Bot
import time

BOT_TOKEN = "8975270571:AAE6cViAggmkHwGBqik-ciTHcg9uer1Dojo"
CHAT_ID = "6569398268"

bot = Bot(token=BOT_TOKEN)

while True:
    try:
        bot.send_message(
            chat_id=CHAT_ID,
            text="🚀 Crypto Bot Running\nBTC & ETH monitoring active."
        )
        time.sleep(3600)  # every hour
    except Exception as e:
        print(e)
        time.sleep(60)
This I have enterd
