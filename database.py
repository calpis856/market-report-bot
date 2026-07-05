import sqlite3
from datetime import date

from models import MarketData


DB_NAME = "market.db"


def create_table():
    """
    テーブルを作成
    """

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS market_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            name TEXT NOT NULL,
            close REAL NOT NULL,
            change REAL NOT NULL,
            change_rate REAL NOT NULL,
            UNIQUE(date, name)
        )
    """)

    conn.commit()
    conn.close()


def save_market_data(data: list[MarketData]):
    """
    マーケットデータ保存
    """

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    today = date.today().isoformat()

    for market in data:

        cursor.execute("""
            INSERT OR REPLACE INTO market_data
            (date, name, close, change, change_rate)
            VALUES (?, ?, ?, ?, ?)
        """, (
            today,
            market.name,
            market.close,
            market.change,
            market.change_rate
        ))

    conn.commit()
    conn.close()