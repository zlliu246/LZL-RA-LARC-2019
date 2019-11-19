"""
transforms text into tfidf-vectorised sparse matrices
"""

e = enumerate
import pandas as pd
from sklearn.model_selection import train_test_split
from helper.text_preprocessor import *
from sklearn.feature_extraction.text import TfidfVectorizer

vec = TfidfVectorizer()

def get_vectorized_tts_xy(filepath):
    data = pd.read_csv(filepath, encoding = "ISO-8859-1")

    x = data.iloc[:,0].values
    y = data.iloc[:,1]

    for i,q in e(x):
        x[i] = clean(q)

    x_train, x_test, y_train, y_test = train_test_split(x,y, shuffle=True)

    x_train = vec.fit_transform(x_train)
    x_test = vec.transform(x_test)

    return x_train, x_test, y_train, y_test

def get_vectorized_test_x(lis, vec):
    for i,val in e(lis):
        lis[i] = clean(val)
    return vec.transform(lis)

"""
    get vectotized train test split for bigram
    input: .csv file
    output: x_train, x_test, y_train, y_teset
        - bigram and tfidf-vectorized
"""
def get_vectorized_tts_xy_bigram(filepath):
    data = pd.read_csv(filepath, encoding = "ISO-8859-1")

    x = data.iloc[:,0].values
    y = data.iloc[:,1]

    for i,q in e(x):
        x[i] = clean(q)

    x_train, x_test, y_train, y_test = train_test_split(x,y, shuffle=True)

    x_train = vec.fit_transform(x_train)
    x_test = vec.transform(x_test)

    return x_train, x_test, y_train, y_test