#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 09:03:32 2017

@author: KELLY
"""

import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from scipy.stats import norm

def problem1(N,n):
    myArr=[]
    for i in range(1,N):
        W=np.random.uniform(1,3,n)
        S=sum(W)
        myArr.append(S)
        mu=np.mean(myArr)
        sigma=np.std(myArr)

    num_bins = 30
    j, bins, patches = plt.hist(myArr, num_bins, normed=1)
    y = mlab.normpdf(bins, mu, sigma)
    plt.plot(bins, y)
    plt.title('PDF of book stack height and comparison with Gaussian')
    plt.xlabel('book stack for height n=%s books'%(n))
    plt.ylabel('PDF')
    
def problem2(N):
    beta=0.5
    myArr=[]
    for i in range(1,N):
        x=np.random.exponential(beta)
        myArr.append(x)
    num_bins = 25
    j, bins, patches = plt.hist(myArr, num_bins, normed=1)
    y = 2*np.exp(-2*bins)
    plt.plot(bins,y)
    plt.title('PDF of 2e^(-2x) and comparison with Gaussian')
    plt.xlabel('2e^(-2x) for beta=%s'%(beta))
    plt.ylabel('PDF')
    
def problem3(N):
    beta=45
    myArr=[]

    for i in range(1,N):    
        W=np.random.exponential(beta,24)
        S=sum(W)
        myArr.append(S)
        mu=24*beta
        sigma=beta*np.sqrt(24)

    num_bins = 50
    fig1=plt.figure(1)
    j, bins, patches = plt.hist(myArr, num_bins, normed=1)
    y = mlab.normpdf(bins, mu, sigma)
    plt.plot(bins, y)
    plt.title('PDF for One Carton of 24 Batteries and Comparison with Gaussian')
    plt.xlabel('Lifetime for a Carton of 24 Batteries')
    plt.ylabel('PDF')
    
    be1=bins[0:np.size(bins)-1]     
    be2=bins[1:np.size(bins)] 
    b1=(be1+be2)/2 
    barwidth=b1[1]-b1[0]
    
    CDF=np.cumsum(j)*barwidth
    fig2=plt.figure(2)
    myPlot=plt.bar(b1, CDF, width=barwidth)
    plt.title('CDF of the Lifetime of a Carton')
    plt.xlabel('Cumulative Lifetime for a Carton of 24 Batteries')
    plt.ylabel('CDF')
    
    y_value1 = np.interp(1095, CDF, b1)
    y_value2 = np.interp(912, CDF, b1) - np.interp(730, CDF, b1)
    #test=1-myPlot[1095].get_ydata()
    print(y_value1)
    print(y_value2)
    
    print(norm.cdf(1095))

