from twython import Twython # pip install twython
import time # standard lib
import re
import sys

print ("retrieving tweets...")
print

''' Go to https://apps.twitter.com/ to register your app to get your api keys '''
CONSUMER_KEY = 'EAsLEre4KeHIEuEbirisIYTRJ'
CONSUMER_SECRET = 'T8laklS7F00wbgo8kn0T4ZjBGuIfXPfSzV0EicJ3pOgjIUjfmV'
ACCESS_KEY = '834049578630574080-a3hDEaBrPCoiTEJ5jUYl2WzcFNCO0jD'
ACCESS_SECRET = '3FTv7r2jG7LERhyKY7EJ8SF4Vp1oGvEzCg1uZKU03hcWr'

twitter = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)
lis = [467020906049835008] ## this is the latest starting tweet id
for i in range(0, 16): ## iterate through all tweets
## tweet extract method with the last list item as the max_id
    user_timeline = twitter.get_user_timeline(screen_name="matteorenzi",
    count=200, include_retweets=False, max_id=lis[-1])
    time.sleep(300) ## 5 minute rest between api calls

    for tweet in user_timeline:
        # sys.stdout=open("tweets.txt","w") # write to file?
        print tweet['text'] ## print the tweet
        lis.append(tweet['id']) ## append tweet id's
        # sys.stdout.close() # write to file?
        
print
print ("done.")