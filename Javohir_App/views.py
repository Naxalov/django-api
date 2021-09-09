from django.shortcuts import render
from django.http import JsonResponse, response
# Create your views here.

def sum_two_digits(request):

	if request.method == 'GET':
		a = request.GET.get("a",0)
		b = request.GET.get("b",0)
		print(a,b)
		response = {"SUM":int(a)+int(b)}
		return JsonResponse(response)
		
