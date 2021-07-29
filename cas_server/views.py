# coding: utf-8

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate

# Create your views here.


def auth(request):
    # return HttpResponse('logined', status=200)
    return HttpResponse('Unauthorized', status=401)


def login(request):
    if request.method == 'GET':
        return render(request, 'cas_server/login.html', {})
    elif request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        remember_me = request.POST.get('remember-me', 'off') == 'on'
        print(username, password, remember_me)
        user = authenticate(username=username, password=password)
        if user is not None:
            # A backend authenticated the credentials
            return HttpResponse('login ok')
        else:
            # No backend authenticated the credentials
            return HttpResponse('login failed')

