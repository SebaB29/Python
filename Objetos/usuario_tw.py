import datetime

class TwitterUser:
    def __init__(self, usuario):
        self.nombre_usuario = usuario
        self.seguidos = []
        self.tuits = []

    def tweet(self, mensaje):
        if len(mensaje) > 280:
            raise Exception("Sobrepasa el limite de caracteres")
        self.tuits.append((datetime.datetime.now(), mensaje))

    def follow(self, otro_usuario):
        if not otro_usuario in self.seguidos:
            self.seguidos.append(otro_usuario)

    def get_timeline(self):
        tuits = []
        for usuario in self.seguidos:
            for tuit in usuario.tuits:
                tuits.append(tuit)

        return tuits