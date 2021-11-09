from Equipo.views import equipo
from rest_framework import serializers
from FutbolStats.models import Jugador

class JugadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jugador
        fields = '__all__'

class JugadorSerializerEquipo(serializers.ModelSerializer):
    class Meta:
        model = Jugador
        fields = ['nombre','fechaDeNacimiento', 'nacionalidad', 'foto', 'id']

class Maximos:
    def __init__(self,nombre,estadistica,equipo):
        self.nombre = nombre
        self.estadistica = estadistica
        self.equipo = equipo

class MaximosSerializer(serializers.Serializer):
    nombre = serializers.CharField()
    estadistica = serializers.IntegerField()
    equipo = serializers.CharField()
