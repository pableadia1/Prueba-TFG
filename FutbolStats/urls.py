from django.urls import path
from FutbolStats import views
urlpatterns = [path('carga/', views.cargar),]