#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 09:24:17 2017

@author: KELLY
"""
#import numpy as np
import random

P0=0.4
P1=1-P0
E0=0.02
E1=0.03

def calculate():
    m=random.uniform(0,1)
        
    if m <= P0:
        S=0
    else:
        S=1
        
    t=random.uniform(0,1)
    
    if S==0 and t<=E0:
        R=1
    elif S==0 and t>E0:
        R=0
    elif S==1 and t>E1:
        R=1
    elif S==1 and t<=E1:
        R=0
    
    return S, R
    
def problem1(N):    
    success=0
    for x in range (0,N):
        S,R=calculate()
            
        if S!=R:
            success+=1
        #test output
        #print('success:',success)
        #print(S)
        #print(R)
    print('probability', success/N)
        
    #testoutput  
    #print(m)
    #print(t)    
    
def problem2(N):
    Sis1=0
    success=0
    for x in range (0,N):
        S,R=calculate()
        
        if S==1:
            Sis1+=1
        if R==1 and S==1:
            success+=1
        #test output
        #print('success:',success)
        #print(S)
        #print(R)
    print(success)
    print(Sis1)
    print('probability', (success/Sis1))   
    
def problem3(N):
    success=0
    Ris1=0
    
    for x in range (0,N):
        S,R=calculate()
            
        if R==1:
            Ris1+=1
        if R==1 and S==1:
            success+=1
        #test output
        #print('success:',success)
        #print(S)
        #print(R)
    print(success)
    print(Ris1)
    print('probability', (success/Ris1))     
    
def problem4(N):
    failure=0
    success=0
    
    for x in range (0,N):
        S=[]
        R=[]
        m=random.uniform(0,1)
                
        if m <= P0:
            for x in range (0,3):
                S.append(0)
        else:
            for x in range (0,3):
                S.append(1)
        for x in range (0,3):
            t=random.uniform(0,1)
            
            if S[x]==0 and t<=E0:
                R.append(1)
            elif S[x]==0 and t>E0:
                R.append(0)
            elif S[x]==1 and t>E1:
                R.append(1)
            elif S[x]==1 and t<=E1:
                R.append(0)
        
        if S.count(0)==3 and R.count(0)>=2:
            D=0
            success+=1
        elif S.count(1)==3 and R.count(1)>=2:
            D=1
            success+=1
        else:
            D=None
            failure+=1
        #test output    
        #print(S) 
        #print(R)
        #print('D: ', D)
    print('sucesss', success) 
    print('failures: ', failure)
    print('probability', failure/N)
    
    #This voting or "majority" method of R provides a small improvement to problem 1 because it 
    #allows a larger margin of error. if 1/3 transmissions of R is incorrect, R is still correct
    #due to the majority method, while problem 1 is very strict whether it is correct or incorrect.
            
    