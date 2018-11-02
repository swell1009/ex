# 本题是实现蛇形方阵的代码
import numpy as np

n = 12  # n阶方阵

arr = np.zeros((n, n))  # 生成0方阵

tot = 1  # 计数标志位
x = 0  # 初始行位置
y = 0  # 初始列位置
arr[x][y] = tot  # 初始位置置数

while (tot < n * n):
    while (y - 1 >= 0 and arr[x][y - 1] == 0):  # 向左判断
        y = y - 1
        tot = tot + 1
        arr[x][y] = tot

    while (y + 1 < n and arr[x][y + 1] == 0):  # 向右判断
        y = y + 1
        tot = tot + 1
        arr[x][y] = tot

    while (x + 1 < n and arr[x + 1][y] == 0):  # 向下判断
        x = x + 1
        tot = tot + 1
        arr[x][y] = tot

    while (x - 1 >= 0 and arr[x - 1][y] == 0):  # 向下判断
        x = x - 1
        tot = tot + 1
        arr[x][y] = tot

print(arr)
