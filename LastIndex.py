# -*- coding: utf-8 -*-
"""
Created on Sun Jul 18 17:22:56 2021

@author: Ayush
"""

def last(arr,s,curr):
    if curr<0:
        return -1
    if arr[curr]==s:
        return curr
    return last(arr,s,curr-1)
if __name__=="__main__":
    n=int(input())
    arr=[]
    for i in range(n):
        arr.append(input())
    s=input()
    print(last(arr, s, n-1))
    