#Fecha: 21/11/2024
#Autor: Sergi Medina Retamero
#Ejercicios propuestos por: ChatGPT

'''
Descripción: Crea una función que reciba una secuencia de ADN y la convierta en una secuencia de ARN. Recuerda 
que en el ARN, la base T (timina) se reemplaza por U (uracilo).
Objetivo: Practicar manipulación de cadenas.
'''

#La siguiente función esta hecha por mi. Devuelve el ARN pero no en forma de cadena concatenada:

correspondencia = {"A":"T",
                   "G":"C",
                   "C":"G",
                   "T":"U"}


def fun_transcripcion (secuencia_adn):
    cadena_arn = ""
    for base in secuencia_adn:

        if base == "A":
            print(correspondencia["A"])
        
        if base == "G":
            print(correspondencia["G"])
        
        if base == "C":
            print(correspondencia["C"])
        
        if base == "T":
            print(correspondencia["T"])
    
    return cadena_arn
        
secuencia_adn = "ATGCGTACGTTAGCCTGAACTGACGTTGACCGTAGCTAACGCTGACTGAA"
resultado = fun_transcripcion(secuencia_adn)
print(resultado)

#Esta es la solución que propone ChatGPT:

# Diccionario de correspondencia ADN -> ARN (complementariedad)
correspondencia = {
    "A": "U",  # Adenina se transcribe a Uracilo en ARN
    "T": "A",  # Timina se transcribe a Adenina
    "C": "G",  # Citosina se transcribe a Guanina
    "G": "C"   # Guanina se transcribe a Citosina
}

def fun_transcripcion(secuencia_adn):
    # Inicializamos la cadena de ARN como una cadena vacía
    cadena_arn = ""
    
    # Iteramos sobre cada base de la secuencia de ADN
    for base in secuencia_adn:
        # Comprobamos si la base está en el diccionario de correspondencia
        if base in correspondencia:
            # Añadimos la base transcrita a la cadena de ARN
            cadena_arn += correspondencia[base]              #Aquí esta la clave para que la cadena este concatenada.
        else:
            # Si hay una base inválida, añadimos un marcador (opcional)
            cadena_arn += "?"
    
    return cadena_arn

# Secuencia de ADN de ejemplo
secuencia_adn = "ATGCGTACGTTAGCCTGAACTGACGTTGACCGTAGCTAACGCTGACTGAA"

# Transcripción de la secuencia de ADN
resultado = fun_transcripcion(secuencia_adn)

# Mostramos el resultado
print("Secuencia de ADN:", secuencia_adn)
print("Secuencia de ARN:", resultado)
