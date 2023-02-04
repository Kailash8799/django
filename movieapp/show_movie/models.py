from django.db import models

# Create your models here.
class Movie(models.Model):
    movie_id = models.AutoField(primary_key=True)
    movie_name = models.CharField(max_length=100)
    movie_desc = models.TextField()
    movie_full = models.FileField(upload_to="video")
    movie_thumb = models.ImageField(upload_to="image")
    movie_issu_date = models.DateTimeField()
    movie_category = models.CharField(max_length=50)

    def __str__(self):
        return self.movie_name