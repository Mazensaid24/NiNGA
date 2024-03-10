from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/b35fd1dfca73b950b1b05.jpg")
START_IMG = getenv("START_IMG", "https://te.legra.ph/file/bb0ff85f2dd44070ea519.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/miika3")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/Fv_av")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5951674553").split()))


FAILED = "https://telegra.ph/file/7d520e2c7d16a566d9bae.jpg"
"
