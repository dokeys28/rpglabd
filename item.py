import pygame


class Item:
    def __init__(self, imagen, cuadro):
        self.pantalla = pygame.display.get_surface()
        self.imagen = pygame.image.load(imagen)
        self.cuadro = cuadro
        
    
    def actualizar(self, inventario):
        inventario.pantalla.blit(self.imagen,(inventario.cuadros[self.cuadro].centerx - self.imagen.get_size()[0]//2,
                        inventario.cuadros[self.cuadro].centery - self.imagen.get_size()[1]//2))
        
 
lista_de_items = [Item('arco.png','cuadro 5'), Item('arco.png', 'cuadro 18')]
        
