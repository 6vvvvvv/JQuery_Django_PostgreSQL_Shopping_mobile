# Generated by Django 3.0.5 on 2020-05-08 22:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('axfapp', '0018_order'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='idDelete',
            new_name='isDelete',
        ),
    ]