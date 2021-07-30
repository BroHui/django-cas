from django.contrib import admin
from django.urls import path, include
from cas_server.views import auth, login

urlpatterns = [
    path('auth', auth),
    path('login', login),
]