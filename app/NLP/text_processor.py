from NLP.helper import *
e = enumerate

def process(query, text="", size=25):
    keywords = list(set(query.split(" ")) - stopwords)
    text = [w for w in clean(text).split(" ") if len(w)>0]# and w in english_words]
    text = split_list(text, size=size)
    
    best_score, index = -1,-1

    for i,row in e(text[:-1]):
        temp = row + text[i+1]
        score = count_keywords(keywords, temp)

        if score > best_score:
            best_score = score
            index = i

    output = []

    start,end = 0,len(text)
    if index>0:
        start = index-1
        while "." not in text[start] and start>0:
            start -= 1
    else:
        output.append(".")

    if index+2<len(text):
        end = index+2
        while "." not in text[end] and end+2<len(text):
            end += 1


    for i in range(start, end+1):
        output.extend(text[i])

    output = " ".join(output)

    start = output.index(".")
    end = output.rindex(".")

    return output[start+1:end].strip(), best_score
    # return output


