"""IDENTAÇÃO E BLOCOS
Identar código é uma forma de manter o código fonte mais legível e manutenível. Mas em Python ela exerce um segundo papel, através da identação o interpretador consegue
determinar onde um bloco de comando inicia e onde ele termina, ou seja, a identação é obrigatório e não se trata apenas de estética.

As  linguagens de programação constumam utilizar caracteres ou palavras reservadas para determinar o início e o fim do bloco. Em Java e C por exemplo, utilizamos chaves.
Cada bloco de comando está à 4 espaço de distancia do início do anterior.
"""
#se você não identa o código, o próprio VSCode mostra que há erro. Agora se vc tenta rodar, o interpretador também avisa que há um erro.
def sacar(a):
    b = 500

    if a <= b:
        print("a é menor que b!\n")
    #fim do if
#fim da função        
sacar(100)

"""ESTRUTURAS CONDICIONAIS
if / if else / elif: a estrutura condicional permite o desvio de fluxo de controle, quando determinadas expressões lógicas são atendidas.
if testa a condição lógica e da um retorno.
if-else torna possível a execução de dois desvios, ou seja, saber o que fazer em duas situações diferentes(contrárias).
if-elif-else torna possível o teste de vários desvios, ou seja, testa várias condições diferentes.
"""
saldo = 2000.0
# # saque = float(input("Informe o valor do saque: "))
# #Teste1
# if saldo >= saque:
#     print("Saque efetuado!")

# if saldo < saque:
#     print("Valor de saque excede o valor de saldo.")
# #Teste2
# if(saldo >= saque):
#     print("Saque efetuado!")
# else:
#     print("Valor de saque excede o valor de saldo.")
#Teste3
opcao = int(input("Informe uma opção: [1]Sacar; [2]Extrato: "))
if (opcao==1):
    valor_saque = float(input("Informe o valor do saque: "))
    if(saldo >= valor_saque):
        print("Saque efetuado!")
    else:
        print("Valor de saque excede o valor de saldo.")
elif(opcao==2):
    print("Valor do saldo em conta:",saldo)
else:
    print("Opção inexistente. Selecione uma opção válida")

"""
if aninhado: pode se criar estruturas condicionais aninhadas, para isso basta adicionar estruturas if/eli/else dentro do bloco de código de estruturas if/elif/else.
"""
"""
if ternário: permite escrever uma condição em uma única linha. Ele é composto por três partes, a primiera parte á o retorno caso a expressão retone verdadeiro, a segunda
parte é a expressão lógica e a terceira parte é o retono caso a expressão não seja atendida.
"""
saque = 300000
#primeira parte = ao que vem antes do if
#segunda parte = à condição do if 
#terceira parte = ao que vem depois do else, ou seja, o que acontece caso a condição não seja verdadeira.
#status é uma string, seu valor é 'Sucesso' ou 'Falha'
status = "Sucesso" if saldo >= saque else "Falha"
print(f"{status} ao realizar o saque!")

