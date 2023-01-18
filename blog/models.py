from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.

class Post(models.Model):
  id = models.IntegerField(primary_key=True)
  subtitle = models.CharField(max_length=300)
  title = models.CharField(max_length=150)
  body = RichTextField()
  autor = models.ForeignKey(User, on_delete=models.CASCADE)
  date = models.DateTimeField(auto_now_add=True)
  img = models.ImageField(null=True)
  
class Mensaje(models.Model):
  id = models.IntegerField(primary_key=True)
  emitter = models.CharField(max_length=200)
  receiver = models.CharField(max_length=200)
  mensaje = models.TextField()
  date = models.DateTimeField(auto_now_add=True)
  

class AvatarImage(models.Model):
    img = models.ImageField(upload_to='user_img')
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class DescripcionUser(models.Model):
    desc = models.TextField(max_length=300)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

