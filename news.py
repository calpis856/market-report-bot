import requests

from config import FINNHUB_API_KEY
from models import NewsData

BASE_URL = "https://finnhub.io/api/v1/news"


def get_market_news(limit: int = 30) -> list[NewsData]:
    """
    Finnhubからマーケットニュースを取得する

    Args:
        limit (int): 取得件数

    Returns:
        list[NewsData]
    """

    params = {
        "category": "general",
        "token": FINNHUB_API_KEY
    }

    try:

        response = requests.get(
            BASE_URL,
            params=params,
            timeout=10
        )

        response.raise_for_status()

    except requests.RequestException as e:

        print(f"ニュース取得エラー: {e}")
        return []

    news_json = response.json()

    news_list = []

    for item in news_json[:limit]:

        news = NewsData(
            source=item.get("source", ""),
            headline=item.get("headline", ""),
            summary=item.get("summary", ""),
            url=item.get("url", ""),
            datetime=item.get("datetime", 0)
        )

        news_list.append(news)

    return news_list