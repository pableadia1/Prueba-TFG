from EstadisticasProcesadas.funciones import encajar
from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers, status

from FutbolStats.models import *

from .funciones import paradas,paraPenalties,encajar

from .serializers import *
    

class Portero(APIView):
    def get(self,request,id_jugador):
        pard = paradas(id_jugador)
        penalties = paraPenalties(id_jugador)
        encj = encajar(id_jugador)
        portero = Portero(penalties=penalties, encajados=encj, paradas=pard)
        serializer = NotasPortero(portero)
        return Response(serializer.data)

        





        

