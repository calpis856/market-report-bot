from dataclasses import dataclass


@dataclass
class MarketData:
    """
    マーケットデータ
    """
    name: str
    close: float
    change: float
    change_rate: float


@dataclass
class NewsData:
    """
    ニュースデータ
    """
    source: str
    headline: str
    summary: str
    url: str
    datetime: int