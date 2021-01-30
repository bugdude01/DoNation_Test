from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login

# Create your views here.


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
                return redirect('currentpledges')
            except IntegrityError:
                return render(request, 'pledges/signupuser.html', {'form': UserCreationForm(), 'error': 'That username has already been taken, Please choose another username!'})
        else:
            return render(request, 'pledges/signupuser.html', {'form': UserCreationForm(), 'error': 'Passwords did not match'})


def currentpledges(request):
    return render(request, 'pledges/currentpledges.html')
