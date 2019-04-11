from pathlib import Path

def findLocation():
    data_folder = Path(r"C:\Users\ktpenny\Desktop\Carmen-s-Code\data")
    file_to_open = data_folder / "nusample"


    #f = open(file_to_open)
    #print(f.read())
    with open(file_to_open,'rt') as f:
        for line in f:
            start = line.find('"place_type":')
            end = line.find('"attributes"', start)
            print(line[start:end])
findLocation()
