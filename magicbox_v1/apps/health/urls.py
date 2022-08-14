'''
Author: Galen Tong
Date: 2022-08-08 10:36:57
LastEditTime: 2022-08-13 23:48:04
Description: 
'''
from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.SimpleRouter()


router.register('', views.HealthInfo, 'health')
urlpatterns = [
]

urlpatterns += router.urls
