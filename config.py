import os

class Config:
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5984042222:AAFOM33lTp7WlKYynROqslNJJV6ZWo6nc5I
")
    API_ID = int(os.environ.get("API_ID", "26712413"))
    API_HASH = os.environ.get("API_HASH", "3298034eb7cec614ef852fda02536153")
    BOT_OWNER = os.environ.get("BOT_OWNER", "nesirovqadirofficiall")
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "QadirSongBot")
    PLAYLIST_NAME = os.environ.get("PLAYLIST_NAME", "https://t.me/darksideplay")
    CHANNEL = os.environ.get("CHANNEL", "darksideplay")
    PLAYLIST_ID = int(os.environ.get("PLAYLIST_ID", "-1001719261837"))
