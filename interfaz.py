import pygame
from constantes import *
from inventario import Inventario

class Interfaz:
    def __init__(self, barras: list, items: list):
        self.barras = barras
        self.inventario = Inventario()
        self.items = items
        self.evento = None
        self.pantalla = pygame.display.get_surface()
        
    
    def actualizar_barras(self):
        for barra in self.barras:
            barra.actualizar(self.pantalla)
            
    def actualizar(self, evento):
        self.actualizar_barras()
        if self.inventario.visible:
            self.inventario.actualizar(evento, self.items) 
        


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

