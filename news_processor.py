from models import NewsData


KEYWORDS = {
    "日本株": [
        "nikkei",
        "japan",
        "tokyo",
        "topix",
        "boj"
    ],
    "米国株": [
        "dow",
        "nasdaq",
        "s&p",
        "wall street",
        "stocks",
        "equity"
    ],
    "為替": [
        "yen",
        "dollar",
        "currency",
        "forex",
        "usd",
        "jpy",
        "eur"
    ],
    "金利": [
        "bond",
        "treasury",
        "yield",
        "interest rate",
        "fed"
    ],
    "半導体": [
        "nvidia",
        "tsmc",
        "semiconductor",
        "chip"
    ]
}


def categorize_news(news_list: list[NewsData]) -> dict[str, list[NewsData]]:
    """
    ニュースをテーマごとに分類
    """

    categorized = {
        category: []
        for category in KEYWORDS
    }

    for news in news_list:

        text = (
            news.headline +
            " " +
            news.summary
        ).lower()

        for category, keywords in KEYWORDS.items():

            if any(keyword in text for keyword in keywords):

                categorized[category].append(news)

    return categorized


def remove_duplicate_news(news_list: list[NewsData]) -> list[NewsData]:
    """
    重複ニュース削除
    """

    seen = set()

    result = []

    for news in news_list:

        if news.headline not in seen:

            seen.add(news.headline)

            result.append(news)

    return result