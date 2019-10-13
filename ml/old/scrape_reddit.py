cn = "_eYtD2XCVieq6emjKBH3m"

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get("https://www.reddit.com/r/AskReddit/controversial")

driver.find_element_by_css_selector("#layoutSwitch--compact > svg").click()

body = driver.find_element_by_tag_name("body")


questions = set()

for i in range(500):
    body.send_keys(Keys.PAGE_DOWN)
    print(i+1,end="\r")
    
    sleep(1)

    qs = driver.find_elements_by_class_name(cn)
    for q in qs:
        questions.add(q.text)

print("\n\n"+"="*150,"\n")

questions = list(questions)

print(len(questions))

with open("data/negative/reddit.csv","a") as f:
    for q in questions:
        try:
            f.write(q + "\n")
        except:
            pass

driver.quit()