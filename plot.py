import matplotlib.pyplot as plt
import numpy as np

def power(x):
    s = []
    for i in range(20):
        s.append(x**i)
    return s

xpoints = np.array(power(2))
ypoints = np.array(power(5))

plt.plot(xpoints, ypoints)
plt.show()