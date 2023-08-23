import pygame



pygame.init()
pantalla = pygame.display.set_mode((600,600))
pygame.display.set_caption('PRUEBAS RPG')
imagen = pygame.image.load('./imagenes/personaje/caminar.png')
n = 0
f = 0
while True:
    
    pantalla.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    if n < 512 and f == 5:
        n += 64
    if n >= 512:
        n = 0
    if f < 5:
        f += 1
    else:
        f = 0
    
    imagen_recortada = imagen.subsurface(pygame.Rect(n,128,64,64))
    pantalla.blit(imagen_recortada,(0,0))

    pygame.display.flip()
    pygame.time.Clock().tick(60)