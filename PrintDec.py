# -*- coding: utf-8 -*-
"""
Created on Sat Jul 17 14:24:45 2021

@author: Ayush
"""

def PrintDec(n):
    if n==0:
        return
    print(n)
    PrintDec(n-1)
    
if __name__=="__main__":
    PrintDec(5)
    