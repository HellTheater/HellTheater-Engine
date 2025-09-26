import requests
from textblob import TextBlob

class InstagramScraper:
    def __init__(self):
        self.api_url = "https://instagram-scraper-api-url"  # Reemplaza por tu endpoint real

    def scrape(self, query, limit=50):
        posts = []
        try:
            response = requests.get(f"{self.api_url}/search", params={"query": query, "limit": limit})
            data = response.json()
            for post in data.get("results", []):
                analysis = TextBlob(post.get("caption", ""))
                polarity = analysis.sentiment.polarity
                sentiment = "positivo" if polarity > 0.1 else "negativo" if polarity < -0.1 else "neutral"
                posts.append({
                    "caption": post.get("caption", ""),
                    "date": post.get("timestamp", ""),
                    "sentiment": sentiment,
                    "sentiment_score": polarity
                })
        except Exception as e:
            return f"Error en el scraping de Instagram: {e}"
        return posts