# -*- coding: utf-8 -*-
"""
Created on Sat Jul 17 19:20:05 2021

@author: Ayush
"""

def ways(curr,n):
    if curr==n:
        return 1
    if curr>n:
        return 0
    c1=ways(curr+1, n)
    c2 = ways(curr+2, n)
    return c1+c2
print(ways(0, 35))

def ways1(n):
    if n==0:return 1
    if n<0:return 0
    c1 = ways1(n-1)
    c2 = ways1(n-2)
    return c1+c2

print(ways1(3))