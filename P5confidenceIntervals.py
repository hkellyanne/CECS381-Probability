#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 08:51:02 2017

@author: KELLY
"""
import random
import numpy as np
import matplotlib.pyplot as plt

def problem1():
    N=1000000
    mu=75
    ro=7.5
    B=mu+np.random.randn(N)*ro
    Y=[]
    mn=[]
    for n in range(1,200):
        X=B[random.sample(range(N), n)]
        Y.append(n)
        mn.append(np.mean(X))
        stdDev=np.std(X)
        
    fig1=plt.figure(1)    
    plt.plot(mu+(1.96*(ro/np.sqrt(Y))), 'r--', lw=2)
    plt.plot(mu-(1.96*(ro/np.sqrt(Y))), 'r--', lw=2)
    plt.axhline(y=mu, color='k')
    plt.scatter(Y,mn, marker='x')
    plt.title('Sample Means and 95% Confidence Intervals')
    plt.xlabel('Sample Size')
    plt.ylabel('x bar')
    #
    fig2=plt.figure(2)
    plt.plot(mu+(2.58*(ro/np.sqrt(Y))), 'r--', lw=2, color='g')
    plt.plot(mu-(2.58*(ro/np.sqrt(Y))), 'r--', lw=2, color='g')
    plt.axhline(y=mu, color='k')
    plt.scatter(Y,mn, marker='x')
    plt.title('Sample Means and 99% Confidence Intervals')
    plt.xlabel('Sample Size')
    plt.ylabel('x bar')
        