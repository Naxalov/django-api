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

def digits_multiplication(request):

	if request.method == 'GET':
		a = request.GET.get("a",1)
		b = request.GET.get("b",1)
		print(a,b)
		response = {"SUM":int(a)*int(b)}
		return JsonResponse(response)

def find_odd_even(request):
	if request.method == 'GET':
		a = int(request.GET.get("a",0))
		b = int(request.GET.get("b",0))
		if a == 0:
			if b == 0:
				response = {"a":"zero number","b":"zero number"}
			else:
				if b%2 == 1:
					response = {"a":"zero number","b":"odd"}
				else:
					response = {"a":"zero number","b":"odd"}
		elif b == 0:
			if a == 0:
				response = {"a":"zero number","b":"zero number"}
			else:
				if a%2 == 1:
					response = {"b":"zero number","a":"odd"}
				else:
					response = {"b":"zero number","a":"odd"}
		else:
			if a%2 == 1:
				if b%2 == 1:
					response = {"b":"odd","a":"odd"}
				else:
					response = {"b":"even","a":"odd"}
			else:
				if b%2 == 1:
					response = {"b":"odd","a":"even"}
				else:
					response = {"b":"even","a":"even"}
		
		return JsonResponse(response)