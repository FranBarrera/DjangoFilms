import requests,json

request_values =  {'api_key':'ce9f97d604b836963b8de8c49437e283','language':'es'};

def movies_popular():
        url = 'http://api.themoviedb.org/3/movie/popular'
        request = requests.get(url,params=request_values)
        resp = json.loads(request.text)
        return resp

def info_peli(api):
        url = 'http://api.themoviedb.org/3/movie/%s' %api
        request = requests.get(url,params=request_values)
        resp = json.loads(request.text)
        return resp

def video_peli(api):
        url = 'http://api.themoviedb.org/3/movie/%s/videos' %api
        request = requests.get(url,params=request_values)
        resp = json.loads(request.text)
        return resp

def similar_peli(api):
        url = 'http://api.themoviedb.org/3/movie/%s/similar' %api
        request = requests.get(url,params=request_values)
        resp = json.loads(request.text)
        return resp

def cast_peli(api):
        url = 'http://api.themoviedb.org/3/movie/%s/credits' %api
        request = requests.get(url,params=request_values)
        resp = json.loads(request.text)
        return resp

def series_popular():
        url = 'http://api.themoviedb.org/3/tv/popular'
        request = requests.get(url,params=request_values)
        resp = json.loads(request.text)
        return resp

def info_serie(api):
        url = 'http://api.themoviedb.org/3/tv/%s' %api
        request = requests.get(url,params=request_values)
        resp = json.loads(request.text)
        return resp

def seasons_series(api,season):
        url = 'http://api.themoviedb.org/3/tv/%s/season/%s' % (api, season)
        request = requests.get(url,params=request_values)
        resp = json.loads(request.text)
        return resp