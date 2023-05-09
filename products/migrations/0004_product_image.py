# Generated by Django 4.2.1 on 2023-05-08 13:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0003_product_available_alter_product_stock"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="image",
            field=models.CharField(
                default="https://upload.wikimedia.org/wikipedia/commons/thumb/6/65/No-Image-Placeholder.svg/1665px-No-Image-Placeholder.svg.png",
                max_length=500,
            ),
        ),
    ]
