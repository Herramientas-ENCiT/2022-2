
def root_int(f, x_list):
    '''
    Función que nos rergresa los interalos donde probablemente haya una raiz.
    f = función
    x_list es un np.array
    Necesitamos import numpy as np antes de correr este código.
    '''
    y = f(x_list)
    sign = np.zeros(len(y)-1)
    intervalos = []

    for i in range(0, len(sign)):
        sign[i] = y[i]*y[i+1]
        if sign[i] <= 0:
            intervalos.append([x[i], x[i+1]])

    return np.array(intervalos)
