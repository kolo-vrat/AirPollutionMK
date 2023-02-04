import tweepy

from decouple import config

API_KEY = config("TWITTER_API_KEY")
API_SECRET = config("TWITTER_API_SECRET")
ACCESS_TOKEN = config("TWITTER_ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = config("TWITTER_ACCESS_TOKEN_SECRET")
BEARER_TOKEN = config("TWITTER_BEARER_TOKEN")


def post_tweet(text, in_reply_to_tweet_id=None):
    client = tweepy.Client(
        bearer_token=BEARER_TOKEN,
        consumer_key=API_KEY,
        consumer_secret=API_SECRET,
        access_token=ACCESS_TOKEN,
        access_token_secret=ACCESS_TOKEN_SECRET
    )
    client.create_tweet(text=text, in_reply_to_tweet_id=in_reply_to_tweet_id)

def search_twitter(query, tweet_fields):
    client = tweepy.Client(
        bearer_token=BEARER_TOKEN,
        consumer_key=API_KEY,
        consumer_secret=API_SECRET,
        access_token=ACCESS_TOKEN,
        access_token_secret=ACCESS_TOKEN_SECRET
    )
    response = client.search_recent_tweets(query, tweet_fields=tweet_fields)
    return response


    
    
