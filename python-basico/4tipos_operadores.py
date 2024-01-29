"""Operadores aritméticos: + - * / % **"""
#Adição
print(1+1)
#Subtração
print(2-2)
print(5-6)
#Multiplicação
print(2*4)
#Divisão
print(12/3)#assim retorna um float
#Divisão inteira
print(12//3)#assim retorna um inteiro
#Módulo
print(10%3)#retorna o resto da divisão
#Exponenciação
print(2**3)#primeiro num elevado ao segundo 
"""Precedência de operações: segue a regra da matemática"""
print(10-5*2)#0
print((10-5)*2)#10
print(10**2*2)#200
print(10**(2*2))#10000
print(10/2*4)#20.0

#Mesmo que o python identifique a precedência de operações, é uma boa pratica separar as operações por parentesis.
#O uso do parentesis é usado ou para mudar as ordens de execução das operações ou para deixar mais claro.

"""Operadores de comparação: o resultado é um valor booleano, logo ele retorna True ou False"""
saldo = 450
saque = 200

print(saque==saldo)#igual
print(saque!=saldo)#diferente
print(saque>saldo)#maior
print(saque>=saldo)#maior ou igual
print(saque<saldo)#menor
print(saque<=saldo)#menor ou igual

"""Operadores de atribuição: são utilizados para definir um valor inicial ou sobrescrever o valor de uma variável"""

valor_saldo = 500 #atribuição simples. Atribuição de valor à um variável
print("Valor da variável: {valor_saldo}")

valor_saldo +=200 #atribuição com adição. Isso é = à valor_saldo=valor_saldo+200
print("Valor da variável + 200: {valor_saldo}")

valor_saldo = 500 #atribuimdo novamente valor à variável
valor_saldo -=300
print("Valor da variável - 300: {valor_saldo}")

#Multiplicando o valor da variável
valor_saldo = 500
valor_saldo *= 2
print("Valor da variável * 2: {valor_saldo}")

#Dividindo o valor da variável
valor_saldo = 500
valor_saldo /= 2
print("Valor da variável / 2: {valor_saldo}")

#Divisão inteira. Dividindo o valor da variável
valor_saldo = 500
valor_saldo //= 2
print("Valor da variável // 2: {valor_saldo}")

#Módulo da divisão do valor da variável
valor_saldo = 500
valor_saldo %= 2
print("Valor da variável % 2: {valor_saldo}")

#Exponenciação do valor da variável
valor_saldo = 500
valor_saldo **= 2
print("Valor da variável ** 2: {valor_saldo}")
#OBSERVAÇÂO: se não atribuir o valor da variável novamente(sobrescrever o valor) sempre vai fazer a proxima conta com o valor resultante da conta anterior.

"""Operadores lógicos: são operadores utilizados em conjutno com os operadores de comparação, para montar uma expressão lógica. Quando um operador de comparação é utilizado,
o resultado retornado é um booleano, dessa forma podemos combinar operadores de comparação com os operadores lógicos."""

saldo = 1000
saque = 200
limite = 100

#Operador lógico 'E'. As duas condições precisam ser verdadeiras/falsas. Se forem diferentes o retorno é False
saldo >= saque and saque <= limite#False, pois uma das condições não é verdadeira

#Operador lógico 'OU'. Pelo menos uma condição tem que ser satisfeita para que o retorno seja True/False, a depender do que se necessita.
saldo >= saque or saque <= limite#True, pois a primeira condição é verdadeira, ou seja, é satisfeita.

#Operador lógico de negação 'NOT'. Nega uma sentença/condição.
contatos_emegencia = []#lista
print("1000 NÃO é > 1500")
print(not 1000 > 1500) #Aqui primeiro se faz a comparação dos valores e depois nega o resultado, ou seja, aqui o retorno é False.

#A lista é uma sequência de objetos
print(not contatos_emegencia) #Lista vazia em Python da False, então aqui ele ta negando a lista, ou seja, o resultado é True.

#A string uma sequência de caracteres
print(not "saque 1500;")#aqui a string é verdadeira, pois está preenchida, logo sua negação e retorno é False.

retorno = not ""#aqui a string é false, pois está vazia, logo sua negação e retorno é True.
print("retorno:", retorno)

#PRECEDÊNCIA DE OPERADORES LÓGICOS: segue da esquerda para direita na sentença, a menos que tenha precedência definida por parentesis.
saldo = 1000
saque = 250
limite_diario = 200
conta_especial = True
print("Problema: se a pessoa tiver conta especial e o saque for >= o saldo ela pode sacar. Se não for conta especial, não pode sacar mais que o  limite diario, e tem que ser menor que o saldo.")

print(saque <= saldo and conta_especial and saque<=saldo)#True
print(not conta_especial and saque > limite_diario)#False
retorno = (saldo >= saque and saque <= limite_diario) or (conta_especial and saque <= saldo)#True
print(retorno)

"""Operadores de indentidade: são operadores utilizados para comparar se os dois objetos testados ocupam o mesmo espaço na memória."""
curso = "Curdo de Python"
nome_curso = curso
saldo, limite = 200, 200

#Objeto A e B estão na mesma região de memória
print(curso is nome_curso) #True

print(curso is not nome_curso) #False(negação)

print(saldo is limite) #True. Também funciona com variáveis inteiras/float, não só com strings

print(curso is saldo) #False, pois não ocupam a mesma região de memória

"""Operadores de associação: são operadores utilizados para verificar se um objeto está presente em uma sequência."""
curso = "Curso de Python"
frutas = ["laranja", "uva", "limão"]
saques = [1500, 100]
#esses operadores são case sensitive, ou seja se está escrito com maiúscula ou minúscula faz diferença
print("Python" in curso)#True
print("Laranja" in frutas)#False
print("laranja" in frutas)#True
print("maçã" not in frutas)#True
print("a" in frutas)
