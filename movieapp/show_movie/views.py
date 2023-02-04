from django.shortcuts import render,redirect
from .models import Movie
from datetime import datetime

# Create your views here.
def home(request):
    movies = Movie.objects.all()
    item = []
    for i in movies:
        item.append(i)
    params = {'item':item,'loggedin':False}
    u_cookie = request.COOKIES.get('u_logincred','')
    if(u_cookie != ''):
        params = {'item':item,'loggedin':True}
    return render(request,'show_movie/home.html',params)

def webseries(request):
    params = {'loggedin':False}
    u_cookie = request.COOKIES.get('u_logincred','')
    if(u_cookie != ''):
        params = {'loggedin':True}
    return render(request,'show_movie/webseries.html',params)

def upload_movie(request):
    movie_name = request.POST.get('movie_name','')
    movie_desc = request.POST.get('movie_desc','')
    movie_cat = request.POST.get('movie_cat','')
    movie_full = request.POST.get('movie_full','')
    movie_thumb = request.POST.get('thumb','')
    params = {'loggedin':False}
    u_cookie = request.COOKIES.get('u_logincred','')
    if(u_cookie != '' and u_cookie == 'kailash@gmail.com' and movie_full != '' and movie_thumb!=''):
        params = {'loggedin':True}
        m1 = Movie(movie_name=movie_name,movie_desc=movie_desc,movie_full=movie_full,movie_thumb=movie_thumb,movie_issu_date=datetime.now(),movie_category=movie_cat)
        m1.save()
    else:
        return redirect('/')
    return render(request,'show_movie/upload_movie.html',params)

def fullMovie(request,id):
    movies = Movie.objects.filter(movie_id=id)
    for i in movies:
        movies = i
    movielist = Movie.objects.all()
    item = []
    for i in movielist:
        item.append(i)
    print(item)
    params = {'loggedin':False,'movie':movies,'movielist':item}
    u_cookie = request.COOKIES.get('u_logincred','')
    if(u_cookie != ''):
        params = {'loggedin':True,'movie':movies,'movielist':item}
    return render(request,'show_movie/fullmovie.html',params)