# Internationalization = i18n
# چندزبانه کردن سایت


# 1
# open "config/settings.py" and edit bellow code
LANGUAGE_CODE = 'fa'

TIME_ZONE = 'Asia/Tehran'

USE_I18N = True

USE_TZ = True

USE_L10N = True # localization

# 2
# in html:
# متن هایی که نیاز به ترجمه دارند را به صورت زیر در می آوریم
"""
{% load i18n %}

<p>
    {% trans '[english-text]' %}
</p>
"""

# 3
# create bellow directory
"[app-name]/locale"

# 4
# run bellow code in commend
"cd [app-name]"
"django-admin makemessages -l fa"

# 5
# نوشتن ترجمه هر متن آورده شده
# ex:
"""
#: .\templates\products\products_detail.html:178
msgid "submit"
msgstr "ارسال"
"""

# 6
# run bellow code in commend
"cd [app-name]"
"django-admin compilemessages"

# fuzzy: کلمات و جملات مشابه رو خودش پر میکنه
