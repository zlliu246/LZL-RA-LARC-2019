# processes and cleans text, used by scrape/main.py

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
def process(query, text="", size=25):
    """
    keywords - significant words within query
    """
    keywords = list(set(query.split(" ")) - stopwords)

    """
    cleans text (using NLP/helper.py) and splits text by space
    text is now a list of words
    """
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

    output = " ".join(output)

    start = output.index(".")
    end = output.rindex(".")

    return output[start+1:end].strip(), best_score


# #testing code here
# query = "how to tell if he is cheating"
# text = "\n\n\n\n\n\n \n\n\n\n\n15 Definite Signs He\u2019s Cheating On You\n\n\n\n\n\n\n\n\n\nby Sabrina Alexis\nJune 26, 2019 \n\n\n\n\n\nTweet\nTweet\nCheating is generally considered the ultimate betrayal and the most difficult issue to bounce back from in a relationship. This is because trust is so critical \u2026 it\u2019s the foundation a relationship is built on. If you can\u2019t trust a man to be honest with you, then everything else you try to build together will just fall apart.\n\n\r\nwdfq.cmd.push( function(){\r\nvar displayOnDevices = ['desktop'];\r\nif(displayOnDevices.indexOf(device) >= 0) {\r\n    googletag.cmd.push(function() { googletag.display('div-gpt-ad-ANewMode_Desktop_Rectangle_A'); });\r\n}\r\n} );\r\n\n\n\n\n\r\nwdfq.cmd.push( function(){\r\nvar displayOnDevices = ['tablet'];\r\nif(displayOnDevices.indexOf(device) >= 0) {\r\n    googletag.cmd.push(function() { googletag.display('div-gpt-ad-ANewMode_Tablet_Rectangle_A'); });\r\n}\r\n} );\r\n\n\n\n\n\r\nwdfq.cmd.push( function(){\r\nvar displayOnDevices = ['mobile'];\r\nif(displayOnDevices.indexOf(device) >= 0) {\r\n    googletag.cmd.push(function() { googletag.display('div-gpt-ad-ANewMode_Mobile_Rectangle_A'); });\r\n}\r\n} );\r\n\n\nIt\u2019s natural not to want to admit it could be happening to you, so you may ignore the signs. Or maybe the signs are there and you\u2019re willing to see them, but you don\u2019t even know what to look for.\nOn the other hand, if you\u2019ve been cheated on before and this is a major issue for you, you may know the signs all too well. This can be a good thing because you\u2019ll be able to recognize what\u2019s going on quickly and get out, or it can be a bad thing because you\u2019re hypersensitive and zeroing in on non-issues because of the trauma in your past, so insecurity and paranoia take over.\nMORE: The\u00a0Real Reason Men Cheat\u00a0\nSometimes it helps to set aside your emotions as much as possible. Maybe that means temporarily letting go of your fear that you could lose everything you have with him if you\u2019re right, or your anxiety that it could be happening to you all over again. Set aside those feelings for just a minute and look logically at his behavior, and you can get to the answer you need.\nOne or two of these signs might not mean anything, but if they start piling up, you need to take the possibility that he might be cheating on you very seriously.\n\nTake The Quiz: Is He Losing Interest?\nClick here to take our quick (and shockingly accurate) \u201cIs He Losing Interest\u201d Quiz right now and find out if he\u2019s really losing interest in you...\n\nDoes he spend time with you as often as he used to? (Question\u00a01\u00a0of\u00a015)\n\n\n\n\n\n\n\n\n\n\n\nYes, but he never seems to want to be there.\n\n\n\n\n\n\nI don't know. I'm so confused. I just want the spark back.\n\n\n\n\n\n\nNo, he never spends time with me. It's like I don't exist. He spends more time doing random things. Internet, friends, work, etc.\n\n\n\n\n\n\nYes, he used to do things I liked, but now he could care less.\n\n\n\n\n\n\nYes, he spends the same amount of time with me as he always has.\n\n\nContinue\nHere Are 15 Signs Your Man Might Be Cheating On You:\n1. He\u2019s on his phone or online more than usual\n\n\u00a0\n\n\r\nwdfq.cmd.push( function(){\r\nvar displayOnDevices = ['desktop'];\r\nif(displayOnDevices.indexOf(device) >= 0) {\r\n    googletag.cmd.push(function() { googletag.display('div-gpt-ad-ANewMode_Desktop_Rectangle_B'); });\r\n}\r\n} );\r\n\n\n\n\n\r\nwdfq.cmd.push( function(){\r\nvar displayOnDevices = ['tablet'];\r\nif(displayOnDevices.indexOf(device) >= 0) {\r\n    googletag.cmd.push(function() { googletag.display('div-gpt-ad-ANewMode_Tablet_Rectangle_B'); });\r\n}\r\n} );\r\n\n\n\n\n\r\nwdfq.cmd.push( function(){\r\nvar displayOnDevices = ['mobile'];\r\nif(displayOnDevices.indexOf(device) >= 0) {\r\n    googletag.cmd.push(function() { googletag.display('div-gpt-ad-ANewMode_Mobile_Rectangle_B'); });\r\n}\r\n} );\r\n\n\nIf he\u2019s suddenly glued to his phone, watch out. This is a major concern, especially if he\u2019s sneaky about it. If he doesn\u2019t tell you who he\u2019s talking to or what he\u2019s doing and gets mad if you ask him or happen to glance at his phone, this is a red flag.\nA man who\u2019s 100% into the relationship and doesn\u2019t have another woman in the mix will have nothing to hide. He won\u2019t be constantly texting someone else and acting funny about it.\nIf you feel like his attention is always elsewhere, either directed at his phone or the computer, then he could be connecting with someone else online. If he acts defensive about it, won\u2019t tell you more, and tries to hide it from you, this is a sign he\u2019s cheating or about to cheat.\n\u00a0\n\n2. Cares about his appearance much more than usual\nIf he suddenly takes a renewed interest in his appearance when you\u2019re in an established relationship, he\u2019s probably not trying to impress you.\nHas he joined a gym out of the blue? Is he trying to lose weight? If he never had an interest in working out before, he could be preening to try to attract someone new.\nIs he trying out a more updated hairstyle? Shopping for new clothes and dressing differently? Maybe wearing a different cologne, one you didn\u2019t choose for him?\n\n\r\nwdfq.cmd.push( function(){\r\nvar displayOnDevices = ['desktop'];\r\nif(displayOnDevices.indexOf(device) >= 0) {\r\n    googletag.cmd.push(function() { googletag.display('div-gpt-ad-ANewMode_Desktop_Rectangle_C'); });\r\n}\r\n} );\r\n\n\n\n\n\r\nwdfq.cmd.push( function(){\r\nvar displayOnDevices = ['tablet'];\r\nif(displayOnDevices.indexOf(device) >= 0) {\r\n    googletag.cmd.push(function() { googletag.display('div-gpt-ad-ANewMode_Tablet_Rectangle_C'); });\r\n}\r\n} );\r\n\n\n\n\n\r\nwdfq.cmd.push( function(){\r\nvar displayOnDevices = ['mobile'];\r\nif(displayOnDevices.indexOf(device) >= 0) {\r\n    googletag.cmd.push(function() { googletag.display('div-gpt-ad-ANewMode_Mobile_Rectangle_C'); });\r\n}\r\n} );\r\n\n\nThese are all common behaviors of men when they\u2019re trying to attract women (you may remember some of them from when you first started dating him!) and don\u2019t really mesh with how a guy acts when he\u2019s already in an established relationship.\nIs it possible he just wants to feel good about himself and maybe impress you? Yes, of course. You can\u2019t take any of these signs in a vacuum. You need to take the whole picture into account.\nMORE: How to Tell If Your Boyfriend is Cheating on You\n3.\u00a0 He\u2019s suddenly very busy with work\nIf he suddenly has to travel out of town more frequently, or he\u2019s having a lot more late nights at the office, it could be cause for concern.\nIf he\u2019s recently been promoted or his job has changed somehow, this might not be something to worry about. But if you know that\u2019s not the case and he\u2019s exhibiting some of the other signs here as well, it\u2019s a definite cause for concern.\nIs he going out after work more frequently for happy hours with people from the office? If there\u2019s a new woman at work this could be a way for him to spend time with her off the clock and away from the office, to get to know her on a more personal level. If he never went to work happy hours before and suddenly starts going regularly, it could be a sign he\u2019s testing the waters to cheat.\nIt\u2019s also possible he\u2019s using \u201cwork\u201d as a cover for whatever he\u2019s out there doing. Saying you have to work is a tough excuse to argue with.\n\n\r\nwdfq.cmd.push( function(){\r\nvar displayOnDevices = ['desktop'];\r\nif(displayOnDevices.indexOf(device) >= 0) {\r\n    googletag.cmd.push(function() { googletag.display('div-gpt-ad-ANewMode_Desktop_Rectangle_D'); });\r\n}\r\n} );\r\n\n\n\n\n\r\nwdfq.cmd.push( function(){\r\nvar displayOnDevices = ['tablet'];\r\nif(displayOnDevices.indexOf(device) >= 0) {\r\n    googletag.cmd.push(function() { googletag.display('div-gpt-ad-ANewMode_Tablet_Rectangle_D'); });\r\n}\r\n} );\r\n\n\n\n\n\r\nwdfq.cmd.push( function(){\r\nvar displayOnDevices = ['mobile'];\r\nif(displayOnDevices.indexOf(device) >= 0) {\r\n    googletag.cmd.push(function() { googletag.display('div-gpt-ad-ANewMode_Mobile_Rectangle_D'); });\r\n}\r\n} );\r\n\n\nMORE: Why Do Guys Cheat?\u00a0\n4. He avoids intimacy with you\n\nThis is not the same as avoiding sex, this is about demonstrating affectionate and loving behavior.\nIf a man is cheating because he\u2019s in love with someone new, it could make him feel like he\u2019s cheating on his new love with you if he\u2019s affectionate and loving with both of you, especially if he\u2019s a loyal guy by nature and cheating is something new for him.\nEven if he\u2019s not in love with the person he\u2019s cheating with, someone engaging in infidelity can feel uncomfortable behaving intimately with a girlfriend because it runs counter to their cheating behavior.\nUnless he\u2019s a total sociopath, he probably still has feelings for you, and that will make him feel guilty. Showing loving behavior toward you when he\u2019s cheating on you would make him feel even worse.\nMORE: 7 Telltale Signs He\u2019s Not in Love Anymore\n\n5. Avoids having sex with you \u2026 or wants it all the time\nSex is a form of intimacy, so if he\u2019s avoiding sex with you it could tie into the previous point."

# print(process(query, text=text, size=25))
