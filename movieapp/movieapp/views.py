from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    params = {'loggedin':False}
    u_cookie = request.COOKIES.get('u_logincred','')
    if(u_cookie):
        params = {'loggedin':True}
    return render(request,'home.html',params)