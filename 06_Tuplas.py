### Tuplas ### 

# Las tuplas son similares a las listas, pero son inmutables, lo que significa que no se pueden modificar después de su creación. Se definen utilizando paréntesis ().

my_tuple = tuple() # Tupla vacía
my_other_tuple = () # Otra forma de crear una tupla vacía

my_tuple = (35, 1.77, "Brais", "Moure", "Brais") # Tupla con diferentes tipos de datos
print(my_tuple) # Imprime la tupla completa

print(my_tuple[0]) # Imprime el primer elemento de la tupla

print(my_tuple.count("Brais")) # Imprime el número de veces que aparece "Brais" en la tupla 
print(my_tuple.index("Moure")) # Imprime el índice de la primera aparición de "Moure" en la tupla

# my_tuple[1] = 1.80 # Esto generará un error porque las tuplas son inmutables

del my_tuple # Elimina la tupla de la memoria
print(my_tuple) # Esto generará un error porque la tupla ha sido eliminada