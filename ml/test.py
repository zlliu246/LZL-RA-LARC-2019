from helper import *
from helper.table import Table
from preprocess import *

import pandas as pd
from sklearn.metrics import accuracy_score

cp("importing modules")

test = pd.read_csv("test.csv")

x_test, y_test = test.iloc[:,0].values, test.iloc[:,1].values

vec, model = load("BernoulliNB_7"); cp("pickle loading")

x_test = get_vectorized_test_x(x_test, vec)
y_pred = model.predict(x_test)

# printing out in structured table format
table = Table()
table.setTable({
    "Question": pd.read_csv("test.csv").iloc[:,0].values,
    "Actual": y_test,
    "Predicted": y_pred
})

print()
table.show()

print("*** Accuracy score:", accuracy_score(y_pred, y_test), "***\n")
print("="*160)

