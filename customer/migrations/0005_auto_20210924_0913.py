# Generated by Django 3.1.7 on 2021-09-24 03:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0004_auto_20210924_0910'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='total_price',
            new_name='price',
        ),
    ]