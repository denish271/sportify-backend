# Generated by Django 5.0.2 on 2024-03-08 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_alter_address_pincode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='pincode',
            field=models.CharField(max_length=100),
        ),
    ]