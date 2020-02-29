from searchAndVideo import searchTwitter, searchAndMakeVideo
from multiprocessing import Pool
import sys
import os
import glob
import tweepy

if __name__ == '__main__':

    if(len(sys.argv) < 2):
        sys.exit("Please provide at least one search term in quotes as an argument. Quitting.\n")

    # Remove all files currently in the folder
    files = glob.glob('resources/imageGen/*')
    for f in files:
        os.remove(f)

    # Remove the DS store file on mac if present
    if os.path.exists("resources/imageGen/.DS_Store"):
        os.remove("resources/imageGen/.DS_Store")

    numTweets = 100

    # Create a list of lists of the function arguments required to starmap
    # to searchAndMakeVideo
    videoFunctionArguments = []
    for argIndex in range(len(sys.argv)-1):
        currentarg = []
        # Skip over first argument to avoid the script name
        currentarg.append(str(sys.argv[argIndex+1]))
        currentarg.append(numTweets)
        currentarg.append(argIndex)
        currentarg.append(str(sys.argv[argIndex+1]) + ".mp4")
        videoFunctionArguments.append(currentarg)

    # Run multiprocessing on the arguments
    # try:
    p = Pool(len(sys.argv)-1)
    p.starmap(searchAndMakeVideo, videoFunctionArguments)
    # except tweepy.error.TweepError:
    #     sys.exit("Tweepy request rate limit exceeded. Quitting.\n")