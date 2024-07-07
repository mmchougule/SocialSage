import anthropic
from config import CLAUDE_API_KEY, DEFAULT_NUM_TWEETS

client = anthropic.Client(api_key=CLAUDE_API_KEY)

def generate_tweet_thread(topic, num_tweets=DEFAULT_NUM_TWEETS):
    """
    Generate a tweet thread based on a given topic using Claude API.
    
    :param topic: str, the main topic for the tweet thread
    :param num_tweets: int, the number of tweets in the thread
    :return: list, generated tweets
    """
    # prompt = f"Generate a {num_tweets}-tweet thread about {topic} for Twitter. Make it engaging, informative, and suitable for a crypto/Web3 audience. Each tweet should be no more than 280 characters."
    prompt = (
        f"Imagine you're a well-informed, witty, and engaging influencer in the crypto/Web3 space. "
        f"Generate a {num_tweets}-tweet thread about {topic}. "
        "Each tweet should be a gem: insightful, sparking curiosity, and packed with value. "
        "Use humor where appropriate, and weave in current trends and jargon. "
        "Ensure each tweet can stand alone yet contributes to a cohesive narrative. "
        "Remember, each tweet is limited to 280 characters."
    )
    # Initialize messages with a basic introduction to fulfill the API requirement
    initial_message = {
        "role": "user",
        "content": f"Starting a thread on {topic} in the crypto/Web3 space."
    }

    response = client.messages.create(
        model="claude-3-5-sonnet-20240620",
        system=prompt,
        max_tokens=4000,
        # max_tokens_to_sample=1000,
        messages=[initial_message],
        temperature=0.7,
    )

# [TextBlock(
#   text='Here's a 1-tweet thread about blockchain, in the voice of a witty and engaging crypto/Web3 influencer:\n\n
# 1/ Blockchain: the tech that lets you exchange virtual cats for enough money to buy a house. But real ones, not the hairless monstrosities. 🐱⛓️\n\n
# 2/ Imagine the entire world running on a decentralized network where nobody's in charge. Kinda like the internet, but without that one relative who shares conspiracy theories. 🌐🔗\n\
# n3/ Smart contracts: code that executes automatically when conditions are met. Like a vending machine, but for money laundering. (Kidding, SEC! ...or am I?) 🤖💰\n\n
# 4/ Web3 is the next phase of the internet, where users own their data and digital assets. Think of it as a massive game of "No Take-Backsies" with actual value. 🌐3️⃣🤑\n\n
# 5/ Non-fungible tokens (NFTs): a way to prove ownership of digital items. Finally, you can flex that you own the original Doge meme without people saying "lol just screenshot it." 🖼️💎\n\n
# 6/ Decentralized Finance (DeFi): banking without the bankers. It's like a piggy bank that pays you interest and lets you buy magic internet money. 🐷💸🪙\n\n
# 7/ The blockchain trilemma: achieving decentralization, security, and scalability all at once. Kinda like trying to be rich, happy, and have a flat stomach. 🔐⚖️🚀', type='text')] Traceback (most recent call last): File "/Users/mayurchougule/development/vistara/vimana-cli/vimana/prompt/CryptoSocialSage/main.py", line 72, in <module> main() File 
# "/Users/mayurchougule/development/vistara/vimana-cli/vimana/prompt/CryptoSocialSage/main.py", line 23, in main categorized_tweets = content_analyzer.analyze_content(query, DEFAULT_NUM_TWEETS) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/Users/mayurchougule/development/vistara/vimana-cli/vimana/prompt/CryptoSocialSage/crypto_social_sage/content_analyzer.py", line 13, in analyze_content tweets = get_simulated_tweets(query, num_tweets) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/Users/mayurchougule/development/vistara/vimana-cli/vimana/prompt/CryptoSocialSage/crypto_social_sage/twitter_api.py", line 16, in get_simulated_tweets 'text': generate_tweet_thread(query, 1)[0], ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/Users/mayurchougule/development/vistara/vimana-cli/vimana/prompt/CryptoSocialSage/crypto_social_sage/content_generator.py", line 50, in generate_tweet_thread tweets = response.content.strip().split('\n\n') ^^^^^^^^^^^^^^^^^^^^^^ AttributeError: 'list' object has no attribute 'strip'
    # print(response.content[0].text, len(response.content))
    # generated_text = response.content.text if hasattr(response, 'text') else response.get_completion()

    # Split the response into individual tweets
    tweets = response.content[0].text.strip().split('\n\n')
    return tweets[:num_tweets]

def generate_engaging_comment(tweet_text):
    """
    Generate an engaging comment for a given tweet using Claude API.
    
    :param tweet_text: str, the text of the tweet to comment on
    :return: str, generated comment
    """
    prompt = f"Generate an engaging and intelligent comment for the following tweet about crypto/Web3. The comment should add value to the conversation and potentially increase the social status of the commenter. Tweet: '{tweet_text}'"

    # Initialize messages with a basic introduction to fulfill the API requirement
    initial_message = {
        "role": "user",
        "content": f"generating an engaging comment on {tweet_text} in the crypto/Web3 space."
    }

    response = client.messages.create(
        model="claude-3-5-sonnet-20240620",
        system=prompt,
        messages=[initial_message],
        max_tokens=400,
        temperature=0.7,
    )

    return response.completion.strip()

def generate_content_ideas(trending_topics, num_ideas=5):
    """
    Generate content ideas based on trending topics using Claude API.
    
    :param trending_topics: list, trending topics in crypto/Web3
    :param num_ideas: int, number of content ideas to generate
    :return: list, generated content ideas
    """
    topics_str = ", ".join(trending_topics)
    prompt = f"Generate {num_ideas} unique content ideas for social media posts about crypto and Web3. Base these ideas on the following trending topics: {topics_str}. Each idea should be engaging, informative, and have the potential to go viral."
    initial_message = {
        "role": "user",
        "content": f"generating an engaging comment on {tweet_text} in the crypto/Web3 space."
    }

    response = client.messages.create(
        model="claude-3-5-sonnet-20240620",
        prompt=prompt,
        max_tokens=4000,
        messages=[initial_message],
        temperature=0.8,
    )

    # Split the response into individual ideas
    ideas = response.completion.strip().split('\n')
    return ideas[:num_ideas]