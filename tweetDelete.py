import tweepy 
import json
from tweepy import Stream
from tweepy.streaming import StreamListener
from datetime import datetime, timedelta


consumer_key = '#'
consumer_secret = '#'
access_token = '#'
access_token_secret = '#'

def get_tweets(username: str, num_tweets: int): 

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
    auth.set_access_token(access_token, access_token_secret) 
    api = tweepy.API(auth) 

    number_of_tweets = num_tweets
    tweets = api.user_timeline(screen_name=username) 
    data = []
    for t in tweets:
        data.append(
            {
                "Text": t.text,
            }
            )
    data = json.dumps(data)

    return data


user = get_tweets("#", 200)

with open('tweets.json', 'w') as outfile:
    json.dump(user, outfile)

def delete_tweets(username: str, cut_off: int):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
    auth.set_access_token(access_token, access_token_secret) 
    api = tweepy.API(auth) 

    cutoff_date = datetime.utcnow() - timedelta(days = cut_off)

    print("Getting timeline tweets to delete.")
    timeline = tweepy.Cursor(api.user_timeline).items()
    deleted = 0
    for t in timeline:
        api.destroy_status(t.id)
        deleted += 1
    
    print(f'Deleted {deleted} tweets.')

