#Aspas triplas permite fazer grandes comentários em python
"""
-A função builtin(é prórpia da linguagem) input é utilizada quando queremos ler dados de entrada padrão(teclado). Ela recebe um argumento do tipo string, que é exibida
para o usuário na saída padrão(tela). A função lê a entrada, converte para string e retorna o valors.
//independente do valor de entrada ele é sempre formatado como string

-A função builtin print é utilizada quando queremos exibir dados na saída padrão(tela). Ela recebe o argumento obrigatório do tipo varargs de objetos e 4 argumentos 
opcionais(sep, end, file e flush). Todos os objetos são convertidos para string, separados por sep e terminados por end. A string final é exibida para o usuário.
"""

nome = "Sabrina"
sobrenome = "R.P"

#dessa forma as variáveis são immpressas apenas com um espaço entre elas
print(nome, sobrenome)

#passando o 'end' como parametro eu adiciono algo ao final da impressão das variáveis. Por padrão o 'end' é somente uma quebra de linha
print(nome, sobrenome, end="...\n")

#passando o 'sep' trocamos o separador padrão(espaço) das variáveis por algo de sua preferência
print(nome, sobrenome, sep="#")

print(nome, sobrenome)