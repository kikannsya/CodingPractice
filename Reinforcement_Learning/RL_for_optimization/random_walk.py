import random
import numpy as np
import matplotlib.pyplot as plt

random.seed(1)

p, q = 0.4, 0.4
r = 1 - p - q
n_steps = 1000
positioin = np.zeros(n_steps)
for t in range(n_steps-1):
    dx = random.choices([1,-1,0], weights=[p, q, r])[0]
    positioin[t+1] = positioin[t] + dx

xvals = np.arange(n_steps)
plt.xlabel('Perios')
plt.ylabel('Position')
plt.title('1-D random walk')
plt.plot(xvals, positioin)
plt.show()