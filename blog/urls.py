from blog.views import *
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', getPosts, name='posts'),
    path('add/', addPost, name='add_post'),
    path('post/<int:pk>/', getPost, name='view_post'),
    path('deletePost/<id>/', deletePost, name='deletePost'),
    path('editPost/<id>/', editPost, name='editPost'),
    path('about/', about, name='about'),
    path('enviar/', emitter, name='send'),
    path('enviar/<emitter>/', emitter, name='send'),
    path('mensajes/', messages, name='mensajes'),
    path('deleteMessage/<id>/', deleteSMS, name='deleteSms'),
    path('you/', viewProfile, name='you_profile'),
    path('profile/<username>/', viewProfile, name='view_profile'),
    path('edit/', editProfile, name='edit_profile'),
    path('avatar/', chargeImgProfile, name='charge_avatar'),
    path('ingreso/', ingreso, name='ingreso'),
    path('cierre/', cierre, name='cierre'),
    path('registro/', registro, name='registro'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)