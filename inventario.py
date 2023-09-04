import pygame

from constantes import *


class Inventario:
    def __init__(self, juego):
        self.posiciones = []
        self.rectas = []
        self.juego = juego
        self.pantalla = self.juego.pantalla
        self.cuadros = dict()
        self.fondo = pygame.Surface((ANCHO_PANTALLA, ALTO_PANTALLA))
        self.fondo.fill(COLOR_FONDO_INVENTARIO)
        self.visible = False
        self.guardar()
        self.item_pisado = None
        self.item_suelto = None
        self.cuadro_x_labo = None
        self.click = False
    
    def guardar(self):
        for fil in range(1,5):
            n = 0
            for col in range(1,8):
                self.posiciones.append((col * TAMANO_CUADROS_INVENTARIO[0] + n ,
                                        fil * TAMANO_CUADROS_INVENTARIO[1] + fil* 10))
                n += TAMANO_CUADROS_INVENTARIO[0]//6
        for cuadro in self.posiciones:
            self.rectas.append(pygame.Rect(cuadro[0],
                                           cuadro[1],
                                           TAMANO_CUADROS_INVENTARIO[0],
                                           TAMANO_CUADROS_INVENTARIO[1]))
        for i, xcuadro in enumerate(self.rectas):
            self.cuadros[f'cuadro {i + 1}'] = xcuadro
            
    def handler(self):
        for c in self.cuadros.keys():
            if self.cuadros[c].collidepoint(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1]):
                self.cuadro_x_labo = c
                #mostrar descripcion del item
                for item in self.juego.lista_de_items:
                    if item.cuadro == self.cuadro_x_labo:
                        self.pantalla.blit(item.descripcion, (64,400))
        
        if not self.click:
            if self.juego.handler.control.mouse_presionado:
                self.click = True
                self.item_pisado = self.cuadro_x_labo
        
        else:
            if not self.juego.handler.control.mouse_presionado:
                self.click = False
                self.item_suelto = self.cuadro_x_labo
                for item in self.juego.lista_de_items:
                    if item.cuadro == self.item_pisado:
                        item.cuadro = self.item_suelto
                    item.actualizar(self)


    def actualizar(self):
        self.pantalla.blit(self.fondo,(0,0))
        for fil in range(1,5):
            n = 0
            for col in range(1,8):
                pygame.draw.rect(self.pantalla,
                                 COLOR_CUADROS_INVENTARIO,
                                 (col * TAMANO_CUADROS_INVENTARIO[0] + n,
                                  fil * TAMANO_CUADROS_INVENTARIO[1] + fil* 10,
                                  TAMANO_CUADROS_INVENTARIO[0],
                                  TAMANO_CUADROS_INVENTARIO[1]))
                n += TAMANO_CUADROS_INVENTARIO[0]//6       
        for item in self.juego.lista_de_items:
            item.actualizar(self)   
        self.handler()
