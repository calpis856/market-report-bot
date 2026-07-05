from models import MarketData, NewsData


def build_prompt(
    market_data: list[MarketData],
    categorized_news: dict[str, list[NewsData]]
) -> str:
    """
    Geminiへ送信するプロンプトを作成する
    """

    prompt = """
あなたはプロの証券アナリストです。

以下のマーケットデータとニュースを参考に、
本日のマーケットを日本語で分析してください。

====================================
【マーケットデータ】
====================================

"""

    # 株価データ
    for market in market_data:

        prompt += (
            f"{market.name}\n"
            f"終値：{market.close}\n"
            f"前日比：{market.change} ({market.change_rate}%)\n\n"
        )

    prompt += """
====================================
【マーケットニュース】
====================================

"""

    # カテゴリごとのニュース
    for category, news_items in categorized_news.items():

        if not news_items:
            continue

        prompt += f"\n【{category}】\n\n"

        for news in news_items:

            prompt += (
                f"タイトル：{news.headline}\n"
                f"概要：{news.summary}\n"
                f"配信元：{news.source}\n\n"
            )

    prompt += """
====================================
【出力条件】
====================================

以下の形式で日本語でまとめてください。

■ 日経平均
・上昇・下落要因を2～3点

■ S&P500
・上昇・下落要因を2～3点

■ NYダウ
・上昇・下落要因を2～3点

■ NASDAQ
・上昇・下落要因を2～3点

■ ドル円
・変動要因を2点

■ ユーロドル
・変動要因を2点

■ 米10年国債利回り
・変動要因を2点

■ 本日の重要ニュース
・特に重要なニュースを3点

■ 明日以降の注目ポイント
・注目イベントを3点

条件
・ニュースに書かれていない内容は推測しないこと
・日本語で分かりやすく書くこと
・箇条書きで簡潔にまとめること
・専門用語は必要最低限にすること
"""

    return prompt