from django.shortcuts import render

# Create your views here.

def mainpage(request):
    return render(request, 'paper_dashboard/mainpage.html')

def condition(request):
    return render(request, 'paper_dashboard/condition.html')

def control(request):
    return render(request, 'paper_dashboard/control.html')

