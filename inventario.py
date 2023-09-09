import pygame

from constantes import *
from item import Item


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
        self._loop(self.guardar)
        self.guardar_rectas()
        self.item_pisado = None
        self.item_suelto = None
        self.cuadro_x_labo = None
        self.click = False
        self.lista_de_items = [Item('espada.png',
                                    'cuadro 5',
                                    'Soy una espada',Slots_equipamiento.MANO_DERECHA.value),
                               Item('escudo.png',
                                    'cuadro 18',
                                    'Soy un escudo',Slots_equipamiento.MANO_IZQUIERDA.value)]
        self.items = [''] * TAMANO_ESPACIOS_INVENTARIO


    def actualizar_items_propios(self):
        self.items = [''] * TAMANO_ESPACIOS_INVENTARIO
        #actualizando items propios del inventario
        for item in self.lista_de_items:
            if item.cuadro != '':
                self.items[int(item.cuadro.split('cuadro ')[1])- 1] = item
        
    
    def _loop(self, func):
        posicion_inicial = (0,64)
        #self.dibujar_bordes(posicion_inicial)
        indice_fila = posicion_inicial[1]

        for fil in ESTRUCTURA_INVENTARIO:
            indice_columna = posicion_inicial[0]
            for col in fil:
                if col == 'x':
                    func(indice_columna, indice_fila)
                indice_columna += TAMANO_CUADROS_INVENTARIO[0]
            indice_fila += TAMANO_CUADROS_INVENTARIO[1]

    def guardar(self, indice_columna, indice_fila):
        self.posiciones.append((indice_columna + BORDE_INVENTARIO // 2,
                                indice_fila + BORDE_INVENTARIO // 2))


    def guardar_rectas(self):
        for cuadro in self.posiciones:
            self.rectas.append(pygame.Rect(cuadro[0],
                                           cuadro[1],
                                           TAMANO_CUADROS_INVENTARIO[0] - BORDE_INVENTARIO,
                                           TAMANO_CUADROS_INVENTARIO[1] - BORDE_INVENTARIO))
        for i, xcuadro in enumerate(self.rectas):
            self.cuadros[f'cuadro {i + 1}'] = xcuadro
            
    def handler(self):
        for c in self.cuadros.keys():
            if self.cuadros[c].collidepoint(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1]):
                self.cuadro_x_labo = c
                #mostrar descripcion del item
                for item in self.lista_de_items:
                    if not item.equipar:
                        if item.cuadro == self.cuadro_x_labo:
                            self.pantalla.blit(item.descripcion, (64,400))
        
        if not self.click:
            if self.juego.handler.control.mouse_presionado:
                self.click = True
                self.item_pisado = self.cuadro_x_labo

                if self.juego.handler.control.mouse_derecho_presionado:
                    for item in self.juego.interfaz.items:
                        if item.cuadro == self.item_pisado:
                            #implementar otro tipo de logica
                            #item.cuadro = ''
                            item.equipar = True
                            item.actualizar(self.juego.interfaz)
        
        else:
            if not self.juego.handler.control.mouse_presionado:
                self.click = False
                self.item_suelto = self.cuadro_x_labo
                for item in self.lista_de_items:
                    if item.cuadro == self.item_pisado and self.items[int(self.item_suelto.split('cuadro ')[1])-1] == '':
                        item.cuadro = self.item_suelto
                    item.actualizar(self.juego.interfaz)


    def actualizar(self):
        self.pantalla.blit(self.fondo,(0,0))
        self._loop(self.dibujar)
        for item in self.lista_de_items:
            item.actualizar(self.juego.interfaz)   
        self.handler()
        self.actualizar_items_propios()

    def dibujar(self, indice_columna, indice_fila):
        pygame.draw.rect(self.pantalla,
                            COLOR_CUADROS_INVENTARIO,
                            (indice_columna + BORDE_INVENTARIO // 2,
                        indice_fila + BORDE_INVENTARIO // 2,
                            TAMANO_CUADROS_INVENTARIO[0] - BORDE_INVENTARIO,
                            TAMANO_CUADROS_INVENTARIO[1] - BORDE_EQUIPAMIENTO))

