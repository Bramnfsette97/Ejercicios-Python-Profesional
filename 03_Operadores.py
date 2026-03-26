# OPERADORES ARITMÉTICOS

print(3 + 4) # Suma
print(3 - 4) # Resta
print(3 * 4) # Multiplicación
print(3 / 4) # División (si el resultado es un número decimal, se muestra con decimales)
print(10 % 3) # Módulo (resto de la división)
print(10 // 3) # División entera (si el resultado es un número decimal, se muestra sin decimales)
print(2 ** 3) # Potenciación (2 elevado a la 3)
print(2 ** 3 + 3 - 7 / 1 // 4) # Operadores combinados (se siguen las reglas de precedencia de los operadores)


print("Hola" + "Python" + "Que tal?") # Concatenación de cadenas (une dos cadenas de texto) 

#print("Hola" + 5) # Esto dará un error porque no se pueden concatenar una cadena de texto con un número entero

print ("Hola" * 5) # Repetición de cadenas (repite la cadena de texto un número determinado de veces)
print("Hola" + str(5)) # Para concatenar una cadena de texto con un número entero, primero debemos convertir el número a cadena de texto usando la función str().

# OPERADORES DE COMPARACIÓN

print(3 > 4) # Mayor que
print(3 < 4) # Menor que
print(3 >= 4) # Mayor o igual que
print(4 <= 4) # Menor o igual que
print(3 == 4) # Igual que
print(3 != 4) # Diferente que
print(3 > 4 == 2) # Operadores combinados (se siguen las reglas de precedencia de los operadores)

print("Hola" > "Python") # Comparación de cadenas (se compara el valor ASCII de cada carácter en la cadena, letra por letra)
print("Hola" < "Python") 
print("Hola" >= "Zola") # La letra "H" tiene un valor ASCII menor que la letra "Z", por lo tanto, "Hola" es menor que "Zola"
print(len("aaaa") >= len("abaa")) # Comparación de la longitud de las cadenas (se compara el número de caracteres en cada cadena)
print("Hola" <= "Python")
print("Hola" == "Hola")
print("Hola" != "Python")

### OPERADORES LÓGICOS ###
print(3 > 4 and "Hola" > "Python") # Operador lógico AND (devuelve True si ambas condiciones son verdaderas)
print(3 > 4 or "Hola" > "Python") # Operador lógico OR (devuelve True si al menos una de las condiciones es verdadera)
print(not (3 > 4)) # Operador lógico NOT (devuelve True si la condición es falsa, y False si la condición es verdadera)

  