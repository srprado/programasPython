# INT PARA FLOAT
# variável int
preco = 10
print("Inteiro: ",preco)
# convertendo para float
preco2 = float(preco)
print("Float: ",preco2)
# ou através da divisão
preco3 = preco/2
print("Conversão por divisão: ",preco3)
preco3 = preco//2
print("Mantendo o número como inteiro após a divisão: ",preco3)

# FLOAT PARA INT
valor = 10.3
print("Valor float: ",valor)
valor = int(valor)
print("Valor sendo int:",valor)

# NUMÉRICO PARA STRING
numero = 10.5
idade = 28
print(f"Imprimindo o número como string: {str(numero)}")
print(f"Imprimindo a idade como string: {str(idade)}")

# STRING PARA NÚMERO
num_texto = "10.50"
idade = "28"
print("String como float: ",float(num_texto))
print("String como int: ",int(idade))
# se não for possível converter a variável(por exemplo, de fato o conteúdo é texto) vai dar um erro dizendo que não é possível fazer a conversão
# mostrando a diferença printando os tipos
x = 10
x_str = str(x)
print(type(x))
print(type(x_str))