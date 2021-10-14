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

class Goleadores:
    def __init__(self, nombre, goles,equipo):
        self.nombre = nombre
        self.goles = goles
        self.equipo = equipo

class GoleadoresSerializer(serializers.Serializer):
    nombre = serializers.CharField()
    goles = serializers.IntegerField()
    equipo = serializers.CharField()

class Asistentes:
    def __init__(self, nombre, asistencias,equipo):
        self.nombre = nombre
        self.asistencias = asistencias
        self.equipo = equipo

class AsistentesSerializer(serializers.Serializer):
    nombre = serializers.CharField()
    asistencias = serializers.IntegerField()
    equipo = serializers.CharField()