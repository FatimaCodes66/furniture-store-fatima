# Generated by Django 3.1.12 on 2025-07-22 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0007_auto_20250630_0756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Bed', 'Bed'), ('Sofa', 'Sofa'), ('Table', 'Table'), ('Living Room', 'Living Room'), ('Bed Room', 'Bed Room'), ('Dinning', 'Dinning'), ('Kitchen', 'Kitchen'), ('Office', 'Office')], max_length=20),
        ),
    ]
