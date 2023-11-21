from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login
from .models import Login


def index(request):
    return render(request, "index.html")


def user(request):
    return render(request, "user.html")


def form(request):
    if request.method == 'POST':
        username = request.POST.get('login')
        password = request.POST.get('password')
        user_authenticated = False

        for user in Login.objects.all():
            if user.name == username and user.password == password:
                user_authenticated = True
                us = user.name
                adm = user.admin_is
                break

        if user_authenticated:
            return render(request, 'user.html',{'us':us, 'adm':adm})
        else:
            return render(request, 'form.html', {'text': 'Логин и(или) пароль не верные.'})
    return render(request, 'form.html')
