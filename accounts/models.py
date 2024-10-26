from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class CustomUser(AbstractUser):
    image = models.ImageField(upload_to='media/products/photos/', default='default.jpg')

    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',  # Уникальное имя для обратной ссылки
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        Permission
        related_name='customuser_set',  # Уникальное имя для обратной ссылки
        blank=True,
    )

    def __str__(self):
        return self.username
