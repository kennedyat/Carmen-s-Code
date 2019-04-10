import gzip
from pathlib import Path
import re

def tweetText():
        data_folder = Path(r"C:\Users\ktpenny\Desktop\Carmen-s-Code\data")
        file_to_open = data_folder / "nusample"


        #f = open(file_to_open)
        #print(f.read())
        with open(file_to_open,'rt') as f:
            for line in f:
                start = line.find('"text":') + 7
                end = line.find('"source"', start)
                print(line[start:end])

tweetText()
#print(openTweets.openLine())
