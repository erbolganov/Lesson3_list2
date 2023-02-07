# 25) Получить среднее арифметическое всех чётных элементов массива,
#     стоящих на нечётных местах.

import random
n = int(input('Enter length: '))
a = []
b = []
q = 0
i = 0
for x in range(n):
    a.append(random.randrange(20))
print("List: ", a)
for x in range(1,n,2):
    if a[x] % 2 == 0:
        b.append(a[x])
        q += a[x]
        i += 1
print("Second list", b)
print("Summ: ", q/i)
