from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate

# Create your views here.

# Здесь реализован обработчик введенных пользователем
# логина и пароля при попытке залогиниться на сайт:
def login(request):
    if request.method == 'POST':
        data = request.POST
        user = authenticate(email=data['email'], password=data['password'])
        if user and user.is_active:
            login(request, user)
            return redirect('index')
        else:
            return HttpResponse('Ваш аккаунт заблокирован')
    else:
            return render(request, 'login.html')


def register(request):
    return HttpResponse('Эта страница для регистрации пользователя')

def logout(request):
    logout(request)
    return redirect('login')

def change_password(request):
    return HttpResponse('Этот обработчик меняет пароль пользователя')
def reset_password(request):
    return HttpResponse('В этом обработчике реализована логика сброса пароля пользователя')

