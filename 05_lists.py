### Lists ###

my_list = list() # Crea una lista vacía
my_other_list = [] # Agregar elementos a la lista

print(len(my_list)) # Imprime la longitud de la lista (0)

my_list = [35, 24, 62, 52, 30, 30, 17] # Crea una lista con elementos   

print(my_list)
print(len(my_list))

my_other_list = [35, 1.77, "Brais", "Moure"] # Crea una lista con diferentes tipos de datos

print(type(my_other_list)) # Imprime el tipo de dato de la lista (list)

print(my_other_list[0]) # Imprime el primer elemento de la lista (35)
print(my_other_list[1]) # Imprime el segundo elemento de la lista (1.77)
print(my_other_list[-1]) # Imprime el último elemento de la lista utilizando un índice negativo (-1)
print(my_other_list[-4]) # Imprime el primer elemento de la lista utilizando un índice negativo (-4)
###print(my_other_list[-5]) # Esto generará un error porque no hay un índice -5
###print(my_other_list[my_other_list.count()]) # Esto generará un error porque el índice es igual a la longitud de la lista, lo que está fuera de rango
print(my_list.count(30)) # Imprime la cantidad de elementos en la lista que son iguales a 30 (2) 

age, height, name, surname = my_other_list # Asignación múltiple de variables a los elementos de la lista
print(name) # Imprime el valor de la variable 'name' (Brais)

###age, height, name = my_other_list # Esto generará un error porque la cantidad de variables no coincide con la cantidad de elementos en la lista

print(my_list + my_other_list) # Imprime la concatenación de las dos listas

###print(my_list - my_other_list) # Esto generará un error porque no se pueden restar listas directamente. La resta de listas no está definida en Python.###

my_other_list.append("MoureDev") # Agrega un nuevo elemento al final de la lista 'my_other_list'
print(my_other_list) # Imprime la lista actualizada con el nuevo elemento

my_other_list.insert(1, "Amarillo") # Inserta un nuevo elemento en la posición 1 de la lista 'my_other_list'
print(my_other_list) # Imprime la lista actualizada con el nuevo elemento insertado

my_other_list[1] = "Azul" # Modifica el elemento en la posición 1 de la lista 'my_other_list' y lo reemplaza con "Amarillo"
print(my_other_list) # Imprime la lista actualizada después de modificar el elemento en la posición 1

my_other_list.remove("Azul") # Elimina el primer elemento que coincide con "Azul" de la lista 'my_other_list'
print(my_other_list) # Imprime la lista actualizada después de eliminar el elemento "Azul"

my_list.remove(30) # Elimina el primer elemento que coincide con 30 de la lista 'my_list'
print(my_list) # Imprime la lista actualizada después de eliminar el primer 30

my_list.pop() # Elimina el último elemento de la lista 'my_list' y lo devuelve
print(my_list) # Imprime la lista actualizada después de eliminar el último elemento

my_pop_element = my_list.pop(2) # Elimina el elemento en la posición 2 de la lista 'my_list' y lo asigna a la variable 'my_pop_element'
print(my_pop_element) # Imprime el valor del elemento eliminado
print(my_list) # Imprime la lista actualizada después de eliminar el elemento en la posición 2

del my_list[2] # Elimina el elemento en la posición 2 de la lista 'my_list' utilizando la declaración 'del'. A diferencia de 'pop', 'del' no devuelve el elemento eliminado, simplemente lo elimina de la lista.
print(my_list) # Imprime la lista actualizada después de eliminar el elemento en la posición 2 utilizando 'del'

my_new_list = my_list.copy() # Crea una copia de la lista 'my_list' y la asigna a la variable 'my_new_list'

my_list.clear() # Elimina todos los elementos de la lista 'my_list', dejándola vacía
print(my_list) # Imprime la lista vacía ([])
print(my_new_list) # Imprime la copia de la lista original antes de ser vaciada, mostrando los elementos que tenía (35, 24, 30)

my_new_list.reverse() # Invierte el orden de los elementos en la lista 'my_new_list'
print(my_new_list) # Imprime la lista 'my_new_list' con los elementos en orden inverso (30, 24, 35)

my_new_list.sort() # Ordena los elementos de la lista 'my_new_list' en orden ascendente
print(my_new_list) # Imprime la lista 'my_new_list' con los elementos ordenados (24, 30, 35)

print(my_new_list[1:2]) # Imprime una porción de la lista 'my_new_list' desde el índice 1 hasta el índice 2 (excluyendo el índice 2), lo que devuelve una nueva lista con el elemento en el índice 1 (30)

my_list = "Hola Python" # Asigna una cadena de texto a la variable 'my_list', lo que sobrescribe la lista anterior. Ahora 'my_list' es una cadena, no una lista.
print(my_list) # Imprime el valor de la variable 'my_list' (Hola Python)
print(type(my_list)) # Imprime el tipo de dato de 'my_list' (str)
