import tweepy
from textblob import TextBlob
import os

class TwitterScraper:
    def __init__(self):
        self.client = tweepy.Client(os.getenv("TWITTER_API_KEY", ""))

    def scrape(self, query, limit=50):
        tweets = []
        try:
            response = self.client.search_recent_tweets(
                query,
                tweet_fields=["context_annotations", "created_at"],
                max_results=limit
            )
            if response.data:
                for tweet in response.data:
                    analysis = TextBlob(tweet.text)
                    polarity = analysis.sentiment.polarity
                    sentiment = "positivo" if polarity > 0.1 else "negativo" if polarity < -0.1 else "neutral"
                    tweets.append({
                        "content": tweet.text,
                        "date": tweet.created_at,
                        "sentiment": sentiment,
                        "sentiment_score": polarity
                    })
        except Exception as e:
            return f"Error en el scraping de Twitter: {e}"
        return tweets