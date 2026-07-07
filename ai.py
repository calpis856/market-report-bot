from google import genai
from google.genai.errors import ServerError
import time

from config import GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)


def generate_summary(prompt: str) -> str:
    """
    Geminiでマーケットニュースを要約する
    503エラーが発生した場合は最大5回までリトライする
    """

    max_retries = 5

    for attempt in range(max_retries):
        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt,
            )

            return response.text

        except ServerError as e:
            # 503エラーのみリトライ
            if getattr(e, "status_code", None) == 503:

                if attempt == max_retries - 1:
                    raise

                wait_time = (attempt + 1) * 10

                print(
                    f"Geminiが高負荷です。"
                    f"{wait_time}秒後に再試行します..."
                )

                time.sleep(wait_time)

            else:
                raise