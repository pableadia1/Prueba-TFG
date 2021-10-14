from django.db.models import fields
from rest_framework import serializers
from FutbolStats.models import Liga, Equipo

class LigaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Liga
        fields = '__all__'

class EquipoSerializer(serializers.ModelSerializer):
    class Meta:
        model= Equipo
        fields = '__all__'