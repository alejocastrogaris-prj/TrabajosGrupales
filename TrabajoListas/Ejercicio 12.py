# Ejercicio 12: Sumar Listas Elemento por Elemento
# Escribe un programa que sume dos listas de números elemento por elemento. Las
# listas deben tener la misma longitud.

lista_1 = [1,2,3,4,5]
lista_2 = [1,2,3,4,5]
resultado = []
for i in range (5):
    resultado.append(lista_1[i] + lista_2[i])
    print(resultado)

