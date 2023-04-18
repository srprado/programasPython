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

def buscaProfundidade(grafo, raiz, objv):
    listaVizitados = []
    lista = []
    
    lista.append(raiz)
    while (len(lista)):
        v = lista.pop() 
        if(v == objv):
            print("Vértice encontrado!")  
            break           
        for no in grafo.get(v):
            if no not in listaVizitados:
                # se não tiver a lista de apoio ele entra em loop com uma única lista
                listaVizitados.append(no)
                lista.append(no)       
        print(' | '.join(lista))           

raiz = input("Digite o vértice de origem: ")
raiz = raiz.upper()
objv= input("Digite o vértice procurado: ")
objv = objv.upper();
buscaProfundidade(grafo,raiz,objv)
