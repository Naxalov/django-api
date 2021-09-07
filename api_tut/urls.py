
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def salom(request):
    return HttpResponse('HI')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hi/',salom)
]
