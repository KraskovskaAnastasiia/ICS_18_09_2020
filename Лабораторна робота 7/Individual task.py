import matplotlib.pyplot as plt
from numpy import *
import numpy as np


def f(t):
    return exp(t ** (1 / 2)) * np.sin (10 * t)


t = np.arange(0, 5, 0.01)
y = f(t)

plt.plot(t, y, 'm')

plt.xlabel('t')
plt.ylabel('y')
plt.title('Y(x)=(x^(1/2)) * sin(10*x), x=[0...5]')

plt.show()
