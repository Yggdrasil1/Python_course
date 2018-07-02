# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import matplotlib.pyplot as plt

fig = plt.figure(figsize=(25,10))

ax = fig.add_subplot(1,1,1)

ax.plot(range(10),range(0,20,2),Lw=2,c='red',label='myLine')
ax.scatter(range(10,20,1),range(0,20,2),s=40,c='blue',label='myScatter')
ax.set_xlabel("[x] a.u.",fontsize=10)
ax.set_ylabel("[y] a.u.",fontsize=10)
ax.tick_params('both',labelsize=10)
ax.legend(loc='best',fontsize=10)
plt.show
