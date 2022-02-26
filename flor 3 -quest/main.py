import matplotlib.pyplot as plt
from data_flor import FlorData
from classificador_flor import ClasificadorFlor


listaTreino = FlorData.listaTreino
listaTeste = FlorData.listaTeste
listaDistancias = []
cont = 0
for i in listaTeste: 
    i1=ClasificadorFlor(i)
    dist = i1.calcularDistancia(1)
    listaDistancias.append(dist)
    if i1.analizarResultado() == True:
        cont = cont+1

    print ('\n')
print ( cont)
#print(listaDistancias)
