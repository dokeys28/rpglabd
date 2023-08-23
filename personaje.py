class Personaje:
    def __init__(self):
        #implementar elegir nombre en configuraciones
        self.nombre: str
        #definir estilo si es mago, melee, ranged
        self.estilo: str
        #para cada estilo definir una subcategoria
        self.sub_categoria: str
        #desarrollar modo batalla por turnos
        self.vida: int
        #personaje ranged empiece tirando piedras
        
        #posicion
        self.x: int
        self.y: int
        self.posicion: list

        #imagen dialogo
        self.imagen_dialogo: str
        
        
        #genero
        self.sexo: str
        
    #actualiza posicion    
    def actualizar_posicion(self):
        self.posicion = [self.x, self.y]
        return self.posicion
    
    

