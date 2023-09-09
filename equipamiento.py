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
        self.rectas = dict()
        self._loop(self.guardar)
        self.visible = False
        self.cuadro_x_labo = None
        self.click = False

    
    def _loop(self, func):
        posicion_inicial = (ANCHO_PANTALLA//2, 64)
        #self.dibujar_bordes(posicion_inicial)
        indice_fila = posicion_inicial[1]
        n = 0
        for fil in ESTRUCTURA_EQUIPAMIENTO:
            indice_columna = posicion_inicial[0]
            for col in fil:
                if col == 'x':
                    func(indice_columna, indice_fila, n)
                    n += 1
                indice_columna += TAMANO_CUADROS_INVENTARIO[0]
            indice_fila += TAMANO_CUADROS_INVENTARIO[1]

    def dibujar(self, indice_columna, indice_fila, n):
        pygame.draw.rect(self.juego.pantalla,
                    COLOR_CUADROS_INVENTARIO,
                    (indice_columna + BORDE_EQUIPAMIENTO//2 ,indice_fila + BORDE_EQUIPAMIENTO//2,
                    TAMANO_CUADROS_INVENTARIO[0] - BORDE_EQUIPAMIENTO,
                    TAMANO_CUADROS_INVENTARIO[1] - BORDE_EQUIPAMIENTO))


    def dibujar_bordes(self, indice_columna, indice_fila, n):
        pygame.draw.rect(self.juego.pantalla,
                    (0,0,0),
                    (indice_columna ,indice_fila,
                    TAMANO_CUADROS_INVENTARIO[0],
                    TAMANO_CUADROS_INVENTARIO[1]))
    

    def guardar(self,indice_columna, indice_fila, n):
        self.rectas['rect' + str(n)] = pygame.Rect(indice_columna + BORDE_EQUIPAMIENTO//2 ,indice_fila + BORDE_EQUIPAMIENTO//2,
                            TAMANO_CUADROS_INVENTARIO[0] - BORDE_EQUIPAMIENTO,
                            TAMANO_CUADROS_INVENTARIO[1] - BORDE_EQUIPAMIENTO)


    def colisiones(self):
        for c in self.rectas.keys():
            if self.rectas[c].collidepoint(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1]):
                self.cuadro_x_labo = c
                self.mostrar_descripcion(self.cuadro_x_labo)
                self.desequipar_item(self.cuadro_x_labo)

    def mostrar_descripcion(self, cuadro):
        #mostrar descripcion del item
        for item in self.juego.interfaz.items:
            if item.equipar:
                if item.tipo == cuadro:
                    self.juego.pantalla.blit(item.descripcion, (64,400))


    def desequipar_item(self, cuadro):
        if not self.click:
            if self.juego.handler.control.mouse_presionado:
                self.click = True
                self.item_pisado = cuadro
                if self.juego.handler.control.mouse_derecho_presionado:
                    for item in self.juego.interfaz.items:
                        if item.tipo == self.item_pisado:
                            #implementar otro tipo de logica
                            item.equipar = False
                            item.actualizar(self.juego.interfaz)
        else:
            self.click = False


    def actualizar(self):
        self._loop(self.dibujar)
        self.colisiones()

