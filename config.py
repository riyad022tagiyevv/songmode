import os

class Config:
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5585571839:AAGvJSFxBCAeOqeaxO9XR7hvzIq3wzFRN-E")
    API_ID = int(os.environ.get("API_ID", "19485442"))
    API_HASH = os.environ.get("API_HASH", "a03fcb372b3ec4e406b5d52f84b02e53")
    BOT_OWNER = os.environ.get("BOT_OWNER", "Rahid_7")
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Rahid_MusicBot")
    PLAYLIST_NAME = os.environ.get("PLAYLIST_NAME", "RahidMusic")
    CHANNEL = os.environ.get("CHANNEL", "Rahid_44")
    PLAYLIST_ID = int(os.environ.get("PLAYLIST_ID", "-1001750384884"))
