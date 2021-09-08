
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

from data_api.views import get_data

urlpatterns = [
    path('admin/', admin.site.urls),
    path('get_data/', get_data),
]
