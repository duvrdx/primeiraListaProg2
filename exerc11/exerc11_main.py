'''
Uma grande emissora de televisão quer fazer uma enquete entre os seus
telespectadores para saber qual o melhor jogador após cada jogo. Para isto, faz-se
necessário o desenvolvimento de um programa, que será utilizado pelas telefonistas,
para a computação dos votos. Sua equipe foi contratada para desenvolver este
programa, utilizando a linguagem de programação Python.
Para computar cada voto, a telefonista digitará um número, entre 1 e 23,
correspondente ao número da camisa do jogador. Um número de jogador igual zero,
indica que a votação foi encerrada. Se um número inválido for digitado, o programa
deve ignorá-lo, mostrando uma breve mensagem de aviso, e voltando a pedir outro
número. Após o final da votação, o programa deverá exibir:

a) O total de votos computados; OK
b) Os númeos e respectivos votos de todos os jogadores que receberam votos; 
c) O percentual de votos de cada um destes jogadores; OK
d) O número do jogador escolhido como o melhor jogador da partida, juntamente
com o número de votos e o percentual de votos dados a ele.
Observe que os votos inválidos e o zero final não devem ser computados como
votos. O resultado aparece ordenado pelo número do jogador. O programa
deve fazer uso de listas. O programa deverá executar o cálculo do percentual
de cada jogador através de uma função. Esta função receberá dois
parâmetros: o número de votos de um jogador e o total de votos. A função
calculará o percentual e retornará o valor calculado.
'''


from exerc11_mod import calcPercentual, calcPercentualCerta


def main():
    #Definindo variáveis
    numCandidatos = int(23)
    totalVotos = int(0)
    inpVoto = int(0)
    votosGanhador = int(0)
    indexGanhador = int(0)
    nomeDoArquivo = "resultado"

    #Definindo listas
    listVotos = []

    with open(f'{nomeDoArquivo}.txt', 'w') as arquivo:
        #Inserindo votos zerados automáticamente
        for x in range(0, numCandidatos):
            listVotos.append(0)
        
        #Iniciando processo de votação
        arquivo.write("Enquete: Quem foi o melhor jogador?\n")
        print("Enquete: Quem foi o melhor jogador?\n")

        arquivo.write("Informe um valor entre 1 e 23 ou 0 para sair!\n")
        inpVoto = int(input("Número do jogador (0=fim): "))

        arquivo.write(f"Numero do jogador (0=fim): {inpVoto:02}\n")

        while inpVoto != 0:
            if inpVoto > 0 and inpVoto <= numCandidatos:
                listVotos[(inpVoto-1)] += 1
                totalVotos += 1
                
            inpVoto = int(input("Número do jogador (0=fim): "))
            arquivo.write(f"Numero do jogador (0=fim): {inpVoto:02}\n")
        
        #Inicio da saida de dados
        arquivo.write("\nResultado da votacao:\n")
        arquivo.write(f"Foram computados {totalVotos} votos.\n")
        arquivo.write(f"\nVotos por jogadores:\n")
        arquivo.write("______________________________________________________\n")
        
        #Imprimindo resultados de cada jogador
        for pos, jogador in enumerate(listVotos):
            posicao = pos + 1

            percentInt, percentDec = calcPercentual(jogador, totalVotos)      

            if jogador>0:
                arquivo.write(f"| Jogador:{posicao:02}     | Votos:{jogador:03}      | Percentual:{percentInt:02},{percentDec}% |\n")

        arquivo.write("|____________________________________________________|\n")

        #Imprimindo resultado do vencedor
        votosGanhador = max(listVotos)
        indexGanhador = listVotos.index(votosGanhador) + 1
        percIntGanhador, percDecGanhador = calcPercentual(votosGanhador, totalVotos)

        arquivo.write(f"O melhor jogador foi o numero {indexGanhador}, com {votosGanhador} votos,\ncorrespondendo a {percIntGanhador:02},{percDecGanhador}%" + " do total de votos.\n")

if __name__ == "__main__":
    main()
