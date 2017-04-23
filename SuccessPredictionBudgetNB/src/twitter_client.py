# Chap02-03/twitter_client.py
import os
import sys
from tweepy import API
from tweepy import OAuthHandler

def get_twitter_auth():
    """Setup Twitter authentication.

    Return: tweepy.OAuthHandler object
    """
    try:
        consumer_key = "DYLog0JNQCt3DIq7AECGDuUzE"
        consumer_secret = "UFzGJRFaFbOjViUAFsX2VluWqChUBGomcwh0PW7kUMjdoyBafC"
        access_token = "838142549365784580-ZaZ6WCWwRENH4LiKz6mkrS6stSiTUsf"
        access_secret = "DTtWJJIk8cYRiL3pHSS2xm8ixd22SoJudmFUWrZ30c54s"
    except KeyError:
        sys.stderr.write("TWITTER_* environment variables not set\n")
        sys.exit(1)    
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    return auth

def get_twitter_client():
    """Setup Twitter API client.

    Return: tweepy.API object
    """
    auth = get_twitter_auth()
    client = API(auth)
    return client
