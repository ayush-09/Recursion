# -*- coding: utf-8 -*-
"""
Created on Sun Jul 18 10:19:02 2021

@author: Ayush
"""

def boardPath(curr,dest):
    if curr==dest:
        return 1
    if curr>dest:
        return 0
    c1= boardPath(curr+1, dest)
    c2= boardPath(curr+2, dest)
    c3= boardPath(curr+3, dest)
    c4= boardPath(curr+4, dest)
    c5= boardPath(curr+5, dest)
    c6= boardPath(curr+6, dest)
    return c1+c2+c3+c4+c5+c6

if __name__=="__main__":
    print(boardPath(0, 10))