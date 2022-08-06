from collections import UserString
from math import nan
import tweepy
import random
import re



consumer_key = "placeholder"
consumer_secret = "placeholder"
access_token = "placeholder"
access_token_secret = "placeholder"
bearer_token = "placeholder"

#Shadowverse id 3321204048



#auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
#auth.set_access_token(access_token, access_token_secret)

api = tweepy.Client(bearer_token, consumer_key, consumer_secret, access_token, access_token_secret)
#ADD THE USER ENTER PART HERE
#print('enter a username')


username= 'shadowversegame'
id = api.get_user(username=username)

id_author = str(id)

posOfID = re.search(r"\d", id_author).start()

#19 is max length of 64bit integer
id_author = id_author[posOfID:posOfID + 19]




Num = False
while Num == False:
    id_author = id_author[0:len(id_author) - 1]
    Num = id_author.isnumeric()


tweets = api.get_users_tweets(id=id_author, user_auth=False, max_results=6)


def get_num_likes(ids):
    users = api.get_liking_users(id=ids)
    return len(users.data)



tweet_ids = []
tweet_data = []
tweet_likes = []

#Pulls tweet id and tweet text
for tweet in tweets.data:
    
    tweet_ids.append(tweet.id) 
    #add check so you can pull video or image and stuff
    tweet_data.append(tweet.text)
    #crewate functiont o get how many likes on a tweet
    tweet_likes.append(get_num_likes(tweet.id))



#Game time

#


