import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-100,100,1000)
y = x[::-1].reshape((-1,1))

def f(x,y):
    return x**2 + (y+1-np.sqrt(np.abs(x))**2) - 1

plt.imshow(f(x,y))
plt.show()