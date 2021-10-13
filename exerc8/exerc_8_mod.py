def ordenarLista(numList):
    listOrd = ""

    for pos, num in enumerate(numList):
        if pos == 0:
            listOrd = (f"Posição: {pos}, Nota: {num};")
        else:
            listOrd += (f" Posição: {pos}, Nota: {num};")
    
    return listOrd
    
def ordenarInvLista(numList):
    listOrdInv = ""

    cont = (len(numList) - 1)

    while cont >= 0:
        if cont == (len(numList) - 1):
            listOrdInv = (f"Posição: {cont}, Nota: {numList[cont]};")
        else:
            listOrdInv += (f" Posição: {cont}, Nota: {numList[cont]};")
        cont -= 1

    return listOrdInv

def somarNotas(numList):
    somaNota = float(0.0)

    for num in numList:
        somaNota += num
    
    return somaNota

def mediaNota(soma, numList):

    return soma/(len(numList))

def acimaMedia(media, numList):
    qnt = int(0)

    for num in numList:
        if num > media:
            qnt += 1
    
    return qnt

def abaixoSete(numList):
    qnt = int(0)

    for num in numList:
        if num < 7:
            qnt += 1
    return qnt