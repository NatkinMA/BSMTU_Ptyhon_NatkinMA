from math import *

xb = float(input('Введите Xbeg='))
xe = float(input('Введите Xend='))
dx = float(input('Введите Dx='))
print("Xbeg={0: 7.2f} Xend={1: 7.2f}".format(xb, xe))
print(" Dx={0: 7.2f}".format(dx))
xt = xb
print("+--------+--------+")
print("I X I Y I")
print("+--------+--------+")
while xt <= xe:
    if xt < -5:
        y = 1
    elif xt >=-5 and xt<0:
        y = -(3/5)*xt-2
    elif xt >= 0 and xt<2:
        y = -sqrt(4-xt**2)
    elif xt >= 2 and xt<4:
        y = xt-2
    elif xt >= 4 and xt<8:
        y = 2+sqrt(4-(xt-6)**2)
    else: y = 2
    print("I{0: 7.2f} I{1: 7.2f} I".format(xt, y))
    xt += dx
print("+--------+--------+")
