import pygame
pygame.init()
fuente = pygame.font.Font(None,30)

def debug(info, pantalla, y = 10, x = 10):
    debug_sur = fuente.render(str(info), True, 'White')
    debug_rect = debug_sur.get_rect(topleft= (x,y))
    pygame.draw.rect(pantalla, 'Black', debug_rect)
    pantalla.blit(debug_sur, debug_rect)