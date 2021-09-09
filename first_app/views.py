from django.shortcuts import render
from django.http import JsonResponse

def first(request):
    return JsonResponse({"data":7})
    
def home(request):
    print(request)
    return JsonResponse({"data":7})