import os
import praw
from textblob import TextBlob

class RedditScraper:
    def __init__(self):
        self.reddit = praw.Reddit(
            client_id=os.getenv("REDDIT_CLIENT_ID", ""),
            client_secret=os.getenv("REDDIT_CLIENT_SECRET", ""),
            user_agent="helltheatre_reddit_scraper"
        )

    def scrape(self, subreddit, limit=50):
        posts = []
        for post in self.reddit.subreddit(subreddit).hot(limit=limit):
            text = f"{post.title} {post.selftext}"
            analysis = TextBlob(text)
            polarity = analysis.sentiment.polarity
            sentiment = "positivo" if polarity > 0.1 else "negativo" if polarity < -0.1 else "neutral"
            posts.append({
                "title": post.title,
                "content": post.selftext[:300],
                "upvotes": post.score,
                "comments": post.num_comments,
                "sentiment": sentiment,
                "sentiment_score": polarity,
                "url": f"https://reddit.com{post.permalink}"
            })
        return posts
