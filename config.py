# Configuration settings for CryptoSocialSage

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Claude API settings
CLAUDE_API_KEY = os.getenv("CLAUDE_API_KEY")

# Twitter API settings
TWITTER_API_KEY = os.getenv("TWITTER_API_KEY")
TWITTER_API_SECRET = os.getenv("TWITTER_API_SECRET")
TWITTER_ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
TWITTER_ACCESS_TOKEN_SECRET = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

# Tavily API settings
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

# Application settings #100
DEFAULT_NUM_TWEETS = 2
DEFAULT_POSTS_PER_DAY = 3
DEFAULT_SCHEDULE_DAYS = 7

# Add any other configuration variables as needed