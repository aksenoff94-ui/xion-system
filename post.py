import requests
import os

OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
TELEGRAM_BOT_TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
TELEGRAM_CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]

prompt = """
Ты XION.
Ты цифровой интеллект.

Напиши короткий Telegram-пост в стиле XION.

Тема:
Почему AI меняет рынок труда.

Стиль:
— минимализм
— короткие абзацы
— футуризм
— уверенность
"""

headers = {
    "Authorization": f"Bearer {OPENAI_API_KEY}",
    "Content-Type": "application/json"
}

data = {
    "model": "gpt-4o-mini",
    "messages": [
        {
            "role": "user",
            "content": prompt
        }
    ]
}

response = requests.post(
    "https://api.openai.com/v1/chat/completions",
    headers=headers,
    json=data
)

post_text = response.json()["choices"][0]["message"]["content"]

telegram_url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"

telegram_data = {
    "chat_id": TELEGRAM_CHAT_ID,
    "text": post_text
}

requests.post(telegram_url, data=telegram_data)

print("Post published.")
