class FacebookUser:
    def __init__(self, usuario):
        self.nombre_usuario = usuario
        self.muro = []
        self.amigos = []

    def pubilcar(self, post):
        self.muro.append(post)

    def agregar_amigo(self, otro_usuario):
        self.amigos.append(otro_usuario.nombre_usuario)
        otro_usuario.amigos.append(self.nombre_usuario)

    def mostrar_amigos(self):
        return f"Amigos: {self.amigos}"

    def mostrar_muro(self):
        for post in range(len(self.muro)-1, -1, -1):
            print(self.muro[post])

    def __str__(self):
        return f"Usuario: {self.nombre_usuario}"

usuario1 = FacebookUser("Sebastian")
usuario2 = FacebookUser("Stephy")

post1 = "Que hermoso día!!!!!!!"
post2 = "Ya la cagué"
post3 = "El peor día de mi vida"

usuario1.pubilcar(post1)
usuario1.pubilcar(post2)
usuario1.pubilcar(post3)

print(usuario1)
# usuario1.mostrar_muro()
usuario1.agregar_amigo(usuario2)
print(usuario1.mostrar_amigos())
print(usuario2.mostrar_amigos())