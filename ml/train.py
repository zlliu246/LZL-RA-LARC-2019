from helper import *
from preprocess import *

cp("importing modules")

NUM = 5

x_train, x_test, y_train, y_test = get_vectorized_tts_xy(f"training_data/train{NUM}.csv"); cp("preprocessing")

from sklearn.naive_bayes import BernoulliNB
from sklearn.metrics import accuracy_score as acc

model = BernoulliNB()
model.fit(x_train, y_train)
y_pred = model.predict(x_test)

print(acc(y_pred, y_test))

# saving model into "saved" folder 
TARGET_NAME = str(model.__class__)[:-2].split(".")[-1] + "_" + str(NUM)

dump((vec,model), f"{TARGET_NAME}")

cpend()