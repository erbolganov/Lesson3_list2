# 8) Требуется заполнить массив числами, которые вводит пользователь,
#    и вычислить их сумму. Если пользователь вводит ноль или превышен размер массива,
#    то запросы на ввод должны прекратиться.

n = int(input('Enter length: '))
a = []
i = s = 0 # s - Summa  i - counter
while i < n:
    x = int(input(f'a[{i}] = '))
    if x == 0:
        break
    a.append(x)
    s += x
    i += 1
print(f'List: {a}')
print(f'Sum of list: {s}')


