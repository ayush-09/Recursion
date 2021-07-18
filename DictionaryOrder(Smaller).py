# -*- coding: utf-8 -*-
"""
Created on Sun Jul 18 19:53:27 2021

@author: Ayush
"""
a=[]
def dictionaryOrder(s,ans):
    if len(s)==0:
        a.append(ans)
        return
    for i in range(len(s)):
        ch = s[i]
        remain = s[0:i]+ s[i+1:]
        dictionaryOrder(remain, ans+ch)
        
if __name__=="__main__":
    s=input()
    dictionaryOrder(s, "")
    a= sorted(a)
    for i in range(len(a)):
        if a[i]!= s:
            print(a[i],end="")
            print()
        else:
            break
        