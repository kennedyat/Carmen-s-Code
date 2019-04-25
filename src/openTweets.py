import gzip


from pathlib import Path

def openLine():
    data_folder = Path(r"C:\Users\ktpenny\Desktop\Carmen-s-Code\data")
    file_to_open = data_folder / "nusample.json"
    tweetLines = ""

    #f = open(file_to_open)
    #print(f.read())

    answer = {}
    with open(file_to_open,'rt') as f:
        for line in f:
            tweetLines= "".join([tweetLines," \n"+ line])
            print(line)
    return tweetLines
openLine();
