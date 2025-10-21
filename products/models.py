from ckeditor.fields import RichTextField
from django.db import models
from django.utils.translation import gettext_lazy as _


class Product(models.Model):
    class Meta:
        verbose_name = _('Продукт')

    name = models.CharField(max_length=64)
    description = RichTextField()
    category = models.ForeignKey("core.Category", on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # discount = models.ForeignKey("core.Discount", on_delete=models.SET_NULL, null=True, blank=True)
    sku = models.CharField(max_length=32, unique=True)
    material = models.ForeignKey("core.Material", on_delete=models.SET_NULL, null=True, blank=True)
    gender = models.ForeignKey("core.Gender", on_delete=models.SET_NULL, null=True, blank=True)
    photos = models.ManyToManyField("core.Photo", related_name="products", blank=True)
    size = models.ForeignKey("core.Size", on_delete=models.SET_NULL, null=True, blank=True)
    colour = models.ForeignKey("core.Colour", on_delete=models.SET_NULL, null=True, blank=True)
    related_products = models.ManyToManyField("self", blank=True)
    full_collection = models.ManyToManyField("self", blank=True)
    quantity = models.PositiveIntegerField(default=0)

    def price_with_discount(self):
        if self.discount:
            return self.price * (1 - self.discount.percentage / 100)
        return self.price

    def __str__(self):
        return self.name
