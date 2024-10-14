from django.db import models
from django.contrib.auth import get_user_model

User=get_user_model()
class Task(models.Model):
    title=models.CharField(max_length=100)
    is_completed=models.BooleanField(default=False)
    is_importsnt=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    owner=models.ForeignKey(User,on_delete=models.CASCADE)                                           

    def __str__(self):
        return  self.title