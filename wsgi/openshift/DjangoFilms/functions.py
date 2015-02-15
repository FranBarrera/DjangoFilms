import requests,json

def info_peli(api):
        url = 'http://api.themoviedb.org/3/movie/%s' %api
        values = {'api_key':'ce9f97d604b836963b8de8c49437e283','language':'es'}
        request = requests.get(url,params=values)
        resp = json.loads(request.text)
        return resp

def movies_popular():
        url = 'http://api.themoviedb.org/3/movie/popular'
        values = {'api_key':'ce9f97d604b836963b8de8c49437e283','language':'es'}
        request = requests.get(url,params=values)
        resp = json.loads(request.text)
        return resp