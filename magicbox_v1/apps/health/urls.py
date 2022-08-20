'''
Author: Galen Tong
Date: 2022-08-08 10:36:57
LastEditTime: 2022-08-15 23:05:34
Description: 
'''
from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.SimpleRouter()


router.register('', views.HealthInfo, 'health')
urlpatterns = [
    path('stastics/', views.HealthStastics.as_view()),
]

urlpatterns += router.urls
