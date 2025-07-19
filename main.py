import asyncio
from aiogram import Bot
from data.config import BOT_TOKEN

async def get_channel_id(username: str):
    async with Bot(token=BOT_TOKEN) as bot:
        try:
            chat = await bot.get_chat(f"@{username}")
            return chat.id
        except Exception as e:
            print(f"Error: {e}")
            return None

async def main():
    username = "uz_capcut_shablon"
    channel_id = await get_channel_id(username)
    if channel_id:
        print(f"Channel ID: {channel_id}")

asyncio.run(main())
