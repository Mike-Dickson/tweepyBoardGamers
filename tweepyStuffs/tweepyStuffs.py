import tweepy
from tweepy import OAuthHandler

## All the important information you were asked to collect from Twitter
twitterKey = 'B5JXoSxcJfKlo2YrfgViYZOsy'
twitterSecret = 'iT0sfzFLgmfpYUzbbKo6hipCLZvH85oNgPjWLKmZoV6TTGlUYX'
accessToken = '1111444476654833666-CfVFuU483RnGbIOsKAM2ctoqPGnTQb'
accessSecret = 'd0Fsa3BGJhCBkWv7TA9kgzQSWEv5CG6YnR9DYyuGOSwKN'

##Authenticate your app
auth = OAuthHandler(twitterKey, twitterSecret)
auth.set_access_token(accessToken, accessSecret)

## Opens a connection to twitter - respecting rate limits (so you don't get stopped)
apiAccess = tweepy.API(auth, wait_on_rate_limit=True)
count = 0
## q is your search string.  lang is the language you want.  count tells the system how much to
##  bring back per call.  .items takes a value that represents the total number of items you
##  want back.
for tweet in tweepy.Cursor(apiAccess.search, q='#boardgames -filter:retweets, -filter:images', lang='en', tweet_mode='extended').items(20):
    """print(tweet.text)"""
    count += 1
    print("Tweet number: " + str(count))
    print(tweet.user.name)
    print(tweet.user.location)
    print(tweet.user.friends_count)
    print(tweet.user.followers_count)
    print(tweet.full_text)
    print()