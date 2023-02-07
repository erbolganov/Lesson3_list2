# 17) Все элементы массива поделить на значение наибольшего элемента этого массива.

import random
n = int(input('Enter length: '))
a = []
b = []
for x in range(n):
    a.append(random.randrange(50))
print("List: ", a)
max_el = max(a)
print(f'Max element: {max_el}')
for x in range(n):
    b.append(a[x] / max_el)
print(b)