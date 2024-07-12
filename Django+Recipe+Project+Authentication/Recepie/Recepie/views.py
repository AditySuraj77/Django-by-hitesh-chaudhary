from django.shortcuts import render,redirect,HttpResponse



def Home(request):
    return render(request,'layout.html')