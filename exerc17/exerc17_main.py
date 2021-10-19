'''
Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes e
armazene os resultados em uma lista . Depois, mostre quantas vezes cada valor foi
conseguido. Dica: use uma lista de contadores(1-6) e uma função para gerar numeros
aleatórios, simulando os lançamentos dos dados.
'''

from exerc17_mod import *

def main():
    #Definindo variaveis
    result = int(0) 
    
    #Definindo lista
    listCont = [0,0,0,0,0,0]
    
    for x in range(0,100):
        result = dado() #Resultado da jogada do dado
       
        #Adicionando o resultado na lista de contadores
        if result == 1:
            listCont[0] += 1
        if result == 2:
            listCont[1] += 1
        if result == 3:
            listCont[2] += 1
        if result == 4:
            listCont[3] += 1
        if result == 5:
            listCont[4] += 1
        if result == 6:
            listCont[5] += 1
    
    for pos, face in enumerate(listCont):
        print("A face",(pos+1),f"caiu {face}" )

if __name__ == "__main__":
    main()
    