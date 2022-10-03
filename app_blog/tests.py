from django.test import TestCase
from django.contrib.auth.models import User
from app_blog.models import Post
import random
import string

class UnitTests(TestCase):

    def test_creacion_usuarios(self):

        for x in range(1000):
            last_name = "".join([random.choice(string.ascii_letters + string.digits) for _ in range(20)])
            first_name = "".join([random.choice(string.ascii_letters + string.digits) for _ in range(20)])
            username = "".join([random.choice(string.ascii_letters + string.digits) for _ in range(15)])
            email = "".join([random.choice(string.ascii_letters + string.digits) for _ in range(12)]) + "@gmail.com"

            usuario = User.objects.create(last_name=last_name , first_name=first_name , username=username , email=email)
            self.assertIsNotNone(usuario.id)
            self.assertEqual(usuario.last_name, last_name)
            self.assertEqual(usuario.first_name, first_name)
            self.assertEqual(usuario.username, username)
            self.assertEqual(usuario.email, email)
    

    def test_creacion_post(self):
        for x in range(1000):
            titulo = "".join([random.choice(string.ascii_letters + string.digits) for _ in range(20)])
            subtitulo = "".join([random.choice(string.ascii_letters + string.digits) for _ in range(20)])
            cuerpo = "".join([random.choice(string.ascii_letters + string.digits) for _ in range(4000)])
            usuario = "".join([random.choice(string.ascii_letters + string.digits) for _ in range(8)])

            post = Post.objects.create(titulo=titulo, subtitulo=subtitulo, cuerpo=cuerpo, usuario=usuario)
            self.assertIsNotNone(post.id)
            self.assertEqual(post.titulo, titulo)
            self.assertEqual(post.subtitulo, subtitulo)
            self.assertEqual(post.cuerpo, cuerpo)
            self.assertEqual(post.usuario, usuario)