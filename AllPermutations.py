# -*- coding: utf-8 -*-
"""
Created on Sun Jul 18 21:52:49 2021

@author: Ayush
"""
def allPer(s,out):
    if len(s)==0:
        print(out)
    
    for i in range(len(s)):
        c = s[i]
        allPer(s[0:i]+s[i+1:], out+c)

if __name__=="__main__":
    s=input()
    allPer(s, "")