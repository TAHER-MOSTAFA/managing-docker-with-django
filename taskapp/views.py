from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import dockerform 


def home(request):
    containers = Docker.objects.all()
    return render(request,'taskapp/base.html',{'containers':containers})


@login_required
def MyContainers(request):
    containers = Docker.objects.filter(user=request.user)
    return render(request,'taskapp/base.html',{'containers':containers})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request,"taskapp/form.html",{'form':form,'title':'Sign Up Now'})

@login_required
def createContainers(request):
    if request.method == 'POST':
        form = dockerform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else :
            return render(request, 'taskapp/form.html', {'form': form})
    else:
        form = dockerform()
        return render(request,"taskapp/form.html",{'title':'Make A New Docker Instance','form':dockerform})
