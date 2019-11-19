from helper import *
from preprocess import *

from sklearn.naive_bayes import BernoulliNB
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression

""" the following algoithms takes an inhibitively long time to train with poor results comparatively """
"""
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.neural_network import MLPClassifier
"""

from sklearn.metrics import accuracy_score as acc

Model = LogisticRegression

cp("importing modules")

for NUM in [1,2,3,4,5,6,7]:
    cp(f"start preprocessing {NUM}")
    x_train, x_test, y_train, y_test = get_vectorized_tts_xy(f"training_data/train{NUM}.csv")
    cp(f"finished preprocessing {NUM}")

    cp(f"start training {NUM}")
    model.fit(x_train, y_train)
    cp(f"finished training {NUM}")

    y_pred = model.predict(x_test)

    print(f"train{NUM}",acc(y_pred, y_test))

    # saving model into "saved" folder 
    TARGET_NAME = str(model.__class__)[:-2].split(".")[-1] + "_" + str(NUM)

    dump((vec,model), f"{TARGET_NAME}")

    print(f"pickle dumped train{NUM}\n")

cpend()

