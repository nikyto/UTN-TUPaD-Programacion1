#ejercicio 1:
#Crear una lista con las notas de 10 estudiantes.
#• Mostrar la lista completa.
#• Calcular y mostrar el promedio.
#• Indicar la nota más alta y la más baja.
notas = [7, 8, 6, 9, 5, 10, 4, 6, 7, 8]
print("Notas de los estudiantes:", notas)

promedio = sum(notas) / len(notas)
print("Promedio:", promedio)

nota_max = max(notas)
nota_min = min(notas)
print("Nota más alta:", nota_max)
print("Nota más baja:", nota_min)
#ejercicio 2:
#Pedir al usuario que cargue 5 productos en una lista.
#• Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted().
#• Preguntar al usuario qué producto desea eliminar y actualizar la lista.
productos = []
for i in range(5):
    producto = input(f"Ingrese el producto {i+1}: ")
    productos.append(producto)

productos_ordenados = sorted(productos)
print("\nLista de productos ordenada alfabéticamente:")
print(productos_ordenados)

eliminar = input("\nIngrese el producto que desea eliminar: ")

if eliminar in productos_ordenados:
    productos_ordenados.remove(eliminar)
    print("\nLista actualizada después de eliminar el producto:")
    print(productos_ordenados)
else:
    print("\nEl producto no se encuentra en la lista.")

#ejercicio 3:
#Generar una lista con 15 números enteros al azar entre 1 y 100.
#• Crear una lista con los pares y otra con los impares.
#• Mostrar cuántos números tiene cada lista.
import random

numeros = [random.randint(1, 100) for _ in range(15)]
print("Lista completa de números:", numeros)

pares = []
impares = []

for n in numeros:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

print("\nNúmeros pares:", pares)
print("Cantidad de pares:", len(pares))

print("\nNúmeros impares:", impares)
print("Cantidad de impares:", len(impares))

#ejercicio 4:
#Dada una lista con valores repetidos:
#• Crear una nueva lista sin elementos repetidos.
#• Mostrar el resultados
datos = [1, 3, 5, 37, 1, 9, 5, 3]

print("Lista original:", datos)

sin_repetidos = []
for d in datos:
    if d not in sin_repetidos:
        sin_repetidos.append(d)

print("Lista sin repetidos:", sin_repetidos)

#ejercicio 5:
#Crear una lista con los nombres de 8 estudiantes presentes en clase.
#• Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente.
#• Mostrar la lista final actualizada.
# Lista inicial con 8 estudiantes
estudiantes = ["Ana", "Luis", "María", "Pedro", "Sofía", "Juan", "Carla", "Diego"]

print("Lista inicial de estudiantes:", estudiantes)

accion = input("\n¿Desea agregar un nuevo estudiante o eliminar uno existente? (agregar/eliminar): ")

if accion.lower() == "agregar":
    nuevo = input("Ingrese el nombre del nuevo estudiante: ")
    estudiantes.append(nuevo)
    print("\nEstudiante agregado correctamente.")

elif accion.lower() == "eliminar":
    eliminar = input("Ingrese el nombre del estudiante que desea eliminar: ")
    if eliminar in estudiantes:
        estudiantes.remove(eliminar)
        print("\nEstudiante eliminado correctamente.")
    else:
        print("\nEse estudiante no está en la lista.")

else:
    print("\nOpción no válida.")

print("\nLista final de estudiantes:", estudiantes)

#ejercicio 6:
#Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha (el 
#último pasa a ser el primero).
numeros = [10, 20, 30, 40, 50, 60, 70]
print("Lista original:", numeros)

rotada = [numeros[-1]] + numeros[:-1]
print("Lista rotada:", rotada)

#ejercicio 7:
#Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una 
#semana.
#• Calcular el promedio de las mínimas y el de las máximas.
#• Mostrar en qué día se registró la mayor amplitud térmica.
temperaturas = [
    [10, 20],
    [12, 25],
    [8, 18],
    [15, 30],
    [11, 22],
    [9, 19],
    [13, 28]
]

suma_min = 0
suma_max = 0
for dia in temperaturas:
    suma_min += dia[0]
    suma_max += dia[1]

promedio_min = suma_min / len(temperaturas)
promedio_max = suma_max / len(temperaturas)

print("Promedio de mínimas:", promedio_min)
print("Promedio de máximas:", promedio_max)

mayor_amplitud = 0
dia_mayor_amplitud = 0
for i, dia in enumerate(temperaturas):
    amplitud = dia[1] - dia[0]
    if amplitud > mayor_amplitud:
        mayor_amplitud = amplitud
        dia_mayor_amplitud = i + 1

print("La mayor amplitud térmica fue de", mayor_amplitud, "grados")
print("Se registró en el día", dia_mayor_amplitud)

#ejercicio 8:
notas = [
    [7, 8, 6],
    [5, 9, 7],
    [8, 6, 9],
    [6, 7, 8],
    [9, 10, 8]
]

print("Promedio de cada estudiante:")
for i, estudiante in enumerate(notas):
    promedio_est = sum(estudiante) / len(estudiante)
    print(f"Estudiante {i+1}: {promedio_est:.2f}")

print("\nPromedio de cada materia:")
materias = len(notas[0])
estudiantes = len(notas)
for j in range(materias):
    suma = 0
    for i in range(estudiantes):
        suma += notas[i][j]
    promedio_mat = suma / estudiantes
    print(f"Materia {j+1}: {promedio_mat:.2f}")


#ejercicio 9:
#Representar un tablero de Ta-Te-Ti como una lista de listas (3x3).
#• Inicializarlo con guiones "-" representando casillas vacías.
#• Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O".
#• Mostrar el tablero después de cada jugada.
tablero = [["-" for _ in range(3)] for _ in range(3)]
def mostrar_tablero(tablero):
    for fila in tablero:
        print(" ".join(fila))
    print()

print("Tablero inicial:")
mostrar_tablero(tablero)

for turno in range(2):
    if turno % 2 == 0:
        jugador = "X"
    else:
        jugador = "O"

    print(f"Turno del jugador {jugador}")
    fila = int(input("Ingrese la fila (0-2): "))
    columna = int(input("Ingrese la columna (0-2): "))

    if tablero[fila][columna] == "-":
        tablero[fila][columna] = jugador
    else:
        print("Casilla ocupada, pierdes el turno.")
    mostrar_tablero(tablero)

#ejercicio 10:
#Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7.
#• Mostrar el total vendido por cada producto.
#• Mostrar el día con mayores ventas totales.
#• Indicar cuál fue el producto más vendido en la semana.
ventas = [
    [10, 20, 15, 30, 25, 18, 22],
    [5, 12, 8, 10, 15, 9, 11],
    [7, 14, 20, 18, 16, 22, 19],
    [12, 18, 25, 20, 30, 28, 26]
]

print("Total vendido por cada producto:")
for i, producto in enumerate(ventas):
    total = sum(producto)
    print(f"Producto {i+1}: {total}")

totales_dias = []
for j in range(7):
    suma_dia = 0
    for i in range(4):
        suma_dia += ventas[i][j]
    totales_dias.append(suma_dia)

mayor_ventas = max(totales_dias)
dia_mayor = totales_dias.index(mayor_ventas) + 1
print(f"\nEl día con mayores ventas totales fue el día {dia_mayor} con {mayor_ventas} unidades.")

totales_productos = [sum(producto) for producto in ventas]
mas_vendido = max(totales_productos)
producto_mas_vendido = totales_productos.index(mas_vendido) + 1
print(f"\nEl producto más vendido en la semana fue el Producto {producto_mas_vendido} con {mas_vendido} unidades.")