'''
Author: Galen Tong
Date: 2022-08-08 10:32:29
LastEditTime: 2022-08-19 17:41:30
Description:
'''
import time
from rest_framework.views import APIView
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


class HealthStastics(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, *args, **kwargs):
        queryset = models.HealthInfo.objects.all().order_by("time")
        ser = HealthListSerializers(queryset, many=True)
        response_data = []
        days = 0
        First = True
        for item in ser.data:
            date_key = item["time"]
            next_date = time.mktime(time.strptime(
                date_key, "%Y-%m-%dT%H:%M:%S"))
            if First:
                pre_date = next_date
                First = False
            days = round((next_date - pre_date) / 3600 / 24)
            print(next_date, "=====", days)
            response_data.append({date_key.split("T")[0]: days})
            pre_date = next_date

        return Response({"code": return_code.SUCCESS, "data": response_data})
