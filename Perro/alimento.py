from time import sleep

def alimentar(self, comida):

	print(f"Carne: {comida['carne']['cantidad']} | Agua: {comida['agua']['cantidad']} | Huesos: {comida['hueso']['cantidad']}")

	alimento = (input("Dar...")).lower()
	
	if alimento in comida.keys() and comida[alimento]['cantidad'] > 0:
		self.hambre += comida[alimento]['aumento']
		comida[alimento]['cantidad'] -= 1
	else:
		print(f"No tienes {alimento}")
		sleep(2)