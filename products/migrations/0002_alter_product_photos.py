# Generated by Django 4.1 on 2024-09-11 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0003_alter_photo_image"),
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="photos",
            field=models.ManyToManyField(
                blank=True, null=True, related_name="products", to="core.photo"
            ),
        ),
    ]
