'''
Author: Galen Tong
Date: 2022-08-08 23:45:09
LastEditTime: 2022-08-14 14:06:09
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


class MagicboxUpdateModelMixin(mixins.UpdateModelMixin):
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(
            instance, data=request.data, partial=partial)
        if not serializer.is_valid():
            return Response({"code": return_code.VALIDATE_ERROR, "detail": serializer.errors})
        res = self.perform_update(serializer)
        if res:
            return Response({"code": return_code.SUCCESS, "data": res})
        else:
            return Response({"code": return_code.SUCCESS, "data": serializer.data})


class MagicboxListModelMixin(mixins.ListModelMixin):
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response({"code": return_code.SUCCESS, "data": serializer.data})


class MagicboxDestroyModelMixin(mixins.DestroyModelMixin):
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        try:
            res = self.perform_destroy(instance)
            if res:
                return Response({"code": return_code.SUCCESS, "data": res})
            else:
                return Response({"code": return_code.SUCCESS, "data": "删除成功"})
        except Exception as e:
            return Response({"code": return_code.OPERATE_ERROR, "detail": str(e)})