# Bubble Sort é um algoritmo de ordenação que pode ser aplicado em Arrays e Listas dinâmicas. Se o objetivo é ordenar os valores em forma 
# decrescente, então, a posição atual é comparada com a próxima posição e, se a posição atual for maior que a posição posterior, é 
# realizada a troca dos valores nessa posição. Caso contrário, não é realizada a troca, apenas passa-se para o próximo par de comparações.

# Se o objetivo é ordenar os valores em forma crescente, então, a posição atual é comparada com a próxima posição e, se a posição atual 
# for menor que a posição posterior, é realizada a troca. Caso contrário, a troca não é feita e passa-se para o próximo par de comparação.
# https://panda.ime.usp.br/panda/static/pythonds_pt/05-OrdenacaoBusca/OBubbleSort.html
import random

vetor = []
for i in range(10):
    n = random.randint(0, 100)
    vetor.append(n)

def ordemCrescente(vetor,cont):
    aux = 0
    print("Ordenação inicial do vetor: ", vetor)
    for num in range(len(vetor)-1,0,-1):
        for i in range(num):
            if (vetor[i] > vetor[i+1]):
                vetor[i] , vetor[i+1] = vetor[i+1], vetor[i]
                # aux = vetor[i]
                # vetor[i] = vetor[i+1]
                # vetor[i+1] = aux
                
    print("Ordem do vetor em ordem crescente: ", vetor)
    return 0

def ordemDecrescente(vetor,cont):
    aux = 0
    print("Ordenação atual do vetor: ",vetor)
    for num in range(len(vetor)-1,0,-1):
        for i in range(num):
            if (vetor[i] < vetor[i+1]):
                aux = vetor[i]
                vetor[i] = vetor[i+1]
                vetor[i+1] = aux
                
    print("Ordem do vetor em ordem crescente: ", vetor)
    return 0

op = int(input("Escolha o tipo de ordenação que deseja. 1-Crescente | 2-Decrescente | 0-Sair: "))
cont = 0
while(op!=0):

    if(op==1):               
        ordemCrescente(vetor,cont)
    if(op==2):
        ordemDecrescente(vetor,cont)
    op = int(input("Escolha o tipo de ordenação que deseja. 1-Crescente | 2-Decrescente | 0-Sair: "))
    
