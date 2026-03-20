import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 10, 100)

A = 1
gamma = 0.2
omega = 2

y = A * np.exp(-gamma * t) * np.cos(omega * t)

plt.plot(t, y)
plt.title("Damped Oscillation - Python")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.show()
