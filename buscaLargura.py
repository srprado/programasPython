# Constução grafo
grafo = {    
    "A": ["C", "J"],
    "B": ["C", "F"],
    "C": ["A", "B", "F"],
    "D": ["G", "M"],
    "E": ["H", "I"],
    "F": ["B", "C", "H"],
    "G": ["D", "J", "M"],
    "H": ["E", "F", "J", "K"],
    "I": ["E", "K"],
    "J": ["A", "G", "H", "M"],
    "K": ["H", "I", "L"],
    "L": ["K"],
    "M": ["D", "J"]
}

def buscaLargura(grafo, raiz, objv):
    # print(raiz, objv)
    # print(grafo.get(raiz))
    lista = []
    largura = {}
    larg = 1


    lista.append(raiz)
    largura[raiz] = larg
    # print(lista)
    while (len(lista)):
        # forma implementada LIFO, se quisesse usar como FIFO, é só colocar v=lista.pop(0),para remover sempre o primeiro
        v = lista.pop()
        if(v == objv):
            print("Vértice encontrado!")
            break #não recomendado
        # print(grafo.values(v))
        else:
            for no in grafo.get(v):
                if not largura.get(no):
                    # se não tiver uma largura atribuida ao meu nó, quer dizer que ele não foi vizitado ainda
                    larg = larg +1
                    lista.append(no)
                    largura[no] = larg
            print(' | '.join(lista))           

raiz = input("Digite o vértice de origem: ")
raiz = raiz.upper()
objv= input("Digite o vértice procurado: ")
objv = objv.upper();
buscaLargura(grafo,raiz,objv)