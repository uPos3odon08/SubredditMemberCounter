import praw
import time
from datetime import datetime

reddit = praw.Reddit(
    client_id="YOUR CLIENT ID HERE",
    client_secret="YOUR CLIENT SECRET HERE",
    user_agent="subreddit member amount scraper 1.5 by u/[YOUR REDDIT USERNAME HERE]",
)
subs = reddit.subreddit("[NAME OF THE SUBREDDIT WITHOUT THE r/]").subscribers
subreddit = reddit.subreddit("[NAME OF THE SUBREDDIT WITHOUT THE r/]")

now = datetime.now()

current_time = now.strftime("%H:%M:%S")

x = 1
while True: 
 print(subreddit.display_name, end= '')
 print("     subs", subs, end= '') 
 print("     🕒 =", current_time)
 time.sleep(100)
x += 1
