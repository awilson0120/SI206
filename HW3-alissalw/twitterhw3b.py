# In this assignment you must do a Twitter search on any term
# of your choice.
# Deliverables:
# 1) Print each tweet
# 2) Print the average subjectivity of the results
# 3) Print the average polarity of the results

# Be prepared to change the search term during demo.

import tweepy
from textblob import TextBlob

consumer_key = "EjzZnHYdYljefY08cA1dIlmoe" 
consumer_secret = "NZqokIblQCUsMngIaHoxPGPEhaetVQ3GzmOH7A2dGDHybBYY1J"
access_token = '755787072926023680-PojkYpSk41Xs9SUBxuW3p5i7Q3hUx7A'
access_token_secret = '554sRkHDAMfYcQaxNHHhef6d4IVyA7v7oCaEy82mTGhlH'

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Hillary Clinton')

for tweet in public_tweets:
	print(tweet.text)
	

subjectivity = []
polarity = []

for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)
	subjectivity.append(analysis.sentiment[1])
	polarity.append(analysis.sentiment[0])
avg_subjectivity = sum(subjectivity)/len(subjectivity)
avg_polarity = sum(polarity)/len(polarity)



print("Average subjectivity is", avg_subjectivity)
print("Average polarity is", avg_polarity)
