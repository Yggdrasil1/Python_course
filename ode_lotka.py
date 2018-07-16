# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

Hasen_start = 10.02
Tiger_start = 9
y0 = [Hasen_start,Tiger_start]


pro_hase = 0.10
pro_tiger = 0.001 
tot_h = 0.01
tot_t = 0.01
pred = 0.01
p = [pro_hase,pro_tiger,tot_h,tot_t,pred]

start = 0
end = 5000
num_time_points = 30000
t  = np.linspace(start, end, num_time_points)

def fun(y,t,p):
    
    Hase = y[0]
    Tigr = y[1]
    
    h1 = p[0]*Hase - p[2]*Hase - p[4]*Hase*Tigr
    t1 = p[1]*Hase*Tigr - p[3]*Tigr
    
    return[h1,t1]
    
result = odeint(fun,y0,t,(p,))

plt.plot(t,result[:,0])
result1 = result[:,1]*np.amax(result[:,0])/np.amax(result[:,1])
plt.plot(t,result1)

print(np.amin(result[:,0]))

print(np.amin(result[:,1]))

plt.show(block=False)
plt.plot(result[0:4000,0],result[0:4000,1])
#plt.plot(result[:,0],result[:,1])

    
    
    
    