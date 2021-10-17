from unittest import result
from django.test import TestCase
from .views import *

class SimpleTest(TestCase):
    def test_zeros(self):
        data = "70"
        resultado_esperado = 70  
        self.assertEqual(Zeros(data), resultado_esperado)
    
    def test_demarcaciones(self):
        data = "(MCO-DEL-EI)"
        resultado_esperado = ["MCO","DEL","EI"]
        self.assertEqual(demarcaciones(data), resultado_esperado)

class CreacionTest(TestCase):
    def setUp(self):
        self.jugador = Jugador.objects.create(nombre="jugador1",nombreCompleto="jugado1",nacionalidad="España",pie="Izquierda",posicion="PO",foto="foto.jpg") 
        esJug = EstadisticasJugador.objects.create(jugador=self.jugador,temporada="2021-2020",equpo="Sevilla")
        lisJug = [esJug]
        lisEstCr = [(5,7)]
        estadisticasCreacion(lisEstCr,lisJug)
    
    def test_creacion(self):
        self.assertEqual(EstadisticasCreacion.pasesGol,5)
    
    def tearDown(self):
        self.jugador.delete()
