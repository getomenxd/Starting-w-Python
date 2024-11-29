#Fecha: 21/11/2024
#Autor: Sergi Medina Retamero
#Ejercicios propuestos por: ChatGPT

"""
Descripción: Escribe un programa que tome una secuencia de ADN y cuente cuántas veces aparece cada base (A, T, C, G).
Objetivo: Practicar cadenas, bucles y conteo.
"""

#Vamos a comenzar el programa

#Definimos la secuencia:

secuencia_adn = "ATGCGTACGTTAGCCTGAACTGACGTTGACCGTAGCTAACGCTGACTGAA"

#También hacemos una lista de las bases:

#Ahora armamos un bucle que nos cuente cuantas veces aparece cada base en la secuencia:
contador_A = 0
contador_C = 0       
contador_G = 0       #Aquí la clave es definir los contadores FUERA del bucle porque sino se reinician a 0 a cada vuelta.
contador_T = 0       

for base in secuencia_adn:

    if base == "A":
        contador_A += 1
    if base == "C":
        contador_C += 1
    if base == "G":
        contador_G += 1
    if base == "T":
        contador_T += 1

print(f"El numero de adeninas en la secuencia es de {contador_A}")
print(f"El numero de adeninas en la secuencia es de {contador_C}")
print(f"El numero de adeninas en la secuencia es de {contador_G}")
print(f"El numero de adeninas en la secuencia es de {contador_T}")
        



