# Generated by Django 2.1 on 2018-09-01 16:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uploadvideos', '0005_auto_20180829_2005'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uploadvideos',
            name='hour',
        ),
        migrations.RemoveField(
            model_name='uploadvideos',
            name='minute',
        ),
    ]
