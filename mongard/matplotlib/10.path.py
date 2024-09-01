"""
- مشخص کردن مساحتی از چارت

- configs
    - MOVETO
        - استارت (برو به اون نقطه)
    - LINETO
        - خط صاف بکش
    - CURVE
        - خط منحنی بکش
    - CLOSEPOLY
        - تمومش کن
"""
from matplotlib import pyplot as plt
from matplotlib.path import Path
from matplotlib import patches


fig = plt.figure()
ax = fig.add_subplot()


# تنظیم مسیر
verts = [(-1.5, 0), (0, 1), (1.5, 0), (0, -1), (-1.5, 0)]
codes = [Path.MOVETO, Path.CURVE4, Path.LINETO, Path.LINETO, Path.CLOSEPOLY]
path = Path(vertices=verts, codes=codes)


# اضافه کردن به اسیکس
patch = patches.PathPatch(path, lw=4)
ax.add_patch(patch)


ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)

plt.show()
