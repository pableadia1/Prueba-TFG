from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from Liga.models import Liga
from Equipo.models import Equipo
from .serializers import LigaSerializer, EquipoSerializer

# Create your views here.

class ligas(APIView):

    def get(self, request):
        ligas = Liga.objects.all()
        serializer = LigaSerializer(ligas, many="True")
        return Response(serializer.data)

    def post(self, request):
        try:
            id = request.data["id_liga"]
        except:
            return Response({"mensaje":"Expecifique el id de liga"},status=status.HTTP_400_BAD_REQUEST)
        try:
            liga = Liga.objects.get(id=id)
            serializer = LigaSerializer(liga)
            return Response(serializer.data)
            
        except:   
            return Response({"mensaje":"No existe dicha liga"},status=status.HTTP_400_BAD_REQUEST)

class tabla(APIView):
    def get(self, request, id_liga):
        equipos = Equipo.objects.filter(liga_id=id_liga)
        serializer = EquipoSerializer(equipos, many="True")
        return Response(serializer.data)






