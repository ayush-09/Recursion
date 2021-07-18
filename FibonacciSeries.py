# -*- coding: utf-8 -*-
"""
Created on Sat Jul 17 19:02:34 2021

@author: Ayush
"""

def fibo(n):
    if n==0 or n==1:
        return n
    r1 = fibo(n-1)
    r2 = fibo(n-2)
    
    return r1+r2

print(fibo(7))