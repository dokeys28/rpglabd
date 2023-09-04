class Updater:
    def __init__(self, juego):
        self.juego = juego
        
    def actualizar_todo(self):
        self.juego.personaje.actualizar()
        self.juego.handler.actualizar()
        self.juego.interfaz.actualizar()