from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, render_to_response
from django.template import RequestContext
#from django.contrib import auth
from django.contrib import auth

def register(request):
    form = UserCreationForm()
    return render(request, "register.html", {
        'form': form,
    })

def check(request):
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            auth.login(request,user)
            request.session['username'] = username
            return HttpResponseRedirect('/')
        else:
            return render(request, '2.html', {})
    else:
        return render(request, '3.html', {})

def login(request):
    if request.session.get("username"):
        return render(request, '1.html', {})
    else:
        return render(request, 'login.html', {})
