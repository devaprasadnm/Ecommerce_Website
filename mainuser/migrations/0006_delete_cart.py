# Generated by Django 3.2.7 on 2021-10-15 09:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainuser', '0005_rename_product_cart'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Cart',
        ),
    ]