#String Cadenas de Caracteres
# modelo de carta
año = 2024
mes = 1
dia = 14
fecha = f"{año}/{mes}/{dia}"
lugar = "Buenos Aires"
pie = f"En {lugar}, a los {dia} del mes {mes} del año {año}"
dni = 35123674
legal = f"""xxxxxxxxxxxxxxxxxxxxxxxxx{fecha}
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxx{dni}xxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
{pie}
"""
nombre = "Ariel"
#print (f"xxxxxxx/{nombre.center(50)}/ xxxxxxx")
#print (f"salida {legal}")
#exit()



obj_1 = 'esto es una cadena de caracteres'
obj_1 = "esto es una cadena de caracteres"
obj_2 = """
esto
es
una
cadena
de caracteres
"""
obj_2 = '''
esto
es
una
cadena
de caracteres
'''
#print (f"el contenido de objeto es {obj_1}")
#print (f"el contenido de objeto es {obj_2}") al
#print ("FIN")
#---------------------------------------------------------------------------------------------------------------
# Varias formas de agregar la "s" si se compra mas de un almaque.

nombre = "Ariel"
cantidad = 1
producto = "almanaque"
#1) FORMA
print (f"{nombre} compro {cantidad} {producto}")
if cantidad == 1:
    print (f"{nombre} compro {cantidad} {producto}")
else:
    print(f"{nombre} compro {cantidad} {producto}")
#---------------------------------------------------------------------------------------------------------------            
#2) FORMA. Otra forma de imprimir el mensaje, utilizando un operador ternario para decidir si agregar 's' al producto    
print (f"{nombre} compro {cantidad} {producto} { '' if cantidad == 1 else 's'}")
#------------------------------------------------------------------------------------------------------------------
#3) FORMA.
item = (f"{nombre} compro {cantidad} {producto}")
if cantidad == 1:
    print (f"{item}")
else:
    print(f"{item}s")
#----------------------------------------------------------------------------------------------------------------------------
#4) FORMA.
item = (f"{nombre} compro {cantidad} {producto}")
if cantidad != 1:
    item += "s" 
#=> item = item + "s"
print (f"{item}")
    
   


exit()
#########################################################################################
obj_1 = 9652
print (f"2do {obj_1} ---> {id(obj_1)=}")
obj_2 = 652
resultado = obj_1 + obj_2
print  (resultado)
#print  (dir(obj_1))

#obj_1 = 1
print (f"1ro {obj_1} ---> {id(obj_1)=}")
pepe = 1 
print (f"{pepe} ---> {id(pepe)=}")
ana = 1
print (f"{ana} ---> {id(ana)=}")
ana = ana + 1
print (f"ana {ana} ---> {id(ana)=}")
ana = "Hola"
print (f"ana {ana} ---> {id(ana)=}")
ana = 5.25
print (f"ana {ana} ---> {id(ana)=}")
exit()
###############################################################################

obj_col = [1,"a",3.14159,True,"pablo","Äriel"]
print ("el contenido de la coleccion {obj_col}")
print (f"el contido de la coleccion {obj_col}")
#la F es el formateo de los datos dentro de la cadena de string la f me permite el control de datos dentro de un string
print (f"el contido de la coleccion {obj_col [0]}")
print (f"el contido de la coleccion {obj_col [1]}")
print (f"el contido de la coleccion {obj_col [2]}")
print (f"el contido de la coleccion {obj_col [3]}")
print (f"el contido de la coleccion {obj_col [4]}")
print (f"el contido de la coleccion {obj_col [5]}")
print (f" el contenido de la coleccion {id(obj_col)}")
print (f" el contenido de la coleccion {id(obj_col[0])}")
#En cuanto a cómo Python guarda los valores de los objetos en la memoria 
# es importante entender que en Python, todo es un objeto. 
# Cuando se asigna un valor a una variable, se crea un objeto que contiene 
# ese valor y la variable se convierte en una referencia a ese objeto. 
# Cuando se reasigna una variable, simplemente se cambia la referencia para 
# apuntar a un nuevo objeto en memoria. Si el objeto original no tiene más 
# referencias apuntando a él, será marcado para la recolección de basura 
# y liberado de la memoria.
exit()
##############################################################################

obj_1 = "Hola"
obj_2 = "Mundo"
resultado = obj_1 + obj_2
print  (resultado.center(50))
#print  (dir(obj_1))
exit()

################################################################################