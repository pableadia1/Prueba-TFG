
from django.contrib import admin
from django.urls import path, include

from Liga.views import ligas,tabla
from Equipo.views import equipos,equipo
from Jugador.views import jugadores,jugador
from Estadisticas.views import maxGoleadoresAsistentesLiga, estadisticasJugador, estadisticasPrueba
from EstadisticasProcesadas.views import *
from FutbolStats import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('carga/', views.cargar),
    path('borrar/', views.borrar),
    path('liga/', ligas.as_view(), name="Liga"),
    path('liga/equipos/<int:id_liga>', equipos.as_view(), name="Equipos"),
    path('liga/tabla/<int:id_liga>', tabla.as_view(), name="Tabla"),
    path('equipo/<int:id_equipo>', equipo.as_view(), name="Equipo"),
    path('equipo/jugadores/<int:id_equipo>',jugadores.as_view(), name="Jugadores"),
    #path('equipo/maximos/<int:id_equipo>',maxGoleadoresAsistentesEquipo.as_view(), name="MaximosEquipo"),
    path('jugador/<int:id_jugador>', jugador.as_view(), name="Jugador"),
    path('jugador/maximos/<int:id_gen>', maxGoleadoresAsistentesLiga.as_view(), name="Maximos"),
    path('jugador/estadisticas/<int:id_jugador>', estadisticasJugador.as_view(), name="estadisticas"),
    path('jugador/estadisticas/portero/<int:id_jugador>', Portero.as_view(), name="portero"),
    path('prueba/<int:id_jugador>', estadisticasPrueba.as_view(), name="est"),
] 


