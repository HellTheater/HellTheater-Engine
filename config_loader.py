import os
from dotenv import load_dotenv

def load_config():
    load_dotenv()
    return {
        "GOOGLE_API_KEY": os.getenv("GOOGLE_API_KEY", ""),
        "OPENAI_API_KEY": os.getenv("OPENAI_API_KEY", ""),
        "SERPER_API_KEY": os.getenv("SERPER_API_KEY", ""),
        "REDDIT_CLIENT_ID": os.getenv("REDDIT_CLIENT_ID", ""),
        "REDDIT_CLIENT_SECRET": os.getenv("REDDIT_CLIENT_SECRET", ""),
        "NEWS_API_KEY": os.getenv("NEWS_API_KEY", ""),
        "SENDGRID_API_KEY": os.getenv("SENDGRID_API_KEY", ""),
        "REPLICATE_API_TOKEN": os.getenv("REPLICATE_API_TOKEN", "")
    }
