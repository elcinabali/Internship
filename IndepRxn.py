#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 21:40:56 2023

@author: elcininmacbookairi
"""


from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt


"x1 <--> x2"

def rxn1(c,t):
    
    dx1dt = (r[1]*c[1]) - (r[0]*c[0])
    dx2dt = (r[0]*c[0]) - (r[1]*c[1])
    
    return [dx1dt, dx2dt]

t = np.linspace(0,20,100)
c_init1 = [4,0] # sets initial conc. of x1 and x2
r = [1.1,1.1] # sets r1 and r2

c_x1x2 = odeint(rxn1, c_init1, t) #1. column = x1, 2. column = x2 

plt.plot(t, c_x1x2[:,0], 'r--', label='x1')
plt.plot(t, c_x1x2[:,1], 'g--', label='x2')


"x2 <--> x3"

def rxn2(c,t):
    
    # dx1dt = (r[1]*c[1]) - (r[0]*c[0])
    dx2dt = (r2[1]*c[1]) - (r2[0]*c[0])
    dx3dt = (r2[0]*c[0]) - (r2[1]*c[1])
    
    return [dx2dt, dx3dt]
t = np.linspace(20,30,100)
c_init2 = [c_x1x2[-1,1], 2] # takes the latest conc. of x2 and sets initial conc. of x3
r2 = [2, 0.2857] # sets  r3 and r4
c_final = odeint(rxn2, c_init2, t) # 1. column = x1, 2. column = x2, 3. column = x3
print('c_final:', c_final)

# plt.plot(t, c_final[:,0], 'r--')
plt.plot(t, c_final[:,0], 'g--')
plt.plot(t, c_final[:,1], 'b--', label='x3')
plt.legend()
plt.grid()
plt.xlabel('time')
plt.ylabel('concentration')

# plt.savefig('[X3] > [X1] > [X2], r3 > r1 > r2 > r4.pdf')
