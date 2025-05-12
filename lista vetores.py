
# # questão 1 - lista
# vetor = [[],[]]
# positivos = 0
# soma_negativos = 0
# for i in range(10):
#     valor = int(input("Insira valor: "))
#     if valor > 0:
#         vetor[0].append(valor)
#         positivos += 1
#     if valor < 0:
#         vetor[1].append(valor)
#         soma_negativos = valor + soma_negativos
# print(vetor)
# print("Quantidade de positivos: ", positivos)
# print("Soma negativos: ", soma_negativos)
        


# # questão 2 - lista
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

# # questão 3 - lista

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

# # questão 4 - lista

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
from random import randint
lista = []
for i in range(30):
    lista.append(randint(1,2))

coroa = 0
cara = 0
for i in range(30):
    if lista[i] ==1:
        coroa = coroa + 1
    else:
        cara = cara + 1
print(lista)
print("Coroa: ", coroa)
print("Cara: ", cara)

# questão 6 - lista
from random import randint
alunos = 0
tamanho = int(input("Quantos elementos: "))
lista = []
for i in range(tamanho):
    lista.append(randint(0,tamanho))
for i in range(len(lista) - 1):
    compara = lista[i]
    print("Comparando", compara)
    for j in range(i + 1, len(lista)):
        if compara == lista[j]:
            lista[j] = - 1
    if lista[i] != -1:
        alunos = alunos + 1
print(lista)
print("Alunos presentes: ", alunos)

# questão 7 - lista

clientes = []
refeicoes = []

for i in range(10):
    nomes = clientes.append(input("Nome dos clientes: "))
    quantidade_refeicao =  refeicoes.append(int(input("Quantidade de refeições: ")))

for i in range(10):
    if refeicoes[i] == 10:
        print(clientes[i], " ", 0)
    else:
        print(clientes[i], " ", refeicoes[i])


# questão extra

temperaturas = []
tamanho = int(input("Quantas temperaturas foram marcadas? "))
soma = 0

for i in range(tamanho):
    temp_dia = float(input("Temperatura do dia: "))
    temperaturas.append(temp_dia)
for i in range(tamanho-1):
    soma = soma + temperaturas[i]
media = (soma / (len(temperaturas) -1)) * 0.75
media = media + temperaturas[len(temperaturas) - 1] * 0.25
print("Temperatura prevista: ", media)