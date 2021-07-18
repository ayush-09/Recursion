# -*- coding: utf-8 -*-
"""
Created on Sun Jul 18 16:46:23 2021

@author: Ayush
"""
arr=[]
def sub(s,curr):
    if len(s)==0:
        arr.append(curr)
        return 
    sub(s[1:],curr+s[0])
    sub(s[1:],curr)
    
if __name__=="__main__":
    s=input()
    sub(s,"")
    for i in reversed(range(len(arr))):
        print(arr[i],end=" ")
    print()
    print(len(arr))