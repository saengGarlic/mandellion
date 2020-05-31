from django.shortcuts import render, redirect
from django.contrib.auth.models import User

import jwt
import datetime
from django.contrib import auth
from django.http import HttpResponse, JsonResponse


# Create your views here.

def saveSession(request, accesstoken, createdtime, username):
    request.session['accessToken'] = accesstoken
    request.session['createdTime'] = createdtime
    request.session['userName'] = username



def signup(request):
    if request.method == "POST":
        if (request.POST["username"]!= '')&(request.POST["password1"]!= '')&(request.POST["password2"]!= ''):
            if request.POST["password1"] == request.POST["password2"]:
                user = User.objects.create_user(username=request.POST["username"], password=request.POST["password2"])

                return redirect('login')
            return render(request, 'signup.html', context={'error': 'failed to confirm password'})
        else:
            return render(request, 'signup.html', context={'error': 'please complete the entries'})

    return render(request, 'signup.html')


def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)

            now = datetime.datetime.now()
            nowstr = str(now.month)+str(now.day)+str(now.hour)+str(now.minute)+str(now.second)

            accesstoken = jwt.encode({'username': username}, nowstr, algorithm='HS256').decode('UTF-8')
            saveSession(request, accesstoken, nowstr, username)
            res = HttpResponse({'success': True})
            res.set_cookie('accessToken', accesstoken)

            return res  #render(request, 'login.html', {'success': res})
        else:
            return render(request, 'login.html', {'error': 'username or password is incorrect'})
    else:
        return render(request, 'login.html')


def logout(request):
    res = HttpResponse({'success': True})
    res.delete_cookie('accessToken')
    request.session.clear()
    auth.logout(request)
    return res

