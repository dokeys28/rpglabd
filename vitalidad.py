import pygame
from constantes import *


class Vitalidad:
    def __init__(self, tipo, cantidad, personaje: pygame.Surface):
        self.tipo = tipo
        self.cantidad = cantidad
        self.personaje = personaje
        self.cantidad_maxima = CONSTANTES_VITALIDAD[self.tipo][0]
        self.cantidad_regeneracion = CONSTANTES_VITALIDAD[self.tipo][1]
        self.frame_rate = CONSTANTES_VITALIDAD[self.tipo][2]
        self.color = CONSTANTES_VITALIDAD[self.tipo][3]
        
    def gastar(self):
        #OJO
        if self.cantidad >= 1:
            self.cantidad -= 1
         
    def regenerar(self):
        if self.personaje.imagen.frame_rate_energia == self.frame_rate:
            if self.cantidad < self.cantidad_maxima:
                self.cantidad += self.cantidad_regeneracion
                if self.cantidad > self.cantidad_maxima:
                    self.cantidad = self.cantidad_maxima
            else:
                self.cantidad = self.cantidad_maxima
        else:
            self.regenerandose = False

class Energia(Vitalidad):
    def __init__(self, cantidad, personaje):
        super().__init__('energia', cantidad, personaje)
        
        
class Vida(Vitalidad):
    def __init__(self, cantidad, personaje):
        super().__init__('vida', cantidad, personaje)
