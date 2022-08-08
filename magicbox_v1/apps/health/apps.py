'''
Author: Galen Tong
Date: 2022-08-08 10:32:29
LastEditTime: 2022-08-08 10:40:43
Description: 
'''
from django.apps import AppConfig


class HealthConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.health'
