from helper import *
from preprocess import *

from sklearn.naive_bayes import BernoulliNB
from sklearn.linear_model import LogisticRegression

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

"""
    Doing manual k-fold cross validation as the sklearn version has some compatibility issues
"""

# with open("cross_validation_report","w") as f:
#     pass

def write(string):
    with open("cross_validation_report","a") as f:
        f.write(f"{string}")

cp("importing modules")

k = 10
DATASET_NUM = 2
Models = [
    ("logistic regression", LogisticRegression),
    ("naive bayes", BernoulliNB)
]

LONGEST_NAME_LENGTH = 0
for name,_ in Models:
    if len(name) > LONGEST_NAME_LENGTH:
        LONGEST_NAME_LENGTH = len(name)

for DATASET_NUM in [5,6,7]:

    write("="*200+"\n")
    write(f"Dataset number: {DATASET_NUM}, k={k}\n\n")

    print(f"{'='*50} PROCESSING {DATASET_NUM} {'='*50}")

    x_train, x_test, y_train, y_test = get_vectorized_tts_xy(f"training_data/train{DATASET_NUM}.csv")
    x_train = pd.DataFrame(x_train.toarray())
    pool_size = x_train.shape[0]//k
    pools = [(x_train.iloc[i*pool_size:(i+1)*pool_size,:], y_train.iloc[i*pool_size:(i+1)*pool_size]) for i in range(k)]

    for model_name, Model in Models:
        for i,(test_x, test_y) in e(pools):

            # print(pools)
            # input(f"{k} {type(k)} >>>")

            train_pools = [pools[j] for j in [j for j in range(k) if j!=i]]


            train_x = pd.concat([x for x,y in train_pools[1:]])
            train_y = pd.concat([y for x,y in train_pools[1:]])
            
            results = {}

            model = Model()
            model.fit(train_x, train_y)

            pred_y = model.predict(test_x)
        
            results = {
                "accuracy": accuracy_score(pred_y, test_y),
                "precision": precision_score(pred_y, test_y),
                "recall": recall_score(pred_y, test_y),
                "f1 score": f1_score(pred_y, test_y)
            }

            write(model_name + ":" + " "*(LONGEST_NAME_LENGTH-len(model_name)) + "\t")
            for key,val in results.items():
                write(f"{key}: {round(val,2)}, ")
            write("\n")
        write("\n")

    write("="*200)

    print(f"{'='*50} DONE WITH {DATASET_NUM} {'='*50}")
