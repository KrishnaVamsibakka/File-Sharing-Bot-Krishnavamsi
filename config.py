import os
import logging
from logging.handlers import RotatingFileHandler




BOT_TOKEN = os.environ.get("BOT_TOKEN", "7795414140:AAHPYxU-Yc7AJ3KcR-zWZmqFOYd4C_mNItQ")
API_ID = int(os.environ.get("API_ID", "29055333"))
API_HASH = os.environ.get("API_HASH", "a6d154242eaef80a163bf5d0a7763882")


OWNER_ID = int(os.environ.get("OWNER_ID", "6828129421"))
DB_URL = os.environ.get("DB_URL", "mongodb+srv://anjireddyb885:MvL27Den1lu7TURr@cluster0.al34wge.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DB_NAME", "Cluster0")


CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002526508320"))
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1002024495069"))


FILE_AUTO_DELETE = int(os.getenv("FILE_AUTO_DELETE", "1800")) # auto delete in seconds


PORT = os.environ.get("PORT", "8080")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))



try:
    ADMINS=[6828129421]
    for x in (os.environ.get("ADMINS", "6828129421").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")









CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

DISABLE_CHANNEL_BUTTON = True if os.environ.get('DISABLE_CHANNEL_BUTTON', "True") == "True" else False

BOT_STATS_TEXT = "<b>BOT UPTIME :</b>\n{uptime}"







USER_REPLY_TEXT = "❌Don't Send Me Messages Directly I'm Only store files of 𝐕𝐚𝐦𝐬𝐢 🐦‍🔥 !"

START_MSG = os.environ.get("START_MESSAGE", "Hello {mention}\n\nI am File Store bot Created by 𝐕𝐚𝐦𝐬𝐢 🐦‍🔥 and he can only use me.")

FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {mention}\n\n<b>You Need To Join In My Channel/Group To Use Me\n\nKindly Please Join Channel</b>")





ADMINS.append(OWNER_ID)
ADMINS.append(6828129421)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
   





# Telegram Channel @Cartooworldtelugu_india
# Backup Channel @Cartoonworldtelugu_india
# Developer @Vamsi_2008_Vamsi
