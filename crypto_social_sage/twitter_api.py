import random
from .content_generator import generate_tweet_thread, generate_engaging_comment

def get_simulated_tweets(query, num_tweets=100):
    """
    Simulate popular tweets based on a given query.
    
    :param query: str, the search query for tweets
    :param num_tweets: int, the number of tweets to simulate
    :return: list of dict, containing simulated tweet data
    """
    tweets = []
    for _ in range(num_tweets):
        tweet = {
            'id': random.randint(1000000000, 9999999999),
            'text': generate_tweet_thread(query, 1)[0],
            'user': f"user_{random.randint(1000, 9999)}",
            'created_at': f"2024-{random.randint(1, 7):02d}-{random.randint(1, 28):02d}",
            'retweet_count': random.randint(0, 1000),
            'favorite_count': random.randint(0, 2000)
        }
        tweets.append(tweet)
    return tweets

def post_tweet(content):
    """
    Simulate posting a tweet.
    
    :param content: str, the content of the tweet
    :return: bool, True if successful, False otherwise
    """
    print(f"Tweet posted: {content}")
    return True

def post_comment(tweet_id, comment):
    """
    Simulate posting a comment on a tweet.
    
    :param tweet_id: int, the ID of the tweet to comment on
    :param comment: str, the content of the comment
    :return: bool, True if successful, False otherwise
    """
    print(f"Comment posted on tweet {tweet_id}: {comment}")
    return True