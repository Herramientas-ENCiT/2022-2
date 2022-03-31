
import numpy as np
import matplotlib.pyplot as plt # Un paquete de graficos
import paq.mincuad as mc

x = np.linspace(0, 10, 30)
error = np.random.rand(len(x)) * 5
y_exp = 3 * x + 2 + error


[m, b] = mc.minimos_cuadrados(x,y_exp)

y_teo = m * x + b

print(m, b)

plt.plot(x, y_exp, marker = '*' )
plt.plot(x, y_teo)

plt.show()


s_res = y_teo - y_exp
s_res = np.dot(s_res,s_res)

s_tot = y_teo - np.mean(y_teo)
s_tot = np.dot(s_tot,s_tot)

r2 = 1 - s_res/s_tot

print(r2)
