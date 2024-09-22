#EJERCICIO 1,2 y 3
#ejercicio 1
import random
arregloA = [random.randint(0,500) for i in range(100)]
indices_pares = [arregloA[i] for i in range(0, len(arregloA), 2)]
print("Estos son los indices pares del arregloA", indices_pares)
mayor = max(arregloA)
print("El numero mayor del arregloA es", mayor)
menor = min(arregloA)
print("El numero menor del arregloA es", menor)
mayorindice = arregloA.index(mayor)
print("El indice del numero mayor es", mayorindice)
menorindice = arregloA.index(menor)
print("El indice del numero menor es", menorindice)
copia_arregloA = arregloA.copy()
suma = sum(copia_arregloA)
print("La suma de los elementos de la copia arregloA es", suma)
promedio = suma/len(copia_arregloA)
print("El promedio de los elementos de la copia arregloA es", promedio)
#EJERCICIO 2
import random
arreglo_1 = [random.randint(0,1000) for i in range(10)]
print("Estos son los elementos aleatorios del arreglo_1", arreglo_1)
numeros_pares = [numero for numero in arreglo_1 if numero % 2 == 0]
print("Estos son los elementos pares del arreglo_1", pares_arreglo_1)
suma_impares = sum(numero for numero in arreglo_1 if numero % 2 != 0)
print("Esta es la suma de los elementos impares del arreglo_1", impares_arreglo_1)
def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True
for numero in arreglo_1:
    if es_primo(numero):
        print(f"El número {numero} es primo.")
#EJERCICIO 3
A = [random.randint(0,300) for i in range(100)]
B = [random.randint(0,300) for i in range(100)]
suma1=sum(A)
suma2=sum(B)
print("La suma de los elementos del arreglo A es", suma1)
print("La suma de los elementos del arreglo B es", suma2)
sumaarreglos=suma1+suma2
print("La suma de los arreglos A y B es", sumaarreglos)
for i in B:
    if i % 2 != 0:
        print(f"Tabla de multiplicar de {i}:")
        for j in range(1, 11):
            print(f"{i} x {j} = {i * j}")