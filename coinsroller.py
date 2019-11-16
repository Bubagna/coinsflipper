import random
import re
#inizio
x = int(input("Quante volte vuoi lanciare la moneta?"))
y = int(input("Quante volte vuoi lanciare l'insieme di monete?"))


def coinpicker():
    number = random.randint(0,1)
    moneta = "" 
    if number == 0:
        moneta = "testa"
    else:
        moneta = "croce"
    return moneta

def lancio(x):
    l = []
    for i in range(x):
        coin = coinpicker()
        l.append(coin)

    lancio.croci = 0
    lancio.teste = 0
    for i in l:
        if i == "croce":
            lancio.croci += 1
        else:
            lancio.teste += 1

lancio(x)

def rapporto():
    try:
        rapporto.rapportoCroci = str((round((lancio.croci/lancio.teste) * 100))/2) + "% di croci"
    except ZeroDivisionError:
        return("100% di croci")

    try:
        rapporto.rapportoTeste = str((round((lancio.teste/lancio.croci) * 100))/2) +  "% di teste"
    except ZeroDivisionError:
        return("100% di teste")
    
    return rapporto.rapportoCroci, rapporto.rapportoTeste


def lanciMultipli():
    crociMultiple = []
    testeMultiple = []
    for i in range(y):
        lancio(x)
        rapporto()
        crociMultiple.append(rapporto.rapportoCroci)
        testeMultiple.append(rapporto.rapportoTeste)
    crociSum = 0
    for i in crociMultiple:
        crociSum += int(re.search(r'\d+', i).group())

    testeSum = 0
    for i in testeMultiple:
        testeSum += int(re.search(r'\d+', i).group())

    if testeSum > crociSum:
        return testeSum
    else:
        return crociSum
    

print(rapporto())
print(lanciMultipli())