#defino una matriz 3 * 3
matriz=[
    [55, 3, 43],
    [18, 60, 2],
    [0, 89, 5]
]

def buscar_valor(matriz,valor):
    # recorrer y buscar el valor
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j]==valor:
             return i, j #retorna_la_posición
    return None

#solcitar el valor a buscar
numero_buscar=89

#llamo a la funcion
resultado =buscar_valor(matriz,numero_buscar)

if resultado:
    print(f"el resultado del numero {numero_buscar} se encuentra en la posición {resultado[0]} {resultado[1]}")
else:
    print(f"el numero no se encuentra en la matriz")






