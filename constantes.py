import os


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


if __name__ == "__main__":
    pass