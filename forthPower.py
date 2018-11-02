import math

x = 1
b = 2
while (b < 100000):
    s = 7 + 7 * b + 7 * b * b
    q = math.sqrt(math.sqrt(s))
    if (abs(q - int(q)) < 0.00000000001):
        print("We got it!")
        print("b=", b, s, q)
        break
    else:
        print(b, s, q)
        b = b + 1
