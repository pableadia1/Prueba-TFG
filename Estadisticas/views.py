import re
from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers, status

from Estadisticas.models import *
from Jugador.views import jugador
from .serializers import *
from Jugador.serializers import JugadorSerializer,Maximos,MaximosSerializer

# Create your views here.



class maxGoleadoresAsistentesLiga(APIView):

    def tipoEstadistica(self,dato,est):
        if dato == "goles":
            res = est.estadisticasGenerales.goles
        elif dato == "asistencias":
            res = est.estadisticasGenerales.asistencias
        elif dato == "minutosJugados":
            res = est.estadisticasGenerales.minutosJugados
        return res

    def get(self,request,id_gen):
        try:
            temporada = request.data["temporada"]
            dato = request.data["dato"]
            todos = request.data["todos"]
            res = []
            estadisticas = EstadisticasJugador.objects.filter(temporada=temporada).order_by("-estadisticasGenerales__" + dato)
            for e in estadisticas[0:10]:
                jug = Jugador.objects.get(id=e.jugador.id)
                estadistica = self.tipoEstadistica(dato,e)
                nombre, equipo, id = jug.nombre, jug.equipoActual.nombre, jug.equipoActual.liga_id
                g = Maximos(nombre=nombre,estadistica=estadistica,equipo=equipo)
                if todos != True:
                    if id == id_gen:
                        res.append(g)
                else:
                    res.append(g)
            serializer = MaximosSerializer(res,many="True")
            return Response(serializer.data)
        except:
            return Response({"mensaje":"Especifique la temporada y la liga"},status=status.HTTP_400_BAD_REQUEST)
 
    def post(self,request,id_gen):
        try:
            temporada = request.data["temporada"]
            dato = request.data["dato"]
            estadisticas = EstadisticasJugador.objects.filter(jugador__equipoActual__id=id_gen,temporada=temporada).order_by("-estadisticasGenerales__goles")[0]

            jug = Jugador.objects.get(id=estadisticas.jugador.id)
            estadistica = self.tipoEstadistica(dato,estadisticas)
            nombre, equipo = jug.nombre, jug.equipoActual.nombre
            g = Maximos(nombre=nombre,estadistica=estadistica,equipo=equipo)
            serializer = MaximosSerializer(g)
            return Response(serializer.data)
        except:
            return Response({"mensaje":"Especifique la temporada y la liga"},status=status.HTTP_400_BAD_REQUEST)
    
class estadisticasJugador(APIView):
    def get(self,request, id_jugador):
        jug = EstadisticasJugador.objects.filter(jugador=id_jugador)
        estadisticas = []
        for j in jug:
            gen = EstadisticasGenerales.objects.get(id = j.estadisticasGenerales.id)
            misc = EstadisticasDiversas.objects.get(id = j.estadisticasDiversas.id)
            est = Estadisticas(temporada=j.temporada, equipo= j.equipo, amarillas= misc.amarillas, rojas= misc.rojas, asistencias= gen.asistencias, pj= gen.partidosJugados,
            titular= gen.titular, min = gen.minutosJugados, goles= gen.goles)
            estadisticas.append(est)
        serializer = EstadisticasJug(estadisticas, many="True")
        return Response(serializer.data)

class estadisticasPrueba(APIView):
    def get(self,request, id_jugador):
        jug = EstadisticasJugador.objects.filter(jugador=id_jugador)
        estadisticas = []
        for j in jug:
            gen = EstadisticasTipoPases.objects.get(id = j.estadisticasTipoPases.id)
            estadisticas.append(gen)
            serializer = TipoPaseSerializer(estadisticas, many="True")
        return Response(serializer.data)

