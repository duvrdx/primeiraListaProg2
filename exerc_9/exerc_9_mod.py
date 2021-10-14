def calcSalario(vendasBrutas):
    return 200 + (vendasBrutas * 0.09)

def contador(salarioList, patternList):
    for num in salarioList:
        if num >= 200 and num <=299:
            patternList[0] += 1

        if num >= 300 and num <=399:
            patternList[1] += 1

        if num >= 400 and num <=499:
            patternList[2] += 1

        if num >= 500 and num <=599:
            patternList[3] += 1

        if num >= 600 and num <=699:
            patternList[4] += 1

        if num >= 700 and num <=799:
            patternList[5] += 1

        if num >= 800 and num <=899:
            patternList[6] += 1

        if num >= 900 and num <=999:
            patternList[7] += 1

        if num >= 1000:
            patternList[8] += 1

    return patternList