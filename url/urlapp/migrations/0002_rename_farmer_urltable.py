# Generated by Django 3.2.5 on 2022-07-30 08:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('urlapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='farmer',
            new_name='urltable',
        ),
    ]