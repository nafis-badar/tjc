from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import auth
from django.contrib import messages
from django.db import IntegrityError

def index(request):
    return render(request,'index.html')


def signup(request):
    if request.method =="GET":
        return render(request, 'signup.html')
    else:
        useron = request.POST['username']
        password = request.POST['password1']
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=useron, password=password)
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'signup.html',{ 'error': 'This Username has been already taken'})
        else:
            return render(request,'signup.html', {'error':'Both password not matched'})

def loginuser(request):
    if request.method=="GET":
        return render(request,'signup.html')
    else:
        user=authenticate(request, username=request.POST['username'],password=request.POST['password'])
        if user is None:
            return render(request,'signup.html', {'error':'This Username or Password incorrect'})
        else:
            login(request,user)
            return redirect('home')


def logout(request):
    auth.logout(request)
    return redirect('signup')