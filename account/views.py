from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth

# Create your views here.

def login(request):
    if request.method == 'POST':
        uname=request.POST['username']
        p1=request.POST['password']
        user=auth.authenticate(username=uname,password=p1)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Invalid details please contact admin...')
            return redirect('login')
    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')