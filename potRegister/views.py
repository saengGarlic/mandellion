from django.shortcuts import render, redirect
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import *
from .serializers import *
from .form import *
import datetime

# Create your views here.

def NewPot(request):
    accesstoken = request.COOKIES.get('accessToken')
    if accesstoken is not None:
        if request.method == "POST":
            form = potReg(request.POST)
            if form.is_valid():
                pot = form.save(commit=False)
                pot.regDate = datetime.datetime.now()
                pot.save()
                return redirect('potlist')

        else:
            form = potReg()
            return render(request, 'potRegister.html', {'form': form})

    else:
        return redirect('')

def PotList(request):
    accesstoken = request.COOKIES.get('accessToken')
    if accesstoken is not None:
        pots = Pot.objects.all()
        return render(request, 'potList.html', {'pots': pots})

    else:
        return redirect('login')


