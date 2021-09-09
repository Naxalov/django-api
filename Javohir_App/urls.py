from django.urls import path

from . import views
urlpatterns = [
    path('sum/', views.sum_two_digits),
    path('mult/', views.digits_multiplication),
    path('odd_even/', views.find_odd_even)
]