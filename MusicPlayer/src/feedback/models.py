from django.db import models
from users.models import User
from geners.models import Song
from main.models import BaseModel

class Like(BaseModel):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    song = models.ForeignKey(Song,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.song

class Comment(BaseModel):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    song = models.ForeignKey(Song,on_delete=models.CASCADE)
    text = models.TextField(max_length=300)

    def __str__(self) -> str:
        return self.user

    def verify(self, admin:User):
        self.verify = admin
        self.save()