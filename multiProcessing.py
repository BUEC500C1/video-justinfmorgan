from helloVideo import *
from multiprocessing import Pool

# searchTerms = [["golden retriever", 50, 0],["labradoodle", 50, 100], ["tibetan mastiff", 50, 200],
#         ["beagle", 50, 300], ["french bulldog", 50, 400]]


# def mapHelper(p):
#     output = searchAndMakeVideo(p)
#     return output

if __name__ == '__main__':
    files = glob.glob('resources/imageGen/*')
    for f in files:
        os.remove(f)

    p = Pool(5)
    p.starmap(searchAndMakeVideo, [["golden retriever", 100, 0, "golden.mp4"],
        ["labradoodle", 100, 100, "labradoodle.mp4"], 
        ["tibetan mastiff", 100, 200, "mastiff.mp4"],
        ["beagle", 100, 300, "beagle.mp4"], 
        ["bulldog", 100, 400, "bulldog.mp4"]])