#Fecha: 27/11/2024
#Autor: Sergi Medina Retamero
#Ejercicios propuestos por: ChatGPT

"""
Descripción: Escribe una función que calcule el porcentaje de bases G y C en una secuencia de ADN.
Fórmula: Porcentaje_GC = (G + C)/longitud * 100 
"""

def calculo_GC (secuencia):

    #Contadores de Guanina, Citosina y longitud de la cadena (bases totales):

    contador_G = 0 
    contador_C = 0
    contador_seq = 0 

    #Bases a detectar

    bases = {"A", "G", "C", "T"}

    for base in secuencia:

        #Contador de bases totales
        if base in bases:
            contador_seq += 1

        #Contador de Guaninas y Citosinas
        if base == "G":
            contador_G += 1
        if base == "C":
            contador_C += 1

    
    print(f"La longitud de la secuencia es de {contador_seq} bases")
    print(f"El número de guaninas totales es de {contador_G}")
    print(f"El número de citosinas totales es de {contador_C}")

    porcentaje_GC = (contador_C + contador_G)/contador_seq * 100

    print(f"El porcentaje de GC es de {porcentaje_GC}%")

    
secuencia = "ATCGATCG"
resultado_x = calculo_GC(secuencia)   
print(resultado_x)

#El código funciona, pero me devuelve un none porque no he aplicado un return en la función. Simplemente me ha faltado aplicar correctamente un return.

#El siguiente código devolveria como resultado un diccionario con un return y se soluciona el none. ChatGPT:

def calculo_GC(secuencia):
    # Contadores de Guanina, Citosina y longitud de la cadena (bases totales):
    contador_G = 0 
    contador_C = 0
    contador_seq = 0 

    # Bases válidas
    bases = {"A", "G", "C", "T"}

    for base in secuencia:
        # Contador de bases totales
        if base in bases:
            contador_seq += 1

        # Contador de Guaninas y Citosinas
        if base == "G":
            contador_G += 1
        if base == "C":
            contador_C += 1

    porcentaje_GC = (contador_C + contador_G) / contador_seq * 100

    # Retornamos un diccionario con toda la información
    return {
        "longitud": contador_seq,
        "guaninas": contador_G,
        "citosinas": contador_C,
        "porcentaje_GC": porcentaje_GC
    }

# Ejecución
secuencia = "ATCGATCG"
resultado_x = calculo_GC(secuencia)  # Ahora devuelve un diccionario
print(resultado_x)  # Mostramos los resultados si queremos
