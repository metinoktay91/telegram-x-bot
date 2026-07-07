import os

# Telegram
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

# X API
TWITTER_API_KEY = os.getenv("TWITTER_API_KEY")
TWITTER_API_SECRET = os.getenv("TWITTER_API_SECRET")
TWITTER_ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
TWITTER_ACCESS_SECRET = os.getenv("TWITTER_ACCESS_SECRET")
TWITTER_BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")

# Takip edilecek hesaplar
ACCOUNTS = [
    "CryptoHayes",
    "AshCrypto",
    "CryptoWizardd",
    "CryptoTony__",
    "RAFAELA_RIGO_",
    "LLuciano_BTC",
    "cryptoknight890",
    "TheOneLanceB"
]

# Kontrol aralığı (saniye)
CHECK_INTERVAL = 60
