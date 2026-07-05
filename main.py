from database import create_table, save_market_data
from stock import get_market_data
from news import get_market_news
from news_processor import (
    categorize_news,
    remove_duplicate_news
)
from prompt_builder import build_prompt
from ai import generate_summary
from discord_notify import send_message

def main():

    print("===== 本日のマーケット =====\n")

    # テーブル作成
    create_table()

    # マーケットデータ取得
    market_data = get_market_data()

    # SQLiteへ保存
    save_market_data(market_data)

    print("マーケットデータをSQLiteへ保存しました。\n")

    # ニュース取得
    print("ニュース取得中...")
    news_list = get_market_news(limit=30)

    # 重複ニュース削除
    news_list = remove_duplicate_news(news_list)

    print(f"取得ニュース数：{len(news_list)}件")

    # ニュース分類
    categorized_news = categorize_news(news_list)

    # AIへ渡すプロンプト作成
    prompt = build_prompt(
        market_data,
        categorized_news
    )

    print("Geminiで要約中...\n")

    # Gemini要約
    summary = generate_summary(prompt)

    print("=" * 60)
    print("📈 AIマーケットサマリー")
    print("=" * 60)
    print(summary)

    # Discordへ送信
    send_message(summary)


if __name__ == "__main__":
    main()