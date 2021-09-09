from django.http import JsonResponse

def get_data(request):
    return JsonResponse({"data":'get_data'})
