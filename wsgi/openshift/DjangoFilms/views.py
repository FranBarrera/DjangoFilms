from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.contrib import auth
import requests,json

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
#        return render_to_response('1.html', {'data_raw': resp },)
        resp = movies_popular()
        return render(request, '1.html', {'data_raw': resp },)
    else:
        return render(request, 'login.html', {})

def movies_popular():
        url = 'http://api.themoviedb.org/3/movie/popular'
        values = {'api_key':'ce9f97d604b836963b8de8c49437e283','language':'es'}
        request = requests.get(url,params=values)
        resp = json.loads(request.text)
        print resp
        return resp

def info(id):
        url = 'http://api.themoviedb.org/3/movie/'+id
        values = {'api_key':'ce9f97d604b836963b8de8c49437e283','language':'es'}
        request = requests.get(url,params=values)
        resp = json.loads(request.text)
        print resp
        return render_to_response('peliculas.html', {'data_raw': resp },)


# http://api.themoviedb.org/3/movie/752?api_key=3ac72c49522e833f35d17c2105f59074&language=es

# url = 'http://api.themoviedb.org/3/movie/752'
# values = {'api_key':'ce9f97d604b836963b8de8c49437e283','language':'es'}
# request = requests.get(url,params=values)
# resp = json.loads(request.text)
# print resp