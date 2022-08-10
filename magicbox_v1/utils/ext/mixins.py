'''
Author: Galen Tong
Date: 2022-08-08 23:45:09
LastEditTime: 2022-08-09 15:19:04
Description: 
'''
from rest_framework import mixins
from rest_framework.response import Response
from utils import return_code


class MagicboxCreateModelMixin(mixins.CreateModelMixin):
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if not serializer.is_valid():
            return Response({"code": return_code.VALIDATE_ERROR, "detail": serializer.errors})

        res = self.perform_create(serializer)
        return res or Response({"code": return_code.SUCCESS, 'data': serializer.data})
