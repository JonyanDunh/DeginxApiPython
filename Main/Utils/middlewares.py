import logging
import json
from django.db import DatabaseError
from django.http.response import JsonResponse,FileResponse,HttpResponse
from django.http import HttpResponseServerError
from django.middleware.common import MiddlewareMixin
from django.core.serializers.json import DjangoJSONEncoder


logger = logging.getLogger('django')


Results={
200: 'Success', 
500: 'Server Error',
404: 'Not Found' ,
400:'Error',
419:'Make sure that the form is complete'
 }


class ExceptionMiddleware(MiddlewareMixin):
    """统一异常处理中间件"""
 

    def process_exception(self, request, exception):
        return HttpResponse(exception,status=500)

    def process_response(self, request, response):
        if isinstance(response, JsonResponse):
            return JsonResponse({'code': response.status_code, 'message': Results[response.status_code],'data': json.loads(response.content.decode("utf-8"))  },encoder=DjangoJSONEncoder,status=response.status_code)
        elif isinstance(response, HttpResponse):
            return JsonResponse({'code': response.status_code, 'message': Results[response.status_code],'data': response.content.decode("utf-8")  }, encoder=DjangoJSONEncoder,status=response.status_code)
        else:
            return response