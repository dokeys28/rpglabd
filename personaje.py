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