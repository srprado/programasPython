"""
ESTRUTURAS DE REPETIÇÃO: são estruturas para repetir um trecho de códigi um determinado número de vezes. Esse número pode ser conhecido previamente ou determinado através de uma
expressão lógica.
"""
##FOR: usada quando se sabe o número exato de vezes que se deve percorre um trecho de código.

texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="\n")
#é possível colocar um else no for, caso nada seja satisfeito. Não é muito comum.
else:
    print("Não tem vogais")

##range(start, stop[,step]) -> range object
print(range(4))#imprimi o começo e fim
print(list(range(4)))#transform o range em uma lista e imprimi do 0(começo) ao 3(fim), totalizando 4 números

#nos parâmetros está passando o começo, o fim, e o step(de quanto em quanto ele pula)
#tabuada do 5
i=0
for numero in range(0,51,5):
    print(f"5 x {i} = {numero}", end="\n")
    i+=1

##While
op = -1
while op != 0:
    op = int(input("[1]Sacar\n[2]Extrato\n[0]Sair: "))
    if op == 1:
        print("Sacando...")
    elif op == 2:
        print("Exibindo o extrato...")
#apesar de não muito utilizado, também há o else no while, executado quanod sai do loop
else:
    print("Obrigada por utilizar nosso sistema bancário...")

#break: palavra reservada que interrompe o laço quando quiser

