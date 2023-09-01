from django.db import models
from users.models import User
from geners.models import Song

class Like(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    song = models.ForeignKey(Song,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.song

class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    song = models.ForeignKey(Song,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return

    def verify(self, admin:User):
        self.verify = admin
        self.save()