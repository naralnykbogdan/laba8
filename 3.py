#виконайте добуток двох квадратних матриць 3*3, врахуйте розмірність Результати множення елементів занесіть до нової матриці та виведіть її на екран
import numpy as np
a = 3
b = 3
mas = []
mas_2=[]
for i in range(a):
    d=[]
    for j in range(b):
        d.append(int(input("Введіть першу матрицю по одному елементу:")))
    mas.append(d)
for i in range(a):
    c=[]
    for j in range(b):
        c.append(int(input("Введіть другу матрицю по одному елементу:")))
    mas_2.append(c)
c=np.array(mas)
b=np.array(mas_2)
print(c.dot(b))
