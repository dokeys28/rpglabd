import pygame
from constantes import *
from interfaz import Barra
from vitalidad import Energia, Vida
from imagen import Imagen

class Personaje(pygame.sprite.Sprite):
    def __init__(self):
        #implementar elegir nombre en configuraciones
        self.nombre: str
        #definir clase si es mago, melee, ranged
        self.clase: str
        #para cada clase definir una subcategoria
        self.sub_categoria: str
        #vida
        self.vida = Vida(VIDA_MAXIMA, self)
        barra_vida = Barra(self.vida, (0, POSICION_BARRA_VIDA))
        #energia
        self.energia = Energia(ENERGIA_MAXIMA, self)
        barra_energia = Barra(self.energia, (0, POSICION_BARRA_ENERGIA))
        
        #barras
        self.barras_vitalidad = [barra_vida, barra_energia]
        
        
         
        #posicion
        self.posicion = pygame.math.Vector2()
        self.x = self.posicion.x
        self.y = self.posicion.y
        self.direccion = [0,0] #corregir realmente no es 0,0
        
        #sprite
        self.imagen = Imagen(pygame.image.load('./imagenes/personaje/caminar.png'),self)
        #estado
        self.estado = 'quieto'
        self.saltando = False
        self.gastando_energia = False
        self.cansado = False
        self.regenerandose = False
        self.caminando = False
        self.camina_derecha = False
        self.camina_izquierda = False
        self.camina_arriba = False
        self.camina_abajo = False
        self.corriendo = False
        self.velocidad = pygame.math.Vector2()
              
        #imagenes
        self.imagenes: list

        #imagen dialogo
        self.imagen_dialogo: str
                       
        #genero
        self.sexo: str
        
        #habilidades
        self.habilidades: list
        self.dic_direccion = {
        'arriba': [0,-1],
        'abajo' :[0,1],
        'derecha' : [1,0],
        'izquierda' : [-1,0]}
        self.dirigiendose = 'abajo'

                 
        
        
    
    #cansar
    def cansar(self):
        if self.energia.cantidad > 50:
            self.cansado = False
            self.frame_rate = FRAME_RATE_CAMINAR
    
    def handler(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if self.caminando:
                    self.corriendo = True
                
            if event.key == pygame.K_UP:
                self.camina_arriba = True

                
            if event.key == pygame.K_DOWN:
                self.camina_abajo = True


            if event.key == pygame.K_LEFT:
                self.camina_izquierda = True


            if event.key == pygame.K_RIGHT:
                self.camina_derecha = True


        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                self.corriendo = False
                
            if event.key == pygame.K_UP:
                self.camina_arriba = False
   
                
            if event.key == pygame.K_DOWN:
                self.camina_abajo = False


            if event.key == pygame.K_LEFT:
                self.camina_izquierda = False


            if event.key == pygame.K_RIGHT:
                self.camina_derecha = False
    
    
    #actualizaciones
    def actualizar(self, evento):
        self.handler(evento)
        self.actualizar_posicion()
        self.imagen.actualizar()
        self.actualizar_estados()
        
    
    def actualizar_estados(self):
        if self.energia.cantidad <= 1:
            self.cansado = True
        if self.energia.cantidad >ENERGIA_MAXIMA//2:
            self.cansado = False
        if self.energia.cantidad < ENERGIA_MAXIMA:
            self.regenerandose = True
        
        
        #caminando
        if self.camina_arriba:
            self.caminando = True
            self.arriba()
            self.mover()
        elif self.camina_abajo:
            self.caminando = True
            self.mover()
            self.abajo()
        elif self.camina_izquierda:
            self.caminando = True
            self.mover()
            self.izquierda()
        elif self.camina_derecha:
            self.caminando = True
            self.mover()
            self.derecha()
        else:
            self.caminando = False
            self.estado = 'quieto'
            
                
        #corriendo
        if self.corriendo:
            self.correr()
            if self.energia.cantidad > 1 and not self.cansado:
                self.gastando_energia = True
            else:
                self.corriendo = False
        else:
            self.velocidad = pygame.math.Vector2(0,0)
            self.gastando_energia = False
         
        if self.estado == 'quieto':
            self.direccion = pygame.math.Vector2(0,0)        
            self.velocidad = pygame.math.Vector2(0,0)
            self.imagen.numero_imagen = 0
                      
        #gastar energia
        if self.gastando_energia:
            self.regenerandose = False
            self.energia.gastar()

        #regenerarse
        if self.regenerandose:
            self.gastando_energia = False
            self.energia.regenerar()
    
    #actualiza posicion    
    def actualizar_posicion(self):
        self.posicion += (self.direccion + self.velocidad )* K_VELOCIDAD
    
           
    #direccion
    def mover(self):
        self.caminando = True
        self.estado = 'caminando'
        
     
    def arriba(self):
        self.direccion = self.dic_direccion['arriba']
        self.dirigiendose = 'arriba'
    def abajo(self):
        self.direccion = self.dic_direccion['abajo']
        self.dirigiendose = 'abajo'
    def izquierda(self):
        self.direccion = self.dic_direccion['izquierda']
        self.dirigiendose = 'izquierda'
    def derecha(self):
        self.dirigiendose = 'derecha'
        self.direccion = self.dic_direccion['derecha']

    def correr(self):
        if self.caminando:
            self.estado = 'corriendo'
            if self.dirigiendose == 'arriba':
                self.velocidad = pygame.math.Vector2(0, VELOCIDAD_JUGADOR * -1)
            if self.dirigiendose == 'abajo':
                self.velocidad = pygame.math.Vector2(0, VELOCIDAD_JUGADOR)
            if self.dirigiendose == 'derecha':
                self.velocidad = pygame.math.Vector2(VELOCIDAD_JUGADOR, 0)
            if self.dirigiendose == 'izquierda':
                self.velocidad = pygame.math.Vector2(VELOCIDAD_JUGADOR * -1, 0)
            


    ###debo implementar direccion
    #direccion

        
    #obtener atributos actualizados
    def obtener_rect(self):
        return self.imagen.rect
    
    def obtener_sprite(self):
        return self.imagen.sprite
    

