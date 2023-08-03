from django.db import models
from epic_quest.models import Category, Tag
from userapp.models import User

class Task(models.Model):
    START= 'start'
    INPORCESS='inprocess'
    DONE = 'done'
    status_choice = [
        (START,'start'),
        (INPORCESS,'inprocess'),
        (DONE,'done')
    ]
    title=models.CharField(max_length=255)
    description=models.TextField()
    due_date=models.DateField(auto_now_add=False)
    category= models.ForeignKey(Category, on_delete=models.PROTECT)
    status_fields=models.CharField(max_length=255, choices=status_choice)
    tag=models.ManyToManyField(Tag)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    # def get_tags(self):
    #     task=Task.objects.get(id=self.id)
    #     tags=task.tag.all()
    #     return list(tags)[0]

    def __str__(self) -> str:
        return self.title
