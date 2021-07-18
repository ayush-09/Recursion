# -*- coding: utf-8 -*-
"""
Created on Sun Jul 18 19:15:26 2021

@author: Ayush
"""

def TeacherAlice(n):
    if n==1 or n==2:
        return n+1
    else:
        c1 = TeacherAlice(n-1)
        c2 = TeacherAlice(n-2)
        return c1+c2

if __name__=="__main__":
    T = int(input())
    for i in range(1,T+1):
        n = int(input())
        a = TeacherAlice(n)
        print("#"+str(i)+" : "+ str(a))
        