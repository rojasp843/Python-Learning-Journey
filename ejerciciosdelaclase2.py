#Funciones: Python es un lenguaje POLIMORFISTA 
# los operadores trabajan de forma distinta sobre los objetos, pero tambien
# hay operadores que pueden trabajar con algunos objetos y otros con que no 
from ast import While
import os
import time
from tkinter import W
try:
    from colorama import *
except Exception as error_:
    import pip
    pip.main(['install', 'colorama'])
    from colorama import *
def limpiar ():
    os.system('cls' if os.name == "ce" or os.name == "nt" or os.name == "dos" else "clear")
 
def pausa():
    input("\tpresione una tecla para continuar")
    print("\n")
    
limpiar();
def ya_hechos():
    pass

limpiar();

def print_color(info):
    texto= f'''{Fore.RED+Back.WHITE}{info}\n{Style.RESET_ALL}'''
    print(texto)
    
print("Hola")
print("Mundo")
print("it 2024")

info ='''
Hola
Mundo
it 2024
'''
print (info)
print_color (info)
print ('''
Hola
Mundo
it 2024
''')

print_color('''
Hola
Mundo
it 2024
''')
print_color("")
################################################################################

if "Mundo" in info:
    print ("Si Mundo esta en info")
else:
    print ("Error, la condicion no esta dada")
###############################################################################

if "planeta" in info:
    print ("Si, planeta esta en info")
else:
    print("Error, la condicion no esta dada")
###########################################################################

info = 5555
dato = 5

if str(dato) in str(info):
    print ("SI, 5 esta en 5555")
else:
    print ("Error, la condicion no esta dada")
##############################################################################
##############################################################################
dato = 1
while dato < 100 :
    print(dato)
    dato = dato + 1 
print ("estaba en la carcel pero sali")

###############################################################################
#FOR:  Es una estructura de control de flujo que permite iterar sobre 
# elementos en una secuencia (como listas, tuplas, cadenas, etc.) 
# o cualquier objeto iterable. 
# En cada iteración, la variable de iteración toma el valor de un elemento
# en la secuencia y se ejecuta el bloque de código dentro del bucle. 
# Se utiliza cuando se conoce de antemano cuántas veces se debe repetir 
# un bloque de código o cuando se quiere iterar sobre una secuencia de
# elementos. 
info = """
Hola
Mundo
it 2024
"""
for caracter in info:
    print (caracter)
print ("Estaba dando vuelta pero sali")
###################################################################################
#WHILE: Es otra estructura de control de flujo que permite ejecutar 
# repetidamente un bloque de código mientras se cumpla una condición 
# específica. 
# El bucle continúa ejecutándose mientras la condición sea verdadera. 
# Se utiliza cuando no se sabe de antemano cuántas veces se debe repetir 
# un bloque de código, sino que depende de una condición que puede cambiar 
# durante la ejecución del programa. Es importante tener cuidado al
# utilizar while para evitar bucles infinitos.

x =11010
while x > 50:
    print(x)
    x=x/2
    print("calculando")
    
print("sali")
########################################################################
if "mundo" in info:
    print ("esto es true")
else:
    print("esto no es true")
###########################################################################
#if("mundo" in info and "2024" in info):

if ("mundo" in info): #and
    if("2024" in info): #and
        print("esto es true para ambas condiciones")
    else:
        print("esto no es true para condicion 1 es falso para condicion 2")
else:
    print("esto no es true para todos")

if ("2024" in info): #and
    print("esto es true para 2024 en info")
else:
    print ("esto es true para condicion 1 falso para condicion 2")

if ("mundo" in info): #or
    print ("esto es true para mundo en info")
else:
    print ("esto es true para condicion 1 y falso para condicion 2")
# ~ OPERADORES AND Y OR: 
# AND _ Este operador devuelve True si ambas expresiones son verdaderas, de lo 
# contrario, devuelve False.
# OR _  Este operador devuelve True si al menos una de las expresiones 
# es verdadera, de lo contrario, devuelve False.
#################################################################################

if 5 < 10 and 50 > 10:
    print ("true")
else:
    print("false")
###############################################################################
if 5 < 10 and 10 < 50:
    print("true")
else:
    print("false")
###############################################################################
if 5 < 10 < 50:
    print ("true")
else:
    print("false")
#############################################################################
dato = 220
if 205 < dato < 230 : # and if 205 < dato and dato < 230 
    print ("true")
else:
    print ("false")        
###################################################################################   
def funcion_pablo():
    global step # objeto variable de un dato ( en colecciones no hace falta)
    # pueden modificarce en el ambito de una funcion para todo el programa
    
    contador = 0
    dato_entrada= dato_salida_desde_main *2
    # dato_salida_desde_main= dato_salida_desde_main *2# este objeto
    # se origina fuera de la funcion # el objeto (met y atributos) solo
    # estan como read no como write,(por que son de esta funcion)
    step = step +2
    while contador < dato_entrada:
        print (contador)
        
        contador+=step 
    print (f"{contador=}")
    
    print ("fin")

dato_salida_desde_main = 999
step = 10
funcion_pablo()
# ~ print (f"{contador=}")
print (f"{dato_salida_desde_main}")

print (f"el step actual es de {step}")