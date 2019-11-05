import pandas as pd

data = pd.read_csv("training_data/train1.csv", encoding="ISO-8859-1")

pos = data[data["relationship_related"]==1].iloc[:5000,:]
neg = data[data["relationship_related"]==0].iloc[:5000,:]

data = pd.concat([pos, neg])
data = data.sample(frac=1)


data.to_csv("jingjing.csv", index=False)