from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate


def home(request):
    return render(request, 'pledges/home.html')


def signupuser(request):
    if request.method == 'GET':
        return render(request, 'pledges/signupuser.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:

                user = User.objects.create_user(
                    request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('myplegdes')
            except IntegrityError:
                return render(request, 'pledges/signupuser.html', {'form': UserCreationForm(), 'error': 'That username has already been taken, Please choose another username!'})
        else:
            return render(request, 'pledges/signupuser.html', {'form': UserCreationForm(), 'error': 'Passwords did not match'})


def loginuser(request):
    if request.method == 'GET':
        return render(request, 'pledges/loginuser.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'pledges/loginuser.html', {'form': AuthenticationForm(), 'error': 'Username and password did not match'})
        else:
            login(request, user)
            return redirect('currentpledges')


def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')


def makeplegde(request):
    return render(request, 'pledges/makepledge.html')


def myplegdes(request):
    return render(request, 'pledges/mypledges.html')


def currentpledges(request):
    return render(request, 'pledges/currentpledges.html')
