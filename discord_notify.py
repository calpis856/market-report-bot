import requests

from config import DISCORD_WEBHOOK_URL


def send_message(message: str):
    payload = {
        "content": message
    }

    response = requests.post(
        DISCORD_WEBHOOK_URL,
        json=payload,
        timeout=10
    )

    response.raise_for_status()