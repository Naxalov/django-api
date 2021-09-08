from django.http import HttpResponse

def get_data(request):
    return HttpResponse("get_data page")

