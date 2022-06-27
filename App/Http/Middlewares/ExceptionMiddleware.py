import logging
import json
from django.db import DatabaseError
from django.http.response import JsonResponse,FileResponse,HttpResponse
from django.http import HttpResponseServerError
from django.middleware.common import MiddlewareMixin
from django.core.serializers.json import DjangoJSONEncoder



class Middleware(MiddlewareMixin):

    def process_exception(self, request, exception):
        return HttpResponse(exception,status=500)
