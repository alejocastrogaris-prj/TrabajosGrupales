# Ejercicio 11: Contar Ocurrencias de un Elemento
# Escribe un programa que permita al usuario ingresar una lista y un número, y cuente
# cuántas veces aparece ese número en la lista.

#------------------------------------------------------------------------------------
# 8. count()
# Cuenta cuántas veces aparece una subcadena en la cadena.
# texto = "Hola Hola Hola"
# print(texto.count("Hola")) # Salida: 3
#------------------------------------------------------------------------------------
lista_1 = []
lista_2 = []
lista_3 = []
while True:
    Seleccionar_lista = int(input("A que lista quiere ingresar? (1,2,3) Si ingresa un numero no el programa terminara"))
    
    if Seleccionar_lista == 1:
        for i in range (10):
            primera_lista_input = int(input("Ingrese 10 numeros del 1 al 10 "))
            lista_1.append(primera_lista_input)
    elif Seleccionar_lista == 2:
        for i in range(10):
            segunda_lista_input = int(input("Ingrese 10 numeros del 1 al 10 "))
            lista_2.append(segunda_lista_input)
    elif Seleccionar_lista == 3:
        for i in range (10):
            tercera_lista_input = int(input("Ingrese 10 numeros del 1 al 10 "))
            lista_3.append(tercera_lista_input)
    else:
        print("Programa finalizado")
        break
    numero_a_buscar = int(input("Ingrese el numero a verificar cuantas veces se repite en la lista seleccionada"))
    break

# numero_a_buscar = int(input("Ingrese el numero a verificar cuantas veces se repite en la lista seleccionada"))

if Seleccionar_lista == 1:
    print(f"El numero {numero_a_buscar} se repite {lista_1.count(numero_a_buscar)} veces en la lista 1")
elif Seleccionar_lista == 2:
    print(f"El numero {numero_a_buscar} se repite {lista_2.count(numero_a_buscar)} veces en la lista 2")
elif Seleccionar_lista == 3:
    print(f"El numero {numero_a_buscar} se repite {lista_3.count(numero_a_buscar)} veces en la lista 3")
else:
    print("No selecciono ninguna lista valida")








