import requests
import pandas as pd
import os
from datetime import datetime
api_key="b678ffe50d894b8ab35234642188cbd4"

def get_news(max_articles=5):
    url = f"https://newsapi.org/v2/everything?q=artificial+intelligence&apiKey={api_key}"
    params = {
        'q': 'artificial intelligence',
        'language': 'en',
        'sortBy': 'publishedAt',
        'pageSize': max_articles,
        'apiKey': api_key
    }
    
    response = requests.get(url , params=params)
    if response.status_code != 200:
        raise Exception(f"Error fetching news: {response.status_code}")
    data = response.json()
    articles = data.get('articles', [])
    news_list = []
    for article in articles:
        news_item = {
            'title': article['title'],
            'source': article['source']['name'],
            'url': article['url'],
            'published_at': article['publishedAt'][:10]  # Just date
        }
        news_list.append(news_item)

    return news_list




def save_news_to_csv(news_list, folder_path='data'):
    if not news_list:
        print("No news to save.")
        return

    # Create data folder if it doesn't exist
    os.makedirs(folder_path, exist_ok=True)

    # Create today's filename
    today = datetime.today().strftime('%Y-%m-%d')
    filename = f'ai_news_{today}.csv'
    file_path = os.path.join(folder_path, filename)

    # Convert news list to DataFrame
    df = pd.DataFrame(news_list)

    # Save to CSV
    df.to_csv(file_path, index=False, encoding='utf-8')
    print(f"Saved {len(df)} articles to {file_path}")

news = get_news()
save_news_to_csv(news)

# Example usage
# if __name__ == '__main__':
#     ai_news = get_news()
#     for news in ai_news:
#         print(f"{news['published_at']} - {news['title']} ({news['source']})\n{news['url']}\n")
        
    
    