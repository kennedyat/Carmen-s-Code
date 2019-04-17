import json
from pathlib import Path

import json

tweets = []
dict = {}
i = 0
for line in open(r'C:\Users\ktpenny\Desktop\Carmen-s-Code\data\nusample.json'):

    tweets.append(dict.update({json.loads(line)}))
    print (tweets)
    #d = json.load(json_data)
    #print(type(d))
    #print(type(d[0]))
    #print(json.dumps(d[0], indent=2))
# example
