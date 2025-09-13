# Ejercicio 10: Eliminar un Elemento por su Índice
# Escribe un programa que permita al usuario ingresar una lista de números y eliminar
# un elemento en un índice especificado.

lista_Numeros = []
for i in range (11):
    numero_ingresado = int(input("Ingrese 10 numeros "))
    lista_Numeros.append(numero_ingresado)
    
print(f"Esta es la lista creada: {lista_Numeros}")

numero_a_eliminar = int(input("Ingrese la posicion del numero a borrar"))
lista_Numeros.remove(numero_a_eliminar)

print(f"Esta es la lista actualizada {lista_Numeros}")