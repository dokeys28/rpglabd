import pygame
from constantes import *


class Equipamiento:
    def __init__(self, juego):
        self.juego = juego
        self.cabeza = None
        self.cuello = None
        self.mano_izquierda = None
        self.mano_derecha = None
        self.accesorio = None
        self.torso = None
        self.piernas = None
        self.estructura = ESTRUCTURA_EQUIPAMIENTO
        self._loop(self.guardar)
        self._loop(self.dibujar)


    
    def _loop(self, func):
        posicion_inicial = (ANCHO_PANTALLA//2, 64)
        #self.dibujar_bordes(posicion_inicial)
        indice_fila = posicion_inicial[1]
        borde = 10
        self.rectas = dict()
        
        for fil in self.estructura:
            indice_columna = posicion_inicial[0]
            for col in fil:
                if col == 'x':
                    func(indice_columna, borde, indice_fila)
                indice_columna += TAMANO_CUADROS_INVENTARIO[0]
            indice_fila += TAMANO_CUADROS_INVENTARIO[1]

    def dibujar(self, indice_columna, borde, indice_fila):
        pygame.draw.rect(self.juego.pantalla,
                    COLOR_CUADROS_INVENTARIO,
                    (indice_columna + borde//2 ,indice_fila + borde//2,
                    TAMANO_CUADROS_INVENTARIO[0] - borde,
                    TAMANO_CUADROS_INVENTARIO[1] - borde))


    def dibujar_bordes(self, indice_columna, borde, indice_fila):
        pygame.draw.rect(self.juego.pantalla,
                    (0,0,0),
                    (indice_columna ,indice_fila,
                    TAMANO_CUADROS_INVENTARIO[0],
                    TAMANO_CUADROS_INVENTARIO[1]))
    

    def guardar(self,indice_columna, borde, indice_fila):
        self.rectas['rect'] = (indice_columna + borde//2 ,indice_fila + borde//2,
                            TAMANO_CUADROS_INVENTARIO[0] - borde,
                            TAMANO_CUADROS_INVENTARIO[1] - borde)


    def actualizar(self):
        self._loop(self.dibujar)


