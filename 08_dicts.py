### Diccionarios ###

my_dict = dict()  # Crear un diccionario vacío
print(type(my_dict))  # <class 'dict'>

my_other_dict = {}  # Otra forma de crear un diccionario vacío
print(type(my_other_dict))  # <class 'dict'>

my_other_dict = {"Nombre": "Brais", "Apellido": "Moure", "Edad": 35, 1:"Python"}

### Un diccionario es una colección de pares clave-valor, donde cada clave es única y se utiliza para acceder a su valor correspondiente. Las claves pueden ser de cualquier tipo de dato inmutable, como cadenas, números o tuplas, mientras que los valores pueden ser de cualquier tipo de dato, incluyendo otros diccionarios.

my_dict = {
    "Nombre": "Brais", 
    "Apellido": "Moure", 
    "Edad": 35, 
    "Lenguajes": {"Python", "Swift", "Kotlin"},
    1: 1.77
    }

print(my_other_dict)
print(my_dict)

# Longitud de un diccionario
print(len(my_other_dict))  # 4
print(len(my_dict))  # 5

# Acceder a los valores del diccionario utilizando sus claves
print(my_dict["Nombre"])  # Brais

# Modificar el valor asociado a la clave "Nombre"
my_dict["Nombre"] = "Pedro"  
print(my_dict["Nombre"])  # Pedro

# Acceder al valor asociado a la clave 1
print(my_dict[1])  # 1.77

# Agregar una nueva clave-valor al diccionario
my_dict["Calle"] = "Calle MoureDev"  
print(my_dict)

# Eliminar la clave "Calle" y su valor asociado
del my_dict["Calle"] 
print(my_dict)

# Verificar si una clave existe en el diccionario 
# El operador "in" se utiliza para verificar si una clave existe en el diccionario. Devuelve True si la clave está presente y False si no lo está.
print("Moure" in my_dict)  # False, "Moure" es un valor, no una clave
print("Apellido" in my_dict)  # True, "Apellido" es una clave
#print("Mouri" in my_dict)  # False

# Devuelve una vista de los pares clave-valor del diccionario
print(my_dict.items())  

# Devuelve una vista de las claves del diccionario
print(my_dict.keys())  

# Devuelve una vista de los valores del diccionario 
print(my_dict.values()) 

# Crea un nuevo diccionario con las claves "Nombre" y 1, y valores None
my_new_dict = my_other_dict.fromkeys(("Nombre", 1, "Piso: ")) 
print(my_new_dict)  # {'Nombre': None, 1: None, 'Piso: ': None} 

my_new_dict = dict.fromkeys(my_dict)
print(my_new_dict)  # {'Nombre': None, 'Apellido': None, 'Edad': None, 'Lenguajes': None, 1: None}

my_new_dict = dict.fromkeys(my_dict, ("Brais", "Moure"))
print(my_new_dict)  

my_new_dict = dict.fromkeys(my_dict)
print(my_new_dict)  # {'Nombre': None, 'Apellido': None, 'Edad': None, 'Lenguajes': None, 1: None}

# Crea un nuevo diccionario con las mismas claves que my_dict, pero con el valor "MoureDev" para cada clave
my_new_dict = dict.fromkeys(my_dict, "MoureDev")
print(my_new_dict)  # {'Nombre': 'MoureDev', 'Apellido': 'MoureDev', 'Edad': 'MoureDev', 'Lenguajes': 'MoureDev', 1: 'MoureDev'}

# Devuelve una vista de los valores del diccionario
my_values = my_new_dict.values()
print(type(my_values))  # <class 'dict_values'>

# Devuelve una vista de las claves del diccionario como una lista
print(list(my_new_dict))  # ['Nombre', 'Apellido', 'Edad', 'Lenguajes', 1]

# Devuelve una vista de las claves del diccionario como una tupla
print(tuple(my_new_dict))  # ('Nombre', 'Apellido', 'Edad', 'Lenguajes', 1)

# Devuelve una vista de las claves del diccionario como un conjunto
print(set(my_new_dict))  # {'Apellido', 'Nombre', 'Edad', 'Lenguajes', 1}