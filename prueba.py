import pygame

from imagen import Imagen
from personaje import Personaje



pygame.init()
pantalla = pygame.display.set_mode((600,600))
pygame.display.set_caption('PRUEBAS RPG')
#imagen = pygame.image.load('./imagenes/personaje/caminar.png')
#imagen = Imagen(imagen)
personaje = Personaje()
while True:
    
    pantalla.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                personaje.corriendo = True
            
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                personaje.corriendo = False
            
    
    if imagen.gastando_energia:
        if imagen.energia >= 1:
            imagen.energia -= 1
    
    if imagen.energia == 0:
        imagen.cansado = True    
    pantalla.blit(imagen.sprite,imagen.posicion)
    pygame.display.flip()
    pygame.time.Clock().tick(60)