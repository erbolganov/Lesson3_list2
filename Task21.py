# 21) Найти сумму тех элементов массива, которые одновременно
#     имеют четные и отрицательные значения.
#     Например, в массиве [3, -5, -2, 4, -8, 0] отрицательными четными элементами
#     являются числа -2 и -8. Их сумма равна -10.
import random

n = int(input('Enter length: '))
a = []
b = []
q = 0
for x in range(n):
    a.append(random.randrange(-20,20))
print("List: ", a)
for x in range(n):
    if a[x] < 0 and a[x] % 2 == 0:
        b.append(a[x])
        q += a[x]
print("Oтрицательными четными элементами являются числа:", b)
print("Их сумма равна:", q)