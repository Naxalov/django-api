from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse


def first(request):
    return JsonResponse({"data":7})
    
def home(request):
    print(request)
    return JsonResponse({"data":7})

def multiply(request):
    #print(request)
    if request.method != 'GET':
        return  JsonResponse({"answer":'Please send Get request!'})

    listOfVal= list(request.GET.dict().values())
    if len(listOfVal)!=2:
        return JsonResponse({"answer":'Please send exactly 2 params!'})
       
    a=listOfVal[0]
    b=listOfVal[1]
    if isfloat(a) and isfloat(b):
        return JsonResponse({"answer":str(float(a)*float(b))})
    return JsonResponse({"answer":'Please send numbsers!'})
    
    

def isfloat(value):
  try:
    float(value)
    return True
  except ValueError:
    return False