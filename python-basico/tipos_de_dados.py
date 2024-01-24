#FORMULÁRIO DE CADASTRO PARA ENTENDER TIPOS DE DADOS

dados = {} #dicionário vazio. Tipo de dado do tipo Sequência
# sinalizando que é uma variável do tipo int
res = int(input("Aceita participar? 0-Não, 1-Sim: "))

if res == 1:
    #string
    nome = input("Nome: ")    
    #int 
    idade = input("Idade: ")     
    #float(ponto flutuante)
    altura = input("Altura: ") 
    
    #adicionando chave e valor
    dados["Nome"] = nome 
    dados["Idade"] = idade
    dados["Altura"] = altura

print("Dados preenchidos")
for chave, valor in dados.items():
    print(f"{chave}:{valor}")


