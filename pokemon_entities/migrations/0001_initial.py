# Generated by Django 3.1.14 on 2022-10-12 18:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pokemon_id', models.IntegerField(default=1, unique=True, verbose_name='Номер_эволюции')),
                ('title', models.CharField(max_length=200, verbose_name='Имя')),
                ('image', models.ImageField(upload_to='', verbose_name='Изображение')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('title_en', models.CharField(blank=True, max_length=200, verbose_name='Английское_имя')),
                ('title_jp', models.CharField(blank=True, max_length=200, verbose_name='Японское_имя')),
            ],
        ),
        migrations.CreateModel(
            name='PokemonEntity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appeared_at', models.DateTimeField(blank=True, null=True, verbose_name='Время_появления')),
                ('disappeared_at', models.DateTimeField(blank=True, null=True, verbose_name='Время_исчезания')),
                ('latitude', models.FloatField(blank=True, null=True, verbose_name='Широта')),
                ('longitude', models.FloatField(blank=True, null=True, verbose_name='Долгота')),
                ('level', models.IntegerField(default=0, verbose_name='Уровень')),
                ('health', models.IntegerField(default=0, verbose_name='Здоровье')),
                ('strength', models.IntegerField(default=0, verbose_name='Сила')),
                ('defence', models.IntegerField(default=0, verbose_name='Защита')),
                ('stamina', models.IntegerField(default=0, verbose_name='Выносливость')),
                ('pokemon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pokemon_entities.pokemon', verbose_name='Покемон')),
            ],
        ),
    ]
