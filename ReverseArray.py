# -*- coding: utf-8 -*-
"""
Created on Sat Jul 17 14:47:23 2021

@author: Ayush
"""

def reverse(arr,curr): #tail Recursion
    if curr==-1:
        return
    print(arr[curr],end=" ")
    reverse(arr, curr-1)
    
def reverse1(arr,curr1,n): #head Recursion
    if curr1==n:
        return
    reverse1(arr, curr1+1,n)
    print(arr[curr1],end=" ")
    
if __name__=="__main__":
    n=int(input())
    arr=[]
    for i in range(n):
        arr.append(input())
    curr1=0
    reverse(arr, n-1)
    print()
    reverse1(arr, curr1, n)