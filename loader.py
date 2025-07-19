from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from data import config
PROXY_URL = "156.228.95.10:3129"

bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML,proxy=PROXY_URL)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
