"""
- وقتی چندتا ایندکس بخوایم داشته باشیم
- levels
    - از بیرونی‌ترین لایه شمرده میشه تا به درونی‌ترین لایه

- pd.MultiIndex
    - .from_arrays
        - آرایه میگیره
    - from_product
        - ابجکت ایتریبل (لیست) میگیره
    - from_tuples
        - تاپل میگیره
    - from_frame
        - دیتافریم میگیره

"""
import pandas as pd


## from tuples
foods = [
    ("Fruit", "Apple"),
    ("Fruit", "Banana"),
    ("Vegetable", "Boroccoli"),
    ("Vegetable", "Tomato")
]
data = [
    (3, 200, 95),
    (2, 130, 105),
    (5, 230, 22),
    (7, 310, 50)
]

mi = pd.MultiIndex.from_tuples(
    tuples=foods,
    # تعیین اسم لول‌ها
    names=["Group", "Item"]
)

store = pd.DataFrame(data=data, columns=["Price", "Weight", "Calory"], index=mi)
# print(store)


## from dataframe
# method 1
mv = pd.read_csv(
    "./files/movies.csv",
    # ستون‌هایی که بعنوان ایندکس درنظر بگیره
    index_col=[0, 1]
)

# method 2
ng = pd.read_csv(
    "./files/neighborhoods.csv",
    index_col=[0, 1, 2],
    # ردیف‌هایی که هدر (تایتل) هستن
    header=[0, 1]
)
print(ng)

# گرفتن ایندکس‌های یک لول مشخص
ng.index.get_level_values("City")

ng.index.get_level_values(1)


# اسم گذاشتن روی مالتی‌ایندکس‌ها
ng.columns.names = ["Category", "SubCategory"]

# سورت کردن دیتا براساس ایندکس‌ها
ng.sort_index(inplace=True)

# فیلتر کردن اطلاعات
# گرفتن همه‌ی دیتا‌های ستون‌های وارد شده
ng[[("Services", "Police"), ("Culture", "Museums")]]

# گرفتن ردیف‌های وارد شده
ng.loc[("VA", "Laurentown")]

# فیلتر ردیف و ستون ترکیبی
x = ng.loc[("VA", "Laurentown"), ("Culture", "Museums")]
print(x)


# سرچ‌کردن در دیتا
ng.xs(key="601 Richards Road", level="Street")

ng.xs(key=("MT", "601 Richards Road"), level=("State", "Street"))


## عوض کردن ترتیب لول‌های دیتا
ng.reorder_levels(order=("City", "Street", "State"))

# ریست کردن همه چیز
ng.reset_index(
    col_level="SubCategory",
    # حذفشون هم بکنه
    drop=True
)

# ست کردن ایندکس
ng.set_index(keys=("City", ))
