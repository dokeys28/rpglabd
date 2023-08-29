import pygame
from constantes import *


class Energia:
    def __init__(self, cantidad, personaje: pygame.Surface):
        self.cantidad = cantidad
        self.personaje = personaje
    
    def gastar(self):
        if self.cantidad >= 1:
            self.cantidad -= 1
         
    def regenerar(self):
        if self.personaje.imagen.frame_rate_energia == 30:
            if self.cantidad < ENERGIA_MAXIMA:
                self.cantidad += REGENERACION_ENERGIA
                if self.cantidad > ENERGIA_MAXIMA:
                    self.cantidad = ENERGIA_MAXIMA
            else:
                self.cantidad = ENERGIA_MAXIMA
        else:
            self.regenerandose = False