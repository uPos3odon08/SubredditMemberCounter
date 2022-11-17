import praw
import time

reddit = praw.Reddit(
    client_id="[CLIENT ID HERE]",
    client_secret="[CLIENT SECRET HERE]",
    user_agent="[USER AGENT HERE]",
)
subs = reddit.subreddit("[ENTER SUBREDDIT HERE WITHOUT THE r/").subscribers

x = 1
while True: 
 print(subs)
 time.sleep(100)
x += 1
