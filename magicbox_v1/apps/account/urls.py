'''
Author: Galen Tong
Date: 2022-08-08 10:51:41
LastEditTime: 2022-08-09 23:10:33
Description: 
'''
from django.urls import path
from . import views
from rest_framework import routers


router = routers.SimpleRouter()

router.register('registry', views.RegistryView, 'registry')

urlpatterns = [
    path('login/', views.LoginView.as_view()),
]

urlpatterns += router.urls
