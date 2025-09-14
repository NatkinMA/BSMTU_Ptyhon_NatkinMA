flag = False
print('Введите координаты X и Y для точки:')
x = float(input('X='))
y = float(input('Y='))

if (x < -1) or (x > 4):
    flag = False
if ((x >= -1) and (x < 1) and (y >= 2*x+2) and (y <= x**3-4*x**2+x+6)
        or (x >= 1) and (x <= 4) and (y >= x**3-4*x**2+x+6) and (y <= 2*x+2)):
    flag = True
else:
    flag = False

print("Точка X={0: 6.2f} Y={1: 6.2f}".format(x, y), end=" ")
if flag:
    print("попадает", end=" ")
else:
    print("не попадает", end=" ")
    print("в область.")
