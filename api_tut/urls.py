
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse


from data_api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hi/', views.get_data),

]
