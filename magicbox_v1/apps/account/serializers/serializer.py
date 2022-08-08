'''
Author: Galen Tong
Date: 2022-08-08 10:57:34
LastEditTime: 2022-08-08 22:13:41
Description: 
'''
from rest_framework import serializers


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(label="用户名", required=True)
    password = serializers.CharField(label="密码", min_length=6, required=True)
    
class RegistrySerializer(serializers.Serializer):
    username = serializers.CharField(label="用户名", required=True)
    password1 = serializers.CharField(label="密码", min_length=3, required=True)
    password2 = serializers.CharField(label="确认密码", min_length=3, required=True)
    