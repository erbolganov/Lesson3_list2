# 2) Даны два массива: ['a', 'b', 'c'] и [1, 2, 3]. Объедините их вместе.
# 3) Дан массив [1, 2, 3]. Сделайте из него массив [3, 2, 1].
# 4)  Дан массив [1, 2, 3]. Добавьте ему в конец элементы 4, 5, 6.

m1 = ['a', 'b', 'c']
m2 = [1, 2, 3]
print(f'List m1: {m1}')
print(f'List m2: {m2}')
print(f'List after join: {m1 + m2}')
m1 = ['a', 'b', 'c']
m2 = [1, 2, 3]
m1.extend(m2)
print('2) List after extend: ', m1 , "\n---------------------------------------------------")
# 3) Дан массив [1, 2, 3]. Сделайте из него массив [3, 2, 1].
m2.reverse()
print(f'3) List m2 after reverse: {m2} \n----------------------------------------------------')
# 4)  Дан массив [1, 2, 3]. Добавьте ему в конец элементы 4, 5, 6.
m2 = [1, 2, 3]
m2.extend([4, 5, 6])
print(f'4) List m2 after extend: {m2}')