from scipy.linalg import svd
from numpy import array
import numpy as np

matrix1 = []
array1 = []
k = 0

m = int(input("Enter Raw and Column Size : "))

if (m * m) == 16:

    for i in range(32):
        k = k + 1
        if k % 2 != 0:
            array1.append(k)

    print("\nMatrix of Size 4x4 with first 16 Odd Number's \n")
    array1 = array(array1).reshape(m, m)

    print("Array : \n", array1)

    X, B, T = svd(array1)

    print("\nX\n", X)
    print("B\n", B)
    print("T\n", T)

    print('X+T : \n', np.add(X, T))
    print('X-T : \n', np.subtract(X, T))

    mul1 = np.multiply(2, X)
    mul2 = np.multiply(X, X)
    print('2X*X*X : \n', np.multiply(mul1, mul2))

else:

    print("Raw and Column Size Must be 4x4")
