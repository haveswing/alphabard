import time
import datetime
import re
import urllib2
import json
import twitter
import markovify

owner = "haveswing"

print
print "-alphabard-"
print
print ("admin: " + owner)

# Get raw text as string.
with open("C:/Users/haveswing/workspace/alphabard/alphabard_database.txt") as f:
    text = f.read()
    
print
print "database: loaded"
print
print "results: "
print

# Build the model.
text_model = markovify.Text(text)

# Print range(number) randomly-generated sentences
for i in range(0):
    print(text_model.make_sentence())

# Print range(number) randomly-generated sentences of no more than 140 characters
for i in range(1000):
    print(text_model.make_short_sentence(140))
    print
