"""
provides helper functions for preprocess.py to process text
"""

import re
import nltk
from string import punctuation
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from nltk.stem import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer

stopwords = set(stopwords.words("english"))
tokenizer = RegexpTokenizer(r"\w+")
lem = WordNetLemmatizer()

def remove_punctuation(string):
    return "".join([i for i in string if i not in punctuation])

def tokenize(string):
    return tokenizer.tokenize(string)

def remove_stopwords(lis):
    return [i for i in lis if i not in stopwords]

"""
input: sentence
output: processed list of words
"""
def clean(string):
    string = string.lower()
    list_words = remove_stopwords(tokenize(remove_punctuation(string)))
    return " ".join([lem.lemmatize(i) for i in list_words])

