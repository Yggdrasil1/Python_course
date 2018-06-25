import numpy as np 
import matplotlib.pyplot as plt

"""
Plotting exercise. 
Fourier series are used to approximate periodic functions with a sum of sine and cosine functions.
In this exercise we have a look at a rectangular pulse. The aim is to plot this rectangular pulse, the individual 
terms of the fourier series and the approximation obtained by the fourier series. Therefore go through the code and 
work on the TODOS."""


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
    x_axis = np.linspace(-np.pi, np.pi, 101)

    fig = plt.figure()  # reference to figure object
    ax = fig.add_subplot(111)  # reference to axis object (this is where you actually plot something)

    # TODO: Plot a rectangular pulse, which is 1 if x is between -2 pi and -pi or between 0 and pi and
    #                                         -1 if x is between -pi and 0 or pi and 2 pi
    #       check out np.ones() and np.where() or use lists

    fourier_sol = fourier_rechteck_puls(x_axis)
    # TODO: Plot the solution of the fourier series, the sum as well as the single terms.







