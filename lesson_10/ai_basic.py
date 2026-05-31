"""ЭТА ВЕРСИЯ ДАЕТ ОШИБКУ, ПОТОМУ ЧТО ТРЕБУЕТСЯ ОПЛАТА ДЛЯ ИИ, следующая версия ai_basic_norm"""

import requests

# API_URL = "https://openrouter.ai/api/v1/chat/completions"
# # ⚠️ ВСТАВЬ СЮДА КЛЮЧ
# API_KEY = "YOUR_OPENROUTER_KEY_HERE"  # ← замени на свой ключ локально
#
# headers = {
#     "Authorization": f"Bearer {API_KEY}",
#     "Content-Type": "application/json",
#     "HTTP-Referer": "https://example.com",
#     "X-Title": "Python Learning Agent"
# }

# # ✅ Используем подтверждённо бесплатную модель
# payload = {
#     "model": "x-ai/grok-build-0.1",
#     "messages": [
#         {"role": "user", "content": "Объясни, что такое рекурсия, в одном предложении."}
#     ]
# }
#
# print("📡 Отправляю запрос к ИИ...")
# response = requests.post(API_URL, headers=headers, json=payload)
#
# if response.status_code == 200:
#     data = response.json()
#     answer = data["choices"][0]["message"]["content"]
#     print("🤖 Ответ ИИ:", answer)
# else:
#     print(f"❌ Ошибка {response.status_code}: {response.text}")
#     print("💡 Проверь бесплатные модели: https://openrouter.ai/models?order=-free")
#
#
# # После получения ответа, если не 200:
# if response.status_code != 200:
#     print("🔍 Доступные бесплатные модели (первые 5):")
#     # Простой запрос к списку моделей
#     models_resp = requests.get("https://openrouter.ai/api/v1/models?order=-free&max_price=0")
#     if models_resp.ok:
#         models = models_resp.json()["data"]
#         for m in models[:5]:
#             print(f"  - {m['id']}")