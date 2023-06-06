def filtrar_numeros(lista):
    numeros_filtrados = []

    for num in lista:
        if num % 2 == 0 and num % 4 != 0:
            numeros_filtrados.append(num)

    return numeros_filtrados





if __name__ == '__main__':
    
    # Casos de pruebas
    
    caso1 = [10, 6, 8, -5, -89, 90]
    caso2 = [30, 21, 6, -30, -6, -21]
    caso3 = [-10]

    # Aplicar el filtro y mostrar los resultados
    print(f"Caso 1: numeros de entrada {caso1}")
    resultado_caso1 = filtrar_numeros(caso1)
    print(f"Numeros de salida {resultado_caso1} \n")

    print(f"Caso 2: numeros de entrada {caso2}")
    resultado_caso2 = filtrar_numeros(caso2)
    print(f"Numeros de salida {resultado_caso2} \n")

    print(f"Caso 3: numeros de entrada {caso3}")
    resultado_caso3 = filtrar_numeros(caso3)
    print(f"Numeros de salida {resultado_caso3} \n")