import numpy as np

t = np.linspace(0, 10, 100)

A = 1
gamma = 0.2
omega = 2

y_python = A * np.exp(-gamma * t) * np.cos(omega * t)
y_matlab = A * np.exp(-gamma * t) * np.cos(omega * t)

error = np.abs(y_python - y_matlab)

print("Max difference:", np.max(error))
