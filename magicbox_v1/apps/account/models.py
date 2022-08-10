'''
Author: Galen Tong
Date: 2022-08-08 10:42:40
LastEditTime: 2022-08-10 22:58:30
Description: 
'''
from django.db import models


class UserInfo(models.Model):
    username = models.CharField(verbose_name="用户名", max_length=20)
    password = models.CharField(verbose_name="密码", max_length=64)
    email = models.EmailField(verbose_name="邮箱", unique=True, null=False)
    created_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True, null=False)
