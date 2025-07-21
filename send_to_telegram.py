# send_to_telegram.py
import requests

def send_news_to_telegram(news_list):
    bot_token = "8185329751:AAHCyQ_dx4BgcI5kc93KcdDy_hi3CSdJQxQ"     
    chat_id = "@ainewsdaily7"       

    for article in news_list:
        title = article['title']
        description = article.get('description', 'No summary available.')
        source = article.get('source', 'Unknown')
        url = article['url']
        image_url = article.get('urlToImage')

        if image_url:
            telegram_url = f"https://api.telegram.org/bot{bot_token}/sendPhoto"
            payload = {
                'chat_id': chat_id,
                'photo': image_url,
                'caption': f"🧠 <b>{title}</b>\n\n{description}\n\n🔗 <a href=\"{url}\">Read More</a>\n📰 Source: {source}",
                'parse_mode': 'HTML'
            }
        else:
            telegram_url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
            payload = {
                'chat_id': chat_id,
                'text': f"🧠 <b>{title}</b>\n\n{description}\n\n🔗 <a href=\"{url}\">Read More</a>\n📰 Source: {source}",
                'parse_mode': 'HTML'
            }

        response = requests.post(telegram_url, data=payload)
        if response.status_code != 200 or not response.json().get("ok"):
            print(f"❌ Failed to send: {title}")
            print(response.text)
        else:
            print(f"✅ Sent: {title}")
