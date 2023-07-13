from django.db import models

class Post(models.Model):
    title=models.CharField(max_length=255,null=False)
    content=models.CharField(max_length=255,null=False)
    author=models.CharField(max_length=255,null=False)
    publication_date=models.DateField(auto_now_add=False)

class Category(models.Model):
    name=models.CharField(max_length=255,)
    description=models.TextField()

class Comment(models.Model):
    post=models.CharField(max_length=255)
    author=models.CharField(max_length=255,null=False)
    content=models.CharField(max_length=255)
    date=models.DateField(auto_now_add=False)