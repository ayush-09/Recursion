# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 21:47:57 2021

@author: Ayush
"""

def gP(ans,oc,cc,n):
    if oc==n and cc==n:
        print(ans)
        return
    if oc<n:
        gP(ans+'(',oc+1,cc,n)
    if oc>cc:
        gP(ans+')',oc,cc+1,n)
        
if __name__=="__main__":
    gP("",0,0,3)
    