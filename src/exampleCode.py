import json
from pathlib import Path

import json


with open(r'C:\Users\ktpenny\Desktop\Carmen-s-Code\data\nusample.json') as json_data:

    datastore = json.load(json_data)
    print (datastore["place"])

    #d = json.load(json_data)
    #print(type(d))
    #print(type(d[0]))
    #print(json.dumps(d[0], indent=2))
# example
