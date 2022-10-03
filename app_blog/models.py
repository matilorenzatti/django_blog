from django.db import models
import datetime
from django.contrib.auth.models import User


class Post(models.Model):
    titulo = models.CharField(max_length=200, unique=True)
    subtitulo = models.CharField(max_length=200)
    cuerpo = models.TextField(max_length=5000)
    fecha_post = models.DateTimeField(default= datetime.datetime.now())
    imagen = models.ImageField(upload_to ="post_img", null=True)
    usuario = models.CharField(max_length=50, default="Usuario Generico" )

    def __str__(self):
        return f'{self.titulo} - {self.usuario}'

class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    imagen = models.ImageField(upload_to = 'avatares', null=True, blank=True)

    def __str__(self):
        return f"Imagen de: {self.user.username}"