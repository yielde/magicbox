'''
Author: Galen Tong
Date: 2022-08-08 10:32:29
LastEditTime: 2022-08-14 13:12:21
Description:
'''
from django.core import serializers
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from .serializers.serializers import HealthSerializers, HealthListSerializers
from utils.ext import mixins
from utils import return_code
from . import models


class HealthInfo(mixins.MagicboxCreateModelMixin, mixins.MagicboxListModelMixin, mixins.MagicboxDestroyModelMixin, mixins.MagicboxUpdateModelMixin, GenericViewSet):
    authentication_classes = []
    permission_classes = []
    queryset = models.HealthInfo.objects.all()
    serializer_class = HealthListSerializers

    def perform_create(self, serializer):
        serializer.save(magicbox_user_id=1)
