import io
import tweepy
import keys
import urllib.request
import json
import subprocess

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

    numTweets = 100
    imageList = []
    alreadyTried = []
    textList = []
    urlList = []

    finalImageList = []
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


    for k in range(len(imageList)):
        # Save the image at the URL to a file
        fileName = "resources/imageFile" + str(k) + ".jpg"
        if(imageList[k] not in alreadyTried):
            try:
                urllib.request.urlretrieve(imageList[k], fileName)
                finalImageList.append(imageList[k])
                finalText.append(textList[k])
                finalUrls.append(urlList[k])
            except(ValueError):
                print("Unable to find an image associated with the terms requested.")
                return -1
        alreadyTried.append(imageList[k])

    return finalImageList, finalText, finalUrls

#ffmpeg -loop 1 -i img.jpg -c:v libx264 -t 30 -pix_fmt yuv420p out.mp4
def makeVideo(imageName):
    subprocess.run(["ffmpeg", "-loop", "1", "-i", imageName, "-c:v", "libx264" ,"-t",
    "30", "-pix_fmt", "yuv420p", "out.mp4"], stdout=subprocess.PIPE)

def main():
    searchTwitter("Cute Turtle")

if __name__ == "__main__":
    main()