# defino matriz 3x3
matriz = [
    [5, 3, 4],
    [1, 6, 2],
    [0, 8, 5]
]
#funcion que ordena una fila usando Bubble Sort.
def bubble_sort(fila):
    n =len(fila)
    for i in range(n):
        for j in range(0, n - i - 1):
            if fila[j] > fila[j + 1]:
                fila[j], fila[j + 1] = fila[j + 1], fila[j]
    return fila


def ordenar_fila_matriz(matriz, fila_index):
    """Ordena la fila especificada de la matriz."""
    if 0 <= fila_index < len(matriz):
        print("Matriz original:")
        for fila in matriz:
            print(fila)

        matriz[fila_index] = bubble_sort(matriz[fila_index])

        print("\nMatriz con la fila ordenada:")
        for fila in matriz:
            print(fila)
    else:
        print("Índice de fila fuera de rango.")


# Elegir la fila a ordenar
fila_a_ordenar = 1  # Segunda fila (índice 1)
ordenar_fila_matriz(matriz, fila_a_ordenar)