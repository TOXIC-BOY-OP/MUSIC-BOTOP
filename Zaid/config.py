##Config
import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")


load_dotenv()
SESSION_NAME = getenv('SESSION_NAME', 'session')
BOT_TOKEN = getenv('BOT_TOKEN')
API_ID = int(getenv("API_ID", "25374274"))
API_HASH = getenv('API_HASH')
DURATION_LIMIT = int(getenv('DURATION_LIMIT', '540000'))
COMMAND_PREFIXES = list(getenv('COMMAND_PREFIXES', '/ !').split())
MONGO_DB_URI = getenv("MONGO_DB_URI")
SUDO_USERS = list(map(int, getenv('SUDO_USERS', '1939017724').split()))
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", '-1001903332290'))
ASS_ID = int(getenv("ASS_ID"))
OWNER_ID = list(map(int, getenv('OWNER_ID', '6109531260').split()))
RESULT_PIC = getenv('RESULT_PIC', "https://graph.org/file/db0705d103a75a09597be.jpg")
PLAYLIST_PIC = getenv('PLAYLIST_PIC', "https://graph.org/file/db0705d103a75a09597be.jpg")
PING_IMG = getenv('PING_IMG', "https://graph.org/file/db0705d103a75a09597be.jpg")
AUTO_LEAVE_TIME = int(getenv("AUTO_LEAVE_ASSISTANT_TIME", "5400"))
AUTO_LEAVE = getenv('AUTO_LEAVING_ASSISTANT', None)
