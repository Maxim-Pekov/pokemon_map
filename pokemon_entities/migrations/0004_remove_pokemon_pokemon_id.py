# Generated by Django 3.1.14 on 2022-10-14 22:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0003_auto_20221012_2344'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pokemon',
            name='pokemon_id',
        ),
    ]
