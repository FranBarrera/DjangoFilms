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


# def insert_media(request,api):
#     if len(models.media.objects.filter(api_id=api).values('id')) == 0:
#         resp = info_peli(api)
#         name = resp['title']
#         insert = models.media(api_id=api,type=2,name=name)
#         insert.save()
#     return HttpResponse('<p>Insertada a media</p>')


def vista(request,api):
    if len(models.media.objects.filter(api_id=api).values('id')) == 0:
        resp = info_peli(api)
        name = resp['title']
        img = resp['poster_path']

        insert_media = models.media(api_id=api,type=2,name=name,img=img)
        insert_media.save()

    username = request.session.get("username")
    user = User.objects.get(username=username)
    media = models.media.objects.get(api_id=api)
    if len(models.usermedia.objects.filter(user=user,media=media,status=1)) == 0:
        insert_user = models.usermedia(user=user,media=media,status=1)
        insert_user.save()
        return HttpResponse('<p>Insertada a vistas</p>')
    else:
        return HttpResponse('<p>Ya esta insertada en vistas</p>')

def pendiente(request,api):
    if len(models.media.objects.filter(api_id=api).values('id')) == 0:
        resp = info_peli(api)
        name = resp['title']
        img = resp['poster_path']
        insert_media = models.media(api_id=api,type=2,name=name,img=img)
        insert_media.save()

    username = request.session.get("username")
    user = User.objects.get(username=username)
    media = models.media.objects.get(api_id=api)
    if len(models.usermedia.objects.filter(user=user,media=media,status=2)) == 0:
        insert_user = models.usermedia(user=user,media=media,status=2)
        insert_user.save()
        return HttpResponse('<p>Insertada a pendientes</p>')
    else:
        return HttpResponse('<p>Ya esta insertada en pendientes</p>')

def user_vistas(request):
    username = request.session.get("username")
    user = User.objects.get(username='Usuario')
    usermedia = models.usermedia.objects.filter(user_id=user,status=1).values('media_id')
    resp = models.media.objects.filter(id__in=usermedia)
    return render_to_response('peliculas_vistas.html', {'data_raw': resp },)

def user_pendientes(request):
    username = request.session.get("username")
    user = User.objects.get(username='Usuario')
    usermedia = models.usermedia.objects.filter(user_id=user,status=2).values('media_id')
    resp = models.media.objects.filter(id__in=usermedia)
    return render_to_response('peliculas_pendientes.html', {'data_raw': resp },)
