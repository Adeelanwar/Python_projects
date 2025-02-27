# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 10:51:26 2019

@author: Adeel
"""
def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)
def nCr(n, r):
    return fact(n) / (fact(r) * fact(n - r))
tsum = 0
for n in range(1,101):
    for r in range(1, n):
       if  nCr(n, r) > 10**6:
           tsum += 1
        