from blog.views import *
from django.urls import path

urlpatterns = [
    path('', getPosts, name='posts'),
    path('add/', addPost, name='add_post'),
    path('post/<int:pk>/', getPost, name='view_post'),
    path('deletePost/<id>/', deletePost, name='deletePost'),
    path('about/', about, name='about'),
    path('enviar/', emitter, name='send'),
    path('enviar/<emitter>/', emitter, name='send'),
    path('mensajes/', messages, name='mensajes'),
    path('deleteMessage/<id>/', deleteSMS, name='deleteSms'),
    path('ingreso/', ingreso, name='ingreso'),
    path('cierre/', cierre, name='cierre'),
    path('registro/', registro, name='registro'),
]