#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 20:32:32 2023

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

t = np.linspace(20,40,100)
c_init2 = [c_x1x2[-1,0], c_x1x2[-1,1], 2] # takes the latest conc. of x1, x2 and sets initial conc. of x3
r = [1, 3.9, 4.81, 0.7] # sets r1, r2, r3 and r4

"x2 <--> x3"

def rxn2(c,t):
    
    dx1dt = (r[1]*c[1]) - (r[0]*c[0])
    dx2dt = (r[0]*c[0]) + (r[3]*c[2]) - (r[1]*c[1]) - (r[2]*c[1])
    dx3dt = (r[2]*c[1]) - (r[3]*c[2])
    
    return [dx1dt, dx2dt, dx3dt]

c_final = odeint(rxn2, c_init2, t) # 1. column = x1, 2. column = x2, 3. column = x3
print('c_final:', c_final)

plt.plot(t, c_final[:,0], 'r--')
plt.plot(t, c_final[:,1], 'g--')
plt.plot(t, c_final[:,2], 'b--', label='x3')
plt.legend()
plt.grid()
plt.xlabel('time')
plt.ylabel('concentration')

# plt.savefig('[X3]=0 [X1]=1 > [X2]=0, r3=4 r1=0.5 0.1  r2=0.5 0.1 r4=4.pdf')

# plt.savefig(pathImage + r'{:.2f}[X1], {:.2f}[X2], {:.2f}[X3], r1{:.2f}, r2{:.2f}, r3{:.2f}, r4{:.2f}.pdf'.format(c_init1[1,0],c_init1[0,1], c_init2[0,0,1],r[1,0,0,0],r[0,1,0,0],r[0,0,1,0],r[0,0,0,1]))
