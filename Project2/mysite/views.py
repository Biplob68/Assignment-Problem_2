from django.urls import path, include
from django.shortcuts import render, redirect
from django.contrib import admin
from django.contrib import messages
from . import views

from mysite.models import Contact
from mysite.models import Login
from mysite.models import Reg
from django.contrib.auth.models import User
from django.contrib.auth.models import User, auth

def index(request):
    return render(request, 'mysite/index.html')


def Register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Already Taken!')
                return redirect('Register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken!')
                return redirect('Register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password1)
                user.save()
                messages.info(request, 'User Created!')
                return redirect('login')
        else:
            messages.info(request, 'Password is not matching!')
            return redirect('Register')
        return redirect('/')

    else:
        return render(request, 'mysite/Register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return render(request, 'mysite/index.html')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('login')
            # return redirect('/')
    else:
        return render(request, 'mysite/login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def contact(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        message = request.POST['message']
        print(first_name, email, message)
        ins = Contact(first_name=first_name, last_name=last_name, email=email, message=message)
        ins.save()
        print("Data has been save in database!")
    return render(request, "mysite/contact.html")
