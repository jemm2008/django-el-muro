from django.contrib import messages
from django.shortcuts import redirect, render
import bcrypt
from .decorators import login_required,admin_requerido
from app01.models import *
from .models import User


@login_required
def index(request):
    context = {
        'all_mensajes': Mensaje.objects.all(),
        'all_comentarios': Comentario.objects.all()
    }
    return render(request, 'index.html', context)


@admin_requerido
def administrador(request):
    context = {
        'saludo': 'ADMINISTRADOR'
    }
    return render(request, 'admin.html', context)


def nuevo_mensaje(request):
    user_id = request.session['usuario']['id']
    #print(request.POST)
    contenido_mensaje = request.POST["cont_msg"]
    user = User.objects.get(id=user_id)
    Mensaje.objects.create(contenido_mensaje = contenido_mensaje, usuario = user)
    return redirect("/")


def nuevo_comentario(request, mensaje_id):
    user_id = request.session['usuario']['id']
    print(request.POST)
    comentario = request.POST["cont_coment"]
    user = User.objects.get(id=user_id)
    mensaje = Mensaje.objects.get(id=mensaje_id)
    Comentario.objects.create(comentario = comentario, usuario = user, mensaje= mensaje)
    return redirect("/")


