frompath = "raw/negative"
topath = "data/negative"

import pandas as pd

data = pd.read_csv(f"{frompath}/train.csv").loc[:,"question_text"]

error = 0
with open(f"{topath}/quora.csv","w") as f:
    for row in data.values:
        try:
            f.write(row.lower()+"\n")
        except:
            error += 1    

print("done", error)
