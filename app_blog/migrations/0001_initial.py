# Generated by Django 4.1.1 on 2022-10-03 09:31

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Post",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("titulo", models.CharField(max_length=200, unique=True)),
                ("subtitulo", models.CharField(max_length=200)),
                ("cuerpo", models.TextField(max_length=5000)),
                (
                    "fecha_post",
                    models.DateTimeField(
                        default=datetime.datetime(2022, 10, 3, 6, 31, 22, 27765)
                    ),
                ),
                ("imagen", models.ImageField(null=True, upload_to="post_img")),
                (
                    "usuario",
                    models.CharField(default="Usuario Generico", max_length=50),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Avatar",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "imagen",
                    models.ImageField(blank=True, null=True, upload_to="avatares"),
                ),
                (
                    "user",
                    models.OneToOneField(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
