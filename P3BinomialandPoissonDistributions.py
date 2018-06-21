# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 17:26:54 2017

@author: KellyHall
"""

import matplotlib.pyplot as plt
import numpy as np
from numpy import random

def createGraph(success, N):   
    b=range(0,16)
    h1, bin_edges=np.histogram(success,bins=b)
    b1=bin_edges[0:15]
    plt.close('all')
    #
    p1=h1/N
    plt.stem(b1,p1)
    plt.title('Stem plot - Sum of three dice equals eighteen: Probability mass function')
    plt.xlabel('Count of times sum==18')
    plt.ylabel('Probability')
    

def problem1(N):
    success=[]
    for x in range (0,N):
        count=0
        for j in range (0,1000):
            r=np.random.randint(1,7,3)
            if sum(r)==18:
                count+=1
        success.append(count) 
    createGraph(success,N)

    
def problem2(N):
    n=1000           #number of times the die are tossed
    P=(1/6)**3       #probability of getting three sixes
    success=np.random.binomial(n, P, N)  
    createGraph(success,N)
    
def problem3(N):
    np = 1000*((1/6)**3) #lambda = np
    success=random.poisson(np, N)
    createGraph(success,N)
    
