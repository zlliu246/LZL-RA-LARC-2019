# do this on desktop-LZL - contains large datasets non-pushable to git
import os
import pandas as pd
from random import sample, shuffle

num = 30000

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

with open(f"training_data/train{len(os.listdir('training_data'))+1}.csv","w") as f:
    f.write("questions,relationship_related\n")
    for i,j in output:
        i = i.replace(",","")
        f.write(f"{i},{j}\n")
