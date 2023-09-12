from constantes import *

class Xp:
    def __init__(self, stat) -> None:
        self.valor_base = 100
        self.CONSTANTE = 25
        self.valor = 0
        self.exp_siguiente_nivel = self.valor_base + self.CONSTANTE
        self.exp_maxima = self.exp_siguiente_nivel * NIVEL_MAXIMO
        self.exp_restante = self.exp_siguiente_nivel - self.valor_base
        self.stat = stat

    def aumentar(self, cantidad):
        suma = self.valor + cantidad
        if suma < self.exp_maxima:
            self.valor = suma
        else:
            self.valor = self.exp_maxima - 1

    
    def siguiente(self):
        self.exp_siguiente_nivel = (self.valor_base + self.CONSTANTE) * self.stat.nivel
        
    def verificar(self):
        if self.valor >= self.exp_siguiente_nivel:
            self.stat.subir()
            self.valor = 0
            self.siguiente()
    def actualizar(self):
        self.exp_restante = self.exp_siguiente_nivel - self.valor
        self.verificar()
 
            

 
class Stat:
    def __init__(self, nombre):
        self.nombre = nombre if nombre else None
        self.nivel = 1 
        self.exp = Xp(self) 
        self._imagen = None
        self.puede_subir = True
          
    def subir(self):
        self.nivel += 1


class TotalLevel(Stat):
    def __init__(self, nombre, stats):
        self.stats = stats
        super().__init__(nombre)
        
    def total(self):
        x = sum([s.nivel for s in self.stats])
        self.nivel = x//len(self.stats)
             
        
        
class Stats:
    def __init__(self, juego):
        self.juego = juego
        self.ataque = Stat('Ataque')
        self.defensa = Stat('Defensa')
        self.arqueria = Stat('Arqueria')
        self.magia = Stat('Magia')
        self.stats = [self.ataque, self.defensa, self.arqueria, self.magia]
        self.level = TotalLevel('Level',self.stats)
        self.visible = False
    
    def mostrar_stats(self):
        for i, s in enumerate(self.stats):
            s.exp.actualizar()
            self.juego.pantalla.blit(FUENTES.STATS.value.render(f'{s.nombre}: {s.nivel}  Exp:{s.exp.valor}//{s.exp.exp_siguiente_nivel}//{s.exp.exp_restante}',True,(0,0,0)), (0, i * 32))
            self.juego.pantalla.blit(FUENTES.STATS.value.render(f'{self.level.nombre}: {self.level.nivel}',True,(0,0,0)), (0, (len(self.stats) + 1)* 32))
            