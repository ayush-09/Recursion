# -*- coding: utf-8 -*-
"""
Created on Sun Jul 18 14:04:51 2021

@author: Ayush
"""

def isSort(arr,n):
    if n==0 or n==1:
        return True
    if arr[n-2]>arr[n-1]:
        return False
    sa = isSort(arr, n-1)
    return sa

if __name__=="__main__":
	n=int(input())
	arr = list(input().split()[:n])
    print(isSort(arr,n))