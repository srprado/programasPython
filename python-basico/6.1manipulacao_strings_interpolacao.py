""" Interpolar valores: """
nome = "Sabrina"
idade = 23
profissao = "Programadora"
linguagem = "Python"
#old style (%):
print("Olá me chamo %s. Eu tenho %d anos de idade, trabalho com %s e estou fazendo um curso de %s." %(nome, idade, profissao, linguagem))
#método format
print("Olá me chamo {}. Eu tenho {} anos de idade, trabalho com {} e estou fazendo um curso de {}.".format(nome, idade, profissao, linguagem))
#método format, mas passando a posição(dentro do parenteses final) em que está a variável a ser colocada no lugar - lembrando que a contagem começa em 0
print("Olá me chamo {3}. Eu tenho {2} anos de idade, trabalho com {1} e estou fazendo um curso de {0}.".format(linguagem, profissao, idade, nome))
#método format, mas passando os argumentos de forma nomeado
print("Olá me chamo {nome}. Eu tenho {idade} anos de idade, trabalho com {profissao} e estou fazendo um curso de {linguagem}.".format(nome=nome, profissao=profissao, idade=idade, linguagem=linguagem))
#método format utilizando dicionário
pessoa = {"nome":nome, "idade":idade, "profissao":"programação", "linguagem":"Python"}
print("Olá me chamo {nome}. Eu tenho {idade} anos de idade, trabalho com {profissao} e estou fazendo um curso de {linguagem}.".format(**pessoa))
#método f string
print(f"Olá me chamo {nome}. Eu tenho {idade} anos de idade, trabalho com {profissao} e estou fazendo um curso de {linguagem}.")
#Formatar strings com f-string
PI=3.14159
print(f"Valor de PI: {PI:.2f}")#2 números após a vírgula
print(f"Valor d PI: {PI:10.2f}")#nesse ele coloca 10 espaços em branco antes do número



