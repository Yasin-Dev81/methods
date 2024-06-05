"""
- groupby
    - برای دسته بندی داده‌ها بکار میره

"""
import pandas as pd


food_data = {
    "Item": ["Bnana", "Cucumber", "Orange", "Tomato", "Watermelon"],
    "Type": ["Fruit", "Vegetable", "Fruit", "Vegetable", "Fruit"],
    "OnlineShop": [True, True, False, False, True, False],
    "count": [10, 23, 45, 14, 2],
    "Price": [0.99, 1.25, 0.25, 0.33, 3.00]
}

superi = pd.DataFrame(data=food_data)

# دسته‌بندی براساس یه ستون
g = superi.groupby(by="Type")
# دسته‌بندی براساس 2 ستون
g2 = superi.groupby(by=["Type", "OnlineShop"])


## mean
# method 1
print(g.mean(numeric_only=True), end="\n-----------------\n")

# method 2
print(g.get_group("Fruit").mean(numeric_only=True))

## دیدن ایندکس‌های هر گروپ
g.groups

# دیدن تعداد هر گروپ
g.size

# اولین مقدار هر گروپ
g.first()

# آخرین مقدار هر گروپ
g.last()

## n امین مقدار هر گروپ
# اولین
g.nth(0)

# از هر گروپ 3تای اول
g.head(3)

# از هر گروپ 3تای آخر
g.tail(3)

# گرفتن یه گروه
g.get_group("Fruit")
g2.get_group(("Fruit", False))

# اجرای فانکشن‌های جداگانه برای هر ستون
x= g.agg(
    func={
        "count": "max",
        "Price": "mean"
    }
)
print(x)

## گرفتن اولین از هر گروپ بر اساس سورت خودمون
# بزرگترین تعداد در هر گروپ
g.apply(lambda i: i.nlargest(1, "count"))
