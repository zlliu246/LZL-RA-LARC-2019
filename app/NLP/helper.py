import nltk
from nltk.corpus import stopwords

stopwords = set(stopwords.words("english"))

english_words = set()
with open("words_alpha.txt") as f:
    for line in f:
        english_words.add(line.strip().lower())

for ch in ".,?":
    english_words.add(ch)

def clean(text):
    for i in ".,?():[]/-":
        text = text.replace(i,f" {i} ")
    for i in "\"\n\t":
        text = text.replace(i,"")
    return text.lower()

def split_list(lis, size=25):
    return [lis[i*size:(i+1)*size] for i in range(len(lis)//size+1)]

def word_not_contain(word, lis):
    for ch in lis:
        if ch in word:
            return False
    return True

def count_keywords(keywords, target):
    total = 0
    for w in keywords:
        total += target.count(w)
    return total