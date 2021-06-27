from django.shortcuts import render


def index(request):
    return render(request, 'mysite/index.html')


def Register(request):
    return render(request, 'mysite/Register.html')


def signin(request):
    return render(request, 'mysite/signin.html')


def contact(request):
    return render(request, 'mysite/contact.html')
