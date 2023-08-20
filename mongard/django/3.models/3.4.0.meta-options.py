"""
یه سری ویژگی های اضافی هستن که روی کل دیتابیس اعمال میشن

- انواع ویژگی ها:
    * ordering
        ~ برای ترتیب در کل دیتابیس
    * abstract
        ~ جلوگیری از تکراری شدن فیلدها در مدل ها
        ~ ویدیوی تک قسمتیش حتما دیده بشه
"""
# ex
from django.db import models
from django.urls import reverse


class Post(models.Model):
	user = models.ForeignKey("User", on_delete=models.CASCADE, related_name='posts')
	body = models.TextField()
	slug = models.SlugField()
	title = models.CharField(max_length=100, null=True, blank=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta: # <------------------------------
		ordering = ['-created']

	def __str__(self):
		return f'{self.slug} - {self.updated}'
