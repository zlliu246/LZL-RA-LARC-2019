# checking the coefs of each saved model

from helper import *

vec, model = load("LogisticRegression_7")
cp("pickle loading vectorizer and model")

# top and bottom n words to get out
n = 30
voc = {val:key for key,val in vec.vocabulary_.items()}

coefs = [(i,v) for i,v in e(model.coef_[0])]
coefs.sort(key=lambda x:x[1], reverse=True)

top = [voc[i] for i,j in coefs[:n]]
bottom = [voc[i] for i,j in coefs[-1*n:]]

print("="*150)
print("top:",top)
print()
print("bottom:",bottom)
print()
print("="*150)