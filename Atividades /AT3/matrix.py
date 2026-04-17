def transpor_matriz(matriz):
    return [[matriz[j][i] for j in range(len(matriz))] for i in range(len(matriz[0]))]


def multiplicar_matriz(matriz_a, matriz_b):
    if len(matriz_a[0]) != len(matriz_b):
        print("Erro: dimensões incompatíveis")
        return None

    resultado = []
    for i in range(len(matriz_a)):
        linha_resultado = []
        for j in range(len(matriz_b[0])):
            soma = 0
            for k in range(len(matriz_b)):
                soma += matriz_a[i][k] * matriz_b[k][j]
            linha_resultado.append(soma)
        resultado.append(linha_resultado)

    return resultado
