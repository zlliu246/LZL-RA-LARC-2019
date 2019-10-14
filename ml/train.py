from helper import *
from helper.text_preprocessor import *
from preprocess import *

cp("importing modules")

x_train, x_test, y_train, y_test = get_tts_xy("training_data/train2.csv"); cp("preprocessing")

from sklearn.naive_bayes import BernoulliNB
from sklearn.metrics import accuracy_score as acc

nb = BernoulliNB()
nb.fit(x_train, y_train)
y_pred = nb.predict(x_test)

print(acc(y_pred, y_test))

cpend()