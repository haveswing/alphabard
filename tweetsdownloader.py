# -*- coding: utf-8 -*-

from twython import Twython # pip install twython
import time # standard lib
import re
import codecs
import sys

name = "Ignazio Marino" #naming db chapter
username = "ignaziomarino" # @username
lis = [836907142535917572] ## this is the latest starting tweet id

print
print "-tdownloader-"
print
print ("subject: " + name)
print
print "data acquisition..."

''' Go to https://apps.twitter.com/ to register your app to get your api keys '''
CONSUMER_KEY = 'EAsLEre4KeHIEuEbirisIYTRJ'
CONSUMER_SECRET = 'T8laklS7F00wbgo8kn0T4ZjBGuIfXPfSzV0EicJ3pOgjIUjfmV'
ACCESS_KEY = '834049578630574080-a3hDEaBrPCoiTEJ5jUYl2WzcFNCO0jD'
ACCESS_SECRET = '3FTv7r2jG7LERhyKY7EJ8SF4Vp1oGvEzCg1uZKU03hcWr'

twitter = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)

class Logger(object): # "http://stackoverflow.com/questions/4675728/redirect-stdout-to-a-file-in-python"
    def __init__(self, filename="Default.log"):
        self.terminal = sys.stdout
        self.log = open(filename, "a")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message.encode('utf8'))

sys.stdout = Logger("tdownload.txt")

print
print name + ":"
print

for i in range(0, 16): ## iterate through all tweets
## tweet extract method with the last list item as the max_id
    user_timeline = twitter.get_user_timeline(screen_name=username,
    count=200, include_retweets=False, max_id=lis[-1])
    time.sleep(300) ## 5 minute(300) rest between api calls

    for tweet in user_timeline:
        # sys.stdout=open("tweets.txt","w") # write to file?
        print tweet['text'] ## print the tweet
        lis.append(tweet['id']) ## append tweet id's
        # sys.stdout.close() # write to file?
        
print
print name + "."
print
print
print
print
