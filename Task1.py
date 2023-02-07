#  1) Дан массив ['a', 'b', 'c']. Добавьте ему в конец элементы 1, 2, 3.

a = ['a', 'b', 'c']
print(f'List: {a}')
a.extend([1,2,3])
print(f'List after extend: {a}')