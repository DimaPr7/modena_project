# Generated by Django 5.1.1 on 2024-10-18 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0005_alter_photo_product"),
        ("products", "0003_alter_product_full_collection_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="full_collection",
            field=models.ManyToManyField(blank=True, to="products.product"),
        ),
        migrations.AlterField(
            model_name="product",
            name="photos",
            field=models.ManyToManyField(
                blank=True, related_name="products", to="core.photo"
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="related_products",
            field=models.ManyToManyField(blank=True, to="products.product"),
        ),
    ]
