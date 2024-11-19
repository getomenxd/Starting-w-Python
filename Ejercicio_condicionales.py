#15/11/2024
#Autor: Sergi Medina
#Ejercicio propuesto por: ChatGPT

'''
Escribe una función que tome un número y devuelva si es par o impar.
Pista: Un número es par si al dividirlo por 2, el residuo es 0 (num % 2 == 0).

'''

#Defino la función

def detecta_numero(numero):
    resultado = numero % 2
    if resultado == 0:
        print("El numero es par")
    else: 
        print("El numero es impar")

    return resultado 

numero = input("Introduzca el número a comprobar: ")
numero = int(numero)
resultado = detecta_numero(numero)
print("La comprobación ha finalizado")
