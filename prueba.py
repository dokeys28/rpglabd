import pygame
from constantes import *
from debug import debug
from handler import Handler
from interfaz import Interfaz
from inventario import Inventario
from item import lista_de_items
from personaje import Personaje


                    
pygame.init()
pantalla = pygame.display.set_mode((ANCHO_PANTALLA,ALTO_PANTALLA))
pygame.display.set_caption('PRUEBAS RPG')
personaje = Personaje()
mapa = pygame.image.load('./imagenes/128x128/Tile/Tile_20-128x128.png')
inventario = Inventario()
lis_mapa = []
handler = Handler()

for col in range(6):
    for fil in range(10):    
        lis_mapa.append((mapa,(fil*128,col*128)))

while True:
    pantalla.fill((255,255,255))
    pantalla.blits([x for x in lis_mapa])
    for event in pygame.event.get():
        handler.actualizar(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


    inventario.visible = True
    personaje.actualizar(handler.obtener_evento())
    pantalla.blit(personaje.obtener_sprite(),personaje.posicion)
    Interfaz(personaje.barras_vitalidad, inventario, lista_de_items).actualizar(handler.obtener_evento())
    debug(pantalla=pantalla)
    pygame.display.flip()
    pygame.time.Clock().tick(60)