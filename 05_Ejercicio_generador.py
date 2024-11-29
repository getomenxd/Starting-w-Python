#Fecha: 29/11/2024
#Autor: Sergi Medina Retamero
#Ejercicios propuestos por: ChatGPT

"""
Descripción: Crea una función que genere una secuencia de ADN aleatoria de longitud n. Usa las bases A, T, C y G con igual probabilidad.
Objetivo: Practicar el uso de la biblioteca random.

"""

#Primero importo la biblioteca:

import random

def generador_seq():

    random_seq = ""

    #Primero definimos las bases posibles de la secuencia:
    bases = ["A", "G", "C", "T"]
    
    longitud_n = random.randint(1, 10)

    for i in bases:
        print(random.choice(bases))

        if len(random_seq) == longitud_n:

            break
    
    return random_seq
     

resultado = generador_seq()
print(resultado)

#Solucion propuesta por chatGPT:

import random

def generador_seq(n):
    # Definimos las bases posibles para la secuencia
    bases = ["A", "T", "C", "G"]
    
    # Inicializamos la secuencia vacía
    random_seq = ""
    
    # Generamos la secuencia aleatoria de longitud n
    for i in range(n):
        random_seq += random.choice(bases)  # Añadimos una base aleatoria
    
    return random_seq

# Definir la longitud de la secuencia (puedes elegir cualquier valor)
longitud = 10  # Por ejemplo, generar una secuencia de longitud 10
resultado = generador_seq(longitud)
print(resultado)

    
