from math import *
from random import *

n = int(input("Задайте количество элементов в массиве (N<=30) N: "))
if n > 30: n = 30
elif n < 5: n = 5
print("Начальное состояние")
arr = []
for i in range(n):
    arr.append(uniform(-5, 5))
    print("{0: 7.3f}".format(arr[i]), end=" ")
print()

max1 = abs(arr[0])
max2 = abs(arr[0])
for i in range(1, len(arr) - 1):
    if max1 < abs(arr[i]):
        max2 = max1
        max1 = abs(arr[i])
    else:
        if max2 < abs(arr[i]):
            max2 = abs(arr[i])
print("Первый и второй максимальные по модулю элементы списка: {0: 7.3f} и {1: 7.3f}".format(max1, max2))

amax = float(input("Пороговое значение Amax: "))

asum = 0.0
for i in range(len(arr)):
    if abs(arr[i]) < 1.0:
        asum = asum + arr[i]
    if abs(arr[i]) > amax:
        arr[i] = 0.0
print("Сумма элементов, модуль которых меньше единицы: {0: 7.3f}".format(asum))

print("Обнуление всех элементов массива, модуль которых превышает Amax = {0: 7.3f}".format(amax))
for i in range(len(arr)):
    if abs(arr[i]) > amax:
        arr[i] = 0.0
    print("{0: 7.3f}".format(arr[i]), end=" ")
print()

print("Отсортированный список, в котором сохранен порядок ненулеых элементов:")
for i in range(len(arr)):
    if arr[i] == 0.0:
        for j in range(i, len(arr)-1):
            arr[j], arr[j+1] = arr[j+1], arr[j]
    print("{0: 7.3f}".format(arr[i]), end=" ")
print()
