# processes and cleans text, used by scrape/main.py
from string import punctuation
from app.NLP.helper import *
e = enumerate

"""
turns raw text from response into a hopefully legitimate answer
input: 
    - query     - question asked by customer
    - text      - raw text from response given by scraping script
    - size      - window size of pool of words
output: hopefully legitimate answer to query
"""
def process(query, text="", size=30):
    """
        removing punctuation from query
    """
    query = "".join([i for i in query if i not in punctuation])

    """
    keywords - significant words within query
    """
    keywords = list(set(query.split(" ")) - stopwords)

    """
    cleans text (using NLP/helper.py) and splits text by space
    text is now a list of words
    """
    text = (text.encode("ascii", "ignore")).decode("utf-8")
    text = [w for w in clean(text).split(" ") if len(w)>0]# and w in english_words]
    
    """
    splits text (a list of words) into
    a list of (list of words of size {2*size})
    """
    text = split_list(text, size=size)
    
    """
    ==========================================================================
    RANKING ALGORITHM STARTS HERE
    ==========================================================================

    assigns a score to each sublist
    scoring algorithm:
        total number of times keyword appears inside sublist
    """
    best_score, best_index = -1,-1
    for i,row in e(text[:-1]):
        temp = row + text[i+1]
        score = count_keywords(keywords, temp)

        if score > best_score:
            best_score = score
            best_index = i

    output = []

    """
    Using the best section index (index and index+1),
        find 
            1) closest end of sentence from (index-1) onwards
            2) closest end of sentence from (index+2) onwards
        
        to return a sentence that
            encompasses the 2 best pools of size {size}
            is a complete sentence

        *** at this point, text is a (list of (list of words))
    """
    start,end = 0,len(text) # in case best_index is at the start or at the end

    if best_index>0:
        start = best_index-1
        while not target_contains(target=text[start], lis=list(".?")) and start>0:
            start -= 1
    else:
        output.append(".")

    if best_index+2<len(text):
        end = best_index+2
        while not target_contains(target=text[end], lis=list(".?")) and end+2<len(text):
            end += 1

    try:
        assert start>=0 and end<len(text)
    except:
        start=0
        end=len(text)-1

    for i in range(start, end+1):
        output.extend(text[i])



    """
        multiply score by percentage of english words
    """

    english_word_score = len([word for word in output if word in english_words])/len(output)

    output = " ".join(output)

    """selecting start of first bucket to end of last bucket"""
    start = 0
    end = len(output)-1

    try: start = output.index(".")
    except: pass

    try: end = output.rindex(".")
    except: pass

    answer = output[start+1:end+1].strip()

    return answer, best_score*english_word_score**3
