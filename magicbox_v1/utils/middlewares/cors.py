'''
Author: Galen Tong
Date: 2022-08-10 00:00:07
LastEditTime: 2022-08-10 00:07:31
Description:
'''

from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse


class CorsMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.method == "OPTIONS":
            return HttpResponse()

    def process_response(self, request, response):
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Headers"] = "*"
        response["Access-Control-Allow-Methods"] = "*"
        return response
