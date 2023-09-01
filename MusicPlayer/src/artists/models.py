from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=50)
    bio = models.TextField(blank=True,null=True)
    image = models.ImageField(upload_to='images/artist', null=True)

    def __str__(self) -> str:
        return self.name