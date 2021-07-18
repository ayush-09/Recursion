# -*- coding: utf-8 -*-
"""
Created on Sun Jul 18 17:56:24 2021

@author: Ayush
"""

def chrFormatter(s,curr):
    if curr+1>=len(s):
        return s
    if s[curr]==s[curr+1]:
        s=s[0:curr+1]+"*"+s[curr+1:]
    return chrFormatter(s, curr+1)

if __name__=="__main__":
    s=input()
    print(chrFormatter(s, 0))