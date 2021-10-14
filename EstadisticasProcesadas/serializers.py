from EstadisticasProcesadas.funciones import encajar, entradas
from rest_framework import serializers
from Estadisticas.models import *

class Portero:
    def __init__(self, penalties, paradas, encajados):
        self.penalties = penalties
        self.paradas = paradas
        self.encajados = encajados

class NotasPortero(serializers.Serializer):
    penalties = serializers.FloatField()
    paradas = serializers.FloatField()
    encajados = serializers.FloatField()
  
class Defensa:
    def __init__(self, robos, entradas, paraRegates):
        self.robos = robos
        self.entradas = entradas
        self.paraRegates = paraRegates

class NotaDefensa(serializers.Serializer):
    robos = serializers.FloatField()
    entradas = serializers.FloatField()
    paraRegates = serializers.FloatField()
''' 
class Tiros:
    def __init__(self, capacidad_goleadora, precision, tiros_lejanos, piernaMala):

class Regates:
    def __init__(self, regates, conduccion):

class Fisico:
    def __init__(self, resistencia, salto ):

class Pases:
    def __init__(self,):

class Mentalidad:
    def __init__(self, amarillas, expulsiones, creación):

''' 