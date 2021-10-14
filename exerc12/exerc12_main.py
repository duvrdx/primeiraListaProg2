'''
Você foi contratado para desenvolver um programa que leia o resultado da enquete e
informe ao final o resultado da mesma. O programa deverá ler os valores até ser
informado o valor 0, que encerra a entrada dos dados. Não deverão ser aceitos
valores além dos válidos para o programa (0 a 6). Os valores referentes a cada uma
das opções devem ser armazenados em uma lista. 

'''
from exerc12_mod import *

def main():
    #Declarando variaveis
    nomeDoArquivo = "resultadoExerc12"
    osGanhador = ""
    numCandidatos = int(6)
    totalVotos = int(0)
    inpVoto = int(0)
    votosGanhador = int(0)
    indexGanhador = int(0)
    percGanhador = int(0)

    #Definindo listas
    listVotos = []

    #Inserindo votos zerados automáticamente
    for x in range(0, numCandidatos):
        listVotos.append(0)

    #Inicio do programa
    with open(f'{nomeDoArquivo}.txt', 'w') as saida:
        saida.write("Qual o melhor Sistema Operacional para uso em servidores?\nAs possiveis respostas sao:\n1- Windows Server\n2- Unix\n3- Linux\n4- Netware\n5- Mac OS\n6- Outro\n")
        
        inpVoto = int(input())

        while inpVoto != 0:
            if inpVoto > 0 and inpVoto <= numCandidatos:
                listVotos[(inpVoto-1)] += 1
                totalVotos += 1

            inpVoto = int(input())

        #Saída de dados 
        
        saida.write("\nSistema Operacional Votos   %\n------------------- ----- ---")
        
        #Imprimindo uma saída pra cada candidato

        for pos, jogador in enumerate(listVotos):
            percent = calcPercentual(jogador, totalVotos)      

            #Aqui utilizei uma função da nova versão do python 3.10, mas poderia ser representado com ifs
            match pos:
                case 0:
                    saida.write(f"\nWindows Server      {jogador:05} {percent:02}%")
                case 1:
                    saida.write(f"\nUnix                {jogador:05} {percent:02}%")
                case 2:
                    saida.write(f"\nLinux               {jogador:05} {percent:02}%")
                case 3:
                    saida.write(f"\nNetware             {jogador:05} {percent:02}%")
                case 4:
                    saida.write(f"\nMac OS              {jogador:05} {percent:02}%")
                case 5:
                    saida.write(f"\nOutro               {jogador:05} {percent:02}%")

        #Imprimindo total
        saida.write("\n------------------- --------- ")
        saida.write(f"\nTotal               {totalVotos:05}")  

        #Buscando o vencedor
        votosGanhador = max(listVotos)
        indexGanhador = listVotos.index(votosGanhador) + 1
        percGanhador = calcPercentual(votosGanhador, totalVotos)

        #Aqui utilizei uma função da nova versão do python 3.10, mas poderia ser representado com ifs
        match indexGanhador:
            case 0:
                osGanhador = ("Windows Server")
            case 1:
                osGanhador = ("Unix")
            case 2:
                osGanhador = ("Linux")
            case 3:
                osGanhador = ("Netware")
            case 4:
                osGanhador = ("Mac OS")
            case 5:
                osGanhador = ("Outro")
        

        #Resultado do vencedor
        saida.write(f"O Sistema Operacional mais votado foi o {osGanhador},\ncom {listVotos[indexGanhador]:02} votos, correspondendo a {percGanhador:02}%"+" dos votos.")          

if __name__ == "__main__":
    main()