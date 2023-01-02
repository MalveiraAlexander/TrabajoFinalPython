from django.http import HttpResponse, HttpResponseRedirect
from blog.forms import *

from .models import *
from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate, logout

# Create your views here.
def addPost(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PostForm(request.POST)
            if form.is_valid():
                info = form.cleaned_data
                post = Post(title=info['title'], body=info['body'], subtitle=info['subtitle'], autor=f'{request.user.first_name} {request.user.last_name}')
                post.save()
            return HttpResponseRedirect('/')
        else:
            formulario = PostForm()
            return render(request, 'addpost.html', {'form': formulario})
    else:
        return HttpResponseRedirect('/ingreso/')
    


def getPosts(request):
    if request.user.is_authenticated:
        posts = Post.objects.all()
        isNull = False
        if len(list(posts)) == 0:
            isNull = True
        return render(request, 'blog.html', {'posts': posts, 'isNull': isNull})
    else:
        return HttpResponseRedirect('/ingreso/')

def getPost(request, pk):
    if request.user.is_authenticated:
        post = Post.objects.get(id = pk)
        return render(request, 'post.html', {'post': post})
    else:
        return HttpResponseRedirect('/ingreso/')


def deletePost(request, id):
    if request.user.is_authenticated:
        post = Post.objects.get(id=id)
        post.delete()
        return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/ingreso/')

def emitter(request, emitter = 'not'):
    
    if request.user.is_authenticated:
        if request.method == 'GET':
            isEmitterExist = False
            emitterUser = 'not'
            if emitter != 'not':
                isEmitterExist = True
                emitterUser = emitter
            
            if isEmitterExist:
                form = SMSResponseForm()
                return render(request, 'emitter.html', {'form': form, 'emitterUser': emitterUser})
            else:
                formulario = SMSForm()
                return render(request, 'emitter.html', {'form': formulario, 'emitterUser': emitterUser})
        if request.method == 'POST':
            isEmitterExist = False
            print(emitter)
            if emitter != 'not':
                isEmitterExist = True
            if isEmitterExist:
                formu = SMSResponseForm(request.POST)
                if formu.is_valid():
                    info = formu.cleaned_data
                    sms = Mensaje(emitter=request.user.username, receiver=emitter, mensaje=info['text'])
                    sms.save()
            else:
                form = SMSForm(request.POST)
                if form.is_valid():
                    info = form.cleaned_data
                    sms = Mensaje(emitter=request.user.username, receiver=info['receiver'], mensaje=info['text'])
                    sms.save()
            return HttpResponseRedirect('/mensajes/')
    else:
        return HttpResponseRedirect('/ingreso/')

def messages(request):
    if request.user.is_authenticated:
        user = request.user.username
        mensajes = Mensaje.objects.filter(receiver=user).values()
        isNull = False
        if len(list(mensajes)) == 0:
            isNull = True
        return render(request, 'receiver.html', {'mensajes': mensajes, 'isNull': isNull})
    else:
        return HttpResponseRedirect('/ingreso/')
    
def deleteSMS(request, id):
    if request.user.is_authenticated:
        mensaje = Mensaje.objects.get(id=id)
        mensaje.delete()
        return HttpResponseRedirect('/mensajes/')
    else:
        return HttpResponseRedirect('/ingreso/')



def about(request):
    return render(request, 'about.html')


def cierre(request):
    logout(request)
    return HttpResponseRedirect('/')

def ingreso(request):
    if request.method == 'GET':
        form = AuthenticationForm()
        return render(request, 'ingreso.html', {'form': form})
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                print(user)
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                print('User not found')
        else:
            # If there were errors, we render the form with these
            # errors
            return render(request, 'ingreso.html', {'form': form})

def registro(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/')
    if request.method == 'GET':
        form = UserCreateForm()
        return render(request, 'registro.html', {'form': form})
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            # https://docs.djangoproject.com/en/1.11/topics/forms/modelforms/#the-save-method
            form.save()
            User = get_user_model()
            uname = form.cleaned_data.get('username')
            user = User.objects.get(username=uname)
            if user is not None:
                user.first_name = form.cleaned_data.get('first_name')
                user.last_name = form.cleaned_data.get('last_name')
                user.email = form.cleaned_data.get('email')
                user.save()
            else:
                print('User not found')
            
            username = uname
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            # If there were errors, we render the form with these
            # errors
            return render(request, 'registro.html', {'form': form})