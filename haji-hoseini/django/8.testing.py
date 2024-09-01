

# 1
# بازکردن فایل زیر
""".\[app-name]\tests.py"""

# 2
# نوشتن کد زیر
from django.test import TestCase
from django.shortcuts import reverse
from django.contrib.auth.models import User

from .models import database_name

# style 1
class TestName(TestCase) :
    def setUp(self) : #== __init__
        self.user_test = User.objects.create(username='user1')
        self.database_name_obj = database_name.objects.create(
            sotoon_name1='everything1', 
            sotoon_name8=database_name.STATUS_CHOICES[0],
            author=self.user_test
        )
    
    # test 404
    def test_testname1(self) :
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    # test url name
    def test_testname2(self) :
        response = self.client.get(reverse('[url-name]'))
        self.assertEqual(response.status_code, 200)

    def test_testname3(self) : # with input
        response = self.client.get(reverse('[url-name]', arg=[self.database_name_obj.id]))
        self.assertEqual(response.status_code, 200)

    # test database 
    def test_testname4(self):
        response = self.client.get(reverse('notes_list'))
        self.assertContains(response, 'everything2') # نشان میدهد این متن در صفحه وجود دارد یا نه

    def test_status_404_if_post_id_not_exist(self):
        response = self.client.get(reverse('blog_detail_url', args=[999]))
        self.assertEqual(response.status_code, 404)

# style 2
class TestName(TestCase) :
    @classmethod
    def setUpTestData(cls) :
        cls.user_test = User.objects.create(username='user1')
        cls.database_name_obj = database_name.objects.create(
            sotoon_name1='everything1', 
            sotoon_name8=database_name.STATUS_CHOICES[0],
            author=cls.user_test
        )
    
    # test 404
    def test_testname1(self) :
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    # test url name
    def test_testname2(self) :
        response = self.client.get(reverse('[url-name]'))
        self.assertEqual(response.status_code, 200)

    def test_testname3(self) : # with input
        response = self.client.get(reverse('[url-name]', arg=[self.database_name_obj.id]))
        self.assertEqual(response.status_code, 200)

    # test database 
    def test_testname4(self):
        response = self.client.get(reverse('notes_list'))
        self.assertContains(response, 'everything2') # نشان میدهد این متن در صفحه وجود دارد یا نه

    def test_status_404_if_post_id_not_exist(self):
        response = self.client.get(reverse('blog_detail_url', args=[999]))
        self.assertEqual(response.status_code, 404)

# نکته:
# قبل همه تابع های تست باید کلمه تست بیاید
""" def test-[test-name] :... """


# 3
# ران کردن زیر
"""python manage.py test"""
