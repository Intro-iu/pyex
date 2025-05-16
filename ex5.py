import numpy as np

# 1. 编写一个 NumPy 程序，创建一个由 30 到 70 的所有偶数整数组成的数组
arr = np.arange(30, 71, 2)
print(arr)

print("-" * 20)

# 2. 编写一个 NumPy 程序来创建一个大小为 10 的空向量，并将第六个值更新为 11
arr = np.zeros(10)
print(arr)
arr[6] = 11
print(arr)

print("-" * 20)

# 3. 编写一个 NumPy 程序，将浮点值的 NumPy 数组转换为整数值的 NumPy 数组
arr = np.array([1.1, 2.2, 3.3, 4.4, 5.5])
arr = arr.astype(int)
print(arr)

print("-" * 20)

# 4. 编写一个 NumPy 程序来获取多维列的最后两列
arr = np.arange(10, 22).reshape(3, 4)
print(arr)
print(arr[:, -2:])
print("-" * 20)