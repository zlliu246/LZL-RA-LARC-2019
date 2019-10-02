import requests
from bs4 import BeautifulSoup
from googlesearch import search

from time import sleep, time
from NLP.text_processor import process

def scrape(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    divs = soup.find_all("div")
    text = ""
    for div in divs:
        if len(div.text) > len(text):
            text = div.text

    return text

def search_google(query, num_results=5):
    a = time()
    output = []
    for url in search(query, stop=num_results, pause=0, only_standard=True):
        response, score = process(query, scrape(url), size=25)
        output.append({"response": response, "score": score, "time taken": time()-a, "url":url})
    return sorted(output, key=lambda x:x["score"], reverse=True)

# query = "am i a rebound"
# url = 'https://www.insider.com/signs-youre-someones-rebound-2019-1'

# print(process(query, text=scrape(url), size=25))
