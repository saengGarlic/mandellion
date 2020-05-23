from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from django.contrib import auth
import jwt
from django.http import HttpResponse, JsonResponse

# Create your views here.


def signup(request):
    if request.method == "POST":
        if (request.POST["username"]!= '')&(request.POST["password1"]!= '')&(request.POST["password2"]!= ''):
            if request.POST["password1"] == request.POST["password2"]:
                user = User.objects.create_user(username=request.POST["username"], password=request.POST["password2"])
                accessToken = jwt.encode({'username':user.username}, user.password, algorithm = 'HS256')
                res = JsonResponse({'success': True})
                res.set_cookie('access_token', accessToken)
                auth.login(request, user)
                return res
            return render(request, 'signup.html', {'error': 'failed to confirm password'})
        else:
            return render(request, 'signup.html',{'error': 'please complete the entries'})

    return render(request, 'signup.html')


def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            accessToken = jwt.encode({'username': username}, password, algorithm='HS256').decode('UTF-8')
            res = JsonResponse({'success': True})
            res.set_cookie('accessToken', accessToken)
            auth.login(request, user)
            return res
        else:
            return render(request, 'login.html', {'error': 'username or password is incorrect'})
    else:
        return render(request, 'login.html')

def logout(request):
    res = JsonResponse({'success': True})
    res.delete_cookie('accessToken')
    auth.logout(request)
    return res

