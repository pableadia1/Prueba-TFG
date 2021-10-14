from rest_framework import serializers
from FutbolStats.models import Equipo

class EquipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipo
        fields = '__all__'