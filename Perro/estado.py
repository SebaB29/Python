def estado(self):

	print(f"Energía: {self.energia} | Hambre: {self.hambre} | Felicidad: {self.felicidad} | Exp: {self.exp}\n\
Comprar | Alimentar | Jugar | Pasear | Truco | Dormir")

	if 0 < self.hambre <= 30:
		print("Tu perro tiene hambre")

	if 0 < self.energia <= 30:
		print("Tu perro esta cansado")

	if (0 < self.felicidad <= 20) and (self.hambre > 0 and self.energia > 0):
		print("Tu perro esta triste")

	if self.hambre <= 0:
		print("Tu perro murió de hambre")	
	elif self.energia <= 0:
		print("Tu perro murió de cansancio")