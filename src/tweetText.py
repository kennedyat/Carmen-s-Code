import gzip
from pathlib import Path
import re

def tweetText():
        data_folder = Path(r"C:\Users\ktpenny\Desktop\Carmen-s-Code\data")
        file_to_open = data_folder / "nusample"

        dict = {}
        i = 0
                #f = open(file_to_open)
        #print(f.read())
        with open(file_to_open,'rt') as f:
            for line in f:
                i = i+1
                start = line.find('"text":') + 7
                end = line.find('"source"', start)
                dict["tweet" + str(i)] = line[start:end]
                print(dict["tweet"+ str(i)])

tweetText()
#print(openTweets.openLine())
