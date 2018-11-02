import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

x = np.arange(-10, 10, 0.1)

y = x**2 -64

mpl.rcParams[u'font.sans-serif'] = ['simsun']
mpl.rcParams['axes.unicode_minus'] = False

plt.title(u"一元二次函数")
plt.plot(x, y)
plt.show()
