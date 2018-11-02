import numpy as np

a = np.array([[3, 5], [6, 10]])
b = np.array([[-7], [2]])
print(np.linalg.solve(a, b))
