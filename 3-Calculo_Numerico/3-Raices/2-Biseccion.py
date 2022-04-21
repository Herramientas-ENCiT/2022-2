
import numpy as np
import matplotlib.pyplot as plt
import paq.raices as rt

x = np.linspace(0,2*np.pi, 50)

def func(x):
    return np.sin(2*x)-np.cos(x)


plt.plot(x,func(x), marker = '*', label = r'$f(x)$')
plt.plot(x,np.zeros(len(x)), label = 'Eje x')
plt.legend()


intervalos = rt.root_int(func, x)
int = intervalos[0]
print(intervalos)

i = 0
n_tot = 100
tol = .001
a = int[0]
b = int[1]
c = (a+b)/2

while ((b-a)/2 > tol and i < n_tot):
    if func(a)*func(c) > 0:
        a = c
    elif func(c)*func(b) > 0:
        b = c
    elif func(c) == 0:
        #return c
        break
    i += 1
    c = (a+b)/2
    print(c)
print("Numero de interaciones:", i)
print("La raíz está en x = ", c)

plt.show()
