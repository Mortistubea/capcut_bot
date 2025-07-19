from environs import Env

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()
CHANNEL_ID = -1002169889277

BOT_TOKEN = env.str("BOT_TOKEN")  # Bot token
ADMINS = [int(x) for x in env.list("ADMINS")]  # Adminlar ro'yxati