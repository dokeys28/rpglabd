import pygame

from constantes import *


class Imagen:
    def __init__(self, imagen):
        self.imagen = imagen
        #define cada cuantos frames se refresca la imagen
        self.frame_rate = VELOCIDAD_CAMINAR
        #secuencia, variacion
        self.frame = 0
        self.ancho_de_sprites = 64
        self.alto_de_sprites = 64
        self.numero_imagen = 0
        self.numero_variacion = 0
        self.tamano_de_sprites = (self.ancho_de_sprites, self.alto_de_sprites)
        self.cantidad_de_imagenes = self.obtener_cantidad_de_imagenes()
        self.secuencia_de_imagenes, self.variacion_de_imagenes = self.cantidad_de_imagenes
        self.energia = 100
        self.gastando_energia = False
        self.cansado = False
    
    def obtener_cantidad_de_imagenes(self) -> tuple:
        tamano = self.imagen.get_size()
        filas = tamano[0]/self.tamano_de_sprites[0]
        columnas = tamano[1]/self.tamano_de_sprites[1]
        return filas, columnas
    
        
    def animacion(self)-> pygame.image:
        self.pixel_numero_imagen = self.numero_imagen * self.ancho_de_sprites
        self.pixel_variacion_de_imagenes = self.numero_variacion * self.alto_de_sprites
        self.imagen_actual = self.imagen.subsurface(pygame.Rect(self.pixel_numero_imagen,
                                                                self.pixel_variacion_de_imagenes, 
                                                                self.ancho_de_sprites, 
                                                                self.alto_de_sprites))
        if self.numero_imagen < self.secuencia_de_imagenes -1 :
            if self.frame == self.frame_rate:
                self.numero_imagen += 1
        else:
            self.numero_imagen = 0
            
        if self.frame < self.frame_rate:
            self.frame += 1
        else:
            self.frame = 0
        
        return self.imagen_actual
    
    def gastar_energia(self):
        if self.energia > 1:
            self.gastando_energia = True
        else:
            print('NO HAY ENERGIA')
            
    def cansar(self):
        if self.cansado:
            self.frame_rate = 10
        if self.energia > 50:
            self.cansado = False

    
    def correr(self, evento):
        
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                if self.energia > 1 and not self.cansado:
                    self.frame_rate = VELOCIDAD_CORRER
                    self.gastar_energia()
        
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_SPACE:
                if not self.cansado:
                    self.frame_rate = VELOCIDAD_CAMINAR
        print(self.energia)
        
