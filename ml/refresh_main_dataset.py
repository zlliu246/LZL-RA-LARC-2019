import pandas as pd
from random import sample, shuffle

num = 10000

output = []
pos, neg = [], []

with open("data/positive.csv") as f:
    for line in f:
        pos.append(line.strip())

with open("data/negative.csv") as f:
    for line in f:
        neg.append(line.strip())

output.extend([(i,1) for i in sample(pos,num)])
output.extend([(i,0) for i in sample(neg,num)])

shuffle(output)

with open("main.csv","w") as f:
    for i,j in output:
        i = i.replace(",","")
        f.write(f"{i},{j}\n")
