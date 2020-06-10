from django.shortcuts import render, redirect
from ..potRegister.models import *

# Create your views here.



def PlantList(request):
    accesstoken = request.COOKIES.get('accessToken')
    if accesstoken is not None:
        
        pots = Pot.objects.all()
        return render(request, 'potList.html', {'pots': pots})

    else:
        return redirect('login')


