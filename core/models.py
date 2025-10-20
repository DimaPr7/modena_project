from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from products.models import Product
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Discount(models.Model):
    name = models.CharField(max_length=100)
    percentage = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name


class Material(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Gender(models.Model):
    name = models.CharField(max_length=10, unique=True, choices=[
        ('mens', _('Mens')),
        ('womens', _('Womans')),
        ('kids', _('Kids')),
    ])

    def __str__(self):
        return self.name


class Photo(models.Model):
    image = models.ImageField(upload_to='products/photos/', blank=True, null=True)

    def __str__(self):
        return f"{self.image.name.split('/')[-1]}"


class Size(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Colour(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Cart(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='cart'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Cart for {self.user.username}"

    def add_product(self, product, quantity=1):
        item, created = CartItem.objects.get_or_create(cart=self, product=product)
        if not created:
            item.quantity += quantity
        item.save()

    def update_total_price(self):
        self.total_price = sum(item.get_total_price() for item in self.items.all())
        self.save()

    def remove_product(self, product):
        CartItem.objects.filter(cart=self, product=product).delete()

    def clear_cart(self):
        self.items.all().delete()

    def get_total_price(self):
        return sum(item.get_total_price() for item in self.items.all())


class CartItem(models.Model):
    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
        related_name='items'
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.product.name} ({self.quantity})"

    def get_total_price(self):
        return self.product.price * self.quantity

    class Meta:
        unique_together = ('cart', 'product')


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_cart(sender, instance, created, **kwargs):
    if created:
        Cart.objects.create(user=instance)
