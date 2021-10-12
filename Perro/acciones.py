from random import choice
from time import sleep

def dormir(self):

	self.energia += 20
	self.hambre -= 5
	self.felicidad -= 2

	print("Durmiendo...")
	sleep(3)

def pasear(self):

	self.energia -= 5
	self.hambre -= 5
	self.felicidad += 8

	print("Caminando...")
	sleep(3)

def jugar(self, juguetes):

	self.energia -= 8
	self.felicidad += 10

	juguete = (input("Usar juguete SI|NO: ")).lower()

	if juguete == "si":
		juguete = (input("Pelota|Soga|Muñeco: ")).lower()

		if juguetes[juguete] == "si":
			print(f"Jugando con {juguete}...")
			sleep(3)
		else:
			print("No tienes ese juguete")
			sleep(2)

	elif juguete == "no":		
		print("Jugando...")
		sleep(3)

def truco(self):

	self.energia -= 8
	self.hambre -= 6
	self.felicidad += 15
	self.exp += 1

	trucos = ["Dar la vuelta...", "Pedir..."]
	truco = choice(trucos)
	
	print(truco)
	sleep(3)

	return trucos

def nuevos_trucos(self, trucos):

	nuevos_trucos = ["Pararse en dos patas...", "Dar la pata...", "Contar...", "Hacerse el muerto..."]
			
	if self.exp % 5 == 0:

		nuevo_truco = choice(nuevos_trucos)
		trucos.append(nuevo_truco)
		nuevos_trucos.remove(nuevo_truco)
			
		print(f"Aprendio a {nuevo_truco}")
		sleep(2)