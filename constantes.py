import os

ANCHO_PANTALLA = 1280
ALTO_PANTALLA = 768
DIRECTORIO_IMAGENES = '/imagenes'
DIRECTORIO_IMAGENES_PERSONAJE = '/imagenes/personajes'
#IMAGENES_PERSONAJE = [imagen_personaje for imagen_personaje in os.listdir(DIRECTORIO_IMAGENES_PERSONAJE)]
LIMITE_CLASES = 2
NIVEL_PARA_ELEGIR_SEGUNDA_CLASE = 10
FRAME_RATE_CORRER = 2
FRAME_RATE_CAMINAR = 2
FRAME_RATE_CANSADO = 11
ANIMACIONES_PERSONAJE = {'caminar':{'arriba':0, 'izquierda': 1, 'abajo':2, 'derecha': 3},
                         'ataque':{'arriba':0, 'izquierda': 1, 'abajo':2, 'derecha': 3}}
ANCHO_PERSONAJE = 64
ALTO_PERSONAJE = 64
REGENERACION_ENERGIA = 10
ENERGIA_MAXIMA = 100
FRAME_RATE = 0
FRAME_RATE_ENERGIA = 30
VELOCIDAD_JUGADOR = 0.5
K_VELOCIDAD = 3
VIDA_INICIAL_JUGADOR = 100
VIDA_MAXIMA = 100
REGENERACION_VIDA = 10
FRAME_RATE_VIDA = 30
CONSTANTES_VITALIDAD = {'vida': [VIDA_MAXIMA, REGENERACION_VIDA, FRAME_RATE_VIDA, (255,0,0)],
                        'energia': [ENERGIA_MAXIMA, REGENERACION_ENERGIA, FRAME_RATE_ENERGIA, (255,255,0)]}
TAMANO_BARRAS = 10
LARGO_BARRAS = 200
MARGEN = 20
POSICION_BARRA_VIDA = ALTO_PANTALLA - (TAMANO_BARRAS * 2) - MARGEN 
POSICION_BARRA_ENERGIA = ALTO_PANTALLA - TAMANO_BARRAS - MARGEN
COLOR_FONDO_INVENTARIO = (77,77,255)
COLOR_CUADROS_INVENTARIO = (50,50,255)
TAMANO_CUADROS_INVENTARIO = (74,74)

ESTRUCTURA_INVENTARIO = [['x','x','x','x','x','x','x']] * 4
BORDE_INVENTARIO = 10
BORDE_EQUIPAMIENTO = 10

    
ESTRUCTURA_EQUIPAMIENTO = [
    ['','x',''],
    ['','x',''],
    ['x','x','x'],
    ['x','x','x'],
    ]

def obtener_tamano_estructura(estructura: list):
    contador = 0
    for lista in estructura:
        for elemento in lista:
            if elemento == 'x':
                contador += 1
    return contador

TAMANO_ESPACIOS_INVENTARIO = obtener_tamano_estructura(ESTRUCTURA_INVENTARIO)
TAMANO_ESPACIOS_EQUIPAMIENTO= obtener_tamano_estructura(ESTRUCTURA_EQUIPAMIENTO)
if __name__ == "__main__":
    pass