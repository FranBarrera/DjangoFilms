from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, render_to_response
from django.template import RequestContext
#from django.contrib import auth
from django.contrib.auth import authenticate, login as auth_login

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
#            return HttpResponseRedirect("/ok/")
            return render_to_response("ok.html",context_instance=RequestContext(request))
    else:
        form = UserCreationForm()
    return render(request, "register.html", {
        'form': form,
    })

def login(request):
    return render(request, 'login.html', {})


def comprobar(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request,user)
            return render(request, '1.html', {})
        else:
            return render(request, '2.html', {})
    else:
        return render(request, '3.html', {})
