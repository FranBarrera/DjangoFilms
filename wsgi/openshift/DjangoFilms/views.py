from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.contrib import auth
import requests,json
from DjangoFilms import models
from django.contrib.auth.models import User
from DjangoFilms.functions import *

def register(request):
 if request.method == 'POST':
     form = UserCreationForm(request.POST)
     if form.is_valid():
         new_user = form.save()
         return HttpResponseRedirect('/')
 else:
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
            return HttpResponse('<p>Usuario inactivo</p>')
    else:
        return HttpResponse('<p>Login Incorrecto.<a href="/">Intentar de nuevo </a></p>')

def login(request):
    if request.session.get("username"):
        resp = movies_popular()
        return render(request, '1.html', {'data_raw': resp },)
    else:
        return render(request, 'login.html', {})


def envia_info_peli(request,api):
    resp = info_peli(api)
    return render_to_response('peliculas.html', {'data_raw': resp },)


def insert_media(request,api):
    if len(models.media.objects.filter(api_id=api).values('id')) = 0:
        resp = info_peli(api)
        name = resp['title']
        insert = models.media(api_id=api,type=2,name=name)
        insert.save()
        return HttpResponse('<p>Insertada a media</p>')


# def vista(request,api):
#     username = request.session.get("username")
#     user_id = User.objects.filter(username=username).values('id')
#     media = models.media.objects.filter(api_id=api).values('id')
#     insert = models.usermedia(user=user_id,media=media,status=1)
#     insert.save()
#     return HttpResponse('<p>Insertada a vistas</p>')
