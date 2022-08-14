'''
Author: Galen Tong
Date: 2022-08-08 10:32:29
LastEditTime: 2022-08-14 12:44:16
Description: 
'''
from django.db import models
from django.utils import timezone
# Create your models here.


class HealthInfo(models.Model):
    magicbox_user = models.ForeignKey(
        "account.UserInfo", verbose_name="创建人", on_delete=models.CASCADE)
    time = models.DateTimeField(verbose_name="记录时间", default=timezone.now)
    health_detail = models.CharField(
        verbose_name="详情记录", max_length=500, null=True, blank=True)
    text = models.IntegerField(verbose_name="疼痛等级", choices=(
        (1, "轻微"),
        (2, "中等"),
        (3, "严重"),
    ), default=3)
