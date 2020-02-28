from helloVideo import *
from multiprocessing import Pool
import sys

# searchTerms = [["golden retriever", 50, 0],["labradoodle", 50, 100], ["tibetan mastiff", 50, 200],
#         ["beagle", 50, 300], ["french bulldog", 50, 400]]


# def mapHelper(p):
#     output = searchAndMakeVideo(p)
#     return output

if __name__ == '__main__':

    # Remove all files currently in the folder
    files = glob.glob('resources/imageGen/*')
    for f in files:
        os.remove(f)

    numTweets = 100

    try:
        p = Pool(5)
        p.starmap(searchAndMakeVideo, [["golden retriever", numTweets, 0, "golden.mp4"],
            ["labradoodle", numTweets, 1, "labradoodle.mp4"], 
            ["tibetan mastiff", numTweets, 2, "mastiff.mp4"],
            ["pomeranian", numTweets, 3, "pomeranian.mp4"], 
            ["shiba inu", numTweets, 4, "shiba.mp4"]])
    except tweepy.error.TweepError:
        sys.exit("Tweepy request rate limit exceeded. Quitting.\n")