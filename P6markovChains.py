#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 21:37:27 2017

@author: kelly
"""
import random
import numpy as np
import matplotlib.pyplot as plt

def problem1():
    ## PROBLEM 1 - THREE STATE MARKOV CHAIN 
    N=10000                   
    n=15                       
    X=np.zeros((n,N),dtype=np.character)   
    M=np.zeros((n,3),dtype=np.float)         
#    S=np.chararray((n,1))
    #S[:]='a'
    #print(S)

    p11=1/3 
    p12=1/3 
    p13=1/3                  
    p21=1/2
    p22=0 
    p23=1/2 
    p31=1/4 
    p32=1/4 
    p33=1/2
    # 
    d01=1/4 
    d02=1/2 
    d03=1/4                  
    #
    #run for 10000times
    for j in range(0,N):
        S=np.chararray((n,1))
        r0=random.random();       
        if(r0<=d01):
            s0='R'     
        elif(r0>d01 and r0<=d01+d02):
            s0='N'    
        elif(r0>d01+d02):
            s0='S'    
        S[0]=s0             
        #
        for k in range(0,n-1):
            s=S[k]
            r=random.random()     
            if (s==b'R'):
                if (r<=p11):
                    S[k+1]='R'         
                elif (r>p11 and r<=p11+p12):
                    S[k+1]='N'        
                elif (r>p11+p12):
                    S[k+1]='S'        
            elif (s==b'N'):         
                if (r<=p21):
                    S[k+1]='R'         
                elif(r>p21 and r<=p21+p22):
                    S[k+1]='N'
                elif (r>p21+p22):
                    S[k+1]='S'
            elif (s==b'S'):
                if (r<=p31): 
                    S[k+1]='R'         
                elif (r>p31 and r<=p31+p32):
                    S[k+1]='N'
                elif (r>p31+p32):
                    S[k+1]='S'
        X[:,[j]]=S 
    #depending on probabilities and previous values, S is created
    #S will be placed in every column j of X
    #print(X)
    for j in range(0,n):
        x=X[j,:]
        ma=(x==b'R').sum()
        mb=(x==b'S').sum()
        mc=(x==b'N').sum()
        M[j,:]=[ma/N,mb/N,mc/N]
        
    fig1=plt.figure(1)
    stateR, = plt.plot(M[:,0], 'ob:', label = 'State R')
    stateN, = plt.plot(M[:,1], 'or:', label = 'State N')
    stateS, = plt.plot(M[:,2], 'og:', label = 'State S')
    plt.xticks(np.arange(0, 16, 1.0))
    plt.yticks(np.arange(0, .6, .1))
    plt.title('Simulation Results -- States R,N,S')
    plt.xlabel('Time step (n)')
    plt.ylabel('Prob(State)')
    plt.legend()    
    #
    P=np.matrix([[p11, p12, p13],
                  [p21, p22, p23],
                  [p31,p32,p33]])
    y0=[1/4, 1/2, 1/4]
    Y=np.zeros((n,3),dtype=np.float)   
    Y[[0],:]=y0
    for k in range(0,n-1):
        Y[[k+1],:]=Y[[k],:]*P
    #    
    fig2=plt.figure(2)
    stateR, = plt.plot(Y[:,0], 'ob:', label = 'State R')
    stateN, = plt.plot(Y[:,1], 'or:', label = 'State N')
    stateS, = plt.plot(Y[:,2], 'og:', label = 'State S')
    plt.xticks(np.arange(0, 16, 1.0))
    plt.yticks(np.arange(0, .6, .1))
    plt.title('Results based on State Transition Matrix -- States R,N,S')
    plt.xlabel('Time step (n)')
    plt.ylabel('Prob(State)')
    plt.legend()
    #
    fig3=plt.figure(3)
    stateR1, = plt.plot(M[:,0], 'ob:', label = 'State R1')
    stateN1, = plt.plot(M[:,1], 'or:', label = 'State N1')
    stateS1, = plt.plot(M[:,2], 'og:', label = 'State S1')
    stateR2, = plt.plot(Y[:,0], 'oc:', label = 'State R2')
    stateN2, = plt.plot(Y[:,1], 'oy:', label = 'State N2')
    stateS2, = plt.plot(Y[:,2], 'om:', label = 'State S2')
    plt.xticks(np.arange(0, 16, 1.0))
    plt.yticks(np.arange(0, .6, .1))
    plt.title('Comparison: Experimental simulation & State transition matrix')
    plt.xlabel('Time step (n)')
    plt.ylabel('Prob(State)')
    plt.legend()
    
def problem2():
    N=10000
    n=20
    X=np.zeros((n,N),dtype=np.character)   
    M=np.zeros((n,5),dtype=np.float)         
    S=np.chararray((n,0))
    
    P=np.matrix([[0, 1, 0, 0, 0],
                 [1/2, 0, 1/2, 0, 0],
                 [1/3, 1/3, 0, 0, 1/3],
                 [1, 0, 0, 0, 0],
                 [0, 1/3, 1/3, 1/3, 0]])
    print(P.shape)

    v=np.matrix([[1/5, 1/5, 1/5, 1/5, 1/5], #v1
                 [0, 0, 0, 0, 1]])          #v2
    
    labels=['A','B','C','D','E']

    for j in range(0,2):
        s0=v[[j],:]
        Y=np.zeros((n,5),dtype=np.float)   
        Y[[0],:]=s0
        for k in range(0,n-1):
            Y[[k+1],:]=Y[[k],:]*P
    
        nv=np.arange(0,n)
        
        fig1=plt.figure(j)
        for i in range(0,5):
            plt.plot(nv, Y[:,[i]], 'o:', label = labels[i])
        plt.xticks(np.arange(0, 21, 1.0))
        plt.yticks(np.arange(0, 1.2, .2))
        plt.title('Page Rank Probabilities')
        plt.xlabel('Time step (n)')
        plt.ylabel('Probability of page visit')
        plt.legend()    
        
    print(Y)
        
