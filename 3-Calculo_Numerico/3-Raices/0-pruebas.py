
import numpy as np
import matplotlib.pyplot as plt
import paq.raices as rt

x = np.linspace(0,2*np.pi+.0001, 50)
def func(x):
    return np.sin(2*x)-np.cos(x)*np.sin(3*x)


plt.plot(x,func(x), marker = '*', label = r'$f(x)$')
plt.plot(x,np.zeros(len(x)), label = 'Eje x')

intervalos = rt.root_int(func, x)
raices = np.zeros(len(intervalos))
print(intervalos)

for i in range(0,len(intervalos)):
    raices[i] = rt.bisection(func, intervalos[i])

plt.plot(raices,np.zeros(len(raices)), marker = '*',label = 'raices')
print(raices)

plt.legend()
plt.show()
