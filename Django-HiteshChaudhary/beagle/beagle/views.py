from django.http import HttpResponse
from django.shortcuts import render


def Home(request):
    # return HttpResponse("Welcome to home")
    return render(request, 'pages/index.html')


def Contact(request):
    return HttpResponse("Welcome to contact")


def About(request):
    return HttpResponse("Welcome to about us")