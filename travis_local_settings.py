ALLOWED_HOSTS = ["*"]

# Modules in use, commented modules that you won't use
MODULES = [
    'FutbolStats',
    'Liga',
    'Equipo',
    'Jugador',
    'Buscador',
    'Estadisticas',
    'EstadisticasProcesadas',
]

APIS = {}

BASEURL = 'http://localhost:8000'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'prueba',
        'USER': 'prueba',
        'PASSWORD': 'prueba',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

# number of bits for the key, all auths should use the same number of bits
KEYBITS = 256