from django.db import models


class Pokemon(models.Model):
    pokemon_id = models.IntegerField(verbose_name='Номер_эволюции', default=1, unique=True)
    title = models.CharField(max_length=200, verbose_name='Имя')
    image = models.ImageField(verbose_name='Изображение')
    description = models.TextField(blank=True, verbose_name='Описание')
    title_en = models.CharField(max_length=200, blank=True, verbose_name='Английское_имя')
    title_jp = models.CharField(max_length=200, blank=True, verbose_name='Японское_имя')

    def previous_evolution(self):
        if self.pokemon_id:
            pokemon = Pokemon.objects.get(pokemon_id=(self.pokemon_id - 1))
            return pokemon
        return None

    def next_evolution(self):
        count_pokemon_id = Pokemon.objects.values("pokemon_id").count()
        if self.pokemon_id >= count_pokemon_id:
            return None
        return Pokemon.objects.get(pokemon_id=(self.pokemon_id+1))

    def __str__(self):
        return f'{self.title}'


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, verbose_name='Покемон')
    appeared_at = models.DateTimeField(blank=True, null=True, verbose_name='Время_появления')
    disappeared_at = models.DateTimeField(blank=True, null=True, verbose_name='Время_исчезания')
    latitude = models.FloatField(blank=True, null=True, verbose_name='Широта')
    longitude = models.FloatField(blank=True, null=True, verbose_name='Долгота')
    level = models.IntegerField(default=0, verbose_name='Уровень')
    health = models.IntegerField(default=0, verbose_name='Здоровье')
    strength = models.IntegerField(default=0, verbose_name='Сила')
    defence = models.IntegerField(default=0, verbose_name='Защита')
    stamina = models.IntegerField(default=0, verbose_name='Выносливость')

    def __str__(self):
        return f'{self.pokemon.title}'

