from rest_framework import serializers
from .models import Pokemon

class PokemonSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'species', 'name', 'level', 'owner', 'caught')
        model = Pokemon