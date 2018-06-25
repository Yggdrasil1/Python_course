import numpy as np 
import matplotlib.pyplot as plt
import operator


"""
Plotting exercise. 
Fourier series are used to approximate periodic functions with a sum of sine and cosine functions.
In this exercise we have a look at a rectangular pulse. The aim is to plot this rectangular pulse, the individual 
terms of the fourier series and the approximation obtained by the fourier series. Therefore go through the code and 
work on the TODOS."""


def simulation(axis,array):
    
    fig = plt.figure(1, figsize=(12, 12))
    
    ax = plt.subplot()
    ax.set_xlabel("Phase")
    ax.set_ylabel("Amplitude")

    #plt.show(block=False) 
    
    plt.plot(x_axis,rechteck[3])
    fig.canvas.draw()
    
    for _ in range(4):    
        for l in range(len(array)):
            
            ax.clear()  # clear the drawing/plotting area
            ax.set_title('Plot {}'.format(l))
            ax.plot(axis,array[l])
            fig.canvas.draw()
            
        
        
        

def fourier_rechteck_puls(x, amp=1, depth=5):
    """
    :param x:
        array like. Used as x values to calculate values of fourier series
    :param amp:
        Amplitude of rectangular pulse
    :param depth:
        Number of terms of series calculated
    :return:
        2 dimensional array with single terms of fourier series
    """
    f_g = []
    for i in range(1, depth + 1):
        f = 4 * amp / np.pi * np.sin((2 * i - 1) * x) / (2 * i - 1)  # i-th term of the fourier series is calculated
        f_g.append(f.tolist())  # i-th term is added to list
    return f_g

    
if __name__ == '__main__':
    # TODO: define x axis from - 2 pi to 2 pi-. HINT: check out numpy arange or numpy linspace
    x_axis = np.linspace(-2*np.pi, 2*np.pi, 101)
   
    fig = plt.figure()  # reference to figure object
    ax = fig.add_subplot(111)  # reference to axis object (this is where you actually plot something)
    
    arr=np.ones(len(x_axis))
    
    for i in range(len(x_axis)):
        if x_axis[i] < (-1 * np.pi) or (x_axis[i] >= 0 and x_axis[i] < np.pi):
            arr[i] = 1
        else:
            arr[i] = -1
            
    #plt.plot(x_axis,arr)
    
    
    # TODO: Plot a rectangular pulse, which is 1 if x is between -2 pi and -pi or between 0 and pi and
    #                                         -1 if x is between -pi and 0 or pi and 2 pi
    #       check out np.ones() and np.where() or use lists

    depths=100

    fourier_sol = fourier_rechteck_puls(x_axis,depth=depths)
    
    rechteck=np.zeros((depths,len(x_axis)))    
    
    for j in range(depths):
        
        for k in range(len(fourier_sol)):
            
            if j == 0:
                rechteck[j,k] = fourier_sol[j][k]
            else:
                rechteck[j,k] = rechteck[j-1,k] + fourier_sol[j][k]
                
    simulation(x_axis,rechteck)
    #for l in range(len(rechteck)):
        
    
        
    
    # TODO: Plot the solution of the fourier series, the sum as well as the single terms.







