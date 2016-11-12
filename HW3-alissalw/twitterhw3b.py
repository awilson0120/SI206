# In this assignment you must do a Twitter search on any term
# of your choice.
# Deliverables:
# 1) Print each tweet
# 2) Print the average subjectivity of the results
# 3) Print the average polarity of the results

# Be prepared to change the search term during demo.

import tweepy
from textblob import TextBlob

access_token = "755787072926023680-G9nP4lXtXbesPI9ll9r4pKE3GuMQihZ"
access_token_secret = "FFMKaapNxMRhAEiopKk07nNrRVaX3tEaiRixS8vr5oYsn"
consumer_key = "B8p7Bj2FmMdAtHM8C5SVKkZEx"
consumer_secret = "iIDkJUDrQAXobB3QnpItYhPlYmAUISG7QDyWK2HrMLAy7p3bNY"

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Hillary Clinton')


	

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
