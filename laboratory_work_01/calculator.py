from math import *

a = float(input('Введите параметр а: '))
x = float(input('Введите значение x: '))

y = tan(x**2/2-1)**2+(2*cos(x-pi/6))/(1/2+sin(a)**2)
print("{0:.2f} {1:.2f} {2:.4f}".format(a, x, y))

tmp = log(3-cos(pi/4+2*x), 3+sin(x))/(1+tan(2*x/pi)**2)
y = pow(2, tmp)
print("{0:.2f} {1:.4f}".format(x, y))
