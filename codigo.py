#n=1
movimientos= [[4, 6],[6, 8], [7, 9], [4, 8], [0, 3, 9], [], [0, 1, 7], [2, 6], [1, 3], [2, 4]]

total_movimientos = sum(len(sublista) for sublista in movimientos)

print("Cantidad total de movimientos:", total_movimientos)

#n cualquiera
movimientos = [[4, 6], [6, 8], [7, 9], [4, 8], [0, 3, 9], [], [0, 1, 7], [2, 6], [1, 3], [2, 4]]

def contar_posibilidades(numero, movimientos_restantes):
    if movimientos_restantes == 0:
        return 1
    total = 0
    for siguiente_numero in movimientos[numero]:
        total += contar_posibilidades(siguiente_numero, movimientos_restantes - 1)
    return total

def calcular_posibilidades(n):
    posibilidades = {i: 0 for i in range(10)}
    for numero_inicio in range(10):
        posibilidades[numero_inicio] = contar_posibilidades(numero_inicio, n)
    total_posibilidades = sum(posibilidades.values())
    return total_posibilidades

n = 8 # Puedes cambiar esto al número de movimientos que desees calcular
posibilidades = calcular_posibilidades(n)

print(f"Cantidad de movimientos: {n}")
print(f"Posibilidades válidas: {posibilidades}")


    