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
