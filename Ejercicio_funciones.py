#15/11/2024
#Autor: Sergi Medina
#Ejercicios propuestos por: ChatGPT

'''
Descripción: Crea una función que convierta una temperatura dada en grados Celsius 
a Fahrenheit y otra que convierta de Fahrenheit a Celsius.

Pista: Usa las fórmulas:
°F = °C * 9/5 + 32
°C = (°F - 32) * 5/9

'''

#Con este ejercicio practicaré las funciones. 
#Primero defininimos la funcion Celsius -> Fahrenheit

def celsius_a_fahrenheit(celsius): #Mi función solo tiene un parámetro: grados celsius
    operacion = celsius * 9/5 + 32  #Escribo que operación debe almacenar la función para hacer la función
    return operacion                #Almaceno el reusultado en la variable "operación"

celsius = input("Introduce los grados celisus: ") #Aquí el usuario introduce los grados celsius que desea convertir.
celsius = int(celsius)                            #Como input() devuelve siempre una cadena de texto, con int() conseguimos convertit en un número. 
#Las dos lineas anteriores son opcionales. Es para hacerlo mas accesible al usuario. 
operacion = celsius_a_fahrenheit(celsius) #Aquí debe ir los grados celsius que se deben conversionar
print(operacion)                          #Se imprime el resultado
print("Se han obtenido fahrenheit")

#Hacemos la funcion inversa:
def funcion_2(fahrenheit):
    operacion2 = (fahrenheit - 32) * 5/9
    return operacion2

fahrenheit = input("Introduce los grados fahrenheit: ")
fahrenheit = int(fahrenheit)
operacion2 = funcion_2(fahrenheit)

print(operacion2) 
print("Se han obtenido celsius")