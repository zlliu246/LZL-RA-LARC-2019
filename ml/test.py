from helper import *
from helper.table import Table
from preprocess import *

import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score

cp("importing modules")

MODEL_NAME = "LogisticRegression_7"
TEST_FILENAME = "test.csv"
DELIMITER = ","

test = pd.read_csv(TEST_FILENAME, delimiter=DELIMITER)

x_test, y_test = test.iloc[:,0].values, test.iloc[:,1].values

vec, model = load(MODEL_NAME); cp("pickle loading")

x_test = get_vectorized_test_x(x_test, vec)
y_pred = model.predict(x_test)
questions = pd.read_csv(TEST_FILENAME, delimiter=DELIMITER).iloc[:,0].values

acc = accuracy_score(y_pred, y_test)
pre = precision_score(y_pred, y_test)
rec = recall_score(y_pred, y_test)

# option to show wrong entries only
SHOW_WRONG_ONLY = False

try:
    arg = sys.argv[1]
    """
        arg = "--wrong-only" --> 
    """

    if arg.strip() == "--wrong-only":
        SHOW_WRONG_ONLY = True
except:
    pass

if SHOW_WRONG_ONLY:
    a,b,c = [],[],[]
    for question, actual, pred in zip(questions, y_test, y_pred):
        if actual != pred:
            a.append(question)
            b.append(actual)
            c.append(pred)   

    questions, y_test, y_pred = a,b,c

# printing out in structured table format
table = Table()
table.setTable({
    "Question": questions,
    "Actual": y_test,
    "Predicted": y_pred
})

print()
table.show()

print("*** Accuracy score:", acc, "***")
print("*** Precision score:", pre, "***")
print("*** Recall score:", rec, "***\n")
print("="*160)