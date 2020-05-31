from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.NewPot, name='newpot'),
    path('/potlist', views.PotList, name='potlist'),

]
