# fetch_news.py
import requests

def get_news(max_articles=10):
    api_key = "b678ffe50d894b8ab35234642188cbd4"
    url = "https://newsapi.org/v2/everything"

    params = {
        'q': '"artificial intelligence" OR "machine learning" OR "deep learning" OR "openai" OR "neural networks"',
        'language': 'en',
        'sortBy': 'publishedAt',
        'pageSize': max_articles,
        'apiKey': api_key,
        'domains': 'techcrunch.com,theverge.com,venturebeat.com,bbc.com,nytimes.com,forbes.com'
    }

    response = requests.get(url, params=params)
    if response.status_code != 200:
        raise Exception(f"Error fetching news: {response.status_code}")
    
    data = response.json()
    articles = data.get('articles', [])

    ai_keywords = ['ai', 'artificial intelligence', 'openai', 'deepmind', 'machine learning', 'neural network']
    filtered_articles = []

    for article in articles:
        title = article.get('title', '').lower()
        description = (article.get('description') or '').lower()
        combined_text = f"{title} {description}"

        if any(keyword in combined_text for keyword in ai_keywords):
            filtered_articles_by= {
                'title': article['title'],
                'description': article.get('description', 'No summary available.'),
                'source': article['source']['name'],
                'url': article['url'],
                'urlToImage': article.get('urlToImage'),
                'published_at': article['publishedAt'][:10]
            }
            filtered_articles.append(filtered_articles_by)

    print(f"✅ Filtered and found {len(filtered_articles)} AI articles.")
    return filtered_articles
