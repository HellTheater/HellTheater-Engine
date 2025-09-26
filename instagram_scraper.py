import instaloader

class InstagramScraper:
    def scrape_hashtag(self, hashtag, limit=20):
        L = instaloader.Instaloader()
        posts = []
        for post in instaloader.Hashtag.from_name(L.context, hashtag).get_posts():
            if len(posts) >= limit:
                break
            posts.append({
                "caption": post.caption,
                "likes": post.likes,
                "comments": post.comments,
                "date": post.date,
                "url": f"https://www.instagram.com/p/{post.shortcode}/"
            })
        return posts
