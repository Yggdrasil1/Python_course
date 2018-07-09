# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

df = pd.read_csv('/local/home/biostudent216/Desktop/data/my_yeast_genome.tsv',sep="\t",header=None)

df.columns = ['Art','id','systematic','standard','function','sequence',
              'gen length','seq mRNA', 'mRNA length']

print(df.head())


mean = np.mean(df['mRNA length'])

print ("Mittlere Länge der mRNA Seq = {}".format(mean))

A = 0

for index in df['sequence']:
    
    for j in index:
        
        if j == 'A':
            A += 1
    
print('Anzahl A = {}'.format(A))


leer = 0

for index in df['sequence']:
    if 'T' not in index and 'A' not in index and 'C' not in index and 'G' not in index:
        leer += 1
        
print('Fehlende Sequenzen = {}'.format(leer))

plt.plot(df['mRNA length'])





            

