# 9) Дан массив из 50 элементов и лежат в диапазоне от -50 до 49 включительно.
#    Требуется из одного массива скопировать в другой массив значения
#    в диапазоне от -5 до 5 включительно и подсчитать их количество.

import random
a = []
b = []

for x in range(50):
    a.append(random.randrange(-50,50))
    if a[x] >= -5 and a[x] < 5:
        b.append(a[x])

print(f'List: {a}')
print(f'Elements between -5 and 5: {b}')
print(f'Length: {len(b)}')