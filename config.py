import os

class Config:
    API_ID = int(os.getenv("API_ID", 22743513))
    API_HASH = os.getenv("API_HASH", '38f450dee835a7668fbaec9655ebcca8')
    BOT_TOKEN = os.getenv("BOT_TOKEN", '5821666908:AAFejt4DmCJJt8xR9TmYU00W5tFg7OKjSVI')
