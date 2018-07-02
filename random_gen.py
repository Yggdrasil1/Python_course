# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
from matplotlib import pyplot as plt

second = []
for i in range(1,11):
    first = ""
    for _ in range(50):
        first += str(round(np.random.uniform(i,5*i)+np.random.uniform(-i,i),2)) + "," 
    first = first[:-1]
    first += '\n'
    second.append(first)
    
    
with open("./janosch_mathe","w") as janosch:    
    janosch.writelines(second)
    

