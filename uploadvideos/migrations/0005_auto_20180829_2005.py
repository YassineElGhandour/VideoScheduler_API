# Generated by Django 2.1 on 2018-08-29 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploadvideos', '0004_uploadvideos_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uploadvideos',
            name='date',
        ),
        migrations.AddField(
            model_name='uploadvideos',
            name='hour',
            field=models.IntegerField(default=12),
        ),
        migrations.AddField(
            model_name='uploadvideos',
            name='minute',
            field=models.IntegerField(default=1),
        ),
    ]
