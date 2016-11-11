# Write a Python file that uploads an image to your 
# Twitter account.  Make sure to use the 
# hashtags #UMSI-206 #Proj3 in the tweet.

# You will demo this live for grading.
import tweepy

access_token = "755787072926023680-PojkYpSk41Xs9SUBxuW3p5i7Q3hUx7A"
access_token_secret = "554sRkHDAMfYcQaxNHHhef6d4IVyA7v7oCaEy82mTGhlH"
consumer_key = "EjzZnHYdYljefY08cA1dIlmoe"
consumer_secret = "NZqokIblQCUsMngIaHoxPGPEhaetVQ3GzmOH7A2dGDHybBYY1J"

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)


api.update_status("#UMSI")
print("""No output necessary although you 
	can print out a success/failure message if you want to.""")