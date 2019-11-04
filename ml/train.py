from helper import *
from preprocess import *
# from sklearn.naive_bayes import BernoulliNB
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score as acc

cp("importing modules")

for NUM in [1,2,3,4,5,8,9]:
    x_train, x_test, y_train, y_test = get_vectorized_tts_xy(f"training_data/train{NUM}.csv"); cp("preprocessing")

    model = LogisticRegression()
    model.fit(x_train, y_train)
    y_pred = model.predict(x_test)

    print(f"train{NUM}",acc(y_pred, y_test))

    # saving model into "saved" folder 
    TARGET_NAME = str(model.__class__)[:-2].split(".")[-1] + "_" + str(NUM)

    dump((vec,model), f"{TARGET_NAME}")

    print(f"pickle dumped train{NUM}")

cpend()

