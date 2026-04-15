from matrix import transpor_matriz, multiplicar_matriz

# Transposição
A = [[1, 2], [3, 4], [5, 6]]
print("Transposta de A:")
print(transpor_matriz(A))

# Multiplicação
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

print("\nMultiplicação A x B:")
print(multiplicar_matriz(A, B))
