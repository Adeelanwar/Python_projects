# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import random

def rolldie():
    return random.choice([1,2,3,4,5,6])

def rolldies(n):
    diescount = {}
    for x in range(n):
        d1 = rolldie()
        d2 = rolldie()
        if diescount.get(d1 + d2) == None:
            diescount[d1 + d2] = 1
        else:
            diescount[d1 + d2] += 1
    return diescount
n = 10000000
results = rolldies(n)
for (key, value) in results.items():
    print (key, str((float(value)/float(n))*100) + "%")


    



