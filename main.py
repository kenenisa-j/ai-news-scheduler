# main.py
from fetch_news import get_news
from send_to_telegram import send_news_to_telegram

def run():
    print("🔍 Fetching news...")
    news = get_news()

    print("📤 Sending to Telegram...")
    send_news_to_telegram(news)

    print("✅ All done!")

if __name__ == '__main__':
    run()
