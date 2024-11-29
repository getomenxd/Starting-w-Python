
#Fecha: 24/11/2024
#Autor: Sergi Medina Retamero
#Ejercicios propuestos por: ChatGPT


"""
Descripción: Escribe una función que verifique si una secuencia es válida (contiene solo A, T, C, G). Si no es válida, el programa debe devolver un error o advertencia.
Objetivo: Usar condicionales y bucles.
"""

seq_invalida = "ATCGZX"
seq_valida = "ATCGATCG"

bases = ["A", "C", "G", "T"] #Bases que debe contenter la secuencia 

#Definimios la función. Seguún como he diseñado el código, si no hay errores no devuelve nada y si hay alguno el analisis se detiene y imprime que la secuencia es erronea.
"""
def detectar_seq (seq_invalida):
    resultado = ""
    for base in seq_invalida:

        if base in bases:
            continue
        if base != bases:
            print("La secuencia contiene un error")
            break 

    return resultado

final = detectar_seq(seq_invalida)
print(final)
"""
#Esta es la version optimizada y corregida de ChatGPT:

def detectar_seq(secuencia):
    # Definimos las bases válidas
    bases_validas = {"A", "C", "G", "T"}  # Usamos un conjunto para búsquedas más rápidas
    
    # Verificamos si todas las bases son válidas
    for base in secuencia:
        if base not in bases_validas:
            print(f"La secuencia contiene un error: carácter no válido '{base}'")
            return False  # Devolvemos un indicador de que la secuencia no es válida

    # Si no se encontró ningún error
    print("La secuencia es válida")
    return True

# Pruebas con ejemplos
seq_invalida = "ATCGZX"
seq_valida = "ATCGATCG"

detectar_seq(seq_invalida)  # Debería indicar el error
detectar_seq(seq_valida)    # Debería indicar que es válida
