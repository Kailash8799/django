from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name="home"),
    path("webseries/",views.webseries,name="webseries"),
    path("upload_movie/",views.upload_movie,name="webseries"),
    path("whatchfullmovie/<id>",views.fullMovie,name="fullmovie"),
]

