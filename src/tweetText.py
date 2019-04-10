import gzip

import re

def tweetText():
        data_folder = Path(r"C:\Users\ktpenny\Desktop\Carmen-s-Code\data")
        file_to_open = data_folder / "nusample"


        #f = open(file_to_open)
        #print(f.read())
        with open(file_to_open,'rt') as f:
            for line in f:
                #start = line.find('"text"') + 3
                 #end = line.find('"source"', start)
                 #print(line[start:end])
                 m = re.search('text(.+?)source', line)
                 if m:found = m.group(1)
tweetText();
#print(openTweets.openLine())
