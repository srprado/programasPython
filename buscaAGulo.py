# Algoritmo A* para escolher qual a proxima cidade ele soma o quanto já andou + a distância até a proxima cidade + a distância da próxima cidade até Bulgarest
# Distância em linha reta das cidades para Bulgarest
distanciaBulgarest = {"Arad":366,"Craiova":160,"Dobreta":242,"Eforie":161,"Fagaras":176,"Giurgiu":77,"Hirsova":151,"Iasi": 226,"Lugoj": 244,"Mehadia": 241,
"Neamt":234,"Oradea":380,"Pitest":10,"RimnicuVilcea":193,"Sibiu":253,"Timisoara":329,"Urziceni":80,"Vaslui":199,"Zerind":374,"Bulgarest":0}
# Distância entre as cidades e seus vizinhos
cidades = [
    {"cidade":"Arad","vizinhos":{"Timisoara":118,"Sibiu":140,"Zerind":75}},
    {"cidade":"Craiova","vizinhos":{"Dobreta":120,"Pitest":120,"RimnicuVilcea":146}},
    {"cidade":"Dobreta","vizinhos":{"Craiova":120,"Mehadia":75}},
    {"cidade":"Eforie","vizinhos":{"Hirsova":86}},
    {"cidade":"Fagaras","vizinhos":{"Bulgarest":211,"Sibiu":99}},
    {"cidade":"Giurgiu","vizinhos":{"Bulgarest":90}},
    {"cidade":"Hirsova","vizinhos":{"Eforie":86,"Urziceni":98}},
    {"cidade":"Iasi","vizinhos":{"Neamt":87,"Vaslui":92}},
    {"cidade":"Lugoj","vizinhos":{"Mehadia":70,"Timisoara":111}},
    {"cidade":"Mehadia","vizinhos":{"Dobreta":75,"Lugoj":70}},
    {"cidade":"Neamt","vizinhos":{"Iasi":87}},
    {"cidade":"Oradea","vizinhos":{"Sibiu":151,"Zerind":71}},
    {"cidade":"Pitest","vizinhos":{"Bulgarest":101,"RimnicuVilcea":97,"Craiova":138}},
    {"cidade":"RimnicuVilcea","vizinhos":{"Pitest": 97, "Sibiu": 80, "Craiova": 146}},
    {"cidade":"Sibiu","vizinhos":{"Fagaras":99,"RimnicuVilcea":80,"Arad":140,"Oradea":151}},
    {"cidade":"Timisoara","vizinhos":{"Arad":118,"Lugoj":111}},
    {"cidade":"Urziceni","vizinhos":{"Bulgarest":85,"Hirsova":98,"Vaslui":142}},
    {"cidade":"Vaslui","vizinhos":{"Urziceni":142,"Iasi":92}},
    {"cidade":"Zerind","vizinhos":{"Arad":75,"Oradea":71}},
    {"cidade":"Bulgarest","vizinhos":{"Giurgiu":90,"Urziceni":85,"Fagaras":211,"Pitesti":101}}

]
#faltante é a distância da cidade atual até Bulgareste.
def calcDistancia(andado, distanciaProximoNo,distanciaBulgarest):
    resultado = andado + distanciaProximoNo + distanciaBulgarest
    return resultado

def buscaAestrela(listaCidade,city,cidadesPassadas,distAndada): 
    menorCaminho = 400
    resultado = 0 
    proximaCidade = ""
    if (city=="Bulgarest"):
        print("Caminho feito até Bulgarest:",cidadesPassadas, "\n")
    else:
        for cid in listaCidade:
            if(cid.get('cidade') == city):
                cidadesPassadas.append(city)
                c = cid.get("vizinhos")
                # print(c)
                for v in c.keys():
                    for i in distanciaBulgarest.keys():  
                        if(v == i):   
                            resultado = distAndada + c[v] + distanciaBulgarest[i]                         
                            # resultado = calcDistancia(distAndada,c[v],distanciaBulgarest[i])                            
                            if(resultado < menorCaminho):
                                menorCaminho = resultado
                                distAndada = distAndada + c[v]
                                proximaCidade = v
                                print(proximaCidade)
    
        # buscaAestrela(listaCidade,proximaCidade,cidadesPassadas,distAndada)

    return 0

def buscaGulosa(listaCidade, city, cidadesPassadas):    
    menorDistancia = 400
    if (city=="Bulgarest"):
        cidadesPassadas.append("Bulgarest")
        print("Caminho feito até Bulgarest:",cidadesPassadas, "\n")
    else:
        for cid in listaCidade:
            if (cid.get('cidade') == city):
                cidadesPassadas.append(city)
                c = cid.get('vizinhos')
                for v in c.keys():
                    for i in distanciaBulgarest.keys():
                        if v == i:
                            if distanciaBulgarest[i] < menorDistancia:
                                menorDistancia = distanciaBulgarest[i]
                                proximaCidade = i
        buscaGulosa(listaCidade, proximaCidade, cidadesPassadas)
    return 0

algoritmo = int(input("Algoritmo desejado: 1-Busca A* | 2-Busca Gulosa | 0-Sair: " ))
while algoritmo != 0:
    city = str(input("Cidade da qual deseja partir: ")) 
    cidadesPassadas = []
    distAndada = 0

    if(algoritmo == 1):
        print("========================= Busca A* =========================")   
        buscaAestrela(cidades,city,cidadesPassadas,distAndada) 
    elif(algoritmo == 2):        
        print("========================= Busca Gulosa =========================")
        buscaGulosa(cidades,city,cidadesPassadas)  
    else:
        print("\n Opção inexistente")
    algoritmo = int(input("Algoritmo desejado: 1-Busca A* | 2-Busca Gulosa | 0-Sair: " ))
