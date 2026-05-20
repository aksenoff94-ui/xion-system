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

# Add error handling
if response.status_code != 200:
    print(f"API Error: {response.status_code}")
    print(response.json())
    exit(1)

response_data = response.json()
if "choices" not in response_data or not response_data["choices"]:
    print(f"Unexpected API response: {response_data}")
    exit(1)

post_text = response_data["choices"][0]["message"]["content"]

telegram_url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"

telegram_data = {
    "chat_id": TELEGRAM_CHAT_ID,
    "text": post_text
}

requests.post(telegram_url, data=telegram_data)

print("Post published.")
