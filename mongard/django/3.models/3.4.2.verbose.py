"""
- verbose_name
    * اسم مستعاری است که برای مدل‌ها میتونیم اختصاص بدیم

- verbose_name_plural
    * نام مستعار بصورت جمع

"""
from django.db import models


class Category(models.Model):
	sub_category = models.ForeignKey('self', on_delete=models.CASCADE, related_name='scategory', null=True, blank=True)
	is_sub = models.BooleanField(default=False)
	name = models.CharField(max_length=200)
	slug = models.SlugField(max_length=200, unique=True)

	class Meta:
		ordering = ('name',)
		verbose_name = 'category'
		verbose_name_plural = 'categories'
