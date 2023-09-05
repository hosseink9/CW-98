from django.db import models
from main.models import BaseModel

class Artist(BaseModel):
    name = models.CharField(max_length=50)
    bio = models.TextField(blank=True,null=True)
    image = models.ImageField(upload_to='images/artist', null=True, blank=True)

    def __str__(self) -> str:
        return self.name