#Fecha: 08/11/2024
#Autor: Sergi Medina
#Asunto: Inicio y primeras pruebas de familiarización con Python
'''
En este código iré probando cosas básicas como variables, listas, tuplas, etc... Para que sea más simple,
lo basaré en nombres de personas simulando que estoy tratando datos familiares. Sobre la marcha y según
se me ocurra, iré jugando con los datos. 
'''
#Primero quiero tratar los datos de una única persona (datos ficticios):

ind_name = "María"
ind_age = 40
ind_dni = "8791B"

#¿Cómo se llama la mujer?
print("El nombre del individuo es:", ind_name)

#¿Qué edad tiene María?
print("¿Qué edad tiene María?")
print ("María tiene:", ind_age, "años")

#¿Su DNI?
print("Su documento de indentifiación es:", ind_dni)

#Bien, ahora quiero tratar varios individuos a la vez. Para ello haré uso de las listas:

name_list = ["María", "Jorge", "Pedro", "Laura", "Juan"]
age_list = [40, 25, 8, 9, 14]
dni_list = ["8791B", "4444A", "4444D", "4444E", "4444F"]

#Quiero saber los datos de Laura:

#Edad
laura_age = age_list[3]
print(laura_age)
#DNI
laura_dni = dni_list[3]
print(laura_dni)

#Ahora solo quiero saber los nombres de los tres primeros individuos
first_3_names = name_list[0:3]
print(first_3_names)

#Quiero imprimir la lista de las edades al reves

reverse_age_list = age_list[::-1]
print(reverse_age_list)

#Ordenar la lista de la edad en orden creciente

#ordered_age_list = age_list.sort()
#print(ordered_age_list)            #Incorrecto porque estoy imprimiendo la función .sort en vez de ejecutarla

#Ordenar la lista de la edad en orden creciente (correcto)
age_list.sort()
ordered_age_list = age_list
print(ordered_age_list)

#Ordenar la lista de la edad en orden decreciente
ordered_age_list.reverse()
reversed_list = ordered_age_list
print(reversed_list)

###DICCIONARIOS###

#Voy a crear un diccionario que tenga los datos de un contacto cualquiera

persona_anonima = {
    "nombre" : "Mariano",
    "edad" : 62,
    "DNI" : "7354J",
    "macota" : {"Wendolyn", "Perro", "Gato"} #Puedo guardar mas de un valor en una clave
}

print(persona_anonima)
print(persona_anonima["edad"])
print(persona_anonima["macota"])

#Ahora voy a intenar crear un diccionario que contenga info de varios contactos

contact_list = [
    {"nombre" : "Mariano", "edad" : 62, "DNI" : "7354J", "mascota" : "Wendolyn"},
    {"nombre" : "Aina", "edad" : 22, "DNI" : "3454M", "mascota" : "Firulais"},
    {"nombre" : "Javi", "edad" : 25, "DNI" : "6543H", "mascota" : "Yamaha"}
]

#Busco info de cada contacto. Bucles:
for contacto in contact_list:
    if contacto["nombre"] == "Aina":
        print(contacto["mascota"])

for contacto_1 in contact_list:
    if contacto_1["mascota"] == "Yamaha": #Aquí por lo que entiendo, mientras le ponga una condicion que sea cierta me imprimirá lo que busco
        print(contacto_1["edad"])

ejemplo = 5

#Otras pruebas con condicionales y bucles
if ejemplo > 5:
    print("Es verdad la condición")
else:
    print("NO es verdad la condición")

print("Ciclo terminado")

ejemplo_2 = 45

while ejemplo_2 <= 20:
    ejemplo_2 += 2
    print("El ciclo funciona")
    if ejemplo_2 == 14:
        break
else:
    print("Ciclo no empezado")