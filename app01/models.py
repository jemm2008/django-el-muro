from django.db import models
import re

# Create your models here.
class UserManager(models.Manager):
    def validador_basico(self, postData):
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        SOLO_LETRAS = re.compile(r'^[a-zA-Z. ]+$')

        errors = {}

        if len(postData['firstname']) < 2:
            errors['firstname_len'] = "Nombre debe tener al menos 2 caracteres de largo"

        if len(postData['lastname']) < 2:
            errors['lastname_len'] = "Apellido debe tener al menos 2 caracteres de largo"

        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "correo invalido"

        if User.objects.filter(email = postData['email'].lower()).exists():
            errors['email'] = "Este Email ya está registrado."

        if not SOLO_LETRAS.match(postData['firstname']):
            errors['solo_letras'] = "solo letras en nombre por favor"

        if not SOLO_LETRAS.match(postData['lastname']):
            errors['solo_letras'] = "solo letras en Apellido por favor"

        if len(postData['password']) < 4:
            errors['password'] = "contraseña debe tener al menos 4 caracteres";

        if postData['password'] != postData['password_confirm'] :
            errors['password_confirm'] = "contraseña y confirmar contraseña no son iguales. "

        return errors



class User(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=70)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

    def __str__(self):
        return f"{self.firstname} {self.lastname}"

    def __repr__(self):
        return f"{self.firstname} {self.lastname}"


class Mensaje(models.Model):
    contenido_mensaje = models.TextField()
    usuario = models.ForeignKey(User, related_name="mensajes", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comentario(models.Model):
    comentario = models.TextField()
    usuario = models.ForeignKey(User, related_name="comentarios", on_delete=models.CASCADE)
    mensaje = models.ForeignKey(Mensaje, related_name="comentarios", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)