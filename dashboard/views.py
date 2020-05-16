from django.shortcuts import render
from django.views.generic import TemplateView, View
from django.http import HttpResponseRedirect


# Create your views here.


def mainpage(request):
    sysUpDate = '16APR20'
    temperature = 99
    ctxt = {
        'sysUpDate' : sysUpDate,
        'temperature' : temperature
    }
    return render(request, 'paper_dashboard/mainpage.html', context=ctxt)

def condition(request):
    return render(request, 'paper_dashboard/condition.html')

def control(request):
    return render(request, 'paper_dashboard/control.html')

