from sympy import *

f = Function('f')
x = Symbol('x')
print(dsolve(diff(f(x), x) - 2 * f(x) * x, f(x)))
