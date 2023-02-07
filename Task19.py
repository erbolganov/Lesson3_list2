# 19) Дан массив, содержащий положительные и отрицательные числа.
#     Заменить все элементы массива на противоположные по знаку.
#     Например, задан массив [1, -5, 0, 3, -4].
#     После преобразования должно получиться [-1, 5, 0, -3, 4].

import random
n = int(input('Enter length: '))
a = []
b = []
for x in range(n):
    a.append(random.randrange(-10, 10))
print("List: ", a)

for x in range(n):
    b.append(-a[x])
print(b)