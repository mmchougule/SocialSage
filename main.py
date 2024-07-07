import sys
from datetime import datetime, timedelta
from crypto_social_sage import content_analyzer, content_generator, scheduler, twitter_api
from config import DEFAULT_NUM_TWEETS, DEFAULT_POSTS_PER_DAY, DEFAULT_SCHEDULE_DAYS

def main():
    print("Welcome to CryptoSocialSage!")
    
    content_scheduler = scheduler.ContentScheduler()

    while True:
        print("\nPlease choose an option:")
        print("1. Analyze trending crypto content")
        print("2. Generate tweet ideas")
        print("3. Schedule posts")
        print("4. View scheduled posts")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            query = input("Enter a search query for crypto content: ")
            categorized_tweets = content_analyzer.analyze_content(query, DEFAULT_NUM_TWEETS)
            print("\nCategorized Tweets:")
            for category, tweets in categorized_tweets.items():
                print(f"\n{category} Engagement:")
                for tweet in tweets[:3]:  # Show top 3 tweets in each category
                    print(f"- {tweet['text'][:100]}...")
            
            trending_topics = content_analyzer.identify_trending_topics([tweet for tweets in categorized_tweets.values() for tweet in tweets])
            print("\nTrending Topics:")
            print(", ".join(trending_topics))

        elif choice == '2':
            topic = input("Enter a topic for tweet ideas: ")
            num_tweets = int(input("Enter the number of tweets to generate: "))
            tweet_ideas = content_generator.generate_tweet_thread(topic, num_tweets)
            print("\nGenerated Tweet Ideas:")
            for i, idea in enumerate(tweet_ideas, 1):
                print(f"{i}. {idea}")

        elif choice == '3':
            content_list = []
            while True:
                content = input("Enter content to schedule (or 'done' to finish): ")
                if content.lower() == 'done':
                    break
                content_list.append(content)
            
            start_date = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
            end_date = start_date + timedelta(days=DEFAULT_SCHEDULE_DAYS)
            content_scheduler.generate_optimal_schedule(content_list, start_date, end_date, DEFAULT_POSTS_PER_DAY)
            print("Posts scheduled successfully!")

        elif choice == '4':
            scheduled_posts = content_scheduler.get_schedule()
            if scheduled_posts:
                print("\nScheduled Posts:")
                for i, (content, post_time) in enumerate(scheduled_posts, 1):
                    print(f"{i}. {post_time}: {content[:50]}...")
            else:
                print("No posts currently scheduled.")

        elif choice == '5':
            print("Thank you for using CryptoSocialSage. Goodbye!")
            sys.exit(0)

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()