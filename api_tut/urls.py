
from django.contrib import admin
from django.urls import path,include
from django.http import HttpResponse


from data_api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('img/',include('first_app.urls'))

]
