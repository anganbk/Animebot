# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01

import re
from os import environ
from Script import script 

id_pattern = re.compile(r'^.\d+$')

# Bot information
SESSION = environ.get('SESSION', 'TechVJBot')
API_ID = int(environ.get('API_ID', '23483999'))
API_HASH = environ.get('API_HASH', 'f7177824ce1cde688f2f9520dfe6339e')
BOT_TOKEN = environ.get('BOT_TOKEN', "8100975548:AAGCztB-QPfx4APvFhL9I2oYmvmuKcGYmhM")

# Start message pictures
PICS = (environ.get('PICS', 'https://graph.org/file/ce1723991756e48c35aa1.jpg')).split()

# Admins & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '7891845883').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '7875649166').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []

# Log & file channels
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002912681437'))
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1002979478084').split()]
REQST_CHANNEL = int(environ.get('REQST_CHANNEL', '-1003083785057'))

# Support & batch
SUPPORT_CHAT_ID = int(environ.get('SUPPORT_CHAT_ID', '-1002905597542'))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '-1002975586815')).split()]

# Auth & force subscribe
AUTH_CHANNEL = int(environ.get('AUTH_CHANNEL', '-1002668132132'))
AUTH_GROUP = int(environ.get('AUTH_GROUP', '-1002978821291'))

# MongoDB
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://ani4angan_db_user:3s2XGT9pY0Ha6tdo@cluster0.pbuuu5s.mongodb.net/?retryWrites=true&w=majority")
DATABASE_NAME = environ.get('DATABASE_NAME', "ani4angan_db_user")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'vjcollection')
MULTIPLE_DATABASE = bool(environ.get('MULTIPLE_DATABASE', False))

O_DB_URI = environ.get('O_DB_URI', "")
F_DB_URI = environ.get('F_DB_URI', "")
S_DB_URI = environ.get('S_DB_URI', "")

# AI & features
AI_SPELL_CHECK = True  # Enabled
PM_SEARCH = bool(environ.get('PM_SEARCH', True))
BUTTON_MODE = bool(environ.get('BUTTON_MODE', True))
MAX_BTN = bool(environ.get('MAX_BTN', True))
AUTO_FFILTER = bool(environ.get('AUTO_FFILTER', True))
AUTO_DELETE = bool(environ.get('AUTO_DELETE', True))
SPELL_CHECK_REPLY = bool(environ.get("SPELL_CHECK_REPLY", True))

# Others
CACHE_TIME = int(environ.get('CACHE_TIME', 1800))
PORT = environ.get("PORT", "8080")
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", f"{script.CAPTION}")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)
LONG_IMDB_DESCRIPTION = bool(environ.get("LONG_IMDB_DESCRIPTION", False))
PROTECT_CONTENT = bool(environ.get('PROTECT_CONTENT', False))
PUBLIC_FILE_STORE = bool(environ.get('PUBLIC_FILE_STORE', True))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', True))

# Links
GRP_LNK = environ.get('GRP_LNK', 'https://t.me/animegp4')
CHNL_LNK = environ.get('CHNL_LNK', 'https://t.me/animegp1')
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'botsupporthd')
OWNER_LNK = environ.get('OWNER_LNK', 'https://t.me/anganbk4')

# Clone mode
CLONE_MODE = bool(environ.get('CLONE_MODE', False))
CLONE_DATABASE_URI = environ.get('CLONE_DATABASE_URI', "")
PUBLIC_FILE_CHANNEL = environ.get('PUBLIC_FILE_CHANNEL', '')

# Online streaming
STREAM_MODE = bool(environ.get('STREAM_MODE', True))
MULTI_CLIENT = False
SLEEP_THRESHOLD = int(environ.get('SLEEP_THRESHOLD', '60'))
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))
URL = environ.get("URL", "https://testofvjfilter-1fa60b1b8498.herokuapp.com/")

# Rename & auto approve
RENAME_MODE = bool(environ.get('RENAME_MODE', False))
AUTO_APPROVE_MODE = bool(environ.get('AUTO_APPROVE_MODE', False))

# Start command reactions
REACTIONS = ["🤝", "😇", "🤗", "😍", "👍", "🎅", "😐", "🥰", "🤩", "😱", "🤣", "😘", "👏", "😛", "😈", "🎉", "⚡️", "🫡", "🤓", "😎", "🏆", "🔥", "🤭", "🌚", "🆒", "👻", "😁"]

# Database URIs
if MULTIPLE_DATABASE == False:
    USER_DB_URI = DATABASE_URI
    OTHER_DB_URI = DATABASE_URI
    FILE_DB_URI = DATABASE_URI
    SEC_FILE_DB_URI = DATABASE_URI
else:
    USER_DB_URI = DATABASE_URI
    OTHER_DB_URI = O_DB_URI
    FILE_DB_URI = F_DB_URI
    SEC_FILE_DB_URI = S_DB_URI

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01

