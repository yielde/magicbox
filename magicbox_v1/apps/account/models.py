'''
Author: Galen Tong
Date: 2022-08-08 10:42:40
LastEditTime: 2022-08-08 12:37:59
Description: 
'''
from django.db import models


class UserInfo(models.Model):
    username = models.CharField(verbose_name="用户名", max_length=20)
    password = models.CharField(verbose_name="密码", max_length=64)


