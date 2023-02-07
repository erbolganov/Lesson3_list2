# 12) Заполнить массив из 10 элементов случайными числами в интервале [0..4]
#     и определить, есть ли в нем одинаковые соседние элементы.
import random

a = []
b = []
q = False
for x in range(10):
    a.append(random.randrange(0,5))
print("List: ", a)
for x in range(9):
    if a[x] == a[x+1]:
        q = True
        print(f'This a[{x}] and a[{x+1}] elements are the same and equals: {a[x]}')
if q == False:
        print("No")