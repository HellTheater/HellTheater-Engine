import snscrape.modules.twitter as sntwitter
from textblob import TextBlob
from datetime import datetime, timedelta

class TwitterScraper:
    def scrape(self, query, limit=100):
        tweets = []
        search_query = f"{query} lang:es since:{(datetime.now() - timedelta(days=7)).strftime('%Y-%m-%d')}"
        for i, tweet in enumerate(sntwitter.TwitterSearchScraper(search_query).get_items()):
            if i >= limit:
                break
            analysis = TextBlob(tweet.content)
            polarity = analysis.sentiment.polarity
            sentiment = "positivo" if polarity > 0.1 else "negativo" if polarity < -0.1 else "neutral"
            tweets.append({
                "user": tweet.user.username,
                "content": tweet.content,
                "date": tweet.date,
                "likes": tweet.likeCount,
                "retweets": tweet.retweetCount,
                "followers": tweet.user.followersCount,
                "sentiment": sentiment,
                "sentiment_score": polarity
            })
        return tweets
