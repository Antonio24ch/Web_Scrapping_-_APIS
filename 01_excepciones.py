# La secuencia de instrucciones puede generar un problema, es posible añadir sentencias para que se
# ejecuten en caso de error, por ejemplo `try` y `except`

instruccion = input('Introduzca la temperatura en Fahrenheit: ')

# Try lo que quiero que haga el programa
try:

    fahrenheit = float(instruccion)
    celsius = (fahrenheit - 32) * 5/9
    print(celsius)

# Except lo que haga en caso de error 
except: 
    print('Introducir un número')

# Ejemplo, si el usuario introduce algún texto, arrojará el mensaje de `except`
