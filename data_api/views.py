from django.http import HttpResponse
from django.http import JsonResponse

def get_data(request):
    return JsonResponse({"data":7})
