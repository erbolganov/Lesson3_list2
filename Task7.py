# 7) Найти максимальный элемент массива и его индекс (max_num   и   max_index).

import random
n = int(input('Enter length: '))
a = []

for x in range(n):
    a.append(random.randrange(50))
max_num = max(a)
max_index = a.index(max_num)
print(f'List: {a}')
print(f'Max element: {max_num}\nIndex of max element: {max_index}')