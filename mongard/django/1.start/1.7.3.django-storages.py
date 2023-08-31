"""
- ذخیره کردن فایل‌ها در استوریج
- برای ابرآروان
    * Amazom S3

"""
# 0
"pip install django-storages"

# 1
# open "./config/settings.py" and edit this
INSTALLED_APPS = [
    '...',

    # Third-party apps
    'storages'
]

# ARVAN CLOUD STORAGE
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_ACCESS_KEY_ID = '44ee66a4-6fa4-40cb-bf7a-ce1d37d4c166'
AWS_SECRET_ACCESS_KEY = '43b318540c8ffda6f086ed6843095f4d4feb48d97ca39eed2817fca761bb488b'
AWS_S3_ENDPOINT_URL = 'https://s3.ir-thr-at1.arvanstorage.com'
AWS_STORAGE_BUCKET_NAME = 'django-shop'
AWS_SERVICE_NAME = 's3'
# اگه فایلی همنام یکی از فایل‌های قبلی آپلود شود جایگزین شود؟
AWS_S3_FILE_OVERWRITE = False
AWS_LOCAL_STORAGE = f'{BASE_DIR}/aws/'
