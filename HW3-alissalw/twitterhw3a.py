# Write a Python file that uploads an image to your 
# Twitter account.  Make sure to use the 
# hashtags #UMSI-206 #Proj3 in the tweet.

# You will demo this live for grading.
import tweepy

access_token = "755787072926023680-G9nP4lXtXbesPI9ll9r4pKE3GuMQihZ"
access_token_secret = "FFMKaapNxMRhAEiopKk07nNrRVaX3tEaiRixS8vr5oYsn"
consumer_key = "B8p7Bj2FmMdAtHM8C5SVKkZEx"
consumer_secret = "iIDkJUDrQAXobB3QnpItYhPlYmAUISG7QDyWK2HrMLAy7p3bNY"

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

img = 'media/IMG_4037.jpg'
api.update_with_media(img, status="#UMSI-206 #Proj3")
print("""No output necessary although you 
	can print out a success/failure message if you want to.""")