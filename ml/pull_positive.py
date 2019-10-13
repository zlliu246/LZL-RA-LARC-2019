import os
import pandas as pd

filepath = "../../OLD_STUFF/old_data"

for i,p in enumerate(os.listdir(filepath)[::-1]):
    data = pd.read_csv(f"{filepath}/{p}").loc[:,"post_title"].values

    with open(f"positive_{p}.csv","w") as f:
        for row in data:
            try:
                f.write(f"{row}\n")
            except:
                pass

    print(p)
            
