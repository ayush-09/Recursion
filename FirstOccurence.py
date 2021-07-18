# -*- coding: utf-8 -*-
"""
Created on Sat Jul 17 17:21:42 2021

@author: Ayush
"""

def firstOccur(arr,n,curr,s):
    if curr==n:
        return -1
    if arr[curr]==s:
        return curr
    res = firstOccur(arr, n, curr+1, s)
    return res
if __name__=="__main__":
    n=int(input())
    arr=[]
    for i in range(n):
        arr.append(input())
    s=input()
    print(firstOccur(arr, n, 0, s))
    