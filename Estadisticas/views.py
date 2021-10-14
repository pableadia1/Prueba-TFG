from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers, status

from Estadisticas.models import *
from .serializers import *
from Jugador.serializers import JugadorSerializer,GoleadoresSerializer,Goleadores, Asistentes,AsistentesSerializer

# Create your views here.


class maxGoleadoresAsistentes(APIView):
    def get(self,request):
        try:
            temporada = request.data["temporada"]
            id_liga =  request.data["id_liga"]
            res = []
            estadisticas = EstadisticasJugador.objects.filter(temporada=temporada).order_by("-estadisticasGenerales__goles")
            for e in estadisticas[0:10]:
                jug = Jugador.objects.get(id=e.jugador.id)
                goles = e.estadisticasGenerales.goles
                nombre, equipo, id = jug.nombre, jug.equipoActual.nombre, jug.equipoActual.liga_id
                g = Goleadores(nombre=nombre,goles=goles,equipo=equipo)
                if id_liga != "all":
                    if id == id_liga:
                        res.append(g)
                else:
                    res.append(g)
            serializer = GoleadoresSerializer(res,many="True")
            return Response(serializer.data)
        except:
            return Response({"mensaje":"Especifique la temporada y la liga"},status=status.HTTP_400_BAD_REQUEST)
    
    def post(self,request):
        try:
            temporada = request.data["temporada"]
            id_liga =  request.data["id_liga"]
            res = []
            estadisticas = EstadisticasJugador.objects.filter(temporada=temporada).order_by("-estadisticasGenerales__asistencias")
            for e in estadisticas[0:10]:
                jug = Jugador.objects.get(id=e.jugador.id)
                asistencias = e.estadisticasGenerales.asistencias
                nombre, equipo, id = jug.nombre, jug.equipoActual.nombre, jug.equipoActual.liga_id
                g = Asistentes(nombre=nombre,asistencias=asistencias,equipo=equipo)
                if id_liga != "all":
                    if id == id_liga:
                        res.append(g)
                else:
                    res.append(g)
            serializer = AsistentesSerializer(res,many="True")
            return Response(serializer.data)
        except:
            return Response({"mensaje":"Especifique la temporada y la liga"},status=status.HTTP_400_BAD_REQUEST)

class maxGoleadoresAsistentesEquipo(APIView):
    def get(self,request, id_equipo):

        temporada = request.data["temporada"]
        estadisticas = EstadisticasJugador.objects.filter(temporada=temporada, equipo__id=id_equipo).order_by("-estadisticasGenerales__goles")

        jug = Jugador.objects.get(id=estadisticas[0].jugador.id)
        goles = estadisticas.estadisticasGenerales.goles
        nombre, equipo = jug.nombre, jug.equipoActual.nombre
        g = Goleadores(nombre=nombre,goles=goles,equipo=equipo)
        serializer = GoleadoresSerializer(g,many="True")
        return Response(serializer.data)

    
    def post(self,request):
        try:
            temporada = request.data["temporada"]
            id_liga =  request.data["id_liga"]
            res = []
            estadisticas = EstadisticasJugador.objects.filter(temporada=temporada).order_by("-estadisticasGenerales__asistencias")
            for e in estadisticas[0:10]:
                jug = Jugador.objects.get(id=e.jugador.id)
                asistencias = e.estadisticasGenerales.asistencias
                nombre, equipo, id = jug.nombre, jug.equipoActual.nombre, jug.equipoActual.liga_id
                g = Asistentes(nombre=nombre,asistencias=asistencias,equipo=equipo)
                if id_liga != "all":
                    if id == id_liga:
                        res.append(g)
                else:
                    res.append(g)
            serializer = AsistentesSerializer(res,many="True")
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

