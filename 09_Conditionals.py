### Conditionals ###

# Si es False no se ejecuta el bloque de codigo del if, si es True se ejecuta el bloque de codigo del if   
my_condition = False 

if my_condition:
    print("Se ejecuta la condicion del if")

my_condition = 5 * 5

if my_condition == 10:
    print("Se ejecuta la condicion del segundo if")

if my_condition > 10 and my_condition < 20:
    print("Es mayor que 10 y menor que 20")
elif my_condition == 25: 
    print("Es igual a 25")
else:
    print("Es menor o igual que 10 o mayor o igual que 20 o  distinto de 25")


print("La ejecusion continua") 

### En Python, los siguientes valores se consideran False en un contexto booleano:
# - None
# - False
# - 0
# - ""
# - []
# - {}

my_string = ""

if my_string:
    print("My cadena de texto no es vacia")

my_string = ""

#if my_string:
    #print("My cadena de texto no es vacia")

### Si la cadena de texto es vacia, se considera False, por lo tanto se ejecuta el bloque de codigo del if
if not my_string:
    print("My cadena de texto es vacia")