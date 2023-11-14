from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

# Create your models here.
# class RegistroUsuario(models.Model):
#     user = models.CharField(max_length=255)
#     password = models.CharField()
#     rol = models.CharField()

class CustomUser(AbstractUser):
    roles = models.CharField(max_length=20, blank=True)
    groups = models.ManyToManyField(
        Group, verbose_name='groups', blank=True,
        related_name='customuser_set', related_query_name='user'
    )
    user_permissions = models.ManyToManyField(
        Permission, verbose_name='user permissions', blank=True,
        related_name='customuser_set', related_query_name='user'
    )

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    # Otros campos relevantes para tu aplicación