from django.db import models
from author.models import Author



class Category(models.Model):
    name=models.CharField(max_length=255,)
    description=models.TextField()
    image=models.ImageField(upload_to='category_images/',blank=True,null=True)

    def __str__(self) -> str:
        return self.name

class Post(models.Model):
    title=models.CharField(max_length=255,null=False)
    content=models.CharField(max_length=255,null=False)
    author=models.ForeignKey(Author, on_delete=models.CASCADE)
    publication_date=models.DateField(auto_now_add=True)
    category=models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    image=models.ImageField(upload_to='post_images/',blank=True,null=True)

    def __str__(self) -> str:
        return self.title
    
class Comment(models.Model):
    post=models.ForeignKey(Post, on_delete=models.CASCADE)
    author=models.ForeignKey(Author, on_delete=models.CASCADE)
    content=models.CharField(max_length=255)
    date=models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.content