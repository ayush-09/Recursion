# -*- coding: utf-8 -*-
"""
Created on Sat Jul 17 14:18:11 2021

@author: Ayush
"""

def PrintInc(n):
    if n==0:
        return
    PrintInc(n-1)
    print(n)
    
if __name__=="__main__":
    PrintInc(5)
    