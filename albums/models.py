from django.db import models

# Create your models here.


class Album(models.Model):
    image = models.ImageField(upload_to='img/')
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    songs = models.TextField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title



