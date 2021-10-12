from os import system
from estado import estado
from mochila import mochila
from tienda import comprar
from alimento import alimentar
from acciones import pasear, jugar, truco, nuevos_trucos, dormir

class Perro:

	def __init__(self, energia=100, hambre=100, felicidad=100, experiencia=0):

		self.energia = energia
		self.hambre = hambre
		self.felicidad = felicidad
		self.exp = experiencia

				
	def main(self):

		comida, juguetes = mochila()

		while self.energia > 0 and self.hambre > 0:

			system("cls")
			estado(self)

			accion = (input()).lower()
			
			if accion == "comprar":
				comprar(comida, juguetes)
			elif accion == "alimentar":
				alimentar(self, comida)
			elif accion == "pasear":
				pasear(self)
			elif accion == "jugar":
				jugar(self,juguetes)
			elif accion == "truco":
				trucos = truco(self)
				nuevos_trucos(self, trucos)
			elif accion == "dormir":
				dormir(self)

		system("cls")
		estado(self)

Perro().main()