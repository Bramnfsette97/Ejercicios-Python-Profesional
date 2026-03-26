### Strings ### 

my_string = "Mi String"
my_other_string = "Mi otro String"

print(len(my_string)) # len() es una función que devuelve la longitud de un objeto, en este caso, la cantidad de caracteres que tiene la cadena de texto.
print(len(my_other_string))

print(my_string + " " + my_other_string)

my_new_line_string = "Este es un String\ncon salto de línea" # \n es un carácter de escape que se utiliza para indicar un salto de línea en una cadena de texto. Cuando se encuentra \n en una cadena, el texto después de este carácter se mostrará en una nueva línea al imprimir la cadena.
print(my_new_line_string)

my_tab_string = "<\tEste es un String con tabulación" # \t es un carácter de escape que se utiliza para indicar una tabulación en una cadena de texto.
print(my_tab_string)

my_scape_string = "\tEste es un string \n escapado" # En este caso, se combinan ambos caracteres de escape, \t para la tabulación y \n para el salto de línea. Al imprimir my_scape_string, el texto se mostrará con una tabulación al principio y luego se dividirá en dos líneas debido al salto de línea.
print(my_scape_string)

# Formateo de Strings #

name, surname, edad = "Brais", "Moure", 35
print("Mi nombre es {} {} y mi edad es {}".format(name, surname, edad)) # El método format() se utiliza para formatear cadenas de texto. Permite insertar valores en una cadena utilizando marcadores de posición, que se representan con %s para cadenas, %d para enteros, etc. En este caso, los valores de name, surname y edad se insertan en la cadena en los lugares correspondientes a los marcadores de posición.
print("Mi nombre es %s %s y mi edad es %d" %(name, surname, edad)) # El operador % también se puede utilizar para formatear cadenas de texto. Funciona de manera similar al método format(), pero utiliza un formato diferente para los marcadores de posición. En este caso, los valores de name, surname y edad se insertan en la cadena utilizando el operador %.

print(f"Mi nombre es {name} {surname} y mi edad es {edad}") # Las f-strings (formatted string literals) son una forma más moderna y concisa de formatear cadenas de texto en Python. Permiten insertar expresiones directamente dentro de la cadena utilizando llaves {}. En este caso, los valores de name, surname y edad se insertan directamente en la cadena utilizando las llaves. (Mejor opción para formatear cadenas de texto, ya que es más legible y fácil de usar que el método format() y el operador %).

### Desempaquetado de caracteres ### 
language = "python"
a, b, c, d, e, f = language
print(a)
print(b)

### División de Strings ###

language_slice = language[1:3] # El slicing es una técnica que se utiliza para obtener una parte de una cadena de texto. En este caso, se obtiene una subcadena que va desde el índice 1 hasta el índice 3 (excluyendo el índice 3) de la cadena language. El resultado será "yt".
print(language_slice)

language_slice = language[1:] # En este caso, se obtiene una subcadena que va desde el índice 1 hasta el final de la cadena language. El resultado será "ython".
print(language_slice)

language_slice = language[-2] # En este caso, se obtiene el carácter que se encuentra en el índice -2 de la cadena language. El índice -2 se refiere al segundo carácter desde el final de la cadena. En este caso, el resultado será "o".
print(language_slice)

### Reverse String ###
reverse_language = language[::-1] # En este caso, se obtiene una subcadena que va desde el principio hasta el final de la cadena language, pero con un paso de -1. Esto significa que se recorre la cadena en orden inverso, lo que da como resultado la cadena "nohtyP".
print(reverse_language)

language_slice = language[1:2:4] # En este caso, se obtiene una subcadena que va desde el índice 1 hasta el índice 2 (excluyendo el índice 2) de la cadena language, con un paso de 4. Sin embargo, dado que el rango especificado es muy pequeño y el paso es mayor que la longitud del rango, el resultado será una cadena vacía "".
print(language_slice)

# Funciones de Strings #

print(language.capitalize()) # El método capitalize() se utiliza para convertir el primer carácter de una cadena a mayúscula y el resto de los caracteres a minúscula. En este caso, el resultado será "Python".

print(language.upper()) # El método upper() se utiliza para convertir todos los caracteres de una cadena a mayúscula. En este caso, el resultado será "PYTHON".

print(language.count("t")) # El método count() se utiliza para contar el número de veces que un carácter o una subcadena aparece en una cadena. En este caso, se cuenta cuántas veces aparece la letra "t" en la cadena language. El resultado será 1, ya que la letra "t" aparece una vez en "python".

print(language.isnumeric()) # El método isnumeric() se utiliza para verificar si todos los caracteres de una cadena son numéricos. En este caso, se verifica si la cadena language está compuesta únicamente por caracteres numéricos. El resultado será False, ya que "python" contiene letras y no es un número.

print(language.lower()) # El método lower() se utiliza para convertir todos los caracteres de una cadena a minúscula. En este caso, el resultado será "python", que es la misma cadena pero en minúscula.

print(language.upper().isupper()) # En este caso, se utiliza el método upper() para convertir la cadena language a mayúscula y luego se verifica si todos los caracteres de la cadena resultante son mayúscula utilizando el método isupper(). El resultado será True, ya que "PYTHON" está compuesto únicamente por caracteres mayúscula.

print(language.startswith("py")) # El método startswith() se utiliza para verificar si una cadena comienza con una subcadena específica. En este caso, se verifica si la cadena language comienza con "py". El resultado será True, ya que "python" comienza con "py".

print(language.endswith("on")) # El método endswith() se utiliza para verificar si una cadena termina con una subcadena específica. En este caso, se verifica si la cadena language termina con "on". El resultado será True, ya que "python" termina con "on".

print(language.find("h")) # El método find() se utiliza para buscar la primera aparición de un carácter o una subcadena en una cadena. En este caso, se busca la letra "h" en la cadena language. El resultado será 3, ya que la letra "h" se encuentra en el índice 3 de la cadena "python".

print(language.replace("t", "x")) # El método replace() se utiliza para reemplazar todas las apariciones de un carácter o una subcadena por otra. En este caso, se reemplaza la letra "t" por la letra "x" en la cadena language. El resultado será "pyxhon", ya que la letra "t" ha sido reemplazada por "x".

