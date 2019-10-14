# helper module for NLP/text_processor.py

import nltk
from nltk.corpus import stopwords
import re

e = enumerate

# set of stopwords from nltk library
stopwords = set(stopwords.words("english"))

# set of all english words (dk if exhaustive) read from words_alpha.txt (from github)
english_words = set()
with open("app/words_alpha.txt") as f:
    for line in f:
        english_words.add(line.strip().lower())

# adding ".", "," and "?" into set of english words so they count
for ch in ".,?":
    english_words.add(ch)


"""
turns raw text into more machine-processable text
input: raw text from scrape - includes html and javascript nonsense
output: cleaned text (str)
  - html and javascript codes are removed
  - everything becomes lowercase
  - spaces are inserted between words and punctuation
"""
def clean(text):
    text = [i.strip().lower() for i in text.split("\n") if len(i)>1]
    
    """
    inputs:
        para        - paragraph whose validity is to be tested
        min_len     - para must have more than {min_len} words to be considered valid
        threshold   - {threshold} % of words in para must be english words for text to be valid
    
    output: whether this paragraph is valid (bool: can be part of final answer) 
    """
    def is_valid(para, min_len=5, threshold=0.8):
        """
        if any of characters in "{}[]:" are inside a section, return invalid (False)
        """
        for ch in "}{][:":
            if ch in para:
                return False

        """
        para is now a list of words (split by space)
        """
        para = [i for i in para.split(" ") if len(i)>0]

        if len(para) < min_len:
            return False

        """
        counting number of words in para that is in the english_words set
        """
        score = 0
        for w in para:
            if re.sub("[.,?-]","",w) in english_words:
                score += 1

        """
        if num english words / total words < threshold --> return invalid (False)
        """
        if score/len(para) < threshold:
            return False

        return True

    """
    Filter paragraphs that are valid  
    """
    valid = []
    for para in text:
        if is_valid(para):
            valid.append(para)

    valid = " ".join(valid)

    """
    insert space between words and punctuation for easier processing     
    """
    for ch in ".,?:":
        valid = valid.replace(ch, f" {ch} ")

    """
    returns a (str) giant paragraph - collection of valid paragraphs
    """
    return valid



"""
turns list of words into list of (list of words of size {size})

input: 
    lis     - list of words
    size    - size of each sublist 

output: each sublist will be at most size {2*size}
    eg. [
        [apple, orange, pear],
        [apple, pineapple, x],
        ...
    ]
"""
def split_list(lis, size=25):
    return [lis[i*size:(i+1)*size] for i in range(len(lis)//size+1)]

"""
counts total number of times a keyword appears in target
input: 
    keywords    - list of keywords
    target      - target list
output:
    total number of times each keyword appears in sublist
"""
def count_keywords(keywords, target):
    total = 0
    for w in keywords:
        total += target.count(w)
    return total

"""
checks if target contains any of the elements found in lis

input:
    target  - target to check
    lis     - list of characters to be checked

output: bool
"""
def target_contains(target=[], lis=[]):
    for ch in lis:
        if ch in target:
            return True
    return False
