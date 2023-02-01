import numpy as np
import matplotlib.pyplot as plt

M = 1000
alpha = 0.7
b = 15
k = 200

def weierstrass(x, N):
	y = np.zeros((1,M))
	for n in range(1,N):
		y = y + np.cos(float(b ** n) * x) * b ** (-n * alpha)
	return y

x = np.linspace(-2,2,M)
y = np.reshape(weierstrass(x,k),(M,))

plt.plot(x, y, 'r-')
plt.show()