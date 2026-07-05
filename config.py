import os
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

TICKERS = {
    "日経平均": "^N225",
    "S&P500": "^GSPC",
    "NYダウ": "^DJI",
    "NASDAQ": "^IXIC",
    "ドル円": "JPY=X",
    "ユーロドル": "EURUSD=X",
    "米10年国債利回り": "^TNX",
}

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
FINNHUB_API_KEY = os.getenv("FINNHUB_API_KEY")
DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")