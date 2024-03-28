# CASO OBJETO DE UN SOLO DATO (variable de 1 solo dato)

def funcion_Pablo(dato_entrada):
    
    contador = 0
    dato_entrada = dato_entrada *2
    while contador < dato_entrada:
        print (contador)
        
        contador+=10
    print (f"{contador=}")
    print ("fin")
dato_salida_desde_main = 999    
funcion_Pablo (dato_salida_desde_main)
#~ print (f"{contador=}")
print (f"{dato_salida_desde_main=}")

#############################################################################
# CASO OBJETO DE UN SOLO DATO (variable de 1 solo dato)
# str, int, float

#tiene que enviarse como argumento de parametros de una funcion
#se puede ver/leer (read) dentro de la funcion obj de afuera
#No se puede MODIFICAR (write) dentro de la funcion obj de afuera

def funcion_Pablo():
    
    contador = 0
    dato_entrada = dato_salida_desde_main *2
    # dato_entrada_desde _main = dato_salida_desde_main *2 # este objeto se origana
    # fuera de la funcion. el objeto (metodos y atributos) salo estan como read
    # no como write,(por que no son de esta funcion) 
    while contador < dato_entrada:
        print (contador)
        
        contador+=10
    print (f"{contador=}")
    print ("fin")
dato_salida_desde_main = 999    
funcion_Pablo ()
#~ print (f"{contador=}")
print (f"{dato_salida_desde_main=}")

###########################################################################################   
# CASO OBJETO DE UN SOLO DATO (variable coleccion)

def funcion_Pablo():
    contador = 0
    dato_salida_desde_main[0]+=1
    dato_entrada= dato_salida_desde_main[0] *2
    # dato_entrada_desde _main = dato_salida_desde_main *2 # este objeto se origana
    # fuera de la funcion. el objeto (metodos y atributos) salo estan como read
    # no como write,(por que no son de esta funcion) 
    while contador < dato_entrada:
        print (contador)
        
        contador+=dato_salida_desde_main[1]
        
    print (f"{contador=}")
    dato_salida_desde_main[0]="chau"
    dato_salida_desde_main[1]="esto es una locura"
    print ("fin")
 
dato_salida_desde_main = [999, 10]        
funcion_Pablo ()
#~ print (f"{contador=}")
print (f"{dato_salida_desde_main=}")
#####################################################################################
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
##########################################################################################
'''
def funcion_pablo(dato):
    dato = dato *2
    print (f"dentro{dato=}")
dato = 4

print (f"antes {dato=}")

#funcion_pablo(dato)
dato = funcion_pablo (dato)

print (f"despues{dato=}") '''
###################################################################################
print ("                             variables de un dato")
def funcion_pablo(datoA, datoB):
    datoA = datoA *2
    datoB = datoB * datoA
    print (f"dentro{datoA=} {datoB=}")
    return datoA,datoB
dato1 = 4 
dato2 = 2 
print (f"antes {dato1=} {dato2=}")


dato1, dato2 = funcion_pablo (dato1,dato2)

print (f"despues{dato1=} {dato2=}")
#==============================================================================================
print ("                       variable de colecciones")
def funcion_pablo(datos):
    datoA = datos[0]
    datoB = datos [1]    
    datoA = datoA *2
    datoB = datoB * datoA
    print (f"dentro{datoA=} {datoB=}")
    return datos

dato1 = 4 
dato2 = 2 
datos = [dato1,dato2]
print (f"antes {datos[0]=} {datos[1]=}") 


datos = funcion_pablo (datos)
print (f"despues{datos[0]=} {datos[1]=}")