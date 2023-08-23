import pygame


class Imagen:
    def __init__(self, imagen):
        self.imagen = imagen
        self.numero_imagen = 0
        #define cada cuantos frames se refresca la imagen
        self.frame_rate = 5
        #secuencia, variacion
        self.cantidad_de_imagenes = self.obtener_cantidad_de_imagenes()
        self.secuencia_de_imagenes, self.variacion_de_imagenes = self.cantidad_de_imagenes
        self.frame = 0
        self.tamano_de_sprites = (64,64)
    
    
    def obtener_cantidad_de_imagenes(self) -> tuple:
        tamano = self.imagen.get_size()
        filas = tamano[0]/self.tamano_de_sprites[0]
        columnas = tamano[1]/self.tamano_de_sprites[1]
        return filas, columnas
    
        
    def animacion(self):
        self.imagen_actual = self.imagen.subsurface(pygame.Rect(self.numero_imagen,128,64,64))
        if self.numero_imagen < self.secuencia_de_imagenes:
            if self.frame == self.frame_rate:
                self.numero_imagen += 64
        if self.frame < self.frame_rate:
            self.frame += 1