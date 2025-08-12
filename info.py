import re
from os import environ

id_pattern = re.compile(r'^.\d+$')

# Bot information
SESSION = environ.get('SESSION', 'StarkMV')
API_ID = int(environ.get('API_ID', '7272529'))
API_HASH = environ.get('API_HASH', '68532ee254128bd6f169a1b32bde7db5')
BOT_TOKEN = environ.get('BOT_TOKEN', "8343203958:AAGxi7TqaDgBNb1aXE6R0xlUW5gt4oWNfn0")

# Bot settings
PORT = environ.get("PORT", "8080")

# Online Stream and Download
MULTI_CLIENT = False
SLEEP_THRESHOLD = int(environ.get('SLEEP_THRESHOLD', '60'))
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
if 'DYNO' in environ:
    ON_HEROKU = True
else:
    ON_HEROKU = False
URL = environ.get("URL", "")

# Admins, Channels & Users
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002793223546'))
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '700871056').split()]

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://rockdmbiot:81Yyppfch4dRjgcY@cluster0.z2tuvdu.mongodb.net/?retryWrites=true&w=majority")
DATABASE_NAME = environ.get('DATABASE_NAME', "StarkMV")

# Shortlink Info
SHORTLINK = bool(environ.get('SHORTLINK', True)) # Set True Or False
SHORTLINK_URL = environ.get('SHORTLINK_URL', 'arolinks.com')
SHORTLINK_API = environ.get('SHORTLINK_API', 'fd5cf33a2e9e4740aa1c3dea099145fe29ec9d1f')
