# Variables

my_variable = "My String variable"
print(my_variable)

my_int_variable = 5
print(my_int_variable) 

my_boolean_variable = False   
print(my_boolean_variable)

#Concatenación de variables en un print
print(my_variable, my_int_variable, my_boolean_variable)
print("Este es el valor de: ", my_boolean_variable)

# Algunas funciones del sistema
print(len(my_variable)) #Cantidad de caracteres de la variable

# Variables en una sola línea (CUIDADO: No es recomendable)
name, surname, alias, age = "Brais", "Moure", "MoureDev", 35
print("Me llamo:", name, surname, ". Mi edad es", age, "años. Y mi alias es:", alias)

# Inputs (Entrada de datos por teclado)
"""
name = input("¿Cuál es tu nombre? ")
age = input("¿Cuál es tu edad? ")

print(name)
print(age)
"""
# Cambiamos su tipo de dato
name = 35
age = "Brais"
print(name)
print(age)

#¿Forzar el tipo de dato de una variable?
address: str = "Mi direccion"
address = 32
print(type(address))