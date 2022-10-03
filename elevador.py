'''
elevador: 
Descripcion:Funcion que ayuda a administrar el recorrido de un elevador de manera eficiente
respetando la dirreccion en la que este se dirige 
Input: lista de enteros que representan los pisos, un entero que representa el piso actual, 
un diccionario donde el valor es un nuevo piso ingresado y la clave es el piso donde se ingreso este nuevo piso"
Output:Recorrido del ascensor impreso en consola
Autor: Santiago Collantes Zuluaga
Fecha: 03/10/2022
'''
def elevator(arrP, act, mapP):
	subiendo =False #Declaramos variables que nos serán utiles para indicar la dirección del elevador
	bajando = False

	if act in mapP: # Nos aseguramos de añadir cualquier piso ingresado el primer piso del arreglo
		arrP.append(mapP[act])
		mapP.pop(act)

	nearest = arrP[min(range(len(arrP)), key = lambda i: abs(arrP[i]-act))] # hallamos el piso mas cercano al piso inicial para determinar
																			# la direccion que va a tomar en un inicio

	if  act < nearest: # Si el piso es mayor o menor al actual decidira nuestra direccion inicial
		subiendo = True
	else:
		bajando = True 

	print("Elevador en piso",act)

	while(len(arrP)>=1):# Iniciamos un ciclo mientras haya piso pendientes por visitar

		if(len(arrP)==1):# Caso base: solo hay un piso pendiente
			if(act == arrP[0]):# Si este piso es el mismo en el que nos encontramos
				break
			if act < arrP[0] :
				print("Elevador subiendo")
				print ("Elevador en piso ", arrP[0])
				print( "Elevador se detiene")
			else:
				print("Elevador bajando")
				print ("Elevador en piso ", arrP[0])
				print( "Elevador se detiene")
			break
		
		if subiendo:# Si la direccion del elevador es hacia arriba nuestro proximo piso será decidido por cual es el piso mas cercano por encima de este	
			if act > max(arrP):# Si nos encontramos en el ultimo piso de subida, cambiamos a bajada
				print("Elevador bajando")
				subiendo = False
				bajando = True
				nearest = max([i for i in arrP if act > i])
			else:
				print("Elevador subiendo")
				nearest = min([i for i in arrP if act < i])#hallamos piso mas cercano al actual por encima de este

		else:
			if act < min(arrP):# Si nos encontramos en el ultimo piso de bajada, cambiamos a subida
				print("Elevador subiendo")
				subiendo = True
				bajando = False
				nearest = min([i for i in arrP if act < i])
			else:
				print("Elevador bajando")
				nearest = max([i for i in arrP if act > i])#hallamos piso mas cercano al actual por debajo de este

		act = nearest # el nuevo piso actual antes de reiniciar el ciclo será el mas proximo hallado previamente
		arrP.remove(nearest) # lo removemos del arreglo al ser ya visitado

		if act in mapP: # chequeamos si en el piso actual se ingresa un nuevo piso y lo añadimos al arreglo
			arrP.append(mapP[act])
			print("Piso ingresado", mapP[act])
			mapP.pop(act)# los sacamos del diccionario de pisos con pisos ingresados

		print ("Elevador en piso ", act)
		print( "Elevador se detiene")

'''
elevador2: Funcion similar a elevador, pero esta acepta input del usuario en cada piso
Input: lista de enteros que representan los pisos, un entero que representa el piso actual
Output:Recorrido del ascensor impreso en consola
Autor: Santiago Collantes Zuluaga
Fecha: 03/10/2022
'''

def elevator2(arrP, act):
	subiendo =False #Declaramos variables que nos serán utiles para indicar la dirección del elevador
	bajando = False

	print("Piso:")# Nos aseguramos de añadir cualquier piso ingresado el primer piso del arreglo
	new_P = input()
	if new_P:
		arrP.append(int(new_P))
	else: 	
	 	pass 
	

	nearest = arrP[min(range(len(arrP)), key = lambda i: abs(arrP[i]-act))] # hallamos el piso mas cercano al piso inicial para determinar
																			# la direccion que va a tomar en un inicio

	if  act < nearest: # Si el piso es mayor o menor al actual decidira nuestra direccion inicial
		subiendo = True
	else:
		bajando = True 

	print("Elevador en piso",act)

	while(len(arrP)>=1):# Iniciamos un ciclo mientras haya piso pendientes por visitar

		if(len(arrP)==1):# Caso base: solo hay un piso pendiente
			if(act == arrP[0]):# Si este piso es el mismo en el que nos encontramos
				break
			if act < arrP[0] :
				print("Elevador subiendo")
				print ("Elevador en piso ", arrP[0])
				print( "Elevador se detiene")
			else:
				print("Elevador bajando")
				print ("Elevador en piso ", arrP[0])
				print( "Elevador se detiene")
			break

		if subiendo:# Si la direccion del elevador es hacia arriba nuestro proximo piso será decidido por cual es el piso mas cercano por encima de este	
			if act > max(arrP):# Si nos encontramos en el ultimo piso de subida, cambiamos a bajada
				print("Elevador bajando")
				subiendo = False
				bajando = True
				nearest = max([i for i in arrP if act > i])
			else:
				print("Elevador subiendo")
				nearest = min([i for i in arrP if act < i])#hallamos piso mas cercano al actual por encima de este

		else:
			if act < min(arrP):# Si nos encontramos en el ultimo piso de bajada, cambiamos a subida
				print("Elevador subiendo")
				subiendo = True
				bajando = False
				nearest = min([i for i in arrP if act < i])
			else:
				print("Elevador bajando")
				nearest = max([i for i in arrP if act > i])#hallamos piso mas cercano al actual por debajo de este

		act = nearest # el nuevo piso actual antes de reiniciar el ciclo será el mas proximo hallado previamente
		arrP.remove(nearest) # lo removemos del arreglo al ser ya visitado

		print("Piso:")# Nos aseguramos de añadir cualquier piso ingresado el primer piso del arreglo
		new_P = input()
		if new_P:
			arrP.append(int(new_P))
		else: 	
	 		pass

		print ("Elevador en piso ", act)
		print( "Elevador se detiene")

