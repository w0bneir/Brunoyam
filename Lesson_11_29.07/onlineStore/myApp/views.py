from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
import datetime

from .models import Product, Price


def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products, 'year': datetime.datetime.now().year})


def product_price(request, product_id):
    product_prices = Price.objects.filter(product_id=product_id)
    return render(request, 'product_price.html', {'product_prices': product_prices, 'year': datetime.datetime.now().year})


def home(request):
    return render(request, 'home.html', {'year': datetime.datetime.now().year})


def reg(request):
    if request.method == 'POST':
        data = request.POST
        login = data.get("login")
        email = data.get("email")
        password = data.get("password")
        existing_user = User.objects.filter(username=login).first()
        existing_email = User.objects.filter(email=email).first()
        if existing_user:
            messages.error(request, 'Пользователь с таким логином уже существует')
        elif existing_email:
            messages.error(request, 'Пользователь с таким email уже существует')
        else:
            user = User.objects.create_user(username=login, email=email, password=password)
            login(request, user)
            return redirect('home')
    return render(request, 'reg.html', {'year': datetime.datetime.now().year})


def login_(request):
    if request.method == 'POST':
        data = request.POST
        username = data.get("login")
        password = data.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Неверный логин или пароль')
    return render(request, 'login.html', {'year': datetime.datetime.now().year})


def logout_(request):
    logout(request)
    return redirect('login')
