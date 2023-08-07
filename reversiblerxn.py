#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 20:32:32 2023

@author: elcininmacbookairi
"""

from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt


# def model(x1,t):
#     r1 = 2
#     r2 = 1
#     x2_int = 0.7
#     dx1dt = (r2*x2_int) - (r1*x1)
#     return dx1dt

# x1_int = [0, 0.5, 1]
# t = np.linspace(0,20,500)
# result = odeint(model,x1_int,t)

# fig,ax = plt.subplots()
# ax.plot(t,result[:,0],label='x1_int=0')
# ax.plot(t,result[:,1],label='x1_int=0.5')
# ax.plot(t,result[:,2],label='x1_int=1')
# ax.legend()
# ax.set_xlabel('t')
# ax.set_ylabel('x1')
 

"x1 <--> x2"

def rxn1(c,t):
    
    dx1dt = (r[1]*c[1]) - (r[0]*c[0])
    dx2dt = (r[0]*c[0]) - (r[1]*c[1])
    
    return [dx1dt, dx2dt]

t = np.linspace(0,5,100)
c_init = [1,0] # sets initial conc. of x1 and x2
r = [2,1] # sets r1 and r2

c_x1x2 = odeint(rxn1, c_init, t) #1. column = x1, 2. column = x2 

plt.plot(t, c_x1x2[:,0], 'r--', label='x1')
plt.plot(t, c_x1x2[:,1], 'g--', label='x2')

t = np.linspace(5,10,100)
c_init = [c_x1x2[-1,0], c_x1x2[-1,1], 0] # takes the latest conc. of x1, x2 and sets initial conc. of x3
r = [2, 1, 4, 7] # sets r1, r2, r3 and r4

"x2 <--> x3"

def rxn2(c,t):
    
    dx1dt = (r[1]*c[1]) - (r[0]*c[0])
    dx2dt = (r[0]*c[0]) + (r[3]*c[2]) - (r[1]*c[1]) - (r[2]*c[1])
    dx3dt = (r[2]*c[1]) - (r[3]*c[2])
    
    return [dx1dt, dx2dt, dx3dt]

c_final = odeint(rxn2, c_init, t) # 1. column = x1, 2. column = x2, 3. column = x3

plt.plot(t, c_final[:,0], 'r--')
plt.plot(t, c_final[:,1], 'g--')
plt.plot(t, c_final[:,2], 'b-', label='x3')
plt.legend()
plt.grid()
plt.xlabel('time')
plt.ylabel('concentration')

