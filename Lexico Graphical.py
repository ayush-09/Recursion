# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 22:14:46 2021

@author: Ayush
"""

def LexicoPrint(start,end):
    if start>end:
        return
    print(start)
    call=0
    if start==0:
        call=1
    while(call<=9):
        LexicoPrint(start*10+call, end)
        call+=1
LexicoPrint(0, 100)