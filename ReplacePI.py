# -*- coding: utf-8 -*-
"""
Created on Sun Jul 18 16:21:42 2021

@author: Ayush
"""

def replacePI(s,curr):
    if curr+1>=len(s):
        return s
    if s[curr]=="p" and s[curr+1]=="i" and curr+1<len(s):
        s= s.replace("pi","3.14")
    return replacePI(s, curr+1)

if __name__=="__main__":
    n=int(input())
    for i in range(n):
        s= input()
        print(replacePI(s, 0))
    