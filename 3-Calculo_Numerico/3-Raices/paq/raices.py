
import numpy as np

def root_int(f, x_list):
    '''
    Función que nos rergresa los interalos donde probablemente haya una raiz.
    f = función
    x_list es un np.array
    '''
    y = f(x_list)
    sign = np.zeros(len(y)-1)
    intervalos = []

    for i in range(0, len(sign)):
        sign[i] = y[i]*y[i+1]
        if sign[i] <= 0:
            intervalos.append([x_list[i], x_list[i+1]])

    return np.array(intervalos)

def bisection(f, int, tol = .001, n_max = 100):
    '''
    Metodo de biseccion para calcilar raices en un intervalo donde se
    garantice que hay una.
    f es una función
    int es una lista de dos elementos donde int[0]<int[1]
    '''
    count = 0
    x_left = int[0]
    x_right = int[1]
    mid_point = 0.5 * (x_left + x_right)
    delta_x = x_right - x_left

    while (delta_x/2 > tol and count < n_max):
        if f(x_left) * f(mid_point) > 0:
            x_left = mid_point
        elif f(mid_point) * f(x_right) > 0:
            x_right = mid_point
        else:
            break
        count += 1
        mid_point = 0.5 * (x_left + x_right)

    return mid_point
