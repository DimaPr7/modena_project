from ckeditor.fields import RichTextField
from django.db import models
from django.utils.translation import gettext_lazy as _


class Product(models.Model):
    class Meta:
        verbose_name = _('Продукт')

    name = models.CharField(max_length=64)
    description = RichTextField()
    category = models.ForeignKey("core.Category", on_delete=models.CASCADE)  # Link to Category
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Decimal for price
    # discount = models.ForeignKey("core.Discount", on_delete=models.SET_NULL, null=True, blank=True)  # Link to Discount
    sku = models.CharField(max_length=32, unique=True)  # Short text for SKU (Stock Keeping Unit)
    material = models.ForeignKey("core.Material", on_delete=models.SET_NULL, null=True, blank=True)  # Link to Material
    gender = models.ForeignKey("core.Gender", on_delete=models.SET_NULL, null=True, blank=True)  # Link to Gender
    photos = models.ManyToManyField("core.Photo", related_name="products", blank=True)  # Related photos
    size = models.ForeignKey("core.Size", on_delete=models.SET_NULL, null=True, blank=True)  # Link to Size
    colour = models.ForeignKey("core.Colour", on_delete=models.SET_NULL, null=True, blank=True)  # Link to Colour
    related_products = models.ManyToManyField("self", blank=True)  # Self-related products
    full_collection = models.ManyToManyField("self", blank=True)  # Self-related collection
    quantity = models.PositiveIntegerField(default=0)  # New field for quantity

    def price_with_discount(self):
        if self.discount:
            return self.price * (1 - self.discount.percentage / 100)
        return self.price

    def __str__(self):
        return self.name
