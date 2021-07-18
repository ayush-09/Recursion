# -*- coding: utf-8 -*-
"""
Created on Sat Jul 17 13:47:33 2021

@author: Ayush
"""

def fact(n): # result while pop the stack
    if n==0 or n==1:
        return 1
    return n * fact(n-1)

if __name__=="__main__":
    print(fact(5))