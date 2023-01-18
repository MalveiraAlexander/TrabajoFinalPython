from django import forms
from django.forms import TextInput
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from ckeditor.widgets import CKEditorWidget
from django.contrib.auth.models import User
    
class PostForm(forms.Form):
    title = forms.CharField(max_length=150, required=True, label='Titulo')
    subtitle = forms.CharField(max_length=300, required=True, label='Sub Titulo')
    body = forms.CharField(widget=CKEditorWidget(), label='Cuerpo')
    img = forms.ImageField(label='Imagen de Portada', help_text = "La imagen debe contener un tamaño de 1920px X 500px como mínimo")
  
class SMSForm(forms.Form):
    User = get_user_model()
    users = User.objects.all()
    receiver = forms.ModelChoiceField(required=True, queryset=users, label='Enviar a')
    text = forms.CharField(widget=forms.Textarea(attrs={'rows':3, 'cols':5}), label='Mensaje')

class SMSResponseForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea(attrs={'rows':3, 'cols':5}), label='Mensaje')

class UserCreateForm(UserCreationForm):
    first_name = forms.CharField(max_length=300, required=True, label='Name')
    last_name = forms.CharField(max_length=300, required=True, label='Lastname')
    email = forms.EmailField(required=True, label='E-Mail')

class EditUser(forms.Form):
    first_name=forms.CharField(label='Nombre')
    last_name=forms.CharField(label='Apellido')
    desc = forms.CharField(widget=forms.Textarea(attrs={'rows':3, 'cols':5}), label='Descripcion')

class AvatarForm(forms.Form):
    img = forms.ImageField(label='Imagen')

