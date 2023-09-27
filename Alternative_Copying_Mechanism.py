#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 11:25:40 2023

@author: elcininmacbookairi
"""

from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

def calculate_r_and_s(N):
   
    r = 1.1
    s = (r * N) - r

    return [r, s]

# c0 =x1, c1=x2, c2=x2-, c3=substrat, c4=complex c5=x2~ c6=x3 

def rxn_all(c,t):
    
    dx1dt = (k[1]*c[1]) - (k[0]*c[0]) - (r3*c[0]) + (r4*c[2])
    dx2dt = (k[0]*c[0]) - (k[1]*c[1]) - (e[0]*c[1]*c[3]) + (e[1]*c[4]) + (alpha*c[5]*c[6])
    dx2_dt = (r3*c[0]) - (r4*c[2]) + (e[2]*c[4])
    dSdt = - (e[0]*c[3]*c[1]) + (e[1]*c[4])
    dcompdt = (e[0]*c[3]*c[1]) - (e[1]*c[4]) - (e[2]*c[4])
    dx2_tildedt = (e[2]*c[4]) - (alpha*c[5]*c[6]) - (beta*c[5])
    dx3dt = - (alpha*c[5]*c[6]) + (beta*c[5])
    
    return [dx1dt, dx2dt, dx2_dt, dSdt, dcompdt, dx2_tildedt, dx3dt]


t = np.linspace(0,30,200)
x1 = 100
x2 = 0
x2_ = 0
x2_tilde = 0 
x3 = 0
S = 100
comp = 0

c_init = [x1, x2, x2_, S, comp, x2_tilde, x3] # sets initial conc. of x1 and x2

N = 3   #len(c_init1)
k = calculate_r_and_s(N) #k[0]=r (r1) and k[1]=s (r2)
r3 = 1.1
r4 = 2.2
e = [10, 1, 10] # sets k1, k2, k3
alpha = 0.05
beta = 1

c_end = odeint(rxn_all, c_init, t)

print('beta/alpha: ', beta/alpha)
print('c_end: ', c_end)
print('r and s: ', k)

plt.plot(t, c_end[:,0], 'r--', label='x1')
plt.plot(t, c_end[:,1], 'g--', label='x2')
plt.plot(t, c_end[:,2], 'k--', label='x2--')
plt.plot(t, c_end[:,3], 'c--', label='Substrat')
plt.plot(t, c_end[:,4], 'y--', label='Complex')
plt.plot(t, c_end[:,5], 'm--', label='~x2')
plt.plot(t, c_end[:,6], 'b--', label='x3')
plt.legend()
plt.grid()
plt.xlabel('time')
plt.ylabel('concentrations')

