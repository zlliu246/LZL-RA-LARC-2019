# checking the coefs of each saved model

from helper import *

vec, model = load("BernoulliNB_9")
cp("pickle loading vectorizer and model")

# top and bottom n words to get out
n = 10
voc = {val:key for key,val in vec.vocabulary_.items()}

coefs = [(i,v) for i,v in e(model.coef_[0])]
coefs.sort(key=lambda x:x[1], reverse=True)

top = [voc[i] for i,j in coefs[:n]]
bottom = [voc[i] for i,j in coefs[-1*n:]]

print("top:",top)
print("bottom:",bottom)