# -*- coding: utf-8 -*-
"""
Created on Sat Jul 17 14:01:31 2021

@author: Ayush
"""

def fact(n,ans): # return while pushing the stack
    if n==0 or n==1:
        print(ans)
        return
    fact(n-1,n*ans)
    
if __name__=="__main__":
    fact(5,1)