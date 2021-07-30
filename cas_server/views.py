# coding: utf-8

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate

# Create your views here.


def auth(request):
    print(request.session.get('user', 'no user'), request.session.get('user_id', 'no id'))
    if request.session.get('user', None):
        login_user = request.session.get('user', '')
        login_user_id = request.session.get('user_id', '')
        response = HttpResponse()
        response.status_code = 200
        response.headers['X-Forwarded-User'] = login_user
        response.headers['X-Idcs-User'] = login_user_id
        return response
    else:
        return HttpResponse('Unauthorized', status=401)


def login(request):
    if request.method == 'GET':
        return render(request, 'cas_server/login.html', {})
    elif request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        remember_me = request.POST.get('remember-me', 'off') == 'on'
        user = authenticate(request=request, username=username, password=password)
        if user is not None:
            # A backend authenticated the credentials
            request.session['user'] = user.get_username()
            request.session['user_id'] = user.id
            print(dir(request.session))
            return HttpResponse('login ok')
        else:
            # No backend authenticated the credentials
            return HttpResponse('login failed')

