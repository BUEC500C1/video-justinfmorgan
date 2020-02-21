import io
import tweepy
import keys
import urllib.request
import json

#####Tweepy API Authentication stuff#######
auth = tweepy.OAuthHandler(keys.consumer_key, keys.consumer_secret)
auth.set_access_token(keys.access_token, keys.access_token_secret)

api = tweepy.API(auth)

### Modifying this to take in a twitter username and take the first 10 tweets from their feed
### Use Tweepy to search twitter for the first image with a tweet related to the search term
def searchTwitter(searchTerm):
    #####Getting the image URL from Tweepy#####
    imageUrl = ''
    fileName = "resources/imageFile.jpg"
    tweetText = ''
    tweetUrl = ''

    for tweet in tweepy.Cursor(api.search, q=searchTerm).items(50):
        try:
            # Grabbing the imageUrl, tweetText, and the tweetUrl from the tweepy JSON generated
            imageUrl = str(tweet._json['entities']['media'][0]['media_url_https'])
            tweetText = str(tweet._json['text'])
            tweetUrl = str(tweet._json['entities']['media'][0]['url'])
        except(tweepy.TweepError, KeyError):
            pass

    # Save the image at the URL to a file
    try:
        urllib.request.urlretrieve(imageUrl, fileName)
    except(ValueError):
        print("Unable to find an image associated with the terms requested.")
        return -1

    return (imageUrl, fileName, tweetText, tweetUrl)