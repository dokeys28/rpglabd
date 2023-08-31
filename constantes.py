import os

ANCHO_PANTALLA = 1280
ALTO_PANTALLA = 720
DIRECTORIO_IMAGENES = '/imagenes'
DIRECTORIO_IMAGENES_PERSONAJE = '/imagenes/personajes'
#IMAGENES_PERSONAJE = [imagen_personaje for imagen_personaje in os.listdir(DIRECTORIO_IMAGENES_PERSONAJE)]
LIMITE_CLASES = 2
NIVEL_PARA_ELEGIR_SEGUNDA_CLASE = 10
VELOCIDAD_CORRER = 2
VELOCIDAD_CAMINAR = 9
VELOCIDAD_CANSADO = 11
ANIMACIONES_PERSONAJE = {'caminar':{'arriba':0, 'izquierda': 1, 'abajo':2, 'derecha': 3},
                         'ataque':{'arriba':0, 'izquierda': 1, 'abajo':2, 'derecha': 3}}
ANCHO_PERSONAJE = 64
ALTO_PERSONAJE = 64
REGENERACION_ENERGIA = 10
ENERGIA_MAXIMA = 500
FRAME_RATE = 0
VELOCIDAD_ENERGIA = 30
VELOCIDAD_JUGADOR = 1

if __name__ == "__main__":
    pass