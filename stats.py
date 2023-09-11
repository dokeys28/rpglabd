from constantes import *


class Stat:
    def __init__(self, nombre):
        self.nombre = nombre if nombre else None
        self.nivel = 1 
        self.exp = 0 
        self._imagen = None
        self.nivel_maximo = 100
        self.exp_maxima = self.nivel_maximo ** POTENCIA_EXPERIENCIA_MAXIMA
        self.puede_subir = True
    
    def subir(self):
        self.nivel += 1
        
    def _experiencia_siguiente(self):
        if self.nivel < self.nivel_maximo:
            self._exp_siguiente_nivel = (self.nivel+1) ** POTENCIA_EXPERIENCIA_MAXIMA
            return self._exp_siguiente_nivel
        else:
            self.puede_subir = False
            self._exp_siguiente_nivel = self.exp_maxima
            return self._exp_siguiente_nivel
        
    
    def verificar_exp_nivel(self):
        if self.exp >= self.exp_maxima:
            print(self.exp, self.exp_maxima)
            self.puede_subir = False 
        if self.exp >= self._exp_siguiente_nivel:
            self.subir()

            
    def ganar_exp(self, cantidad_de_xp):
        if self.puede_subir:
            self._experiencia_siguiente()
            self.verificar_exp_nivel()
            suma = self.exp + cantidad_de_xp
            if suma < self.exp_maxima:
                self.exp = suma
            else:
                self.exp = self.exp_maxima
   

        
class Stats:
    def __init__(self, juego):
        self.juego = juego
        self.level = Stat('Level')
        self.ataque = Stat('Ataque')
        self.defensa = Stat('Defensa')
        self.arqueria = Stat('Arqueria')
        self.magia = Stat('Magia')
        self.visible = False
    
    def x_list(self):
        self.stats = [self.level, self.ataque, self.defensa, self.arqueria, self.magia]
        listado = []
        for i, s in enumerate(self.stats):
            listado.append((FUENTES.STATS.value.render(f'{s.nombre}: {s.nivel}',True,(0,0,0)), (0, i * 32)))
        return listado
    
    def mostrar_stats(self):
        self.juego.pantalla.blits(x for x in self.x_list())

            