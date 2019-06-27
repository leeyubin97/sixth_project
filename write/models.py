from django.db import models
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()

class Comment(models.Model):
    post=models.ForeignKey('write.Post', related_name='comments', on_delete=models.CASCADE)
    nickname= models.CharField(max_length=200)
    text=models.TextField()

    def __str__(self):
        return self.text
# Create your models here.
