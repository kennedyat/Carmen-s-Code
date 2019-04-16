from pathlib import Path
from openTweets import file_to_open

def findLocation():

    #f = open(file_to_open)
    #print(f.read())
    locations = {}
    i = 0
    with open(file_to_open,'rt') as f:
        for line in f:
            start = line.find('"location":')
            end = line.find('"url"', start)
            #locations["tweet" + str(i) + " Location"] =

            print(line[start:end])
findLocation()
