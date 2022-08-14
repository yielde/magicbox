'''
Author: Galen Tong
Date: 2022-08-10 23:44:09
LastEditTime: 2022-08-14 13:01:42
Description: 
'''
from rest_framework import serializers, exceptions
from rest_framework.exceptions import ValidationError
from .. import models


class HealthSerializers(serializers.ModelSerializer):
    id = serializers.IntegerField(allow_null=True)
    class Meta:
        model = models.HealthInfo
        fields = ['id', 'time', 'health_detail', 'text']


class HealthListSerializers(serializers.ModelSerializer, serializers.Serializer):
    id = serializers.IntegerField(allow_null=True)
    class Meta:
        model = models.HealthInfo
        fields = ['id', 'time', 'health_detail', 'text']
        extra_kwargs = {
            'text':{
                'error_messages':{
                    'invalid_choice':'标签选择错误',
                    'null':'标签为必选项',
                }
            }
        }