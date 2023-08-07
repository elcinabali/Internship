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

"1. yol"

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

"2. yol" 

def rxn(c,t):
    
    dx1dt = (r[1]*c[1]) - (r[0]*c[0])
    dx2dt = (r[0]*c[0]) - (r[1]*c[1])
    
    return [dx1dt, dx2dt]

t = np.linspace(0,5,100)
c_int = [1,0]
r = [2,1]

c_x1x2 = odeint(rxn, c_int, t)

plt.plot(t, c_x1x2[:,0], 'r--', label='x1')
plt.plot(t, c_x1x2[:,1], 'g-', label='x2')
plt.legend()
plt.grid()
plt.xlabel('time')
plt.ylabel('concentration')

t = np.linspace(5,10,100)
c_int = [c_x1x2[-1,1],0]
c_x2x3 = odeint(rxn, c_int, t)

plt.plot(t, c_x2x3[:,0], 'g-')
plt.plot(t, c_x2x3[:,1], 'b--', label='x3')
plt.legend()
plt.grid()
plt.xlabel('time')
plt.ylabel('concentration')



