import schedule
import time
from datetime import datetime, timedelta
import random
from config import DEFAULT_POSTS_PER_DAY, DEFAULT_SCHEDULE_DAYS
from .twitter_api import post_tweet

class ContentScheduler:
    def __init__(self):
        self.scheduled_posts = []

    def add_post(self, content, post_time):
        """
        Add a post to the schedule.

        :param content: str, the content to be posted
        :param post_time: datetime, the time to post the content
        """
        self.scheduled_posts.append((content, post_time))
        self.scheduled_posts.sort(key=lambda x: x[1])  # Sort by post_time

    def remove_post(self, index):
        """
        Remove a post from the schedule.

        :param index: int, the index of the post to remove
        """
        if 0 <= index < len(self.scheduled_posts):
            del self.scheduled_posts[index]

    def get_schedule(self):
        """
        Get the current schedule of posts.

        :return: list of tuples (content, post_time)
        """
        return self.scheduled_posts

    def clear_schedule(self):
        """
        Clear all scheduled posts.
        """
        self.scheduled_posts = []

    def generate_optimal_schedule(self, content_list, start_date=None, end_date=None, posts_per_day=DEFAULT_POSTS_PER_DAY):
        """
        Generate an optimal posting schedule for the given content.

        :param content_list: list of str, content to be scheduled
        :param start_date: datetime, start date for the schedule (default: today)
        :param end_date: datetime, end date for the schedule (default: start_date + DEFAULT_SCHEDULE_DAYS)
        :param posts_per_day: int, number of posts per day
        """
        self.clear_schedule()
        
        if start_date is None:
            start_date = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
        if end_date is None:
            end_date = start_date + timedelta(days=DEFAULT_SCHEDULE_DAYS)
        
        days = (end_date - start_date).days + 1
        total_slots = days * posts_per_day

        if len(content_list) > total_slots:
            content_list = random.sample(content_list, total_slots)
        
        time_slots = [
            (8, 10),  # Morning
            (12, 14),  # Afternoon
            (19, 21)  # Evening
        ]

        current_date = start_date
        for content in content_list:
            if current_date > end_date:
                break
            
            hour, minute = random.randint(*random.choice(time_slots)), random.randint(0, 59)
            post_time = current_date.replace(hour=hour, minute=minute)
            
            self.add_post(content, post_time)
            
            if len(self.scheduled_posts) % posts_per_day == 0:
                current_date += timedelta(days=1)

    def run_scheduler(self):
        """
        Run the scheduler to post content at scheduled times.
        """
        def job(content):
            print(f"Posting: {content}")
            post_tweet(content)

        for content, post_time in self.scheduled_posts:
            schedule.every().day.at(post_time.strftime("%H:%M")).do(job, content).tag('scheduled_post')

        while True:
            schedule.run_pending()
            time.sleep(60)  # Check every minute

# Example usage
if __name__ == "__main__":
    scheduler = ContentScheduler()
    
    # Generate some sample content
    sample_content = [f"Sample post {i}" for i in range(10)]
    
    # Generate an optimal schedule for the next DEFAULT_SCHEDULE_DAYS
    scheduler.generate_optimal_schedule(sample_content)
    
    print("Generated Schedule:")
    for content, post_time in scheduler.get_schedule():
        print(f"{post_time}: {content}")
    
    # Uncomment the following line to actually run the scheduler
    # scheduler.run_scheduler()