from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from todo import models
from todo.models import TODOO
from django.contrib.auth import authenticate
from django.contrib.auth import authenticate,login,logout

def signup(request):
 if request.method == 'POST':
    username = request.POST.get('username')
    email = request.POST.get('email')
    password = request.POST.get('password')
    print(username,email,password)
    my_user = User.objects.create_user(username=username, email=email, password=password)
    my_user.save()
    return redirect('/login')
 return render(request,'signup.html')

def loginn(request):
 if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')
    print(username,password)
    user = authenticate(request,username = username,password=password)
    if user is not None:
        login(request,user)
        return redirect('/todopage')
    else:
        return redirect('/login')

 return render(request,'login.html')

def todo(request):
  if request.method == 'POST':
    title= request.POST.get('title')
    print(title)
    obj=models.TODOO(title=title,user=request.user)
    obj.save()
    
  return render(request,'todo.html')