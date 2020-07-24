from django.contrib.auth.models import User
from django.shortcuts import render,redirect ,get_object_or_404
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import auth
from django.contrib import messages
from django.db import IntegrityError
from .models import Todo


def index(request):
    if request.method=="GET":
        return render(request, 'index.html')




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
                return redirect('currenttodo')
            except IntegrityError:
                return render(request, 'signup.html',{ 'error': 'This Username has been already taken'})
        else:
            return render(request,'signup.html', {'error':'Both password not matched'})


def loginuser(request):
    if request.method=="GET":
        return render(request,'login.html')
    else:
        user=authenticate(request, username=request.POST['username'],password=request.POST['password'])
        if user is None:
            return render(request,'login.html', {'error':'This Username or Password incorrect'})
        else:
            login(request,user)
            return redirect('currenttodo')


def logout(request):
    auth.logout(request)
    return redirect('home')


def currenttodo(request):
    todos=Todo.objects.filter(user=request.user,datecompleted__isnull=True)
    return render(request,'currenttodo.html',{"todos":todos})


def viewtodo(request,todo_pk):
    todos = get_object_or_404(Todo,id=todo_pk, user=request.user)
    if request.method=="GET":
        return render(request,'viewtodo.html',{'todos':todos})
    if request.method=="POST":
        todo = Todo.objects.get(id=todo_pk, user= request.user)
        todo.title = request.POST['title']
        todo.memo = request.POST['memo']
        todo.important = request.POST['important']
        todo.user = request.user
        todo.save()
        return redirect("currenttodo")



def createtodo(request):
    if request.method=="GET":
        return render(request,'createtodo.html')
    else:
        try:
            todo = Todo()
            todo.title = request.POST['title']
            todo.memo = request.POST['memo']
            todo.important=request.POST['important']
            todo.user = request.user
            todo.save()
            return redirect("currenttodo")
        except ValueError:
            return redirect('createtodo',{'error':"bad data inserted"})