"""
provides helper functions eg. time functions etc.
"""

import os
import sys
import pickle
from time import time, sleep
from random import random, randrange as rr, shuffle, sample
from sklearn.utils import shuffle as skshuffle

t_ = [time()]

def clear():
    os.system("cls")

def r(n,dp=4):
    return round(n,dp)

e = enumerate

def cp(string="",t=t_,edge="-"*60, end=False):
    now = time()
    timetaken = r(now-t_[-1])
    if end:
        string = "total time taken"
        timetaken = r(now-t_[0])
    string = edge+" "+f"{string} --> {timetaken} seconds"
    print(string,"-"*(160-len(string)))
    t_.append(now)

def cpend():
    cp(end=True)

def pbar(i,num_iter,dp=1):
    i += 1
    perc = r(min(i*100/num_iter,100),dp)
    num = int(perc)
    print(f"[{'#'*num}{'-'*(100-num)}] {perc} %"+dp*" ", end="\r")

def mkdir(dirname="saved"):
    try:
        os.listdir(dirname)
    except:
        os.system("mkdir "+dirname)

def load(filename):
    mkdir()
    return pickle.load(open(f"saved/{filename}.sav","rb"))

def dump(thing, filename):
    mkdir()
    pickle.dump(thing, open(f"saved/{filename}.sav","wb"))

DATA = "/projects/datasets/"
DATA2 = "E:/datasets/"
cp("start")

