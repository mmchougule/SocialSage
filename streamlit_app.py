import streamlit as st
import sys
from datetime import datetime, timedelta
from crypto_social_sage import content_analyzer, content_generator, scheduler, twitter_api
from config import DEFAULT_NUM_TWEETS, DEFAULT_POSTS_PER_DAY, DEFAULT_SCHEDULE_DAYS

# Set page config for dark theme
st.set_page_config(page_title="CryptoSocialSage", page_icon="🧠", layout="wide", initial_sidebar_state="expanded")

# Apply dark theme
st.markdown("""
<style>
    .reportview-container {
        background: #0e1117;
        color: #fafafa;
    }
    .sidebar .sidebar-content {
        background: #262730;
    }
    .Widget>label {
        color: #fafafa;
    }
    .stTextInput>div>div>input {
        color: #fafafa;
    }
</style>
""", unsafe_allow_html=True)

# Initialize ContentScheduler
content_scheduler = scheduler.ContentScheduler()

def main():
    st.title("xSage 🧠💰")

    menu = [" Crypto Content", "Generate Tweet Ideas", "Schedule Posts", "View Scheduled Posts"]
    choice = st.sidebar.selectbox("Choose an option", menu)

    if choice == "what's hyped right now":
        analyze_trending_content()
    elif choice == "give me tweet ideas":
        generate_tweet_ideas()
    elif choice == "pencil my posts":
        schedule_posts()
    elif choice == "view my posts":
        view_scheduled_posts()

def analyze_trending_content():
    st.header("what's hyped in")
    query = st.text_input("interests:")
    if st.button("go"):
        with st.spinner("asking agents..."):
            categorized_tweets = content_analyzer.analyze_content(query, DEFAULT_NUM_TWEETS)
            st.subheader("some of the most talked about")
            for category, tweets in categorized_tweets.items():
                st.write(f"**{category} engagement:**")
                for tweet in tweets[:3]:
                    st.write(f"- {tweet['text'][:100]}...")
            
            trending_topics = content_analyzer.identify_trending_topics([tweet for tweets in categorized_tweets.values() for tweet in tweets])
            st.subheader("trending topics")
            st.write(", ".join(trending_topics))

def generate_tweet_ideas():
    st.header("give me tweet ideas")
    topic = st.text_input("interests:")
    num_tweets = st.number_input("how many do you want to generate:", min_value=1, max_value=10, value=3)
    if st.button("go"):
        with st.spinner("cooking tweet ideas..."):
            tweet_ideas = content_generator.generate_tweet_thread(topic, num_tweets)
            st.subheader("here's some ideas")
            for i, idea in enumerate(tweet_ideas, 1):
                st.write(f"{i}. {idea}")

def schedule_posts():
    st.header("Schedule Posts")
    content_list = []
    for i in range(5):  # Allow up to 5 posts to be scheduled at once
        content = st.text_area(f"Enter content for post {i+1}:", key=f"post_{i}")
        if content:
            content_list.append(content)
    
    if st.button("Schedule Posts"):
        if content_list:
            start_date = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
            end_date = start_date + timedelta(days=DEFAULT_SCHEDULE_DAYS)
            content_scheduler.generate_optimal_schedule(content_list, start_date, end_date, DEFAULT_POSTS_PER_DAY)
            st.success("Posts scheduled successfully!")
        else:
            st.warning("Please enter at least one post to schedule.")

def view_scheduled_posts():
    st.header("View Scheduled Posts")
    scheduled_posts = content_scheduler.get_schedule()
    if scheduled_posts:
        for i, (content, post_time) in enumerate(scheduled_posts, 1):
            st.write(f"**{i}. {post_time}:** {content[:50]}...")
    else:
        st.info("No posts currently scheduled.")

if __name__ == "__main__":
    main()