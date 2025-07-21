# save_news.py
import pandas as pd
import os
from datetime import datetime

def save_news_to_csv(news_list, folder_path='data'):
    if not news_list:
        print("No news to save.")
        return

    os.makedirs(folder_path, exist_ok=True)
    today = datetime.today().strftime('%Y-%m-%d')
    filename = f'ai_news_{today}.csv'
    file_path = os.path.join(folder_path, filename)

    df = pd.DataFrame(news_list)
    df.to_csv(file_path, index=False, encoding='utf-8')
    print(f"✅ Saved {len(df)} articles to {file_path}")
