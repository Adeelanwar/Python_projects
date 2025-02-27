6# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 10:56:51 2019

@author: Adeel
"""
seen1 = {1:1}
seen89 = {}
def digsq(n):
    digsum = 0
    while n != 0:
        digsum += (n % 10) ** 2
        n = int(n / 10)
    return digsum

for i in range(1,101):

    print(str(i) + "->",end="")

    temp = digsq(i)

    while temp != 1 and temp != 89 :

        print(str(temp) + "->",end="")

        temp = digsq(temp)

    print(str(temp) + "\n")


for i in range(1,10**7):
    counter = 0
    temp = digsq(i)
    while temp != 1 and temp != 89:
        temp = digsq(temp)
        if seen89[temp] != None:
            if temp == 89: 
                counter += 1
print(counter)
    
