from django.http.response import HttpResponse


from django.http import HttpResponse

def get_data():
    return HttpResponse('hi')