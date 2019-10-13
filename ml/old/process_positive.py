import os
import re
import pandas as pd

from lzl.helper import *

data = load("temp"); cp("loading data")

def valid(string):
    if "?" not in string:
        return False
    return True

def clean(string):
    return re.sub("[ ]{1,}"," ",re.sub(r"[\[\(].*?[\]\)]","", string)).lower()

data = [clean(i) for i in data if valid(i)]; cp("cleaning data")

with open("data/positive.csv","w") as f:
    for row in data:
        f.write(f"{row}\n")

cp("writing to csv")

cpend()




exit()
data = []
fp = "raw/positive"
for p in os.listdir(fp):
    try:
        with open(f"{fp}/{p}") as f:
            for line in f:
                data.append(line.strip())
        # print(len(data))
    except:
        print("oops")

from lzl.helper import *

dump(data,"temp")

print("done")