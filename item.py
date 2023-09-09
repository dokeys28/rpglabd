import pygame


class Item:
    def __init__(self, imagen, cuadro, descripcion, tipo):
        self.pantalla = pygame.display.get_surface()
        self.imagen = pygame.image.load(imagen)
        #implementar otro tipo de logica
        '''
        Agregar a la lista de items = [['', '' , '' , ''],
                                        ['', '' , item (por ende esta seria la ubicacion del cuadro) , ''],
                                        ['', '' , '' ,'']]
        '''
        self.cuadro = cuadro
        self.descripcion = pygame.font.Font(None, 30).render(descripcion,True, (0,0,0))
        self.tipo = tipo
        self.equipar = False
        
    def actualizar(self, interfaz):
        #colocar en inventario
        if not self.equipar:
            interfaz.pantalla.blit(self.imagen,(interfaz.inventario.cuadros[self.cuadro].centerx - self.imagen.get_size()[0]//2,
                            interfaz.inventario.cuadros[self.cuadro].centery - self.imagen.get_size()[1]//2))
        #colocar en equipamiento
        if self.equipar:
            interfaz.pantalla.blit(self.imagen,(interfaz.equipamiento.rectas[self.tipo].centerx - self.imagen.get_size()[0]//2,
                            interfaz.equipamiento.rectas[self.tipo].centery - self.imagen.get_size()[1]//2))
