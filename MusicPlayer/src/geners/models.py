from django.db import models
from artists.models import Artist


class Gener(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Song(models.Model):
    title = models.CharField(max_length=60)
    upload_date = models.DateField(auto_now_add=True)
    cover_photo = models.ImageField(upload_to='images/cover_photo', null=True)
    audio_file = models.FileField(upload_to='music')
    artist = models.ManyToManyField(Artist)
    geners = models.ForeignKey(Gener,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title