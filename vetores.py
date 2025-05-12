# lista = ["bergamota","laranja","tangerina","maça","uva"]
# print(lista)
# fruta = input("Insira mais frutas na lista: ")
# nova_futa = lista.append(fruta)
# print(lista)

v = [20,5,9,14,27,28,4,37]

# #imprimir um elemento por linha
# for i in range (len(v)):
#     print(v[i])
# #quantidade de elementos
# print(len(v))
# #imprimir o elemento do meio
# meio = len(v)//2
# print(v[meio])
# contador = 0
# #cada mult 3, some 3
# for i in range(len(v)):
#     if v[i] % 3 == 0:
#         v[i] = v[i]+3
#         print(v[i])
#     else:
#         contador += 1
#         print(contador)

# exemplo slide
# media = 0
# somatotal = 0
# dias = 0
# semana = []
# for i in range(7):
#     valores = float(input("Insira a temperatura: "))
#     semana.append(valores)
#     somatotal = somatotal + valores
#     if len(semana) == 7:
#         media = somatotal / len(semana)

# for i in range(len(semana)):
#     if semana[i]>media:
#         dias = dias + 1

# print(semana)

# print(f"Temperatura média: {media}")

# print(f"Dias acima da média: {dias}")

# maior = semana[0]

# for i in range(len(semana)):
#     if semana[i] > maior:
#         maior = semana[i]
# print(f"Dia com maior temperatura da semana: {maior}")

# vetor = []
# for i in range(4):
#     vetor.append(int(input("Digite valor: ")))
# print(vetor)


# questão 1 - lista
# vetor = [[],[]]
# for i in range(10):
#     valor = int(input("Insira valor: "))
#     if valor > 0:
#         vetor[0].append(valor)
#     else:
#         sum(vetor[1])
# print(vetor[0])
# print(vetor[1])

# questão 2 - lista
# dado = []
# lado = int(input("Insira um valor do lado de um D6:"))
# freq_1 = 0
# freq_2 = 0
# freq_3 = 0
# freq_4 = 0
# freq_5 = 0
# freq_6 = 0
# if lado > 6 or lado == 0:
#     print("É um D6, os valores só vao até 6. ")
# else:
#     for i in range(20):
#         lado = int(input("Insira um valor do lado de um D6:"))
#         dado.append(lado)
#         if lado == 1:
#             freq_1 = freq_1 + 1
#         elif lado == 2:
#             freq_2 = freq_2 + 1
#         elif lado == 3:
#             freq_3 = freq_3 + 1
#         elif lado == 4:
#             freq_4 = freq_4 + 1
#         elif lado == 5:
#             freq_5 = freq_5 + 1
# calculo_freq1 = freq_1/20
# calculo_freq2 = freq_2/20
# calculo_freq3 = freq_3/20
# calculo_freq4 = freq_4/20
# calculo_freq5 = freq_5/20
# calculo_freq6 = freq_6/20
# print(calculo_freq1)
# print(calculo_freq2)
# print(calculo_freq3)
# print(calculo_freq4)
# print(calculo_freq5)
# print(calculo_freq6)

# questão 3 - lista

# lista = []
# for i in range(9):
#     lista.append(int(input("Valores: ")))
# for i in range(9):
#     n = lista[i]
#     contador = 0
    
#     for j in range(1,n + 1):
#         if n % j == 0:
#             contador = contador + 1
#     if contador == 2:
#         print(n,i)
# print(lista)

# questão 4 - lista

# lugar = ["Disponível","Disponível","Disponível","Disponível","Disponível","Disponível","Disponível","Disponível"]

# for i in range(8):
#     valor = int(input("lugar: "))
#     if valor > -1:
#         lugar[i] = valor
#         if valor > 0 or valor < 7:
#             lugar.remove(valor)
#             lugar.insert(valor,(str(input("Nome: "))))
#     else:
#         print(lugar)
#         exit()

# print(lugar)

# questão 5 - lista
# from random import randint
# lista = []
# for i in range(30):
#     lista.append(randint(1,2))

# coroa = 0
# cara = 0
# for i in range(30):
#     if lista[i] ==1:
#         coroa = coroa + 1
#     else:
#         cara = cara + 1
# print(lista)
# print("Coroa: ", coroa)
# print("Cara: ", cara)

# questão 6 - lista
# from random import randint
# alunos = 0
# tamanho = int(input("Quantos elementos: "))
# lista = []
# for i in range(tamanho):
#     lista.append(randint(0,tamanho))
# for i in range(len(lista) - 1):
#     compara = lista[i]
#     print("Comparando", compara)
#     for j in range(i + 1, len(lista)):
#         if compara == lista[j]:
#             lista[j] = - 1
#     if lista[i] != -1:
#         alunos = alunos + 1
# print(lista)
# print("Alunos presentes: ", alunos)

# questão 7 - lista

# clientes = []
# refeicoes = []

# for i in range(10):
#     nomes = clientes.append(input("Nome dos clientes: "))
#     quantidade_refeicao =  refeicoes.append(int(input("Quantidade de refeições: ")))

# for i in range(10):
#     if refeicoes[i] == 10:
#         print(clientes[i], " ", 0)
#     else:
#         print(clientes[i], " ", refeicoes[i])


# questão extra

# temperaturas = []
# tamanho = int(input("Quantas temperaturas foram marcadas? "))
# soma = 0

# for i in range(tamanho):
#     temp_dia = float(input("Temperatura do dia: "))
#     temperaturas.append(temp_dia)
# for i in range(tamanho-1):
#     soma = soma + temperaturas[i]
# media = (soma / (len(temperaturas) -1)) * 0.75
# media = media + temperaturas[len(temperaturas) - 1] * 0.25
# print("Temperatura prevista: ", media)