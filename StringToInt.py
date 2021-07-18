# -*- coding: utf-8 -*-
"""
Created on Sun Jul 18 17:48:15 2021

@author: Ayush
"""

def strToint(s):
    if len(s)==1:
        return int(s[0])
    y= strToint(s[1:])
    x = int(s[0])
    x = int(x*pow(10,len(s)-1)+y)
    return x

if __name__=="__main__":
    s=input()
    print(strToint(s))