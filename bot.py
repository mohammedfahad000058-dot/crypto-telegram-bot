import asyncio
from telegram import Bot

BOT_TOKEN = "8975270571:AAE6cViAggmkHwGBqik-ciTHcg9uer1Dojo"
CHAT_ID = "6569398268"

async def main():
    bot = Bot(token=BOT_TOKEN)
    await bot.send_message(
        chat_id=CHAT_ID,
        text="🚀 Crypto Bot Running\nBTC & ETH monitoring active."
    )

asyncio.run(main())
