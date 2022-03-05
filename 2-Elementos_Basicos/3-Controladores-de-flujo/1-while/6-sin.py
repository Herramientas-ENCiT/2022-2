

n = 8
i = 1

x = 3.1416325 / 4
sin = 0
factorial = 1
potencia = 1

while i <= 8:
    signo = (-1) ** (i + 1)
    sin = sin + signo * (x ** (2 *i - 1) )  / factorial
    factorial = factorial *(2 * i )*(2 *i + 1)
    i =  i + 1

print(sin, 2**(.5) / 2)
