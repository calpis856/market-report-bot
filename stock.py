import yfinance as yf

from config import TICKERS
from models import MarketData


def get_market_data():

    market_data = []

    for name, symbol in TICKERS.items():

        try:

            ticker = yf.Ticker(symbol)

            hist = ticker.history(period="2d")

            if len(hist) < 2:
                print(f"{name}: データ不足")
                continue

            latest = hist.iloc[-1]
            previous = hist.iloc[-2]

            close = float(latest["Close"])
            previous_close = float(previous["Close"])

            # 米10年国債利回り補正
            if symbol == "^TNX":
                close /= 10
                previous_close /= 10

            change = close - previous_close
            change_rate = (change / previous_close) * 100

            market = MarketData(
                name=name,
                close=round(close, 2),
                change=round(change, 2),
                change_rate=round(change_rate, 2)
            )

            market_data.append(market)

        except Exception as e:
            print(f"{name}: {e}")

    return market_data