'''
Author: Galen Tong
Date: 2022-08-08 10:42:40
LastEditTime: 2022-08-11 21:23:33
Description: 
'''
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from utils import return_code
from .serializers.serializer import LoginSerializer, RegistrySerializer
from . import models
from utils.ext import mixins


class LoginView(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        if not serializer.is_valid():
            # 用户名密码不能为空
            return Response({"code": return_code.FIELD_ERROR, "detail": serializer.errors})

        username = serializer.validated_data.get("username")
        password = serializer.validated_data.get("password")
        user_object = models.UserInfo.objects.filter(
            username=username, password=password).first()
        if not user_object:
            return Response({"code": return_code.VALIDATE_ERROR, "detail": "用户名或密码错误"})

        return Response({"code": return_code.SUCCESS, "data": {"username": username}})


class RegistryView(mixins.MagicboxCreateModelMixin, GenericViewSet):
    authentication_classes = []
    permission_classes = []
    serializer_class = RegistrySerializer

    def perform_create(self, serializer):
        serializer.save(magicbox_user_id=self.request.user.user_id)
