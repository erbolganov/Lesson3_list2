# 11) Дан массив из N элементов в диапазоне [100;300]. Сжать массив,
# оставив в нем только те элементы, сумма цифр которых четная.

import random
n = int(input("Вводите длина списка: "))
a = []
b = []
q = 0
for x in range(n):
    a.append(random.randrange(100,300))
print("List: ", a)
#b = str(a)
for x in a:
    for i in str(x):
        q += int(i)
    if q % 2 == 0:
        b.append(x)
    q = 0
print("элементы, сумма цифр которых четная:", b)