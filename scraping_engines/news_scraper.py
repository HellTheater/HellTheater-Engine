import requests
from textblob import TextBlob
import os

class NewsScraper:
    def __init__(self):
        self.api_key = os.getenv("NEWS_API_KEY", "")
        self.api_url = "https://newsapi.org/v2/everything"

    def scrape(self, query, limit=50):
        articles = []
        try:
            response = requests.get(self.api_url, params={
                "q": query,
                "pageSize": limit,
                "apiKey": self.api_key
            })
            data = response.json()
            for article in data.get("articles", []):
                analysis = TextBlob(article.get("title", "") + " " + article.get("description", ""))
                polarity = analysis.sentiment.polarity
                sentiment = "positivo" if polarity > 0.1 else "negativo" if polarity < -0.1 else "neutral"
                articles.append({
                    "title": article.get("title", ""),
                    "description": article.get("description", ""),
                    "date": article.get("publishedAt", ""),
                    "sentiment": sentiment,
                    "sentiment_score": polarity
                })
        except Exception as e:
            return f"Error en el scraping de NewsAPI: {e}"
        return articles