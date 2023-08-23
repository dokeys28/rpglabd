import pygame




pygame.init()
pantalla = pygame.display.set_mode((600,600))
pygame.display.set_caption('PRUEBAS RPG')

while True:
    
    pantalla.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    

    #pantalla.blit(imagen.animacion(),(0,0))
        
    pygame.display.flip()
    pygame.time.Clock().tick(60)