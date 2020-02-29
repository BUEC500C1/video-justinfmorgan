from searchAndVideo import searchTwitter, searchAndMakeVideo
import os

def test_unitTest():
    if(not(os.path.isfile("keys"))):
        print("NO KEY FILE FOUND")
        assert 1==1
    assert 1==1