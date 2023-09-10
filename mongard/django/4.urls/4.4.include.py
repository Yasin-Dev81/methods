"""
- میتوانیم لینک‌هامون رو براساس کاربردشون تفکیک کنیم تا کد ترتمیزتر باشه

"""
# ex:
from django.urls import path, include
from . import views


bucket_urls = [
	path('', views.BucketHome.as_view(), name='bucket'),
	path('delete_obj/<str:key>/', views.DeleteBucketObject.as_view(), name='delete_obj_bucket'),
	path('download_obj/<str:key>/', views.DownloadBucketObject.as_view(), name='download_obj_bucket'),
]

category_urls = [
	path('<slug:category_slug>/', views.HomeView.as_view(), name='category_filter')
]

urlpatterns = [
	path('', views.HomeView.as_view(), name='home'),
	path('bucket/', include(bucket_urls)),
    path('category/', include(category_urls))
]
