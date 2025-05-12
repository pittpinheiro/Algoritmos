#matriz zig zag
matriz = []

for i in range(4):
    linha = []
    for j in range(4):
        linha.append(int(input("Valores: ")))
    matriz.append(linha)
for i in range(4):
    if i%2 == 0:
        for j in range(4):
            print(matriz[i][j], end = " ")
    else:
        for j in range(len(matriz)-1,-1,-1):
            print(matriz[i][j], end = " ")
    print()

#menor elemneto da matriz

menor = linha[0][0]
linhamenor = 0

for i in range(4):
    for j in range(4):
        if matriz[i][i] < linhamenor:
            linhamenor = j
            linhamenor = matriz[i]
print(menor)