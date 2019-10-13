# from lzl.helper import *
import os
import pandas as pd

data = pd.read_csv("raw/negative/questions.csv").loc[:,["question1", "question2","is_duplicate"]].values

lis = []

def valid(string):
    string = string.lower()
    blacklist = "relationship boyfriend girlfriend rebound marry sexual".split(" ")
    for word in blacklist:
        if word in string:
            return False
    return True

def clean(string):
    return string.lower()

error = 0
for a,b,dup in data:
    try:
        if dup == 0:
            if valid(a):
                lis.append(clean(a))
            if valid(b):
                lis.append(clean(b))
        else:
            if valid(a):
                lis.append(clean(a))
    except:
        error += 1

print(error)

error = 0

with open("data/negative.csv","w") as f:
    for row in lis:
        try:
            f.write(row+"\n")
        except:
            error += 1

print(len(lis), error)
