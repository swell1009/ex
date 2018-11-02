from sympy import *

t = Symbol('t')
x = Symbol('x')
m = integrate(sin(t) / (pi - t), (t, 0, x))
n = integrate(m, (x, 0, pi))
print(n)
