# -*- coding: utf-8 -*-
"""
Created on Sun Jul 18 15:12:47 2021

@author: Ayush
"""
c=[]
def asciiSe(s,curr,i):
    if i==len(s):
        if len(curr)>=0:
            print(curr,end=" ")
            c.append(1)
        return 
    char = s[i]
    asciiSe(s, curr, i+1)
    asciiSe(s, curr+char, i+1)
    asciiSe(s, curr+str(ord(char)), i+1)

if __name__=="__main__":
    s=input()
    asciiSe(s, "", 0)
    print()
    print(sum(c))
    
