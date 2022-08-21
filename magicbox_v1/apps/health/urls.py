'''
Author: Galen Tong
Date: 2022-08-08 10:36:57
LastEditTime: 2022-08-20 19:04:32
Description: 
'''
from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.SimpleRouter()


router.register('', views.HealthInfo, 'health')
urlpatterns = [
    path('stastic/', views.HealthStastics.as_view()),
]

urlpatterns += router.urls
