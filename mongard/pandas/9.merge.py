"""
- ترکیب دیتافریم‌ها
    - concat
    - merge

"""
import pandas as pd


g1 = pd.read_csv("./files/groups1.csv")
g2 = pd.read_csv("./files/groups2.csv")

cat = pd.read_csv("./files/categories.csv")
city = pd.read_csv("./files/cities.csv", dtype={"zip": "string"})


### concat
# چسباندن چند دیتافریم
# method 1
# ایندکس جدید ساخته میشه
groups1 = pd.concat(
    (g1, g2),
    # ایندکس‌های جدید بسازه
    ignore_index=True,
    axis=0
)

# method 2
# ایندکس‌های قبلی میان
groups2 = pd.concat(
    (g1, g2),
    # مشخص کردن هر دیتافریم
    keys=["G1", "G2"]
)

### merge
# left: groups1, right: cat

# گرفتن اسم کتگوری از دیتافریم دیگه
# just (in left)
groups1.merge(right=cat, how="left", on="category_id")

# فقط مشترک‌ها رو برمیگردونه
# (in left) and (in right)
groups1.merge(right=cat, how="inner", on="category_id")

# اجتماع
# (in left) or (in right)
groups1.merge(right=cat, how="outer", on="category_id")

# اگه اسم ستون فارن‌کی فرق داشته باشه
groups1.merge(right=city, how="outer", left_on="city_id", right_on="id",
            #   بر چه اساسی اومده
              indicator=True
)

## استفاده از ایندکس
city = city.set_index("id")
groups1.merge(right=cat, how="left", left_on="city_id", right_index=True)
