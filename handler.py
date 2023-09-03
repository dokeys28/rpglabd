class Handler:
    def __init__(self):
        self.evento = None

    #cuando el juego sea una clase
    # def __init__(self, juego):
    #     self.juego = juego
    #     self.evento = None  
    
    # def actualizar(self):
    #     self.evento = self.juego.evento
    
    def actualizar(self, evento):
        self.evento = evento
        
    def obtener_evento(self):
        return self.evento