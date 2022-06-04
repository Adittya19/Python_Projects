# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 14:14:14 2022

@author: DELL
"""

def fact(n):
    if n==1:
        return n
    else:
        return n*fact(n-1)

print(fact(5))