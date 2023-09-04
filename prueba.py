import pygame
from constantes import *
from debug import debug
from handler import Handler
from interfaz import Interfaz
from inventario import Inventario
from item import lista_de_items
from personaje import Personaje

class Controles:
    def __init__(self) -> None:
        self.derecha_presionada = False
        self.izquierda_presionada = False
        self.arriba_presionada = False
        self.abajo_presionada = False

control = Controles()
                    
pygame.init()
pantalla = pygame.display.set_mode((ANCHO_PANTALLA,ALTO_PANTALLA))
pygame.display.set_caption('PRUEBAS RPG')
personaje = Personaje()
mapa = pygame.image.load('./imagenes/128x128/Tile/Tile_20-128x128.png')
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
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                control.arriba_presionada = True
            if event.key == pygame.K_DOWN:
                control.abajo_presionada = True
            if event.key == pygame.K_LEFT:
                control.izquierda_presionada = True
            if event.key == pygame.K_RIGHT:
                control.derecha_presionada = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                control.arriba_presionada = False
            if event.key == pygame.K_DOWN:
                control.abajo_presionada = False
            if event.key == pygame.K_LEFT:
                control.izquierda_presionada = False
            if event.key == pygame.K_RIGHT:
                control.derecha_presionada = False
                


    personaje.actualizar(control)
    pantalla.blit(personaje.obtener_sprite(),personaje.posicion)
    Interfaz(personaje.barras_vitalidad, lista_de_items).actualizar(handler.obtener_evento())
    debug(info= personaje.camina_arriba, pantalla=pantalla)
    pygame.display.flip()
    pygame.time.Clock().tick(60)