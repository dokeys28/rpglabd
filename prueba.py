import pygame

from personaje import Personaje



pygame.init()
pantalla = pygame.display.set_mode((600,600))
pygame.display.set_caption('PRUEBAS RPG')
personaje = Personaje()
while True:
    
    pantalla.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if personaje.caminando:
                    personaje.corriendo = True
                
            if event.key == pygame.K_UP:
                personaje.camina_arriba = True

                
            if event.key == pygame.K_DOWN:
                personaje.camina_abajo = True


            if event.key == pygame.K_LEFT:
                personaje.camina_izquierda = True


            if event.key == pygame.K_RIGHT:
                personaje.camina_derecha = True
 


        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                personaje.corriendo = False
                
            if event.key == pygame.K_UP:
                personaje.camina_arriba = False
   
                
            if event.key == pygame.K_DOWN:
                personaje.camina_abajo = False


            if event.key == pygame.K_LEFT:
                personaje.camina_izquierda = False


            if event.key == pygame.K_RIGHT:
                personaje.camina_derecha = False

            
    personaje.actualizar()

    pantalla.blit(personaje.obtener_sprite(),personaje.posicion)
    pygame.display.flip()
    pygame.time.Clock().tick(60)