from django.db import models

class Author(models.Model):
    name=models.CharField(max_length=255,null=False)
    bio=models.TextField()

    def __str__(self) -> str:
        return self.name
