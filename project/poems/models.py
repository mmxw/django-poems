from django.db import models
from django.contrib.auth.models import User


class Collection(models.Model): 
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=200)


class Genre(models.Model):
    genre = models.CharField(max_length=30, unique=True)
    collection = models.ForeignKey(Collection, related_name='genres', on_delete=models.CASCADE)
    starter = models.ForeignKey(User, related_name='genres', on_delete=models.CASCADE)


class Poem(models.Model):
    poem_title = models.CharField(max_length=255)
    poem_body = models.TextField(max_length=5000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, related_name='poems', on_delete=models.CASCADE)
    updated_by = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='+')