'''
Elevador3: Propuesta de funcion para el ultimo bonus de la entrevista, que por tiempo no pudo ser completado
def elevator3(arrP, act, mapP):

	subiendo = True
	bajando = False

	el1=[subiendo,act]
	el2=[subiendo,act]


	if act in mapP: # Nos aseguramos de añadir cualquier piso ingresado el primer piso del arreglo
		arrP.append(mapP[act])
		mapP.pop(act)

	nearest = arrP[min(range(len(arrP)), key = lambda i: abs(arrP[i]-act))] # hallamos el piso mas cercano al piso inicial para determinar
																			# la direccion que va a tomar en un inicio

	if  act < nearest: # Si el piso es mayor o menor al actual decidira nuestra direccion inicial		
		el1[0] = subiendo
	else:
		el1[0] = bajando

	print("Elevador 1 en piso",el1[1])
	print("Elevador 2 en piso",el2[1])

	while(len(arrP)>=1):# Iniciamos un ciclo mientras haya piso pendientes por visitar

		if(len(arrP)==1):# Caso base: solo hay un piso pendiente
			if( el1[1] == arrP[0] or el2[1] == arrP[0] ):# Si este piso es el mismo en el que nos encontramos
				break
			if(abs(el1[1]- arrP[0])<= abs(el2[1]- arrP[0]):
				if(el1[1] < arrP[0]):
					print("Elevador 1 subiendo")
					print ("Elevador1 en piso ", arrP[0])
					print( "Elevador1 se detiene")
				else:
					print("Elevador1 bajando")
					print ("Elevador1 en piso ", arrP[0])
					print( "Elevador1 se detiene")
			else:
				if(el2[1] > arrP[0]):
					print("Elevador2 bajando")
					print("Elevador2 en piso ", arrP[0])
					print( "Elevador2 se detiene")
				else:
					print("Elevador2 bajando")
					print("Elevador2 en piso ", arrP[0])
					print( "Elevador2 se detiene")
			break
		
		if (el1[0]==subiendo):
			if(abs(el1[1]- arrP[0])<= abs(el2[1]- arrP[0]) or el2[0]!= el2[0]):# Si la direccion del elevador es hacia arriba nuestro proximo piso será decidido por cual es el piso mas cercano por encima de este
				print("Elevador1 subiendo")	
				if el1[1] > max(arrP):# Si nos encontramos en el ultimo piso de subida, cambiamos a bajada
					el1[0]= bajando
					nearest = max([i for i in arrP if act > i])
				else:
					nearest = min([i for i in arrP if act < i])#hallamos piso mas cercano al actual por encima de este
			else:

		else:
			if()
			print("Elevador bajando")
			if act < min(arrP):# Si nos encontramos en el ultimo piso de bajada, cambiamos a subida
				subiendo = True
				bajando = False
				nearest = min([i for i in arrP if act < i])
			else:
				nearest = max([i for i in arrP if act > i])#hallamos piso mas cercano al actual por debajo de este

		act = nearest # el nuevo piso actual antes de reiniciar el ciclo será el mas proximo hallado previamente
		arrP.remove(nearest) # lo removemos del arreglo al ser ya visitado

		if act in mapP: # chequeamos si en el piso actual se ingresa un nuevo piso y lo añadimos al arreglo
			arrP.append(mapP[act])
			print("Piso ingresado", mapP[act])
			mapP.pop(act)# los sacamos del diccionario de pisos con pisos ingresados

		print ("Elevador en piso ", act)
		print( "Elevador se detiene")

'''
def main():
	print("Arreglo de pisos:")
	arrP = list(map(int, input().split()))
	print("Piso inicial de ejecución:")
	actP = int(input())
	print("Pisos ingresados:")
	mapP = input()
	dic = dict(subString.split(":") for subString in mapP.split())
	dic = {int(k):int(v) for k,v in dic.items()}
	print("Prueba de Elevador:")
	elevator(arrP,actP,dic)
	print("Prueba de Elevador 2 :")
	elevator2(arrP,actP)

main()