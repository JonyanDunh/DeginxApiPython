import logging
import json
from django.db import DatabaseError
from django.http.response import JsonResponse,FileResponse,HttpResponse
from django.http import HttpResponseServerError
from django.middleware.common import MiddlewareMixin
from django.core.serializers.json import DjangoJSONEncoder



Results={
200: 'Success', 
500: 'Server Error',
404: 'Not Found' ,
400:'Error',
403:'Forbidden',
419:'Verify that the form data is accurate',
452:'The user already exists',
453:'Failed to create user, please try again',
454:'The user does not exist or has an incorrect password'
 }


class Middleware(MiddlewareMixin):

    def process_response(self, request, response):
        if isinstance(response, JsonResponse):
            return JsonResponse({'code': response.status_code, 'message': Results[response.status_code],'data': json.loads(response.content.decode("utf-8"))  },encoder=DjangoJSONEncoder,status=response.status_code)
        elif isinstance(response, HttpResponse):
            return JsonResponse({'code': response.status_code, 'message': Results[response.status_code],'data': response.content.decode("utf-8")  }, encoder=DjangoJSONEncoder,status=response.status_code)
        else:
            return response