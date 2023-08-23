import pygame
from constantes import *

class Personaje:
    def __init__(self):
        #implementar elegir nombre en configuraciones
        self.nombre: str
        #definir estilo si es mago, melee, ranged
        self.estilo: str
        #para cada estilo definir una subcategoria
        self.sub_categoria: str
        self.vida: int
        
        #posicion
        self.x: int
        self.y: int
        self.posicion: list

        
        #imagenes
        self.imagenes: list

        #imagen dialogo
        self.imagen_dialogo: str
        
        #imagen actual
        self.imagen_actual = 0
                
        #genero
        self.sexo: str
        
        #habilidades
        self.habilidades: list
        
        #sprite
        self.sprite = pygame.image.load(self.imagenes[self.imagen_actual])
        
        #rect
        self.rect = self.sprite.get_rect()
         
        #tamano
        self.tamano = self.sprite
    #actualiza posicion    
    def actualizar_posicion(self):
        self.posicion = [self.x, self.y]
        return self.posicion
    
    

