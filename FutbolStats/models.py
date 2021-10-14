from django.db import models
from django.contrib.postgres.fields import ArrayField
    
class Liga(models.Model):
    nombre = models.CharField(max_length= 80)
    logo = models.CharField(max_length= 200)
    pais = models.CharField(max_length= 100)
    objects = models.Manager()


class Equipo(models.Model):
    nombre = models.CharField(max_length= 80)
    escudo = models.CharField(max_length= 200)
    liga = models.ForeignKey(Liga, on_delete=models.CASCADE)
    partidosJugados = models.IntegerField()
    victorias = models.IntegerField()
    derrotas = models.IntegerField()
    empates = models.IntegerField()
    golesFavor = models.IntegerField()
    golesContra = models.IntegerField()
    puntos  = models.IntegerField()
    objects = models.Manager()


class Jugador(models.Model):
    nombre = models.CharField(max_length= 50)
    nombreCompleto = models.CharField(max_length= 80)
    nacionalidad = models.CharField(max_length= 40)
    fechaDeNacimiento = models.DateField( null=True)
    edad = models.IntegerField( null=True)
    altura = models.FloatField( null=True)
    peso = models.FloatField( null=True)
    pie = models.CharField(max_length=10, choices=(("Izquierda","Zurdo"),("Derecha","Diestro"),("Ambos","Ambidiestro")))
    posicion =   models.CharField(max_length= 2, choices=(("PO","Portero"),("DF", "Defensa"), ("CC", "CentroCampista"), ("DL", "Delantero")))
    demarcaciones = ArrayField(models.CharField(max_length= 3), null=True)
    equipoActual = models.ForeignKey(Equipo,on_delete=models.CASCADE)
    foto = models.CharField(max_length= 150)
    objects = models.Manager()


class EstadisticasGenerales(models.Model):
    partidosJugados = models.IntegerField()
    titular = models.IntegerField()
    partidosCompletos = models.IntegerField()
    entraSuplente = models.IntegerField()
    goles = models.IntegerField()
    minutosJugados =  models.IntegerField()
    asistencias = models.IntegerField()
    objects = models.Manager()

    
class EstadisticasTiros(models.Model):
    tiros = models.IntegerField()
    tirosPorteria = models.IntegerField()
    distanciaTiros = models.FloatField()
    tirosFalta = models.IntegerField()
    penalties = models.IntegerField()
    penaltiesMarcados = models.IntegerField()
    objects = models.Manager()


class EstadisticasTipoPases(models.Model):
    conPresion = models.IntegerField()
    centros =  models.IntegerField()
    pasesPieDerecho = models.IntegerField()
    pasesPieIzquierdo = models.IntegerField()
    pasesCabeza = models.IntegerField()
    cornersLanzados = models.IntegerField()
    pasesFueraJuego = models.IntegerField()
    pasesFueraCampo = models.IntegerField()
    paseSuelo = models.IntegerField()
    paseBajo = models.IntegerField()
    paseAlto = models.IntegerField()
    objects = models.Manager()


class EstadisticasPases(models.Model):
    distanciaPases = models.IntegerField()
    pasesCortos = models.IntegerField()
    pasesCortosEfectivos =models.IntegerField()
    pasesMedios =models.IntegerField()
    pasesMediosEfectivos = models.IntegerField()
    pasesLargos = models.IntegerField()
    pasesLargosEfectivos = models.IntegerField()
    objects = models.Manager()


class EstadisticasDefensa(models.Model):
    entradas =  models.IntegerField()
    entradasAtaque =  models.IntegerField()
    entradasMedio =models.IntegerField()
    entradasDefensa = models.IntegerField()
    entradasGanadas = models.IntegerField()
    presion =models.IntegerField()
    presionAtaque =models.IntegerField()
    presionMedio = models.IntegerField()
    presionGanada =models.IntegerField()
    presionDefensa = models.IntegerField()
    intentoRegate = models.IntegerField()
    regateParado =  models.IntegerField()
    objects = models.Manager()


class EstadisticasRegates(models.Model):
    balonTocadoAreaPenaltyPropia = models.IntegerField()
    balonTocadoDefensa = models.IntegerField()
    balonTocadoMedio = models.IntegerField()
    balonTocadoAtaque = models.IntegerField()
    balonTocadoAreaPenaltyContr = models.IntegerField()
    regates = models.IntegerField()
    regatesCompletados = models.IntegerField()
    controles = models.IntegerField()
    distanciaPosesion = models.IntegerField()
    controlesFallidos =  models.IntegerField()
    pasesObjetivo =  models.IntegerField()
    pasesRecibidos = models.IntegerField()
    objects = models.Manager()


class EstadisticasDiversas(models.Model):
    balonesAereosGanados = models.IntegerField()
    balonesAereosPerdidos = models.IntegerField()
    balonesSueltosRecuperados =models.IntegerField()
    amarillas = models.IntegerField()
    dobleAmarillas = models.IntegerField()
    rojas = models.IntegerField()
    faltasRecibidas = models.IntegerField()
    faltasCometidas = models.IntegerField()
    fueraJuego = models.IntegerField()
    penaltiesConcedidos = models.IntegerField()
    objects = models.Manager()


class EstadisticasPortero(models.Model):
    golesRecibidos = models.IntegerField()
    tirosRecibidos = models.IntegerField()
    paradasRecibidos =models.IntegerField()
    cleanSheet =models.IntegerField()
    penaltiesEncagados = models.IntegerField()
    penaltiesParados = models.IntegerField()
    penaltiesFalladosContrario = models.IntegerField()
    objects = models.Manager()


class EstadisticasCreacion(models.Model):
    pasesGol = models.IntegerField()
    pasesMuertosGol = models.IntegerField()
    objects = models.Manager()


class EstadisticasJugador(models.Model):
    temporada = models.CharField(max_length=30, null=True)
    equipo = models.CharField(max_length=80, null=True)
    jugador = models.ForeignKey(Jugador,on_delete=models.CASCADE)
    estadisticasGenerales = models.OneToOneField(EstadisticasGenerales,on_delete=models.CASCADE, null=True)
    estadisticasPortero = models.OneToOneField(EstadisticasPortero,on_delete=models.CASCADE, null=True)
    estadisticasTiros = models.OneToOneField(EstadisticasTiros,on_delete=models.CASCADE, null=True)
    estadisticasPases = models.OneToOneField(EstadisticasPases,on_delete=models.CASCADE, null=True)
    estadisticasTipoPases = models.OneToOneField(EstadisticasTipoPases,on_delete=models.CASCADE, null=True)
    estadisticasDefensa = models.OneToOneField(EstadisticasDefensa,on_delete=models.CASCADE, null=True)
    estadisticasDiversas = models.OneToOneField(EstadisticasDiversas,on_delete=models.CASCADE, null=True)
    estadisticasCreacion = models.OneToOneField(EstadisticasCreacion,on_delete=models.CASCADE, null=True)
    estadisticasRegates = models.OneToOneField(EstadisticasRegates,on_delete=models.CASCADE, null=True)
    objects = models.Manager()

