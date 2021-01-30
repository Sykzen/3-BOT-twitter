import tweepy
from _token import *

    


auth = tweepy.OAuthHandler(API_KEYS, API_SECRET_KEYS)
auth.set_access_token(TOKEN, TOKEN_SECRET)

api = tweepy.API(auth)
try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")
    
#-----------------get timeline-----------------------------
timeline = api.home_timeline()
#-----------------spot user -----------------------------------
user = api.get_user('Sykzen') # the tag
print(user.screen_name) # get the name @
print(user.name) # get the name
print(user.description) # get the description
print(user.location) # get the localisation
for follower in user.followers(): # loop over friend
    print(follower.name)

print(user.followers_count) # get the number of followers
for friend in user.friends(): # loop over Sykzen friend
   print(friend.screen_name)   #print the @friendname
#-----------------get timeline tweet-------------------------
for tweet in timeline:
    print(f"{tweet.user.name} said {tweet.text}") #print(tweet.user.name,"said", tweet.text)
#------tweet a msg----------------------
api.update_status("Test tweet from Tweepy Python")
#---------follow quelqu'un-----------------
api.create_friendship("realpython")
#--------------changer sa description -----------------------
api.update_profile(description="I like Python")
#----------------------like a tweet------------------
tweet=api.get_user('Sykzen') 
api.create_favorite(tweet.id)
#------------------------------like tweet et follow personne  a partir d'un tweet-----
#tweet=le tweet
tweet.favorite() #like
tweet.user.follow() # follow la personne
# par exemple en peut loop sur un dictionnaire de tweet et liker ceux avec le mot "python"
#------ CURSOR-----------------------
for tweet in tweepy.Cursor(api.home_timeline).items(100):
    print(f"{tweet.user.name} said: {tweet.text}")
#--------------------Voir les utulisateurs bloquée----------------------------
for block in api.blocks():
    print(block.name)
#-------------------tout les tweet donc api est mentionée -----------------------------
tweets = api.mentions_timeline()
#---------------------récup les 10 derniers tweet avec le mot "sykzen"---------------
for tweet in api.search(q="Sykzen", lang="fr", rpp=10):
    print(f"{tweet.user.name}:{tweet.text}")
#---------------Récup les tweet tendance du monde-----------------
trends_result = api.trends_place(1) # le 1 veut dire dans tout le monde
for trend in trends_result[0]["trends"]:
    print(trend["name"])
# pour cherche dans une zone précise
woeid=3369
trends_result = api.trends_place(id=woeid)
for trend in trends_result[0]["trends"]:
    print(trend["name"])
#on récupere les id en utulisant
api.trends_available()
#or
def fetchCountry(Country):
    for i,e in enumerate(api.trends_available()):
        if i['name']==Country:
            return i['woeid']
#then:
woeid=fetchCountry("Paris")
trends_result = api.trends_place(id=woeid)
#-------------------------Récup des tweet en temps réel------------------
class MyStreamListener(tweepy.StreamListener):
    
    def __init__(self, api):
        self.api = api
        self.me = api.me()
        
    def on_status(self, tweet):
        print(f"{tweet.user.screen_name}:{tweet.text}")
        
    def on_error(self, status):
        print("Error detected")
#puis
tweets_listener = MyStreamListener(api)
stream = tweepy.Stream(api.auth, tweets_listener)
stream.filter(track=["Python", "Django", "Tweepy"], languages=["en"])
