# -*- coding: utf-8 -*-
"""
Created on Sat Jul 17 17:50:34 2021

@author: Ayush
"""
def allOccur(arr,n,cur,s,c):
    if cur==n:
        a=[0]*int(c)
        if len(a)==0:
            print(-1)
        return a
    if arr[cur]==s:
        ra = allOccur(arr, n, cur+1, s,c+1)
        ra[c]=cur
        return ra
    else:
        ra = allOccur(arr, n, cur+1, s,c)
        return ra
        
if __name__=="__main__":
    ans = allOccur([1,2,3,2,5], 5, 0, 0, 0)
    for i in ans:
        print(i,end=" ")
