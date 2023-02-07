# 14) Заполнить массив из 10 элементов случайными числами в интервале [-10..10]
#     и сделать реверс отдельно для 1-ой и 2-ой половин массива.

import random

a = []
b = []
c = []
q = False
for x in range(10):
    a.append(random.randrange(100))
print("List: ", a)
b = a[0:5]
c = a[5:10]
b.reverse()
c.reverse()

print(f'Result: \n{(b + c)}')
