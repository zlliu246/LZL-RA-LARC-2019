# https://python-googlesearch.readthedocs.io/en/latest/

from googlesearch import search
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import time

def scrape(url, headless=True):
    options = Options()
    options.add_argument("--headless")
    if headless:
        driver = webdriver.Chrome(chrome_options=options)
    else:
        driver = webdriver.Chrome()

    driver.get(url)

    text = ""
    try:
        for div in driver.find_elements_by_tag_name("div"):
            if len(div.text) > len(text):
                text = div.text
    except:
        return "url"

    driver.quit()
    return text


def search_google(query):
    a = time()
    output = []
    for j in search(query, stop=5, pause=0, only_standard=True):
        output.append({"response": scrape(j), "time taken": time()-a, "url":j})
    return output
