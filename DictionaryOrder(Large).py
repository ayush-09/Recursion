# -*- coding: utf-8 -*-
"""
Created on Sun Jul 18 21:44:41 2021

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
    temp=False
    for i in range(len(a)):
        if a[i]== s:
            temp=True
        elif(temp):
            print(a[i],end="")
        