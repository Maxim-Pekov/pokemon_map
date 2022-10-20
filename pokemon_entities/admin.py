from django.contrib import admin
from .models import Pokemon, PokemonEntity

@admin.register(Pokemon)
class Pokemon(admin.ModelAdmin):
    list_display = ('title', 'id', 'image', 'description')


@admin.register(PokemonEntity)
class PokemonEntity(admin.ModelAdmin):
    list_display = ('pokemon', 'latitude', 'longitude', 'appeared_at', 'disappeared_at')

