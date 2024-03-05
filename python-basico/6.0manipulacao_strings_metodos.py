""" (Principais)Métodos úteis para manipular objtos do tipo string """
#Maiúscula, Minúscula e Título
curso = "PyHoN"
print(curso.upper())#tudo maiúscula
print(curso.lower())#tudo minúscula
print(curso.title())#Converte tudo para minúsculo, exceto a primeira letra
#Espaços no começo e fim
curso2 = "  Curso Python - Espaço  "
print(curso2.strip())#remove os espaços em branco da esquerda e da direita(começo e fim da frase/palavra)
print(curso2.lstrip())#remove os espaços em branco da esquerda
print(curso2.rstrip())#remove os espaços em branco da direita
#Junções e centralização
curso3 = "PythonJunções"
print(curso3.center(10, "#"))#centraliza entre os novos caracteres. Argumentos(1º argumento:nº de caracteres que vai ocupar; 2º argumento é opcional:vai ser os caracteres adicionados)
print(".".join(curso3))#Vai passar item a item do objeto e vai colocar o item e o caracter(ou frase) passado
print(curso.upper().center(10,"#"))
