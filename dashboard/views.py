from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from django.views.generic import UpdateView
from django.http import HttpResponseRedirect
import datetime
import random


# Create your views here.



def dash(request):

    if request.session.get('accessToken', default=True):
        sysUpDate = '12apr20'
        temperature = random.randint(15, 30)
        ctxt = {
            'sysUpDate': sysUpDate,
            'temperature': temperature
        }
        return render(request, 'paper_dashboard/dash.html', context=ctxt)

    else:
        return redirect('login')


def condition(request):
    if request.session.get('accessToken', default=False):
        return render(request, 'paper_dashboard/condition.html')

    else:
        return redirect('login')

def control(request):
    if request.session.get('accessToken', default=False):
        return render(request, 'paper_dashboard/control.html')

    else:
        return redirect('login')
