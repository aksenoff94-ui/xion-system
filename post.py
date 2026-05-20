import requests
import os

GROQ_API_KEY = os.environ["GROQ_API_KEY"]
TELEGRAM_BOT_TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
TELEGRAM_CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]

prompt = """
Ты XION.

Ты цифровой интеллект.

Напиши короткий Telegram-пост.

Тема:
Почему AI заменяет рутину.

Стиль:
— минимализм
— футуризм
— короткие абзацы
— уверенность
"""

headers = {
    "Authorization": f"Bearer {GROQ_API_KEY}",
    "Content-Type": "application/json"
}

data = {
    "model": "llama3-70b-8192",
    "messages": [
        {
            "role": "user",
            "content": prompt
        }
    ]
}

response = requests.post(
    "https://api.groq.com/openai/v1/chat/completions",
    headers=headers,
    json=data
)

result = response.json()

post_text = result["choices"][0]["message"]["content"]

telegram_url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"

telegram_data = {
    "chat_id": TELEGRAM_CHAT_ID,
    "text": post_text
}

requests.post(telegram_url, data=telegram_data)

print("XION POSTED")
