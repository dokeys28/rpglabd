import pygame

from constantes import *


class Imagen:
    def __init__(self, imagen , personaje: pygame.sprite.Sprite):
        self.imagen = imagen
        self.personaje = personaje
        #define cada cuantos frames se refresca la imagen
        self.frame_rate = VELOCIDAD_CAMINAR
        self.ancho_de_sprites = ANCHO_PERSONAJE
        self.alto_de_sprites = ALTO_PERSONAJE
        self.numero_variacion = ANIMACIONES_PERSONAJE['caminar']['abajo']
        self.tamano_de_sprites = (self.ancho_de_sprites, self.alto_de_sprites)
        self.cantidad_de_imagenes = self.obtener_cantidad_de_imagenes()
        self.secuencia_de_imagenes, self.variacion_de_imagenes = self.cantidad_de_imagenes
        self.numero_imagen = 0
        self.frame = 0
        self.frame_rate_energia = VELOCIDAD_ENERGIA
        self.sprite = pygame.Surface((ANCHO_PERSONAJE,ALTO_PERSONAJE))
        self.rect = self.sprite.get_rect(topleft = (self.personaje.posicion))
    
    def obtener_cantidad_de_imagenes(self) -> tuple:
        tamano = self.imagen.get_size()
        filas = tamano[0]/self.tamano_de_sprites[0]
        columnas = tamano[1]/self.tamano_de_sprites[1]
        return filas, columnas
    
        
    def animacion(self)-> pygame.image:
        #recortar la imagen
        self.pixel_numero_imagen = self.numero_imagen * self.ancho_de_sprites
        #recorta segun variacion
        self.pixel_variacion_de_imagenes = self.numero_variacion * self.alto_de_sprites
        self.imagen_actual = self.imagen.subsurface(pygame.Rect(self.pixel_numero_imagen,
                                                                self.pixel_variacion_de_imagenes, 
                                                                self.ancho_de_sprites, 
                                                                self.alto_de_sprites))
        return self.imagen_actual
        
    def sumar_frame_rates(self):
        if self.frame_rate_energia < 30:
            self.frame_rate_energia += 1
        else:
            self.frame_rate_energia = 0

        #actualiza frame
        if self.frame < self.frame_rate:
            self.frame += 1
        else:
            self.frame = 0
            
            
    def actualizar(self):
        
        #si no esta quieto entonces anima
        if self.personaje.estado != 'quieto':
            #ANIMACION
            if self.numero_imagen < self.secuencia_de_imagenes -1 :
                if self.frame == self.frame_rate:
                    self.numero_imagen += 1
            else:
                self.numero_imagen = 0        
        
        
        if self.personaje.caminando:
            self.numero_variacion = ANIMACIONES_PERSONAJE['caminar'][self.personaje.dirigiendose]
            if not self.personaje.corriendo:
                self.frame_rate = VELOCIDAD_CAMINAR        
            else:
                self.frame_rate = VELOCIDAD_CORRER
            
        
        
        elif self.personaje.cansado:
            self.frame_rate = VELOCIDAD_CANSADO
        else:
            self.frame_rate = VELOCIDAD_CAMINAR


        
        self.sumar_frame_rates()
       
        
        self.sprite = self.animacion()
