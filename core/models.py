from django.db import models

from products.models import Product


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
    name = models.CharField(max_length=50)  # Название пола (например, Мужской, Женский, Унисекс)

    def __str__(self):
        return self.name


class Photo(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_photos")
    image = models.ImageField(upload_to='products/photos/', blank=True, null=True)

    def __str__(self):
        return f"Photo {self.id} for {self.product.name}"


class Size(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Colour(models.Model):
    name = models.CharField(max_length=50)  # Название цвета (например, Красный, Синий, Зелёный)

    def __str__(self):
        return self.name
