"""
- cartopy
    - extra-pac
    - برای ایجاد کردن نقشه‌های جغرافیایی

- Coordinate reference systems (CRS)
    - سیستم مرجع مختصات
    - هسته‌ی این داستان

"""
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cf


fig = plt.figure(figsize=(13, 13))
ax = fig.add_subplot(projection=ccrs.PlateCarree())


## Base
# کشیدن خطوط ساحلی
# ax.coastlines()

# کشیدن نقشه جغرافیای
ax.stock_img()


## Feature
# خطوط ساحلی
ax.add_feature(cf.COASTLINE, lw=0.3, color="r")

# مرز کشورها
ax.add_feature(cf.BORDERS, lw=0.3)

# رودخانه‌ها
ax.add_feature(cf.RIVERS, lw=0.3, color="b")


plt.show()
