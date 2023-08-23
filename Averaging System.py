#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 13:03:18 2023

@author: elcininmacbookairi
"""

from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

"x1 <--> x2"

def calculate_r_and_s(N):
   
    r = 1.1
    s = (r * N) - r

    return [r, s]

def rxn1(c,t):
    
    dx1dt = (k[1]*c[1]) - (k[0]*c[0])
    dx2dt = (k[0]*c[0]) - (k[1]*c[1])
    
    return [dx1dt, dx2dt]

t = np.linspace(0,20,100)
c_init1 = [4,0] # sets initial conc. of x1 and x2

N = len(c_init1)
k = calculate_r_and_s(N) #k[0]=r (r1) and k[1]=s (r2)

c_x1x2 = odeint(rxn1, c_init1, t) #1. column = x1, 2. column = x2

print('c_x1x2:', c_x1x2)
print('k:', k)

plt.plot(t, c_x1x2[:,0], 'r--', label='x1')
plt.plot(t, c_x1x2[:,1], 'g--', label='x2')


'x2 + x3 --> 2x3'
'x3 --> x2'

def treshold_rxn(c,t):
    dx2dt = (-alpha*c[0]*c[1]) + (beta*c[1])
    dx3dt = (alpha*c[0]*c[1]) - (beta*c[1])
    
    return [dx2dt, dx3dt]

t = np.linspace(20,30,100)
c_init2 = [c_x1x2[-1,1], 0.1] # takes the latest conc. of x2 and sets initial conc. of x3
alpha = 2
beta = 1
c_x2x3 = odeint(treshold_rxn, c_init2, t) #1. column = x2, 2. column = x3
print('c_x2x3:', c_x2x3)


plt.plot(t, c_x2x3[:,0], 'g--')
plt.plot(t, c_x2x3[:,1], 'b--', label='x3')
plt.legend()
plt.grid()
plt.xlabel('time')
plt.ylabel('concentration')

