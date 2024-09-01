"""
- coordinates
    - کشیدن یک خط
- آدرس دهی با طول و عرض جغرافیایی انجام میشه

"""
import matplotlib.pyplot as plt
import cartopy.crs as ccrs


fig = plt.figure(figsize=(13, 13))
ax = fig.add_subplot(projection=ccrs.PlateCarree())

ax.stock_img()


# کشیدن نقطه در لندن و نیویورک
ax.plot(-0.12, 51, "o")
ax.text(2, 51, "London")
ax.plot(-74, 40, "o")
ax.text(-74, 44, "New York")

# کشیدن خط
ax.plot(
    # طول‌های جغرافیایی
    [-0.12, -74],
    # عرض‌های جغرافیایی
    [51, 40],
)


plt.show()
