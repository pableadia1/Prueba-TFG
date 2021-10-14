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
