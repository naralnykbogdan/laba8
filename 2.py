#виведіть на екран транспоновану матрицю 3*3( початкова матриця задана користувачем)
import numpy as np
a = np.array([[0, 1, 2], [4, 5, 6], [7,8,9]])
a = a.transpose()
print(a)
