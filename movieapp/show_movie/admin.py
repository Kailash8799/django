from django.contrib import admin
from .models import Movie

@admin.register(Movie)

class MovieRegister(admin.ModelAdmin):
    list_display = ['movie_id','movie_name','movie_issu_date','movie_category']