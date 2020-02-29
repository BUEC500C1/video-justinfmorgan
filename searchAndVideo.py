import tweepy
import urllib.request
import subprocess
from textToImage import captionImage
import configparser
import os

config = configparser.ConfigParser()
config.read('keys')
auth = tweepy.OAuthHandler(config.get('auth', 'consumer_key').strip(),
                           config.get('auth', 'consumer_secret').strip())

auth.set_access_token(config.get('auth', 'access_token').strip(),
                      config.get('auth', 'access_secret').strip())

#####Tweepy API Authentication stuff#######
# auth = tweepy.OAuthHandler(keys.consumer_key, keys.consumer_secret)
# auth.set_access_token(keys.access_token, keys.access_token_secret)

api = tweepy.API(auth)

### Modifying this to take in a twitter username and take the first 10 tweets from their feed
### Use Tweepy to search twitter for the first image with a tweet related to the search term
def searchTwitter(searchTerm, numTweets, startNum):
    #####Getting the image URL from Tweepy#####
    if (numTweets > 100):
        print("Number of tweets must be less than 100")
        return -1
    imageUrl = ''
    fileName = "resources/imageFile.jpg"
    tweetText = ''
    tweetUrl = ''

    imageList = []
    alreadyTried = []
    textList = []
    urlList = []

    finalImageList = []
    finalImageNames = []
    finalText = []
    finalUrls = []

    for tweet in tweepy.Cursor(api.search, q=searchTerm).items(numTweets):
        try:
            # Grabbing the imageUrl, tweetText, and the tweetUrl from the tweepy JSON generated
            imageUrl = str(tweet._json['entities']['media'][0]['media_url_https'])
            tweetText = str(tweet._json['text'])
            tweetUrl = str(tweet._json['entities']['media'][0]['url'])

            imageList.append(imageUrl)
            textList.append(tweetText)
            urlList.append(tweetUrl)
        except(tweepy.TweepError, KeyError):
            pass

    nameCounter = startNum*100
    for k in range(len(imageList)):
        # Save the image at the URL to a file
        fileName = "resources/imageGen/img" + "{0:0=3d}".format(nameCounter) + ".png"
        if(imageList[k] not in alreadyTried):
            nameCounter+=1
            try:
                urllib.request.urlretrieve(imageList[k], fileName)
                finalImageList.append(imageList[k])
                finalText.append(textList[k])
                finalUrls.append(urlList[k])
                finalImageNames.append(fileName)
            except(ValueError):
                print("Unable to find an image associated with the terms requested.")
                return -1
        alreadyTried.append(imageList[k])

    for imagePath in finalImageNames:
        captionImage(imagePath, finalText[finalImageNames.index(imagePath)])

    return finalImageList, finalText, finalUrls

def makeVideo(start_number, outputName):
    subprocess.run(["ffmpeg", "-y", "-framerate", "1", "-s", "1920x1080", "-loglevel", \
        "quiet", "-start_number", str(start_number*100), "-i", "resources/imageGen/img%03d.png", "-vf", "pad=ceil(iw/2)*2:ceil(ih/2)*2", \
        "-vcodec", "libx264", "-pix_fmt", "yuv420p", str(outputName)], stdout=subprocess.PIPE)

def searchAndMakeVideo(searchTerm, numTweets, startNum, outputName):
    searchTwitter(searchTerm, numTweets, startNum)
    makeVideo(startNum, outputName)