from helper import *
from preprocess import *

cp("importing modules")

test = [
    "who lives in a pineapple under the sea?",
    "how to get over my ex"
]

vec, model = load("BernoulliNB_2")
test = get_vectorized_test_x(test, vec)

y_pred = model.predict(test)
print(y_pred)