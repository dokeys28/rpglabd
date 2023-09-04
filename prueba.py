import pygame
from updater import Updater
from constantes import *
from debug import debug
from handler import Handler
from interfaz import Interfaz
from item import Item
from personaje import Personaje

class Juego:  
    def __init__(self):                               
        pygame.init()
        self.pantalla = pygame.display.set_mode((ANCHO_PANTALLA,ALTO_PANTALLA))
        pygame.display.set_caption('PRUEBAS RPG')
        self.lis_mapa = []
        self.mapa = pygame.image.load('./imagenes/128x128/Tile/Tile_20-128x128.png')
        self.lista_de_items = [Item('arco.png',
                                    'cuadro 5',
                                    'Soy un arco 1'),
                               Item('arco.png',
                                    'cuadro 18',
                                    'Soy un arco 2')]
        self.personaje = Personaje(self)
        self.handler = Handler(self)
        self.interfaz = Interfaz(self)
        self.updater = Updater(self)
        self._modo_debug = False
        #Creando mapa
        for col in range(6):
            for fil in range(10):    
                self.lis_mapa.append((self.mapa,(fil*128,col*128)))
    def correr(self):
        while True:
            self.pantalla.fill((255,255,255))
            self.pantalla.blits([x for x in self.lis_mapa])
            #main loop
            self.updater.actualizar_todo()
            #debug
            if self._modo_debug:
                debug(info= self.personaje.camina_arriba, pantalla=self.pantalla)
            pygame.display.flip()
            pygame.time.Clock().tick(60)

if __name__ == "__main__":
    juego = Juego()
    juego.correr()