from .models import Pokemon
from .serializers import PokemonSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

class PokemonListView(ListCreateAPIView):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer

class PokemonDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer