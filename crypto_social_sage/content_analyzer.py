import pandas as pd
from .twitter_api import get_simulated_tweets
from config import DEFAULT_NUM_TWEETS

def analyze_content(query, num_tweets=DEFAULT_NUM_TWEETS):
    """
    Analyze simulated tweets based on a given query and categorize them.
    
    :param query: str, the search query for tweets
    :param num_tweets: int, the number of tweets to analyze
    :return: dict, categorized tweets
    """
    tweets = get_simulated_tweets(query, 2) #num_tweets)
    df = pd.DataFrame(tweets); df.show();print(df.head())
    
    # Basic categorization based on engagement metrics
    df['engagement'] = df['retweet_count'] + df['favorite_count']
    df['category'] = pd.cut(df['engagement'], 
                            bins=[0, 500, 1500, float('inf')],
                            labels=['Low', 'Medium', 'High'])
    
    # Group tweets by category
    categorized_tweets = {
        'High': df[df['category'] == 'High'].to_dict('records'),
        'Medium': df[df['category'] == 'Medium'].to_dict('records'),
        'Low': df[df['category'] == 'Low'].to_dict('records')
    }
    
    return categorized_tweets

def identify_trending_topics(tweets):
    """
    Identify trending topics from a list of tweets.
    
    :param tweets: list of dict, tweets to analyze
    :return: list, trending topics
    """
    all_text = ' '.join([tweet['text'] for tweet in tweets])
    words = all_text.lower().split()
    word_freq = pd.Series(words).value_counts()
    trending_topics = word_freq.head(10).index.tolist()
    
    return trending_topics