import pygame

from imagen import Imagen



pygame.init()
pantalla = pygame.display.set_mode((600,600))
pygame.display.set_caption('PRUEBAS RPG')
imagen = pygame.image.load('./imagenes/personaje/caminar.png')
imagen = Imagen(imagen)
imagen.numero_variacion = 2
while True:
    
    pantalla.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        imagen.correr(event)
    
    if imagen.gastando_energia:
        imagen.energia -= 1
    
    if imagen.energia == 1:
        imagen.cansado = True    

    pantalla.blit(imagen.animacion(),(0,0))
        
    pygame.display.flip()
    pygame.time.Clock().tick(60)