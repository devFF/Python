# Generated by Django 4.1.5 on 2023-01-14 08:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_salesorder_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='salesorder',
            old_name='product',
            new_name='products',
        ),
    ]
