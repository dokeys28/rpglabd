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
 
            

 
class StatLevel:
    def __init__(self, nombre):
        self.nombre = nombre if nombre else None
        self.nivel = 1 
        self.exp = Xp(self)
        self._imagen = None
        self.puede_subir = True
          
    def subir(self):
        self.nivel += 1


class TotalLevel(StatLevel):
    def __init__(self, nombre, stats):
        self.stats = stats
        super().__init__(nombre)
        
    def total(self):
        x = sum([s.nivel for s in self.stats])
        self.nivel = x//len(self.stats)
             
class Stat:
    def __init__(self, stat):
        self.stat = stat
        self.nombre = self.stat.nombre
        self.valor = 0
        self.buffs = 0
        self.valor_base = self.buffs + self.valor + (self.stat.nivel * 10)
    
    def actualizar(self):
        self.valor_base = self.buffs + self.valor + (self.stat.nivel * 10)
    
    def aumentar(self, cantidad):
        self.valor += cantidad 
           
    def buff(self, cantidad):
        self.buffs += cantidad    
    
        
class Stats:
    def __init__(self, juego):
        self.juego = juego
        self.visible = False
        #STATS LEVELS
        self.ataque_level = StatLevel('Ataque')
        self.defensa_level = StatLevel('Defensa')
        self.arqueria_level = StatLevel('Arqueria')
        self.magia_level = StatLevel('Magia')
        self.stats_levels = [self.ataque_level, self.defensa_level, self.arqueria_level, self.magia_level]
        #TOTAL
        self.level = TotalLevel('Total Level',self.stats_levels)
        #STATS
        self.ataque = Stat(self.ataque_level)
        self.defensa = Stat(self.defensa_level)
        self.arqueria = Stat(self.arqueria_level)
        self.magia = Stat(self.magia_level)
        self.stats = [self.ataque, self.defensa, self.arqueria, self.magia]
    
    def mostrar_stats_levels(self):
        for i, s in enumerate(self.stats_levels):
            s.exp.actualizar()
            self.juego.pantalla.blit(FUENTES.STATS.value.render(f'{s.nombre}: {s.nivel}  Exp: {s.exp.valor} // Exp Siguiente: {s.exp.exp_siguiente_nivel} // Exp Restante: {s.exp.exp_restante}',True,(0,0,0)), (0, (i  * 32)+ 500 ))
            self.juego.pantalla.blit(FUENTES.STATS.value.render(f'{self.level.nombre}: {self.level.nivel}',True,(0,0,0)), (0, ((len(self.stats_levels))* 32)+500))
    
    def mostrar_stats(self):
        for i, s in enumerate(self.stats):
            s.actualizar()
            self.juego.pantalla.blit(FUENTES.STATS.value.render(f'{s.nombre}: {s.valor_base}',True,(0,0,0)), (ANCHO_PANTALLA - 500, (i  * 32)+ 500))