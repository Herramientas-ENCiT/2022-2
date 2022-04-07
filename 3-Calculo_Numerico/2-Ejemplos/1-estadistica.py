
import numpy as np
import matplotlib.pyplot as plt # Un paquete de graficos

# Definimos la distribución gaussiana
def gauss(x,mu,std):    # mu -> promedio   # std -> Desviación estándar
    return np.exp(-(x - mu)**2 /(2 * std*std)) / np.sqrt(std*std*2*np.pi)

def estadistica(lista):
    lista.sort()
    elements = [ lista[0] ]
    freq = []
    i = 1
    j = 1
    while i < len(lista):
        if lista[i] != elements[-1]:
            freq.append(j)
            j = 0
            elements.append(lista[i])
        i += 1
        j += 1
    freq.append(j)
    return np.array([elements, freq])


gauss = np.vectorize(gauss)
x = np.linspace(0,100,100)

mu = 50; std = 10
y = gauss(x, mu, std)


x_data = np.linspace(0,100,100)
# data = np.random.normal(mu, std, size = (len(x_data),len(x_data)))
data = np.random.rand(100*100) * 50
data = data.reshape(100,100)


# Estadística de todo el arreglo
mu = data.mean()
std = data.std()
mu_1 = data.sum()/(len(data)*len(data))
std_1 = np.sqrt(((data - mu_1)**2).sum()/(len(data)*len(data)))
print("data.mean ?= data.sum()/(len(data)*len(data))   --> ", mu_1 == mu )
print("data.std() ?= std_1 = np.sqrt(((data - mu_1)**2).sum()/(len(data)*len(data)))   --> ", std_1 == std )
y_all = gauss(x, mu, std)

# Estadistica de cada columna y c
sorted_row = np.sort(data) # No usamos data.sort() porque eso cambiaría totalmente a data y queremos mantenerlo así
sorted_col = np.transpose(np.sort(data)) # No usamos data.sort() porque eso cambiaría totalmente a data y queremos mantenerlo así
sorted_grad = np.sort(sorted_col)
sorted_all = np.sort(data.flatten()).reshape(100,100)
mu_col = data.mean(axis=0)
mu_row = data.mean(axis=1)
std_col = data.std(axis=0)
std_row = data.std(axis=1)


fig, ax1 = plt.subplots(2,2, sharex=True, sharey = True)
#fig, ax2 = plt.subplots()
ax1[0,0].imshow(data,extent=(0,len(data),0,50))
ax1[0,0].set_title("Datos al azar")

ax1[0,1].imshow(sorted_row,extent=(0,len(data),0,50))
ax1[0,1].set_title("Datos ordenando renglón")
ax1[0,1].plot(mu_row,np.arange(1,len(mu_row)+1)/2, color = 'r', label = r'$\mu$')
ax1[0,1].plot(std_row,np.arange(1,len(mu_row)+1)/2, color = 'g',label = r'$\sigma$')


ax1[1,0].imshow(sorted_col,extent=(0,len(data),0,50))
ax1[1,0].set_title("Datos ordenados columna")
ax1[1,0].plot(mu_col, color = 'r', label = r'$\mu$')
ax1[1,0].plot(std_col, color = 'g',label = r'$\sigma$')


ax1[1,1].imshow(sorted_grad,extent=(0,len(data),0,50))
ax1[1,1].set_title("Datos ordenados")
plt.legend()

fig_ordered, ax2 = plt.subplots(sharex=True, sharey = True)
ax2.imshow(sorted_all,extent=(0,len(data),0,50))


[x_dat, y_dat] = estadistica(np.rint(data.flatten()))
y_dat = y_dat/y_dat.sum()

fig_stat , ax = plt.subplots()
ax.plot(x, y_all , color = 'g', label =r'$\mu = '+str(np.rint(mu))+",\, \sigma = "+str(np.rint(std))+"$", marker = '*')
ax.plot(x_dat, y_dat , color = 'r', label =r'Datos', marker = 'o')
plt.legend()
ax.set_xlabel(r'$x$')
ax.set_ylabel(r'$y(x)$')


plt.show()
