import requests
from bs4 import BeautifulSoup
from googlesearch import search

from time import sleep, time
from app.NLP.text_processor import process

"""
input:  given url
output: longest piece of text within div within response
"""
def scrape(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    divs = soup.find_all("div")
    text = ""
    for div in divs:
        if len(div.text) > len(text):
            text = div.text

    return text

"""
input: 
    query       - what end user wants to ask
    num_results - number of results to return
output:
    list of json: 

    {
        response:   string containing answer
        score:      given_score,
        time taken: time taken to process this 
        url:        original url
    }
"""
def search_google(query, num_results=5):
    a = time()
    output = []

    query = "".join([ch for ch in query.lower() if ch in "abcdefghijklmnopqrstuvwxyz '"])

    for url in search(query, stop=num_results*2, pause=0, only_standard=True):
        """
        process from NLP/text_processor.py used here
        """
        response, score = process(query, scrape(url), size=50)
        answer = {"response": response, "score": score, "time taken": time()-a, "url":url}
        
        if len(response)>0:
            output.append(answer)

        if len(output) >= num_results:
            break

    return sorted(output, key=lambda x:x["score"], reverse=True)
