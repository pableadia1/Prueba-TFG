from FutbolStats.models import *

def paraPenalties(id_jugador):
    def notaPenalties(encajados,parados,fallados):
        total = encajados + parados + fallados
        res = ((parados * 2 + fallados)/total) * 10
        return round(res,1)
    jug = EstadisticasJugador.objects.filter(jugador=id_jugador)
    penEncagados,penParados,penFallados = 0,0,0
    try:
        for j in jug:
            por = EstadisticasPortero.objects.get(id = j.estadisticasPortero.id)
            penEncagados += por.penaltiesEncagados
            penParados += por.penaltiesParados
            penFallados += por.penaltiesFalladosContrario
        res = notaPenalties(penEncagados,penParados,penFallados)
        if res > 10.0:
            res = 10
    except:
        res = 0
    return res

def paradas(id_jugador):
    def notaParadas(recibidos,paradas,pj):
        res = (paradas/recibidos) * 10
        if pj <= 5:
            res = 0
        return round(res,1)
    jug = EstadisticasJugador.objects.filter(jugador=id_jugador) 
    tirosRecibidos,tirosParados,pj = 0,0,0
    try:
        for j in jug:
            por = EstadisticasPortero.objects.get(id = j.estadisticasPortero.id)
            gen = EstadisticasGenerales.objects.get(id = j.estadisticasGenerales.id)
            pj += gen.partidosJugados
            tirosRecibidos += por.tirosRecibidos
            tirosParados += por.paradasRecibidos
        res = notaParadas(tirosRecibidos,tirosParados,pj)
    except:
        res = 0
    return res

def encajar(id_jugador):
    def notaEncajar(goles,pj):
        golesPartido = goles/pj
        res = 8/golesPartido
        if res > 10:
            res = 10
        return round(res,1)
    jug = EstadisticasJugador.objects.filter(jugador=id_jugador)
    golEncajados,pj = 0,0
    try:
        for j in jug:
            por = EstadisticasPortero.objects.get(id = j.estadisticasPortero.id)
            gen = EstadisticasGenerales.objects.get(id = j.estadisticasGenerales.id)
            golEncajados += por.golesRecibidos
            pj += gen.partidosJugados
        res = notaEncajar(golEncajados,pj)
    except:
        res = 0
    return res


def calcularPuntuacion(buenos,realizados,mint=None,potn=0,corte1=0,corte2=0,corte3=0,corte4=0):
    if mint != None:
        potenciador = ((realizados/mint) * 60) * potn 
    else:
        potenciador = 0
    res = ((buenos/realizados) * 10 ) + potenciador
    if realizados < corte3:
        if res > 9.0:
            res = 9.0
    if realizados < corte2:
        if res > 8.0:
            res = 8.0
    if realizados < corte1:
        if res > 7.0:
            res = 7.0
    if realizados < corte4:
        if res > 5.0:
            res = 5.0
    if res > 10.0:
        res = 10.0
    return round(res,1)

def entradas(id_jugador):
    jug = EstadisticasJugador.objects.filter(jugador=id_jugador)
    buenas,realizadas,mint = 0,0
    try:
        for j in jug:
            defn = EstadisticasDefensa.objects.get(id = j.estadisticasDefensa.id)
            gen = EstadisticasGenerales.objects.get(id = j.estadisticasGenerales.id)
            buenas += defn.golesRecibidos
            realizadas += defn
            mint += gen.minutosJugados
        res = calcularPuntuacion()
    except:
        res = 0
    
    return res