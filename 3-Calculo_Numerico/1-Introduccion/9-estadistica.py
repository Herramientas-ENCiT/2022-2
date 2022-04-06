

import numpy as np
import matplotlib.pyplot as plt # Un paquete de graficos

def gauss(x,mu,std):
    return np.exp(-(x - mu)**2 /(2 * std*std)) / np.sqrt(std*std*2*np.pi)

gauss = np.vectorize(gauss)
x = np.linspace(0,100,100)
mu = 50
std = 10
y = gauss(x, mu, std)

err = (np.random.rand(len(x)) -.5)*.01 # Valores al azar de un arreglo de 5x10x15
y_err = y + err

x_data = np.linspace(0,100,100)
data = np.random.normal(mu, std, size = (len(x_data),len(x_data)))
fig, ax1 = plt.subplots()

mu = data.mean()
std = data.std()

mu_1 = data.sum()/(len(data)*len(data))
std_1 = np.sqrt(((data - mu_1)**2).sum()/(len(data)*len(data)))


y_teo = gauss(x, mu, std)
y_teo1 = gauss(x, mu_1, std_1)
ax1.scatter(x_data,data[:,1])
ax1.scatter(x_data,data[:,2], color = 'r')

fig , ax = plt.subplots()

ax.plot(x, y, color = 'r', label =r'$\mu = 50, \sigma = 10 $', marker = '*')
ax.plot(x, y_teo , color = 'g', label =r'Exp', marker = '*')
ax.plot(x, y_teo1 , color = 'b', label =r'Exp 2', marker = '*')


plt.legend()
ax.set_xlabel(r'$x$')
ax.set_ylabel(r'$y(x)$')


plt.show()
