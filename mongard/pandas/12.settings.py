"""

"""
import pandas as pd

# دیدن آپشن‌های پانداز‍
pd.describe_option()

# دیدن وضعیت یه آپشن خاص
pd.describe_option("display.max_rows")

# گرفتن مقدار آپشن موردنظر
pd.get_option("display.max_rows")
# or
pd.options.display.max_rows


# تنظیم آپشن
pd.set_option("display.max_rows", 200)
# or
pd.options.display.max_rows = 200


# تنظیم تعداد رقم اعشار
pd.options.display.precision = 2


# اگه عددی کمتر از این بود ارزش تحلیل نداره و صفرش کن
pd.options.display.chop_threshold = 0.25
