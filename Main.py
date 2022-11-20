import praw
import time
import logging
from datetime import datetime

logging.basicConfig(filename="SubMembers.log", 
					format='%(asctime)s %(message)s', 
					filemode='w') 

logger=logging.getLogger() 
logger.setLevel(logging.INFO)

sub=("[FILL IN THE NAME OF THE SUBREDDIT WITHOUT THE r/]") #Provides the entire script with what subreddit to track

reddit = praw.Reddit(
    client_id="YOUR CLIENT ID HERE",
    client_secret="YOUR CLIENT SECRET HERE",
    user_agent="subreddit member amount scraper 1.5 by u/[YOUR REDDIT USERNAME HERE]",
)

subreddit = reddit.subreddit(sub) 



print("Author = u/Pos3odon08")

while True: 
 now = datetime.now()
 subs = reddit.subreddit(sub).subscribers
 current_time = now.strftime("%Hh %Mm %Ss") 
 print("\033[1;93m",subreddit.display_name, end= '')
 print("     subs", subs, end= '') 
 print("     🕒 =", current_time)
 logger.info("--------HERE--------")
 logger.info(subs)
 logger.info(current_time)
 logger.info("--------------------")
 time.sleep(60) #time between checks is set to one minute (60 seconds) 
