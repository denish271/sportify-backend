# Generated by Django 5.0.2 on 2024-03-05 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_product_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='feature',
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
