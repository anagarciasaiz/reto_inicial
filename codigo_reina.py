def es_seguro(tablero, fila, columna):
    # Verifica si es seguro colocar una reina en la fila y columna dada.
    for i in range(columna):
        if tablero[i] == fila or \
           tablero[i] - i == fila - columna or \
           tablero[i] + i == fila + columna:
            return False
    return True

def encontrar_solucion_n_reinas(n):
    soluciones = []
    def backtrack(columna, tablero):
        if columna == n:
            soluciones.append(tablero[:])  # Se encontró una solución
            return
        for fila in range(n):
            if es_seguro(tablero, fila, columna):
                tablero.append(fila)
                backtrack(columna + 1, tablero)
                tablero.pop()
    
    backtrack(0, [])
    return soluciones

# Rellenar la tabla con el número de soluciones encontradas
valores_de_n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15]
tabla_soluciones = {}

for n in valores_de_n:
    soluciones = encontrar_solucion_n_reinas(n)
    tabla_soluciones[n] = len(soluciones)

# Imprimir la tabla de soluciones
print("n-reinas\tTodas las soluciones")
for n in valores_de_n:
    print(f"{n}\t\t{tabla_soluciones[n]}")

