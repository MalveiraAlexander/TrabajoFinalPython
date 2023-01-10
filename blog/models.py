from django.db import models


# Create your models here.

class Post(models.Model):
  id = models.IntegerField(primary_key=True)
  subtitle = models.CharField(max_length=300)
  title = models.CharField(max_length=150)
  body = models.TextField()
  autor = models.CharField(max_length=200, null=True)
  date = models.DateTimeField(auto_now_add=True)
  img = models.ImageField(upload_to='blog/album_imgs/', null=True)
  
class Mensaje(models.Model):
  id = models.IntegerField(primary_key=True)
  emitter = models.CharField(max_length=200)
  receiver = models.CharField(max_length=200)
  mensaje = models.TextField()
  date = models.DateTimeField(auto_now_add=True)
  
