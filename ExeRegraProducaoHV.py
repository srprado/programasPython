vLinha = 0
vColuna = 0
hLinha = 0
hColuna = 0
boLinha = 0
boColuna = 0
isBonus = False

from random import *
vLinha = randint(0, 9)
vColuna = randint(0, 9)
hLinha = randint(0, 9)
hColuna = randint(0, 9)
boLinha = randint(0, 9)
boColuna = randint(0, 9)
while((vLinha==hLinha) & (vColuna==hColuna)):
    vLinha = randint(0, 9)
    vColuna = randint(0, 9)
    hLinha = randint(0, 9)
    hColuna = randint(0, 9)

print("Vilão: [",vLinha,"] [",vColuna,"]")
print("Herói: [",hLinha,"] [",hColuna,"]")
print("Local bonus: [",boLinha,"] [",boColuna,"]")

# Matriz = [linha][coluna] <=> inicia em [0][0]
def montaMatriz(vLinha, vColuna, hLinha, hColuna, boLinha, boColuna):
    print("==================== POSIÇÕES ====================")
    matriz = [ [0 for i in range(10)] for j in range(10)]
    for linha in range(10):    
        for coluna in range(10):
            if((linha==vLinha) & (coluna==vColuna)):
                matriz[linha][coluna] = "V"
            elif((linha==hLinha) & (coluna==hColuna)):
                matriz[linha][coluna] = "H"
            elif((linha==vLinha) & (coluna==vColuna) & (vLinha==hLinha) & (vColuna==hColuna)):
                matriz[linha][coluna] = "H"
            elif((linha==boLinha) & (coluna==boColuna)):
                matriz[linha][coluna] = "B"
            else:
                matriz[linha][coluna] = "O"

    for linha in range(10):
        for coluna in range(10):
            print("%4c" % matriz[linha][coluna], end='')
        print()

def verificaRegra(vLinha, vColuna, hLinha, hColuna, boLinha, boColuna, ataque, vidaV):
    global isBonus
    regra = 0
    # vidaV = vidaV - ataque
    if((vLinha==hLinha) and (vColuna==hColuna)):        
        regra = 1  
        # atacar o vilão  
    if((hColuna > vColuna)):
        regra = 2
        # andar para a esquerda: diminuir o valor da coluna
    if((hColuna < vColuna)):
        regra = 3
        # andar para a direita: aumentar o valor da coluna
    if(hLinha > vLinha):
        regra = 4 
        # andar para cima: diminuir o valor da linha  
    if(hLinha < vLinha):
        regra = 5
        # andar para baixo: aumentar o valor da linha                       
    if((hLinha==boLinha) and (hColuna==boColuna) and (isBonus==False)):
        regra = 6
        isBonus = True
        print("BONUS")
        # mando o valor da regra
        # ataque = 2
    
    return regra

def posicao(vLinha, vColuna, hLinha, hColuna, boLinha, boColuna, ataque, vidaV): 
    valorR = verificaRegra(vLinha, vColuna, hLinha, hColuna, boLinha, boColuna, ataque, vidaV)
    while((vidaV > 0)):                    
        if(valorR==1):
            ataque = 1
            vidaV = vidaV - ataque
            vLinha = randint(0, 9)
            vColuna = randint(0, 9)
            print("==================== ATAQUE ====================")   
            print(vidaV) 
            if(vidaV==0):
                print("==================== FIM DE JOGO ====================")
                
        elif(valorR==2):
            hColuna = hColuna-1
            montaMatriz(vLinha, vColuna, hLinha, hColuna, boLinha, boColuna)
            
        elif(valorR==3):
            hColuna = hColuna+1
            montaMatriz(vLinha, vColuna, hLinha, hColuna, boLinha, boColuna)

        elif(valorR==4):
            hLinha = hLinha-1
            montaMatriz(vLinha, vColuna, hLinha, hColuna, boLinha, boColuna)

        elif(valorR==5):
            hLinha = hLinha+1
            montaMatriz(vLinha, vColuna, hLinha, hColuna, boLinha, boColuna)
            
        elif(valorR==6):
            ataque=2
            vidaV = vidaV - ataque
            montaMatriz(vLinha, vColuna, hLinha, hColuna, boLinha, boColuna)
        valorR = verificaRegra(vLinha, vColuna, hLinha, hColuna, boLinha, boColuna, ataque, vidaV)

print("==================== Iniciando jogo ====================")
ataque = 0
vidaV = 3
montaMatriz(vLinha, vColuna, hLinha, hColuna, boLinha, boColuna)
posicao(vLinha, vColuna, hLinha, hColuna, boLinha, boColuna, ataque, vidaV)