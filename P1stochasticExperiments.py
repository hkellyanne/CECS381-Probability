# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import matplotlib.pyplot as plt
import numpy as np
import random

#given example
def test(N):
    d1=np.random.randint(1,7,size=N)
    d2=np.random.randint(1,7,size=N)
    s=d1+d2
    
    b=range(1,15)
    h1, bin_edges=np.histogram(s,bins=b)
    b1=bin_edges[0:13]
    plt.close('all')
    #
    fig1=plt.figure(1)
    plt.stem(b1,h1)
    plt.title('Stem plot - Sum of two dice')
    plt.xlabel('Sum of two dice')
    plt.ylabel('Number of occurences')
    #
    fig2=plt.figure(2)
    p1=h1/N
    plt.stem(b1,p1)
    plt.title('Stem plot - Sum of two dice: Probability mass function')
    plt.xlabel('Sum of two dice')
    plt.ylabel('Probability')
    
#how many times it will take to get to 7
def problem1(N):
    success=[]
    for x in range (0,N):
        count=1        
        d1 = np.random.randint(1,7)
        d2 = np.random.randint(1,7)
        s=d1+d2        
        while(s!=7):
            count+=1
            d1 = np.random.randint(1,7)
            d2 = np.random.randint(1,7)
            s=d1+d2
        success.append(count)
    #return success
    b=range(1,20)
    h1, bin_edges=np.histogram(success,bins=b)
    b1=bin_edges[0:18]
    plt.close('all')
    #
    fig1=plt.figure(2)
    p1=h1/N
    plt.stem(b1,p1)
    plt.title('Stem plot - Sum of two dice equals seven: Probability mass function')
    plt.xlabel('Rolls made until Sum=7')
    plt.ylabel('Probability')
   
#    
def problem2(N):
    count=0
    for x in range(0,N):
        coin=np.random.randint(0,2,100)
        heads=sum(coin)
        if(heads==50):
            count+=1       
        #test output    
        #print('heads: ', heads)
        #print('total success: ', count)
        #
    print('probability', count/N)

        
def problem3(N):
    from collections import namedtuple
    Card = namedtuple('Card', ['value', 'suit'])
    suits = ['hearts', 'diamonds', 'spades', 'clubs']
    deck = [Card(value, suit) for value in range(1,14) for suit in suits]
    success=0
    for x in range(0,N):
        card=random.sample(range(0,52), 5)
        hand=card
        for x in hand:
            count=0
            #test output
            #print(deck[x].value,'of',deck[x].suit)
            for y in hand:
                if deck[x].value==deck[y].value:
                    count+=1
        if count==4:
            success+=1
        #test output    
        #print ('count:',count)
        #print (hand)
        #print ('success:',success)
        #
    print('probability', success/N)
        
def problem4(N):
    import string
    success=0
    for x in range(0,N):
        hackersList=[]
        myPassword=''
        m=300900
        for x in range(0,m):
            candidate=''
            for y in range(0,4):
                x = random.choice(string.ascii_letters)
                candidate+=x.lower()
            hackersList.append(candidate)
        for z in range(0,4):
            a = random.choice(string.ascii_letters)
            myPassword+=a.lower()         
        count=hackersList.count(myPassword)
        if count>=1:
            success+=1
        #test output    
        #print (hackersList)
        #print (myPassword)
        #print ('password appears:',count)
    print ('success:',success)
    print('probability', success/N)

    
    



