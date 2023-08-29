import pygame
from constantes import *
from imagen import Imagen

class Personaje(pygame.sprite.Sprite):
    def __init__(self):
        #implementar elegir nombre en configuraciones
        self.nombre: str
        #definir clase si es mago, melee, ranged
        self.clase: str
        #para cada clase definir una subcategoria
        self.sub_categoria: str
        self.vida: int
        
        #posicion
        self.x: int
        self.y: int
        self.posicion: list
        self.direccion: tuple
        
        #estado
        self.estado = 'quieto'
        self.saltando = False
        
        #sprite
        self.imagen = Imagen(pygame.image.load('./imagenes/personaje/caminar.png'))
        
        #imagenes
        self.imagenes: list

        #imagen dialogo
        self.imagen_dialogo: str
                       
        #genero
        self.sexo: str
        
        #habilidades
        self.habilidades: list
        
                 
        #
        self.energia = 100
        self.gastando_energia = False
        self.cansado = False
        self.regenerandose = False
        self.corriendo = False
        
    
    #cansar
    def cansar(self):
        if self.energia > 50:
            self.cansado = False
            self.frame_rate = VELOCIDAD_CAMINAR
    
    #actualizaciones
    def actualizar(self):
        self.actualizar_posicion()
        self.imagen.actualizar()
    
    def actualizar_estados(self):
        if self.energia <= 1:
            self.cansado = True
        if self.energia >50:
            self.cansado = False
        if self.energia < 100:
            self.regenerandose = True
        
        #corriendo
        if self.corriendo:
            if self.energia > 1 and not self.cansado:
                self.gastando_energia = True
            else:
                self.corriendo = False
    
    
    
    #actualiza posicion    
    def actualizar_posicion(self):
        self.imagen.actualizar()
        self.posicion = [self.x, self.y]
        return self.posicion
    
    ###debo implementar direccion
    #direccion
    arriba = [0,-1]
    abajo = [0,1]
    derecha = [1,0]
    izquierda = [-1,0]
    
        
    #obtener atributos actualizados
    def obtener_rect(self):
        return self.imagen.rect
    
    def obtener_sprite(self):
        return self.imagen.sprite
    

