# Generated by Django 3.1.7 on 2021-10-08 19:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0005_auto_20210924_0913'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='order_datetime',
            new_name='order_date',
        ),
    ]
