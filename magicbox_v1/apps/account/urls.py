'''
Author: Galen Tong
Date: 2022-08-08 10:51:41
LastEditTime: 2022-08-08 22:04:47
Description: 
'''
from django.urls import path
from . import views


urlpatterns  = [
    path('auth/', views.LoginView.as_view()),
    path('registry/', views.Registry.as_view()),
]