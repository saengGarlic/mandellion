from django.urls import path
from . import views

urlpatterns = [
    path('dash/', views.dash, name='dash'),
    path('condition/', views.condition, name='condition'),
    path('control/', views.control, name='control')

]
