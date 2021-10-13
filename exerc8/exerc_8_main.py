'''
Faça um programa que leia um número indeterminado de valores, correspondentes a
notas, encerrando a entrada de dados quando for informado um valor igual a -1 (que
não deve ser armazenado). Após esta entrada de dados, faça:
a) Mostre a quantidade de valores que foram lidos;
b) Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
c) Exiba todos os valores na ordem inversa à que foram informados, um ao lado do
outro;
d) Calcule e mostre a soma dos valores;
e) Calcule e mostre a média dos valores;
f) Calcule e mostre a quantidade de valores acima da média calculada;
g) Calcule e mostre a quantidade de valores abaixo de sete;
h) Encerre o programa com uma mensagem.
'''

from exerc_8_mod import *
import time

def main():
    #Definindo variáveis
    numInput = float(0.0)
    numSoma = float(0.0)
    numMedia = float(0.0)
    acimaDaMedia = int(0)
    abaixoDeSete = int(0)

    #Strings de saída
    ord = str("")
    ordInv = str("")

    #Definindo listas e/ou tuplas
    numList = []

    #Pegando primeira nota
    print("Insira as notas! \nCondição de parada: -1")
    numInput = float(input(""))

    while numInput != -1:
        numList.append(numInput) #Adicionando número atual a lista
        numInput = float(input(""))
    
    #Criando string com todos os valores na ordem
    ord = ordenarLista(numList)
    
    #Criando string com todos os valores na ordem inversa
    ordInv = ordenarInvLista(numList)

    #Somando notas
    numSoma = somarNotas(numList)

    #Calculando média
    numMedia = mediaNota(numSoma, numList)

    #Calculando notas acima da média
    acimaDaMedia = acimaMedia(numMedia, numList)

    #Calculando notas abaixo de sete
    abaixoDeSete = abaixoSete(numList)
        
    #Saída do programa
    print(f"\nLista em Ordem:\n{ord}\n")
    print(f"Lista em Ordem Inversa:\n{ordInv}\n")
    print(f"Soma de notas: {numSoma:.2f}\n")
    print(f"Média de notas: {numMedia:.2f}\n")
    print(f"Quantidade de Notas acima da média: {acimaDaMedia}\n")
    print(f"Quantidade de Notas abaixo de sete: {abaixoDeSete}\n")


    #Usando função 'time.sleep()' para que o usuário possa ler as informações
    #antes do encerramento do programa
    time.sleep(20)


    print("O programa irá fechar em 5s...")
    time.sleep(5)


if __name__ == "__main__":
    main()