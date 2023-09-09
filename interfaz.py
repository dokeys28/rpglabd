import pygame
from constantes import *
from equipamiento import Equipamiento
from inventario import Inventario

class Interfaz:
    def __init__(self, juego):
        self.juego = juego
        self.barras = self.juego.personaje.barras_vitalidad
        self.inventario = Inventario(self.juego)
        self.equipamiento = Equipamiento(self.juego)
        self.items = self.inventario.lista_de_items
        self.evento = None
        self.pantalla = self.juego.pantalla
        #hay que poner todas las cosas visibles e invisibles aqui
        self.inventario.visible = False
    
    def actualizar_barras(self):
        for barra in self.barras:
            barra.actualizar(self.pantalla)
            
    def actualizar(self):
        self.actualizar_barras()
        if self.juego.handler.control.i_presionada and not self.inventario.visible:
            self.inventario.visible = True
            if not self.equipamiento.visible:
                self.equipamiento.visible = True
            self.juego.handler.control.i_presionada = False
        elif self.juego.handler.control.i_presionada and self.inventario.visible:
            self.inventario.visible = False
            self.equipamiento.visible = False
            self.juego.handler.control.i_presionada = False  
        
        #Actualiza si son visibles
        if self.inventario.visible:
            self.inventario.actualizar()
        if self.equipamiento.visible:
            self.equipamiento.actualizar()
        if self.inventario.visible:
            for item in self.items:
                item.actualizar(self)


class Barra:
    def __init__(self, vitalidad, posicion) -> None:
        self.vitalidad = vitalidad
        self.cantidad = None
        self.posicion = posicion
        self.color = self.vitalidad.color
        self.cantidad_maxima = self.vitalidad.cantidad

    def actualizar(self, pantalla):
        self.cantidad = self.vitalidad.cantidad
        self.largo = self.cantidad * LARGO_BARRAS / self.cantidad_maxima 
        punto_inicio = ANCHO_PANTALLA//2 - self.largo//2
        pygame.draw.line(pantalla, self.color,(punto_inicio ,self.posicion[1]+ TAMANO_BARRAS//2 ), (self.largo + punto_inicio, self.posicion[1]+ TAMANO_BARRAS//2), TAMANO_BARRAS)

