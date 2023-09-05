import pygame


class Item:
    def __init__(self, imagen, cuadro, descripcion):
        self.pantalla = pygame.display.get_surface()
        self.imagen = pygame.image.load(imagen)
        self.cuadro = cuadro
        self.descripcion = pygame.font.Font(None, 30).render(descripcion,True, (0,0,0))
        
    def actualizar(self, inventario):
        inventario.pantalla.blit(self.imagen,(inventario.cuadros[self.cuadro].centerx - self.imagen.get_size()[0]//2,
                        inventario.cuadros[self.cuadro].centery - self.imagen.get_size()[1]//2))
