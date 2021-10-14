from rest_framework import serializers
from Estadisticas.models import *

class Estadisticas:
    def __init__(self,temporada,equipo,amarillas,rojas,goles,asistencias,pj,titular,min):
        self.temporada = temporada
        self.equipo = equipo
        self.amarillas = amarillas
        self.rojas = rojas
        self.goles = goles
        self.asistencias= asistencias
        self.pj = pj
        self.titular = titular
        self.min = min
        
class EstadisticasJug(serializers.Serializer):
    temporada = serializers.CharField()
    equipo = serializers.CharField()
    amarillas = serializers.IntegerField()
    rojas = serializers.IntegerField()
    goles = serializers.IntegerField()
    asistencias = serializers.IntegerField()
    pj = serializers.IntegerField()
    titular = serializers.IntegerField()
    min = serializers.IntegerField()

class GeneralesSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadisticasGenerales
        fields = '__all__'

class TirosSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadisticasTiros
        fields = '__all__'

class CreacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadisticasCreacion
        fields = '__all__'

class DiversasSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadisticasDiversas
        fields = '__all__'

class PasesSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadisticasPases
        fields = '__all__'

class TipoPaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadisticasTipoPases
        fields = '__all__'

class DefensaSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadisticasDefensa
        fields = '__all__'

class RegatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadisticasRegates
        fields = '__all__'

class PorteroSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadisticasPortero
        fields = '__all__'