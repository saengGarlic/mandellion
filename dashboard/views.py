from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from django.views.generic import UpdateView
from django.http import HttpResponseRedirect, JsonResponse

#from django.contrib.auth.decorators import login_required

import datetime
import random


# Create your views here.


#@login_required
def dash(request):
    accesstoken = request.COOKIES.get('accessToken')
    if accesstoken is not None:
        if request.session.get('accessToken') == accesstoken:
            username = request.session.get('userName')
            sysUpDate = str(datetime.datetime.now())
            temperature = random.randint(15, 30)
            ctxt = {
                'sysUpDate': sysUpDate,
                'temperature': temperature,
                'user': username
            }
            return render(request, 'paper_dashboard/dash.html', context=ctxt)

        else: return redirect('login')

    else:
        return redirect('login')


def condition(request):
    accesstoken = request.COOKIES.get('accessToken')
    if accesstoken is not None:
        if request.session.get('accessToken') == accesstoken:
            username = request.session.get('userName')
            return render(request, 'paper_dashboard/condition.html', context={'user':username})

        else:
            return redirect('login')

    else:
        return redirect('login')

def control(request):
    accesstoken = request.COOKIES.get('accessToken')
    if accesstoken is not None:
        if request.session.get('accessToken') == accesstoken:
            username = request.session.get('userName')
            return render(request, 'paper_dashboard/control.html', context={'user':username})

        else:
            return redirect('login')

    else:
        return redirect('login')
