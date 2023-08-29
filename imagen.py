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
        self.frame_rate_energia = 30
        self.sprite = pygame.Surface((ANCHO_PERSONAJE,ALTO_PERSONAJE))
        self.rect = self.sprite.get_rect(topleft = (personaje.posicion))
    
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


    def regenerarse(self):
            if self.frame_rate_energia == 30 and self.energia < 100:
                self.energia += 10
            if self.energia > 100: 
                self.energia = 100
                self.regenerandose = False
            return self.energia
    
    def actualizar(self):
        
        #si no esta quieto entonces anima
        if self.estado != 'quieto':
            #cambiar imagen
            if self.numero_imagen < self.secuencia_de_imagenes -1 :
                if self.frame == self.frame_rate:
                    self.numero_imagen += 1
            else:
                self.numero_imagen = 0
            
        #actualiza frame
        if self.frame < self.frame_rate:
            self.frame += 1
        else:
            self.frame = 0
        
        self.sumar_frame_rates()
        if self.regenerandose:
            self.regenerarse()
        
        if self.personaje.corriendo:
            self.numero_variacion = ANIMACIONES_PERSONAJE['caminar'][self.personaje.direccion]
            self.frame_rate = VELOCIDAD_CORRER
        else:
            self.frame_rate = VELOCIDAD_CAMINAR        
        
        if self.personaje.cansado:
            self.frame_rate = VELOCIDAD_CANSADO
        else:
            self.frame_rate = VELOCIDAD_CAMINAR
        
       
        
        self.sprite = self.animacion()
