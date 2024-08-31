"""
- نمودارهای 3 بعدی

"""
from matplotlib import pyplot as plt
import numpy as np


fig = plt.figure(figsize=(12, 10))
ax = fig.add_subplot(projection="3d")

a = np.arange(-5, 5, 0.2)
b = np.arange(-5, 5, 0.2)
x, y = np.meshgrid(a, b)
z = np.cos(x) * np.sin(y)

surf = ax.plot_surface(x, y, z, cmap=plt.cm.summer)

fig.colorbar(
    surf,
    # نصف کردن سایز کالربار
    shrink=0.5
)

plt.show()
