# 13) Определите в массиве A номер первого элемента, равного X.
#     Определите номер первого элемента, равного X, в первой половине массива A
#     (массив имеет чётное число элементов).
#     Определите номер первого элемента, равного X, во второй половине массива A
#     (массив имеет чётное число элементов).
import random
A = []
for x in range(10):
    A.append(random.randrange(15))
print("List: ", A)
X = int(input("Enter the searching element: "))
print(f'index of {X} in first half of the list: {A.index(X, 0, 6)}')
print(f'index of {X} in second half of the list: {A.index(X, 6, 10)}')
