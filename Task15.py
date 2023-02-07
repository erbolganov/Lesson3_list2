# 15) Заполнить массив из 12 элементов случайными числами в интервале [-12..12]
#     и выполнить циклический сдвиг ВПРАВО на 4 элемента.
import random
a = []
b = []
q = False
for x in range(12):
    a.append(random.randrange(-13,13))
print("List: ", a)

for x in range(4):
    a.insert(0, a[-1])
    a.pop()
print('List after rotate right by 4 elements: ', a)
