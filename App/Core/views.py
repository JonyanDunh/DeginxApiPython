from django.http.response import JsonResponse,FileResponse,HttpResponse
from django.core.serializers.json import DjangoJSONEncoder
def handler404(request, *args, **argv):
    return HttpResponse("The requested resource was not found on this server.",status=404)


def handler500(request, *args, **argv):
    return HttpResponse("Server Error",status=500)