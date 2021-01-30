import tweepy
from ScrapData import *

from _token import *

k=0
    
auth = tweepy.OAuthHandler(API_KEYS, API_SECRET_KEYS)
auth.set_access_token(TOKEN, TOKEN_SECRET)
api = tweepy.API(auth)
try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")
def chdir():
    k=k+1
    return k
