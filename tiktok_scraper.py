import os
import requests

class TikTokScraper:
    def scrape(self, hashtag):
        url = f"https://tiktok-scraper-api.p.rapidapi.com/hashtag/{hashtag}"
        headers = {
            "X-RapidAPI-Key": os.getenv("RAPIDAPI_KEY", ""),
            "X-RapidAPI-Host": "tiktok-scraper-api.p.rapidapi.com"
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json().get("data", [])
        else:
            return []
