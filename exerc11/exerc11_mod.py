#Essa função não precisaria de retornar 2 valores, retornei 2 para ajudar na formatação da saida
def calcPercentual(numJogador, totalVotos):
    percentInt = (numJogador * 100) // totalVotos
    percentDec = (numJogador * 100) % totalVotos

    return percentInt, percentDec

#Função que retorna apenas um valor
def calcPercentualCerta(numJogador, totalVotos):
    percent = (numJogador * 100) / totalVotos

    return percent