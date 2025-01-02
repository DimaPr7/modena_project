from django.db import models

from products.models import Product
from django.utils.translation import gettext_lazy as _



class Category(models.Model):
    name = models.CharField(max_length=100)  # Название категории
    description = models.TextField(blank=True, null=True)  # Описание категории

    def __str__(self):
        return self.name


class Discount(models.Model):
    name = models.CharField(max_length=100)  # Название скидки
    percentage = models.DecimalField(max_digits=5, decimal_places=2)  # Процент скидки

    def __str__(self):
        return self.name


class Material(models.Model):
    name = models.CharField(max_length=100)  # Название материала

    def __str__(self):
        return self.name


class Gender(models.Model):
    name = models.CharField(max_length=10, unique=True, choices=[
        ('mens', _('Mens')),
        ('womens', _('Womans')),
        ('kids', _('Kids')),
    ])


class Photo(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="product_photos",
        blank=True,
        null=True,
    )
    image = models.ImageField(upload_to='products/photos/', blank=True, null=True)

    def __str__(self):
        return f"Photo {self.id} for {self.product.name if self.product else 'No Product'}"



class Size(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Colour(models.Model):
    name = models.CharField(max_length=50)  # Название цвета (например, Красный, Синий, Зелёный)

    def __str__(self):
        return self.name
