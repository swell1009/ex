import math

s = 0
c = 1
for i in range(1, 10):
    for j in range(0, 9):
        s = 10 * i + j
        q = math.sqrt(i + j)
        if (abs(q - int(q)) < 0.00000000001):
            print(c, "=", s)
            c = c + 1
