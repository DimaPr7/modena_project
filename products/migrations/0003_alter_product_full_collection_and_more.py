# Generated by Django 4.1 on 2024-09-11 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0002_alter_product_photos"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="full_collection",
            field=models.ManyToManyField(blank=True, null=True, to="products.product"),
        ),
        migrations.AlterField(
            model_name="product",
            name="related_products",
            field=models.ManyToManyField(blank=True, null=True, to="products.product"),
        ),
    ]
