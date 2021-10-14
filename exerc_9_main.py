'''
Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus
vendedores com base em comissões. O vendedor recebe R$200 por semana mais 9
por cento de suas vendas brutas daquela semana. Por exemplo, um vendedor que
teve vendas brutas de R$3000 em uma semana recebe R$200 mais 9 por cento de
$3000, ou seja, um total de $470. Escreva um programa (usando uma lista de
contadores) que determine quantos vendedores receberam salários nos seguintes
intervalos de valores:
a) R$200 - R$299
b) R$300 - R$399
c) R$400 - R$499
d) R$500 - R$599
e) R$600 - R$699
f) R$700 - R$799
g) R$800 - R$899
h) R$900 - R$999
i) R$1000 em diante
Desafio: Crie uma função para chegar na posição da lista a partir do salário, sem
fazer vários ifs aninhados.
'''

from exerc_9_mod import *
import time

def main():
    #Definindo variáveis
    vendasBrutas = float(0.0) 

    #Definindo listas e/ou tuplas
    patternList = [0,0,0,0,0,0,0,0,0] #Lista que armazena os contadores, começando todos zeradas
    salarioList = [] #Lista com salário de cada vendedor

    #Inserindo vendedores na lista
    print("Cadastrando salários: \n(Para sair digite um numero menor que 0)\n")
    vendasBrutas = float(input("Vendas brutas desse vendedor:\n"))

    while vendasBrutas >= 0:
        salarioList.append(calcSalario(vendasBrutas)) #Calculando salário, e inserindo na lista
        print("Cadastrando novo salário: \n(Para sair digite um numero menor que 0)\n")
        vendasBrutas = float(input("Vendas brutas desse vendedor:\n"))
    
    #Contando o numero de salários nos intervalos
    result = contador(salarioList, patternList)
    print(result)

    #Imprimindo resultados
    print(f"Quantidade de vendedores com salário entre R$200 e R$299: {result[0]}")
    print(f"Quantidade de vendedores com salário entre R$300 e R$399: {result[1]}")
    print(f"Quantidade de vendedores com salário entre R$400 e R$499: {result[2]}")
    print(f"Quantidade de vendedores com salário entre R$500 e R$599: {result[3]}")
    print(f"Quantidade de vendedores com salário entre R$600 e R$699: {result[4]}")
    print(f"Quantidade de vendedores com salário entre R$700 e R$799: {result[5]}")
    print(f"Quantidade de vendedores com salário entre R$800 e R$899: {result[6]}")
    print(f"Quantidade de vendedores com salário entre R$900 e R$999: {result[7]}")
    print(f"Quantidade de vendedores com salário acima de R$1000: {result[8]}")

    #Usando função 'time.sleep()' para que o usuário possa ler as informações
    #antes do encerramento do programa
    time.sleep(20)


    print("O programa irá fechar em 5s...")
    time.sleep(5)


if __name__ == "__main__":
    main()