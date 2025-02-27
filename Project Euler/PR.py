# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 10:23:35 2019

@author: Adeel
"""

def sumn(n):
    dic = {}
    while n != 0:
        try:
            dic[n % 10] += 1
        except KeyError:
            dic[n%10] = 1
            
        n = int(n / 10)
    return dic

for i in range(1,1000000000):
    if sumn(i).__eq__(sumn(2 * i)) and sumn(i).__eq__(sumn(3 * i)) and sumn(i).__eq__(sumn(4 * i)) and sumn(i).__eq__(sumn(5 * i)) and sumn(i).__eq__(sumn(6 * i)):
        print(i, 2*i , 3*i, 4*i, 5*i , 6*i)
