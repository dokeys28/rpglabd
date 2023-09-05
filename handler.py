import pygame

class Controles:
    def __init__(self) -> None:
        self.derecha_presionada = False
        self.izquierda_presionada = False
        self.arriba_presionada = False
        self.abajo_presionada = False
        self.mouse_presionado = False
        self.i_presionada = False
        self.espacio_presionada = False


    
class Handler:
    def __init__(self, juego):
        self.juego = juego
        self.evento = None
        self.control = Controles()

    def actualizar(self):
        for event in pygame.event.get():
        
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            #TECLADO
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.control.arriba_presionada = True
                if event.key == pygame.K_DOWN:
                    self.control.abajo_presionada = True
                if event.key == pygame.K_LEFT:
                    self.control.izquierda_presionada = True
                if event.key == pygame.K_RIGHT:
                    self.control.derecha_presionada = True
                if event.key == pygame.K_i:
                    self.control.i_presionada = True
                if event.key == pygame.K_SPACE:
                    self.control.espacio_presionada = True
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    self.control.arriba_presionada = False
                if event.key == pygame.K_DOWN:
                    self.control.abajo_presionada = False
                if event.key == pygame.K_LEFT:
                    self.control.izquierda_presionada = False
                if event.key == pygame.K_RIGHT:
                    self.control.derecha_presionada = False
                if event.key == pygame.K_i:
                    self.control.i_presionada = False
                if event.key == pygame.K_SPACE:
                    self.control.espacio_presionada = False
           
            #MOUSE
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.control.mouse_presionado = True
                       
            if event.type == pygame.MOUSEBUTTONUP:
                self.control.mouse_presionado = False