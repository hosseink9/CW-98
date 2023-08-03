from django.db import models
# from task.models import Task

class Category(models.Model):
    name=models.CharField(max_length=255,)
    description=models.TextField(null=True,blank=True)
    # image=models.ImageField(upload_to='category_images/',blank=True,null=True)

    def __str__(self) -> str:
        return self.name
    
class Tag(models.Model):
    name=models.CharField(max_length=255)
    

    def __str__(self) -> str:
        return self.name