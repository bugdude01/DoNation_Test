from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .forms import PledgeForm
from .models import Pledge


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
            return redirect('myplegdes')


def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')


def makeplegde(request):
    form = PledgeForm()
    if request.method == 'GET':
        return render(request, 'pledges/makepledge.html', {'form': form})
    else:
        form = PledgeForm(request.POST)
        newpledge = form.save(commit=False)
        newpledge.user = request.user
        newpledge.save()
        return redirect('myplegdes')

    return render(request, 'pledges/makepledge.html', {'form': form})


def myplegdes(request):
    pledges = Pledge.objects.filter(user=request.user)
    return render(request, 'pledges/mypledges.html', {'pledges': pledges})


def allpledges(request):
    pledges = Pledge.objects.all()
    return render(request, 'pledges/allpledges.html', {'pledges': pledges})


def viewpledge(request, pledge_pk):
    pledge = get_object_or_404(Pledge, pk=pledge_pk)
    return render(request, 'pledges/viewpledge.html', {'pledge': pledge})
