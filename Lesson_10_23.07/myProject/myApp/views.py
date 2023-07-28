from django.shortcuts import render, redirect
from .models import User
from django.db import IntegrityError


def index(request):
    return render(request, 'index.html')


def add_user(request):
    if request.method == 'POST':
        # Обработка данных из формы и сохранение в базе данных
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name', '')

        try:
            user = User(username=username, email=email, password=password, first_name=first_name, last_name=last_name)
            user.save()
        except IntegrityError:
            error_message = "Данные уже используются другим пользователем."
            return render(request, 'add_user.html', {'error_message': error_message})
        else:
            error_message = "Данные успешно добавлены."
            return render(request, 'add_user.html', {'error_message': error_message})
    return render(request, 'add_user.html')
def users_list(request):
    users = User.objects.all()
    return render(request, 'users_list.html', {'users': users})