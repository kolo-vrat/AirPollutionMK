import tweepy

from decouple import config


BASE_URL = config("TWITTER_BASE_URL")
API_KEY = config("TWITTER_API_KEY")
API_SECRET = config("TWITTER_API_SECRET")
ACCESS_TOKEN = config("TWITTER_ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = config("TWITTER_ACCESS_TOKEN_SECRET")
BEARER_TOKEN = config("TWITTER_BEARER_TOKEN")


def post_tweet(text):
    client = tweepy.Client(
        bearer_token=BEARER_TOKEN,
        consumer_key=API_KEY,
        consumer_secret=API_SECRET,
        access_token=ACCESS_TOKEN,
        access_token_secret=ACCESS_TOKEN_SECRET
    )
    client.create_tweet(text=text)
