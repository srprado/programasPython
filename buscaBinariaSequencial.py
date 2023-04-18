import time
def menu():
    print('\n1 - Algoritmo sequencial;\n2 - Algoritmo binário;\n0 - Sair.')
    op = int(input('Escolha uma opção: '))
    return op


def sequencial(num, vetor):
    start = time.time()
    for i in vetor:
        if (num == vetor[i]):
            print('Valor na posição ', i)
    end = time.time()
    print('Tempo de execução = ',end-start)
    print('==================================================')


def binario(num, vetor):
    inicio = 0
    fim = len(vetor)
    start = time.time()
    while inicio <= fim:
        meio = (inicio+fim) // 2
        if (num == vetor[meio]):
            pos = meio
            end = time.time()  
            print('Tempo de execução = ',end-start)         
            return pos
        elif (num < vetor[meio]):
            fim = meio - 1
        else:  # (num > vetor[meio])
            inicio = meio + 1
         
    return pos

# for i in range (100):
#     vetor.append(i)
vetor = range(1000)
# for i in vetor:
#     print(vetor[i], end='  ')

opc = menu()
while opc != 0:
    if (opc == 1):
        print('=========================Sequencial=========================')
        num = int(input('Digite um numero a ser encontrado: '))
        sequencial(num, vetor)

    elif (opc == 2):
        print('=========================Binário=========================')
        num = int(input('Digite um numero a ser encontrado: '))
        posi = binario(num, vetor)
        print('Valor na posição ', posi)
        print('==================================================')

    else:
        print('\n Opção inexistente')
    opc = menu()
