import praw
from textblob import TextBlob
import os

class RedditScraper:
    def __init__(self):
        self.reddit = praw.Reddit(
            client_id=os.getenv("REDDIT_CLIENT_ID", ""),
            client_secret=os.getenv("REDDIT_CLIENT_SECRET", ""),
            user_agent="HellTheaterScraper"
        )

    def scrape(self, query, limit=50):
        posts = []
        try:
            for submission in self.reddit.subreddit("all").search(query, limit=limit):
                analysis = TextBlob(submission.title + " " + submission.selftext)
                polarity = analysis.sentiment.polarity
                sentiment = "positivo" if polarity > 0.1 else "negativo" if polarity < -0.1 else "neutral"
                posts.append({
                    "title": submission.title,
                    "content": submission.selftext,
                    "date": submission.created_utc,
                    "sentiment": sentiment,
                    "sentiment_score": polarity
                })
        except Exception as e:
            return f"Error en el scraping de Reddit: {e}"
        return posts