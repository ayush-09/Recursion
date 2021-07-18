# -*- coding: utf-8 -*-
"""
Created on Sun Jul 18 18:10:03 2021

@author: Ayush
"""

a=[]
def xToend(s,n,curr):
    if curr>=n:
        return
    st = s[curr]
    if st != 'x':
        a.append(st)
    xToend(s, n, curr+1)
    if st=='x':
        a.append('x')
    return 

if __name__=="__main__":
    s=input()
    xToend(s, len(s), 0)
    for i in range(len(a)):
        print(a[i],end="")
    