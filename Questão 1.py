valor = int(input("Insira valores/para parar insira (000): "))
lista = []
if valor == 000:
    print(" ")
else:
    while True:
        valor = int(input("Insira valores/para parar insira (000): "))
        if valor > 0:
            lista.append(valor)
            if len(lista) == 10:
                print(len(lista))
        else:
            lista.append(valor)
            if len(lista) == 10:
                print(sum.lista())
        
        
