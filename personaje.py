class Personaje:
    def __init__(self):
        #implementar elegir nombre en configuraciones
        self.nombre: str
        #definir estilo si es mago, melee, ranged
        self.estilo: str
        #para cada estilo definir una subcategoria
        self.sub_categoria: str
        self.vida: int
        
        #posicion
        self.x: int
        self.y: int
        self.posicion: list

        #imagen dialogo
        self.imagen_dialogo: str
        
        #genero
        self.sexo: str
        
        #habilidades
        self.habilidades: list
        
    #actualiza posicion    
    def actualizar_posicion(self):
        self.posicion = [self.x, self.y]
        return self.posicion
    
    

