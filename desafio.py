from random import randint
matriz = []
tamanho = int(input("Insira o tamanho da matriz(sempre impar): "))
centro = (tamanho - 1)//2

if tamanho%2 != 0:
    for i in range(tamanho):
        linha = []
        for j in range(tamanho):
            if i == 0 or i == tamanho -1 or j == 0 or j == tamanho - 1:
                 linha.append(1)
            else:
                 linha.append(randint(0,9))
        matriz.append(linha)
    matriz[centro][centro] = 9
    for i in range(tamanho):
            for j in range(tamanho):
                print(matriz[i][j], end = " ")
            print()
    
else:
    print("Insira um valor válido.")
distancia = int(input("Insira o tamanho da distância da matriz: "))
if distancia < centro and distancia > 0:
    soma = 0
    for i in range(centro - distancia,centro + distancia+1):
        for j in range(centro - distancia,centro + distancia+1):
            if (j == centro - distancia or j == centro + distancia) or (i == centro - distancia or i == centro + distancia):              soma += matriz[i][j]
    print(soma)