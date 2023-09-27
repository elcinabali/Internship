#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 14:58:28 2023

@author: elcininmacbookairi
"""

from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

def calculate_r_and_s(N):
   
    r = 0.1
    s = 0.1 #(r * N) - r

    return [r, s]

def rxn1(c,t):
    
    dx1dt = (k[1]*c[1]) - (k[0]*c[0])
    dx2dt = (k[0]*c[0]) - (k[1]*c[1])
    
    return [dx1dt, dx2dt]

def rxn_all(c,t):
    
    dx1dt = (k[1]*c[1]) - (k[0]*c[0])
    dx2dt = (k[0]*c[0]) - (k[1]*c[1]) - (e[0]*c[1]*c[3]) + (e[1]*c[4])
    dx3dt = (-alpha*c[5]*c[2]) + (beta*c[5])
    dEdt = - (e[0]*c[1]*c[3]) + (e[1]*c[4]) + (e[2]*c[4])
    dcompdt = (e[0]*c[1]*c[3]) - (e[1]*c[4]) - (e[2]*c[4])
    dPdt = (e[2]*c[4]) - (beta*c[5]) + (alpha*c[5]*c[2])
    
    return [dx1dt, dx2dt, dx3dt, dEdt, dcompdt, dPdt]
# c0 =x1, c1=x2, c2=x3, c3=enzyme, c4=complex c5=product 

t1 = np.linspace(0,20,200)

x1 = 5
x2 = 0

c_init = [x1, x2] # sets initial conc. of x1 and x2


N = 3   #len(c_init1)
k = calculate_r_and_s(N) #k[0]=r (r1) and k[1]=s (r2)

c_x1x2 = odeint(rxn1, c_init, t1) #1. column = x1, 2. column = x2

plt.plot(t1, c_x1x2[:,0], 'r--', label='x1')
plt.plot(t1, c_x1x2[:,1], 'g--', label='x2')

t2 = np.linspace(20,100,200)

x1 = c_x1x2[-1,0]
x2 = c_x1x2[-1,1]
x3 = 0
E = 50
comp = 0
P = 0

c_init2 = [x1, x2, x3, E, comp, P] # sets initial conc. of x1 and x2

N = 3   #len(c_init1)
k = calculate_r_and_s(N) #k[0]=r (r1) and k[1]=s (r2)
e = [100, 1, 100] # sets k1, k2, k3
alpha = 0.05
beta = 1

c_end = odeint(rxn_all, c_init2, t2)

print('beta/alpha: ', beta/alpha)
print('c_x1x2: ', c_x1x2)
print('c_end: ', c_end)

plt.plot(t2, c_end[:,0], 'r--')
plt.plot(t2, c_end[:,1], 'g--')
plt.plot(t2, c_end[:,2], 'b--', label='x3')
plt.plot(t2, c_end[:,3], 'c--', label='Enzyme')
plt.plot(t2, c_end[:,4], 'y--', label='Complex')
plt.plot(t2, c_end[:,5], 'm--', label='~x2')
plt.legend()
plt.grid()
plt.xlabel('time')
plt.ylabel('concentrations')

# plt.savefig('New enzyme rxn alpha=0.05 beta=1 E=50 X1=10 r=1.1.pdf')
