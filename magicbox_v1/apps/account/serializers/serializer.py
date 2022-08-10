'''
Author: Galen Tong
Date: 2022-08-08 10:57:34
LastEditTime: 2022-08-10 22:17:39
Description: 
'''
from rest_framework import serializers, exceptions
from rest_framework.exceptions import ValidationError
from .. import models


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(label="用户名", required=True)
    password = serializers.CharField(label="密码", min_length=3, required=True)


class RegistrySerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(
        label="确认密码", min_length=3, write_only=True, error_messages={"min_length": "密码不可以小于3位"})
    password = serializers.CharField(
        label="密码", min_length=3, write_only=True, error_messages={"min_length": "密码不可以小于3位"})

    class Meta:
        model = models.UserInfo
        fields = ['username', 'password', 'confirm_password', 'email']

    def validate_username(self, value):
        exists = models.UserInfo.objects.filter(username=value).exists()
        if exists:
            raise ValidationError("用户名已存在")
        return value

    def validate_confirm_password(self, value):
        password = self.initial_data.get("password")
        if password == value:
            return value
        raise ValidationError("两次输入密码不一致")

    def validate_email(self, value):
        exists = models.UserInfo.objects.filter(email=value).exists()
        if exists:
            raise ValidationError("该邮箱已经存在")
        return value
