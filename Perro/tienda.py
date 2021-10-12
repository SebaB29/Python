from os import system

def comprar(comida, juguetes):

	comprado = ""

	while not comprado:

		system("cls")

		comprar = (input("Que quiere comprar? Alimentos | Juguetes : ")).lower()

		if comprar == "alimento":
			print(f"Carne: {comida['carne']['cantidad']}|Agua: {comida['agua']['cantidad']}|Huesos: {comida['hueso']['cantidad']}")

			producto = (input("Que queres comprar?: ")).lower()

			if producto in comida.keys():
				cantidad = input("Cuánto quieres comprar?: ")
				if cantidad.isdecimal():
					comida[producto]['cantidad'] += int(cantidad)
					comprado = producto


		if comprar == "juguete":
			print("Pelota | Soga | Muñeco")

			producto = (input("Que quieres comprar?: ")).lower()

			if producto in juguetes.keys():
				juguetes[producto] = "si"
				comprado = producto