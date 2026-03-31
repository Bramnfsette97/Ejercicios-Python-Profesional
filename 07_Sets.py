### Sets ###
# Un set es una colección de elementos únicos, sin orden específico y mutable. Se utilizan para almacenar elementos no repetidos y realizar operaciones matemáticas como la unión, intersección y diferencia.   

my_set = set()  # Crear un set vacío
my_other_set = {}  # Esto no crea un set, sino un diccionario vacío. Para crear un set con elementos, se puede usar la función set() o las llaves {} con elementos separados por comas.

print(type(my_set))  # <class 'set'>

my_other_set = {"Brais", "Moure", 35} # Crear un set con elementos
print(type(my_other_set))  # <class 'set'>

print(len(my_other_set))  # 3


### print(my_other_set[0])  # Esto no es posible, los sets no tienen índices

my_other_set.add("MoureDev")  # Agregar un elemento al set
print(my_other_set)  # {'Brais', 'Moure', 35, 'MoureDev'}

### Un set no es una estructura de datos ordenada, por lo que no se puede acceder a sus elementos mediante índices. Sin embargo, se pueden realizar operaciones como la unión, intersección y diferencia entre sets.

### Un set no permite elementos duplicados, por lo que si intentamos agregar un elemento que ya existe en el set, no se agregará nuevamente.

###Verificar si un elemento está en el set
print("Moure" in my_other_set)  # True
print("Mourinho" in my_other_set)  # False

### Eliminar un elemento del set
my_other_set.remove("Moure")  # Eliminar un elemento del set
print(my_other_set)  # {'Brais', 35, 'MoureDev'}

### Eliminar todos los elementos del set
my_other_set.clear()  
print(my_other_set)  # set()

### Eliminar el set completamente en lugar de solo vaciarlo
del my_other_set 
### print(my_other_set)  # Esto generará un error, ya que el set ha sido eliminado.

### Convertir un set a una lista, no es recomendable, ya que los sets no tienen un orden específico, por lo que la lista resultante puede tener un orden diferente cada vez que se ejecute el código. Sin embargo, si se desea convertir un set a una lista, se puede usar la función list().
my_set = {"Brais", "Moure", 35}
my_list = list(my_set) 
print(my_list)  # ['Brais', 'Moure', 35]

### Unión de sets 
my_other_set = {"Kotlin", "Swift", "Python"}
my_new_set = my_set.union(my_other_set)  
print(my_new_set)  # {'Brais', 'Moure', 35, 'Kotlin', 'Swift', 'Python'}

### Diferencia de sets
print(my_new_set.difference(my_set))  # {'Kotlin', 'Swift', 'Python'} - Elementos que están en my_new_set pero no en my_set 

### Intersección de sets
print(my_new_set.intersection(my_set))  # {'Brais', 'Moure', 35} - Elementos que están en ambos sets

### Diferencia simétrica de sets
print(my_new_set.symmetric_difference(my_set))  # {'Kotlin', 'Swift', 'Python'} - Elementos que están en my_new_set o en my_set pero no en ambos

### Subconjuntos y superconjuntos
print(my_set.issubset(my_new_set))  # True - my_set es un subconjunto de my_new_set
print(my_new_set.issuperset(my_set))  # True - my_new_set es un superconjunto de my_set 

### Copiar un set 
my_copied_set = my_set.copy() 
print(my_copied_set)  # {'Brais', 'Moure', 35} - my_copied_set es una copia de my_set